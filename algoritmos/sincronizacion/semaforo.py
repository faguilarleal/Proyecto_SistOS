class Semaforo:
    def __init__(self, count):
        self.count = count
        self.permisos = count
        self.entradas = {}  # PID: tiempo de liberación

    def acquire(self, pid, tiempo):
        if self.permisos > 0:
            self.permisos -= 1
            self.entradas[pid] = tiempo + 1  # ocupa por un ciclo
            return "ACCESSED"
        return "WAITING"

    def update(self, tiempo):
        # Liberar procesos cuyo tiempo terminó
        liberados = [pid for pid, t_fin in self.entradas.items() if tiempo >= t_fin]
        for pid in liberados:
            self.permisos += 1
            del self.entradas[pid]


def simular_semaforo(args: dict):
    procesos = args["procesos"]
    recursos = args["recursos"]  # ahora indica cuántos permisos tiene cada recurso
    acciones = args["acciones_por_ciclo"]

    semaforos = {r: Semaforo(count) for r, count in recursos.items()}
    acciones_pendientes = sorted(acciones[:], key=lambda a: a["CICLO"])
    acciones_esperando = []

    tiempo = 0
    gantt = []

    while acciones_pendientes or acciones_esperando:
        # Actualizar semáforos (liberar recursos)
        for semaforo in semaforos.values():
            semaforo.update(tiempo)

        # Filtrar acciones para este ciclo
        acciones_este_ciclo = [a for a in acciones_pendientes if a["CICLO"] == tiempo]
        acciones_pendientes = [a for a in acciones_pendientes if a["CICLO"] > tiempo]

        # Añadir reintentos
        acciones_este_ciclo += acciones_esperando
        acciones_esperando = []

        # Ordenar por prioridad (menor número = mayor prioridad)
        acciones_este_ciclo.sort(key=lambda a: procesos[a["PID"]]["Priority"])

        for accion in acciones_este_ciclo:
            pid = accion["PID"]
            tipo = accion["ACCION"]
            recurso = accion["RECURSO"]

            # Verificar si el proceso ya llegó
            if procesos[pid]["AT"] > tiempo:
                accion["CICLO"] += 1
                acciones_pendientes.append(accion)
                continue

            estado = semaforos[recurso].acquire(pid, tiempo)
            gantt.append((f"{pid}-{tipo}-{estado}", tiempo, tiempo + 1))

            if estado == "WAITING":
                accion["CICLO"] += 1
                acciones_esperando.append(accion)

        tiempo += 1

    return gantt

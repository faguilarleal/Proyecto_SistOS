class Mutex:
    def __init__(self):
        self.locked = False
        self.owner = None
        self.release_time = 0

    def acquire(self, pid, tiempo):
        if not self.locked:
            self.locked = True
            self.owner = pid
            self.release_time = tiempo + 1
            return "ACCESSED"
        return "WAITING"

    def update(self, tiempo):
        if self.locked and tiempo >= self.release_time:
            self.locked = False
            self.owner = None


def simular_mutex(args: dict):
    procesos = args["procesos"]
    recursos = args["recursos"]
    acciones = args["acciones_por_ciclo"]

    mutexes = {r: Mutex() for r in recursos}
    acciones_pendientes = sorted(acciones[:], key=lambda a: a["CICLO"])
    acciones_esperando = []

    tiempo = 0
    gantt = []

    while acciones_pendientes or acciones_esperando:
        # Liberar recursos que ya cumplieron su tiempo
        for mutex in mutexes.values():
            mutex.update(tiempo)

        # Acciones que deben ejecutarse este ciclo (originalmente o reintentos)
        acciones_este_ciclo = [a for a in acciones_pendientes if a["CICLO"] == tiempo]
        acciones_pendientes = [a for a in acciones_pendientes if a["CICLO"] > tiempo]

        # Añadir reintentos de acciones que estaban esperando
        acciones_este_ciclo += acciones_esperando
        acciones_esperando = []

        # Ordenar por prioridad
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

            estado = mutexes[recurso].acquire(pid, tiempo)
            gantt.append((f"{pid}-{estado}-{tipo}", tiempo, tiempo + 1))

            if estado == "WAITING":
                accion["CICLO"] += 1
                acciones_esperando.append(accion)

        tiempo += 1

    return gantt

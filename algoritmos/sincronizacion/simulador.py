
from algoritmos.sincronizacion.mutex import Mutex
from algoritmos.sincronizacion.semaforo import Semaphore

# from mutex import Mutex
# from semaforo import Semaphore

class Simulador:
    def __init__(self, procesos, recursos, acciones, mecanismo="mutex"):
        self.tiempo = 0
        self.procesos = procesos
        self.recursos = self.init_recursos(recursos, mecanismo)
        self.acciones = acciones
        self.mecanismo = mecanismo
        self.eventos = []

        print(self.acciones)

    def init_recursos(self, recursos, mecanismo):
        res = {}
        for nombre, count in recursos.items():
            if mecanismo == "mutex":
                res[nombre] = Mutex()
            else:
                res[nombre] = Semaphore(count)
        return res

    def simular(self, ciclos=10):
        for t in range(ciclos):
            for accion in self.acciones:
                if accion["CICLO"] == t:
                    pid = accion["PID"]
                    op = accion["ACCION"]
                    recurso = accion["RECURSO"]
                    estado = "WAITING"

                    if self.mecanismo == "mutex":
                        if op in ("READ", "WRITE"):
                            ok = self.recursos[recurso].acquire(pid)
                            if ok:
                                estado = "ACCESSED"
                    else:
                        if op in ("READ", "WRITE"):
                            ok = self.recursos[recurso].wait(pid)
                            if ok:
                                estado = "ACCESSED"

                    self.eventos.append((f"{pid} - {op} - {estado}", t, t + 1))
        return self.eventos





# Entrada proporcionada
procesos = {
    "P1": {"BT": 8, "AT": 0, "Priority": 1},
    "P2": {"BT": 4, "AT": 1, "Priority": 2},
}

recursos = {
    "R1": 1,
    "R2": 2,
    "R3": 3
}

# acciones = [
#     {"PID": "P1", "ACCION": "READ", "RECURSO": "R1", "CICLO": 0},
#     {"PID": "P2", "ACCION": "READ", "RECURSO": "R1", "CICLO": 0},
#     {"PID": "P1", "ACCION": "WRITE", "RECURSO": "R1", "CICLO": 2},
# ]

# acciones = [
#     {'PID': 'P1', 'ACCION': 'READ', 'RECURSO': 'R1', 'CICLO': 0}, 
#     {'PID': 'P2', 'ACCION': 'WRITE', 'RECURSO': 'R2', 'CICLO': 1}, 
#     {'PID': 'P3', 'ACCION': 'READ', 'RECURSO': 'R3', 'CICLO': 2}, 
#     {'PID': 'P4', 'ACCION': 'WRITE', 'RECURSO': 'R1', 'CICLO': 3}, 
#     {'PID': 'P5', 'ACCION': 'READ', 'RECURSO': 'R2', 'CICLO': 4}, 
#     {'PID': 'P1', 'ACCION': 'WRITE', 'RECURSO': 'R2', 'CICLO': 5}, 
#     {'PID': 'P2', 'ACCION': 'READ', 'RECURSO': 'R3', 'CICLO': 6}, 
#     {'PID': 'P3', 'ACCION': 'WRITE', 'RECURSO': 'R1', 'CICLO': 7}, 
#     {'PID': 'P4', 'ACCION': 'READ', 'RECURSO': 'R2', 'CICLO': 8}, 
#     {'PID': 'P5', 'ACCION': 'WRITE', 'RECURSO': 'R3', 'CICLO': 9}
# ]

# # Ejecutar simulación
# sim = Simulador(procesos, recursos, acciones, mecanismo="semaphore")  # o "semaphore"
# eventos = sim.simular(ciclos=5)

# for evento in eventos:
#     print(evento)

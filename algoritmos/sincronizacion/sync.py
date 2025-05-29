from mutex import Mutex
from semaforo import Semaphore

def simular_mutex(procesos, recursos, acciones):
    recursos_mutex = {r: Mutex() for r in recursos}
    resultados = []

    for accion in sorted(acciones, key=lambda a: a['CICLO']):
        ciclo = accion['CICLO']
        pid = accion['PID']
        tipo = accion['ACCION']
        recurso = accion['RECURSO']
        proceso = procesos[pid]

        if proceso['AT'] > ciclo:
            continue

        mutex = recursos_mutex[recurso]
        if tipo == 'READ' or tipo == 'WRITE':
            accedido = mutex.acquire(pid)
            estado = 'ACCESSED' if accedido else 'WAITING'
            resultados.append((f'{pid} - {tipo} - {estado}', ciclo, ciclo + 1))
            if accedido:
                mutex.release(pid)

    return resultados


def simular_semaforo(procesos, recursos, acciones):
    recursos_semaforo = {r: Semaphore(recursos[r]['contador']) for r in recursos}
    resultados = []

    for accion in sorted(acciones, key=lambda a: a['CICLO']):
        ciclo = accion['CICLO']
        pid = accion['PID']
        tipo = accion['ACCION']
        recurso = accion['RECURSO']
        proceso = procesos[pid]

        if proceso['AT'] > ciclo:
            continue

        sem = recursos_semaforo[recurso]
        accedido = sem.wait(pid)
        estado = 'ACCESSED' if accedido else 'WAITING'
        resultados.append((f'{pid} - {tipo} - {estado}', ciclo, ciclo + 1))
        if accedido:
            sem.signal()

    return resultados

# Entrada proporcionada
procesos = {
    "P1": {"BT": 8, "AT": 0, "Priority": 1},
    "P2": {"BT": 4, "AT": 1, "Priority": 2},
}

recursos = {
    "R1": 1,
}

acciones = [
    {"PID": "P1", "ACCION": "READ", "RECURSO": "R1", "CICLO": 0},
    {"PID": "P2", "ACCION": "READ", "RECURSO": "R1", "CICLO": 0},
    {"PID": "P1", "ACCION": "WRITE", "RECURSO": "R1", "CICLO": 2},
]

print(simular_mutex(procesos=procesos, recursos=recursos, acciones=acciones))
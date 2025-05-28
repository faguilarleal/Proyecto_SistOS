# fifo_scheduler.py

def fifo_scheduler(procesos: dict):
    """
    Algoritmo FIFO: recibe un diccionario de procesos y retorna una lista
    con el orden de ejecución (PID, inicio, fin).

    procesos: {
        "P1": {"BT": 8, "AT": 0, "Priority": 1},
        "P2": {"BT": 4, "AT": 2, "Priority": 2},
        ...
    }

    Retorna: Lista de tuplas (PID, inicio, fin) para construir el diagrama de Gantt.
    """
    # Convertimos el diccionario en una lista ordenada por Arrival Time
    lista_procesos = sorted([
        {"PID": pid, **datos} for pid, datos in procesos.items()
    ], key=lambda p: p["AT"])

    tiempo_actual = 0
    resultado = []

    for proceso in lista_procesos:
        llegada = proceso["AT"]
        duracion = proceso["BT"]
        pid = proceso["PID"]

        # Si el proceso llega después del tiempo actual, hay espera (idle)
        if llegada > tiempo_actual:
            tiempo_actual = llegada

        inicio = tiempo_actual
        fin = tiempo_actual + duracion
        resultado.append((pid, inicio, fin))
        tiempo_actual = fin

    return resultado


# -------------- PRUEBA ---------------
procesos = {
    "P1": {"BT": 8, "AT": 0, "Priority": 1},
    "P2": {"BT": 4, "AT": 2, "Priority": 3},
    "P3": {"BT": 3, "AT": 5, "Priority": 2}
}

orden_ejecucion = fifo_scheduler(procesos)

for p in orden_ejecucion:
    print(p)
# Salida esperada: lista con tuplas (PID, inicio, fin)
# [('P1', 0, 8), ('P2', 8, 12), ('P3', 12, 15)]


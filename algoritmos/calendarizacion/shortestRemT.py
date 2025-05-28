# srtf_scheduler.py

def srtf_scheduler(args: dict):
    """
    Algoritmo SRTF (Shortest Remaining Time First, expropiativo).
    Recibe un diccionario de procesos y retorna una lista de ejecuciones:
    (PID, inicio, fin), útil para construir el diagrama de Gantt.

    procesos: {
        "P1": {"BT": 8, "AT": 0, "Priority": 1},
        ...
    }

    Retorna: Lista [(PID, inicio, fin), ...] indicando tramos ejecutados.
    """
    procesos = args["procesos"]

    procesos_restantes = [
        {"PID": pid, "AT": datos["AT"], "BT": datos["BT"], "restante": datos["BT"]}
        for pid, datos in procesos.items()
    ]

    tiempo_actual = 0
    ejecucion = []
    proceso_actual = None
    inicio_actual = None

    while procesos_restantes or proceso_actual:
        # Obtener procesos disponibles en este ciclo
        disponibles = [p for p in procesos_restantes if p["AT"] <= tiempo_actual]

        # Incluir el proceso actual (aunque llegó antes) si sigue ejecutando
        if disponibles or proceso_actual:
            if proceso_actual:
                disponibles.append(proceso_actual)

            # Elegir el de menor tiempo restante
            siguiente = min(disponibles, key=lambda p: p["restante"])

            # Si el proceso cambia, guardar el anterior
            if proceso_actual is None or siguiente["PID"] != proceso_actual["PID"]:
                if proceso_actual:
                    ejecucion.append((proceso_actual["PID"], inicio_actual, tiempo_actual))
                proceso_actual = siguiente
                inicio_actual = tiempo_actual

            # Ejecutar por 1 ciclo
            proceso_actual["restante"] -= 1

            if proceso_actual["restante"] == 0:
                ejecucion.append((proceso_actual["PID"], inicio_actual, tiempo_actual + 1))
                if proceso_actual in procesos_restantes:
                    procesos_restantes.remove(proceso_actual)
                proceso_actual = None
                inicio_actual = None

            tiempo_actual += 1
        else:
            # No hay procesos disponibles, avanzar el tiempo
            tiempo_actual += 1

    return ejecucion



# --------------prueba-----------
procesos = {
    "P1": {"BT": 8, "AT": 0, "Priority": 1},
    "P2": {"BT": 4, "AT": 1, "Priority": 2},
    "P3": {"BT": 2, "AT": 2, "Priority": 3}
}

orden = srtf_scheduler(procesos)

for evento in orden:
    print(evento)
# Posible salida:
# [('P1', 0, 1), ('P2', 1, 2), ('P3', 2, 4), ('P2', 4, 6), ('P1', 6, 13)]

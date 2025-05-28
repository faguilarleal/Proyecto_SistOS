# sjf_scheduler.py

def sjf_scheduler(procesos: dict):
    """
    Algoritmo Shortest Job First (no expropiativo).
    Recibe un diccionario de procesos y retorna una lista de tuplas:
    (PID, inicio, fin), útil para construir el diagrama de Gantt.

    procesos: {
        "P1": {"BT": 8, "AT": 0, "Priority": 1},
        "P2": {"BT": 4, "AT": 2, "Priority": 3},
        ...
    }

    Retorna: Lista de ejecuciones [(PID, inicio, fin), ...]
    """
    procesos_restantes = [
        {"PID": pid, **datos} for pid, datos in procesos.items()
    ]
    completados = []
    tiempo_actual = 0

    while procesos_restantes:
        # Obtener los procesos que ya llegaron
        disponibles = [p for p in procesos_restantes if p["AT"] <= tiempo_actual]

        if not disponibles:
            # No hay procesos disponibles, adelantar el tiempo
            tiempo_actual = min(p["AT"] for p in procesos_restantes)
            continue

        # Elegir el de menor Burst Time
        siguiente = min(disponibles, key=lambda p: p["BT"])

        inicio = tiempo_actual
        fin = inicio + siguiente["BT"]
        completados.append((siguiente["PID"], inicio, fin))

        tiempo_actual = fin
        procesos_restantes.remove(siguiente)

    return completados
# -------------- PRUEBA ---------------

procesos = {
    "P1": {"BT": 8, "AT": 0, "Priority": 1},
    "P2": {"BT": 4, "AT": 2, "Priority": 3},
    "P3": {"BT": 2, "AT": 5, "Priority": 2}
}

orden = sjf_scheduler(procesos)

for evento in orden:
    print(evento)
# Ejemplo de salida:
# [('P1', 0, 8), ('P3', 8, 10), ('P2', 10, 14)]

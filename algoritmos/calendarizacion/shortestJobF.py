def sjf_scheduler(args: dict):
    """
    Algoritmo Shortest Job First (no expropiativo).
    No deja el CPU inactivo si hay al menos un proceso disponible.
    """
    procesos = args["procesos"]

    procesos_restantes = [
        {"PID": pid, **datos} for pid, datos in procesos.items()
    ]
    completados = []
    tiempo_actual = 0

    while procesos_restantes:
        disponibles = [p for p in procesos_restantes if p["AT"] <= tiempo_actual]

        if not disponibles:
            # Si no hay procesos disponibles, saltar al siguiente que llegue
            tiempo_actual = min(p["AT"] for p in procesos_restantes)
            continue

        # Ejecutar el más corto entre los que ya llegaron
        siguiente = min(disponibles, key=lambda p: p["BT"])
        inicio = tiempo_actual
        fin = inicio + siguiente["BT"]
        completados.append((siguiente["PID"], inicio, fin))

        tiempo_actual = fin
        procesos_restantes.remove(siguiente)

    return completados

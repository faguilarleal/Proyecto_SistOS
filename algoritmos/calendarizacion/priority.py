def priority_scheduler(args: dict):
    """
    Algoritmo Priority No Preemptive: recibe un diccionario de procesos y retorna una lista
    con el orden de ejecución (PID, inicio, fin).

    procesos: {
        "P1": {"BT": 8, "AT": 0, "Priority": 1},
        "P2": {"BT": 4, "AT": 2, "Priority": 2},
        ...
    }

    Retorna: Lista de tuplas (PID, inicio, fin) para construir el diagrama de Gantt.
    """
    procesos = args["procesos"]

    # Lista de procesos no ejecutados
    lista_procesos = [
        {"PID": pid, **datos} for pid, datos in procesos.items()
    ]

    tiempo_actual = 0
    resultado = []
    procesos_ejecutados = set()

    while len(procesos_ejecutados) < len(lista_procesos):
        # Filtrar procesos que ya llegaron y no están ejecutados
        procesos_listos = [p for p in lista_procesos if p["AT"] <= tiempo_actual and p["PID"] not in procesos_ejecutados]

        if not procesos_listos:
            # No hay proceso listo: avanzar tiempo (idle)
            tiempo_actual += 1
            continue

        # Elegir proceso con prioridad más alta (número más bajo)
        proceso = min(procesos_listos, key=lambda p: p["Priority"])

        inicio = tiempo_actual
        fin = inicio + proceso["BT"]

        resultado.append((proceso["PID"], inicio, fin))

        tiempo_actual = fin
        procesos_ejecutados.add(proceso["PID"])

    return resultado


# procesos = {
#     "P1": {"BT": 10, "AT": 0, "Priority": 3},
#     "P2": {"BT": 1,  "AT": 2, "Priority": 1},
#     "P3": {"BT": 2,  "AT": 1, "Priority": 4},
#     "P4": {"BT": 1,  "AT": 3, "Priority": 2},
# }

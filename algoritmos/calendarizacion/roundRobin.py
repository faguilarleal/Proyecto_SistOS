# rr_scheduler.py

from collections import deque

def rr_scheduler(args: dict):
    """
    Algoritmo Round Robin.
    
    Recibe:
    - procesos: diccionario { PID: {BT, AT, Priority} }
    - quantum: entero con el valor del quantum asignado

    Retorna:
    - Lista de tuplas (PID, inicio, fin), útil para el diagrama de Gantt
    """
    procesos = args["procesos"]
    quantum = args["quantum"]

    # Convertir a lista de procesos con estado adicional
    todos = [
        {"PID": pid, "AT": datos["AT"], "BT": datos["BT"], "restante": datos["BT"]}
        for pid, datos in procesos.items()
    ]

    tiempo_actual = 0
    cola = deque()
    ejecucion = []
    procesos_listos = []
    visitados = set()

    while todos or cola or procesos_listos:
        # Agregar procesos que han llegado al tiempo actual
        for p in list(todos):
            if p["AT"] <= tiempo_actual:
                procesos_listos.append(p)
                todos.remove(p)

        # Mover los que llegaron a la cola de ejecución
        for p in procesos_listos:
            if p["PID"] not in visitados:
                cola.append(p)
                visitados.add(p["PID"])

        procesos_listos.clear()

        if cola:
            proceso = cola.popleft()
            inicio = tiempo_actual
            ejecucion_ciclo = min(quantum, proceso["restante"])
            tiempo_actual += ejecucion_ciclo
            proceso["restante"] -= ejecucion_ciclo
            ejecucion.append((proceso["PID"], inicio, tiempo_actual))

            # Agregar procesos nuevos que llegaron mientras este proceso ejecutaba
            for p in list(todos):
                if p["AT"] <= tiempo_actual:
                    procesos_listos.append(p)
                    todos.remove(p)

            for p in procesos_listos:
                if p["PID"] not in visitados:
                    cola.append(p)
                    visitados.add(p["PID"])
            procesos_listos.clear()

            if proceso["restante"] > 0:
                cola.append(proceso)
        else:
            # CPU idle, avanzar tiempo al próximo proceso disponible
            if todos:
                tiempo_actual = min(p["AT"] for p in todos)
            else:
                break

    return ejecucion


# --------- PRUEBA ------------
# procesos = {
#     "P1": {"BT": 8, "AT": 0, "Priority": 1},
#     "P2": {"BT": 4, "AT": 1, "Priority": 2},
#     "P3": {"BT": 3, "AT": 2, "Priority": 3}
# }

# orden = rr_scheduler(procesos, quantum=2)

# for evento in orden:
#     print(evento)
# # Ejemplo de salida:
# # [('P1', 0, 2), ('P2', 2, 4), ('P3', 4, 6), ('P1', 6, 8), ('P2', 8, 10), ('P1', 10, 14)]

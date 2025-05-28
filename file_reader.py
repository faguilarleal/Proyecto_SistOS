def read_files(process_path: str, resource_path: str, action_path: str):
    procesos = {}  # PID -> {BT, AT, Priority}
    recursos = {}  # Recurso -> {contador, lectores_activos, escritor_activo}
    acciones_por_ciclo = {}  # Ciclo -> [acciones]

    # Leer procesos
    with open(process_path, 'r') as f:
        for linea in f:
            if linea.strip():
                pid, bt, at, prioridad = map(str.strip, linea.strip().split(','))
                procesos[pid] = {
                    "BT": int(bt),
                    "AT": int(at),
                    "Priority": int(prioridad),
                    "tiempo_restante": int(bt)  # útil para la simulación
                }

    # Leer recursos
    with open(resource_path, 'r') as f:
        for linea in f:
            if linea.strip():
                recurso, contador = map(str.strip, linea.strip().split(','))
                recursos[recurso] = {
                    "contador": int(contador),
                    "lectores_activos": set(),
                    "escritor_activo": None
                }

    # Leer acciones
    with open(action_path, 'r') as f:
        for linea in f:
            if linea.strip():
                pid, accion, recurso, ciclo = map(str.strip, linea.strip().split(','))
                ciclo = int(ciclo)
                if ciclo not in acciones_por_ciclo:
                    acciones_por_ciclo[ciclo] = []
                acciones_por_ciclo[ciclo].append({
                    "PID": pid,
                    "accion": accion.upper(),  # READ o WRITE
                    "recurso": recurso
                })

    return procesos, recursos, acciones_por_ciclo

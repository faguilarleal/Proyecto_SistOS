def read_files(process_path: str, resource_path: str, action_path: str):
    procesos = {}  # PID -> {BT, AT, Priority}
    recursos = {}  # Recurso -> {contador, lectores_activos, escritor_activo}
    acciones = []  # Ciclo -> [acciones]

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
                # recursos[recurso] = {
                #     "contador": int(contador),
                #     "lectores_activos": set(),
                #     "escritor_activo": None
                # }
                recursos[recurso] = int(contador)

    # Leer acciones
    acciones = []
    with open(action_path, 'r') as f:
        for linea in f:
            if linea.strip():
                pid, accion, recurso, ciclo = map(str.strip, linea.strip().split(','))
                acciones.append({
                    "PID": pid,
                    "ACCION": accion.upper(),   # "READ" o "WRITE"
                    "RECURSO": recurso,
                    "CICLO": int(ciclo)
                })

        print(acciones)
    

    return procesos, recursos, acciones

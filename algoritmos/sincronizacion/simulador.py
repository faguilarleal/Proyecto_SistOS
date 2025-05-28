from mutex import *
from semaforo import * 
from collections import defaultdict





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


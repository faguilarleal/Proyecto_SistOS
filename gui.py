import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from chart import dibujar_gantt
from file_reader import read_files
from algoritmos.calendarizacion.fifo import fifo_scheduler
from algoritmos.calendarizacion.priority import priority_scheduler
from algoritmos.calendarizacion.roundRobin import rr_scheduler
from algoritmos.calendarizacion.shortestJobF import sjf_scheduler
from algoritmos.calendarizacion.shortestRemT import srtf_scheduler
from algoritmos.sincronizacion.simulador import Simulador

def aux_sim_function(args: dict):
    print("acciones 2\n")
    print(args["acciones_por_ciclo"])
    sim = Simulador(procesos=args["procesos"], recursos=args["recursos"], acciones=args["acciones_por_ciclo"], mecanismo=args["mecanismo"])
    return sim.simular()

#
input_algorithm_map_cal = {
    "First In First Out": fifo_scheduler,
    "Shortest Job First": sjf_scheduler,
    "Shortest Remaining Time": srtf_scheduler,
    "Round Robin": rr_scheduler,
    "Priority": priority_scheduler,
}

input_algorithm_map_sync = {
    "Mutex Locks": aux_sim_function,
    "Semaphore": aux_sim_function
}

st.title("CPU Simulation App")

# Step 1: Main Category Selection
category = st.radio("Select a Category:", ["Calendarization", "Synchronization"])

# Step 2: Sub-options
algorithm = None
quantum = None
if category == "Calendarization":
    algorithm = st.selectbox("Choose an algorithm:", input_algorithm_map_cal.keys())    
    if algorithm == "Round Robin":
        quantum = st.number_input("Quantum value:", min_value=1, value=4)        

elif category == "Synchronization":
    algorithm = st.selectbox("Choose a method:", [
        "Mutex Locks",
        "Semaphore"
    ])

# Step 3: File Inputs
st.subheader("Input Files")
acciones_path = st.text_input("Actions path:", value="./input/test1/acciones.txt")
process_path = st.text_input("Process path:", value="./input/test1/procesos_sync.txt")
resources_path = st.text_input("Resources path:", value="./input/test1/recursos.txt")

# Step 4: Run Button
run = st.button("Run")

if run:
    
    procesos, recursos, acciones_por_ciclo = read_files(process_path=process_path, resource_path=resources_path, action_path=acciones_path)
    args = {
        "procesos": procesos,
        "recursos": recursos,
        "acciones_por_ciclo": acciones_por_ciclo,
        "quantum" : quantum,
        "mecanismo": algorithm
    }

    st.success(f"Running {algorithm} under {category}...")


    if category == "Calendarization":
        ejecuciones = input_algorithm_map_cal[algorithm](args)    

    elif category == "Synchronization":
        ejecuciones = input_algorithm_map_sync[algorithm](args)
    

    # Step 5: Plot (just a placeholder example)
    fig = dibujar_gantt(ejecuciones=ejecuciones)
    st.pyplot(fig)
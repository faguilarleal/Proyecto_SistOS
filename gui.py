import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from chart import dibujar_gantt
from file_reader import read_files
from algoritmos.calendarizacion.fifo import fifo_scheduler

#
input_algorithm_map = {
    "First In First Out": fifo_scheduler,
    "Shortest Job First": "",
    "Shortest Remaining Time": "",
    "Round Robin": "",
    "Priority": ""
}

st.title("CPU Simulation App")

# Step 1: Main Category Selection
category = st.radio("Select a Category:", ["Calendarization", "Synchronization"])

# Step 2: Sub-options
algorithm = None
quantum = None
if category == "Calendarization":
    algorithm = st.selectbox("Choose an algorithm:", input_algorithm_map.keys())    
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
        "quantum" : quantum
    }

    st.success(f"Running {algorithm} under {category}...")
        
    ejecuciones = input_algorithm_map[algorithm](args)

    # Step 5: Plot (just a placeholder example)
    fig = dibujar_gantt(ejecuciones=ejecuciones)
    st.pyplot(fig)
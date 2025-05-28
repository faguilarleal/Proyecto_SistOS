import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("CPU Simulation App")

# Step 1: Main Category Selection
category = st.radio("Select a Category:", ["Calendarization", "Synchronization"])

# Step 2: Sub-options
algorithm = None
if category == "Calendarization":
    algorithm = st.selectbox("Choose an algorithm:", [
        "First In First Out",
        "Shortest Job First",
        "Shortest Remaining Time",
        "Round Robin",
        "Priority"
    ])
    quantum = None
    if algorithm == "Round Robin":
        quantum = st.number_input("Quantum value:", min_value=1, value=4)

elif category == "Synchronization":
    algorithm = st.selectbox("Choose a method:", [
        "Mutex Locks",
        "Semaphore"
    ])

# Step 3: File Inputs
st.subheader("Input Files")
file1 = st.text_input("File 1 path:", value="path/to/file1.txt")
file2 = st.text_input("File 2 path:", value="path/to/file2.txt")
file3 = st.text_input("File 3 path:", value="path/to/file3.txt")

# Step 4: Run Button
run = st.button("Run")

if run:
    st.success(f"Running {algorithm} under {category}...")

    # Step 5: Plot (just a placeholder example)
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title("Sample Output Chart")
    st.pyplot(fig)
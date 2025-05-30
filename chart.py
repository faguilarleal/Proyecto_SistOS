import streamlit as st
import matplotlib.pyplot as plt
import time

def crear_figura(ejecuciones, ciclo):
    fig, ax = plt.subplots(figsize=(10, 3))
    colores = {}
    colores_disponibles = plt.cm.get_cmap('tab10').colors
    pid_indices = {}

    ejecuciones_hasta_ciclo = [e for e in ejecuciones if e[2] <= ciclo]

    for idx, (pid_estado, inicio, fin) in enumerate(ejecuciones_hasta_ciclo):
        pid = pid_estado.split('-')[0]
        if pid not in colores:
            colores[pid] = colores_disponibles[len(colores) % len(colores_disponibles)]
        if pid not in pid_indices:
            pid_indices[pid] = len(pid_indices)

        duracion = fin - inicio
        ax.broken_barh([(inicio, duracion)], (10 * pid_indices[pid], 9), facecolors=colores[pid])
        ax.text(inicio + duracion / 2, 10 * pid_indices[pid] + 4.5, pid_estado, ha='center', va='center', color='white', fontsize=9, fontweight='bold')

    ax.set_yticks([10 * i + 4.5 for i in pid_indices.values()])
    ax.set_yticklabels(pid_indices.keys())
    ax.set_xlabel("Ciclos")
    ax.set_title(f"Diagrama de Gantt - Ciclo {ciclo}")

    ax.grid(True)
    ax.set_ylim(0, 10 * max(1, len(pid_indices)))
    ax.set_xlim(0, max(e[2] for e in ejecuciones) + 1)

    plt.tight_layout()
    return fig

def animar_gantt_streamlit(ejecuciones):
    max_ciclo = max(e[2] for e in ejecuciones)
    placeholder = st.empty()  # Contenedor para actualizar el gráfico

    for ciclo in range(1, max_ciclo + 2):
        fig = crear_figura(ejecuciones, ciclo)
        placeholder.pyplot(fig=fig)
        time.sleep(0.5)  # Pausa para ver la animación
    plt.close(fig) 


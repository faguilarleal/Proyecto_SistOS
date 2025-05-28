import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def dibujar_gantt(ejecuciones):
    """
    Dibuja un diagrama de Gantt.
    
    ejecuciones: Lista de tuplas (PID, inicio, fin)
    """
    fig, ax = plt.subplots(figsize=(10, 3))
    
    colores = {}
    colores_disponibles = plt.cm.get_cmap('tab10').colors
    pid_indices = {}
    
    for idx, (pid, inicio, fin) in enumerate(ejecuciones):
        if pid not in colores:
            colores[pid] = colores_disponibles[len(colores) % len(colores_disponibles)]
        if pid not in pid_indices:
            pid_indices[pid] = len(pid_indices)
        
        duracion = fin - inicio
        ax.broken_barh([(inicio, duracion)], (10 * pid_indices[pid], 9), facecolors=colores[pid])
        ax.text(inicio + duracion / 2, 10 * pid_indices[pid] + 4.5, pid, ha='center', va='center', color='white', fontsize=9, fontweight='bold')
    
    # Configurar eje Y
    ax.set_yticks([10 * i + 4.5 for i in pid_indices.values()])
    ax.set_yticklabels(pid_indices.keys())
    ax.set_xlabel("Ciclos")
    ax.set_title("Diagrama de Gantt")

    # Límites y rejilla
    ax.grid(True)
    ax.set_ylim(0, 10 * len(pid_indices))
    ax.set_xlim(0, max(e[2] for e in ejecuciones) + 1)

    return fig

# Proyecto_SistOS

## Ejecución del programa

Crear un ambiente virtual 
```
python -m venv venv
```
Activar el entorno 

- Windows:
```
./venv/Scripts/activate
```
- Linux:
```
source venv/bin/activate
```

Instalar las librerias del archivo de texto
```
pip install -r requirements.txt
```
Correr la parte visual 
```
streamlit run gui.py
```



## Explicación de código 
#### Estructura 



### 📂 Descripción de Carpetas

- `algoritmos/`  
  Contiene los algoritmos principales del proyecto.
  
  - `calendarizacion/`: Algoritmos de planificación de procesos.  
    - `fifo.py`: Algoritmo First In First Out.  
    - `priority.py`: Planificación por prioridad.  
    - `roundRobin.py`: Algoritmo Round Robin.  
    - `shortestJobF.py`: Shortest Job First.  
    - `shortestRemT.py`: Shortest Remaining Time.
  
  - `sincronizacion/`: Algoritmos de sincronización.  
    - `mutex.py`: Implementación con exclusión mutua.  
    - `semaforo.py`: Sincronización con semáforos.

- `input/`: Carpeta para entrada de datos
    - `acciones.txt`
    - `procesos.txt`
    - `recursos.txt`

- `chart.py`: Módulo para generación de gráficas 

- `file_reader.py`: Módulo para lectura de archivos de entrada.

- `gui.py`: Interfaz gráfica del usuario para interactuar con el sistema.


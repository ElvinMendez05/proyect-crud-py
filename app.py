import sys
sys.path.append('./src/my_project')  # Asegúrate de que esta ruta sea correcta

# Importa el archivo crud.py como módulo (sin .py)
import crud

# Si CrudApp es una clase definida dentro de crud.py, accedemos a ella con 'crud.CrudApp'
from tkinter import Tk  # Asegúrate de importar Tkinter
root = Tk()
app = crud.CrudApp(root)  # Asumiendo que CrudApp está en crud.py
root.mainloop()
 

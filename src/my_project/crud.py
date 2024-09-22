from tkinter import *
from tkinter import messagebox
import sqlite3

class CrudApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario de registro F1 y Crud de datos")
        self.root.iconbitmap("public/assets/f1.ico")
        self.root.config(bg="grey")
        
        self.cuadros_id = StringVar()
        self.cuadros_nombre = StringVar()
        self.cuadros_apellido = StringVar()
        self.cuadros_direccion = StringVar()
        self.cuadros_password = StringVar()

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        
        barra_menu = Menu(self.root)
        self.root.config(menu=barra_menu, width=300, height=300)

        bbdd_menu = Menu(barra_menu, tearoff=0)
        bbdd_menu.add_command(label="Conectar", command=self.conectar_base)
        bbdd_menu.add_command(label="Salir", command=self.salir_crud)

        borrar_menu = Menu(barra_menu, tearoff=0)
        borrar_menu.add_command(label="Borrar", command=self.borrar_datos)

        crud_menu = Menu(barra_menu, tearoff=0)
        crud_menu.add_command(label="Create", command=self.crear_datos)
        crud_menu.add_separator()
        crud_menu.add_command(label="Read", command=self.leer_datos)
        crud_menu.add_separator()
        crud_menu.add_command(label="Update", command=self.actualizar_datos)
        crud_menu.add_separator()
        crud_menu.add_command(label="Delete", command=self.eliminar_datos)

        ayuda_menu = Menu(barra_menu, tearoff=0)
        ayuda_menu.add_command(label="Licencia")
        ayuda_menu.add_command(label="Acerca de")

        barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
        barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
        barra_menu.add_cascade(label="Crud", menu=crud_menu)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

    def create_widgets(self):
        frame = Frame(self.root)
        frame.pack()

        Label(frame, text="Id: ").grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.cuadro_id = Entry(frame, textvariable=self.cuadros_id)
        self.cuadro_id.grid(row=0, column=1, padx=10, pady=10)
        self.cuadro_id.config(fg="grey", justify="center")

        Label(frame, text="Nombre: ").grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.cuadro_nombre = Entry(frame, textvariable=self.cuadros_nombre)
        self.cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
        self.cuadro_nombre.config(fg="grey", justify="center")

        Label(frame, text="Apellido: ").grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.cuadro_apellido = Entry(frame, textvariable=self.cuadros_apellido)
        self.cuadro_apellido.grid(row=2, column=1, padx=10, pady=10)
        self.cuadro_apellido.config(fg="grey", justify="center")

        Label(frame, text="Direccion: ").grid(row=3, column=0, sticky="e", padx=10, pady=10)
        self.cuadro_direccion = Entry(frame, textvariable=self.cuadros_direccion)
        self.cuadro_direccion.grid(row=3, column=1, padx=10, pady=10)
        self.cuadro_direccion.config(fg="grey", justify="center")

        Label(frame, text="Password: ").grid(row=4, column=0, sticky="e", padx=10, pady=10)
        self.cuadro_password = Entry(frame, textvariable=self.cuadros_password)
        self.cuadro_password.grid(row=4, column=1, padx=10, pady=10)
        self.cuadro_password.config(fg="grey", justify="center", show="*")

        Label(frame, text="Comentarios: ").grid(row=5, column=0, sticky="e", padx=10, pady=10)
        self.texto_comentario = Text(frame, width=20, height=10)
        self.texto_comentario.grid(row=5, column=1, padx=10, pady=10)
        scrollvert = Scrollbar(frame, command=self.texto_comentario.yview)
        scrollvert.grid(row=5, column=2, sticky="nsew")
        self.texto_comentario.config(yscrollcommand=scrollvert.set)

        btns_frame = Frame(self.root)
        btns_frame.pack()
        Button(btns_frame, text="Create", command=self.crear_datos).grid(row=1, column=0, sticky="e", padx=16, pady=10)
        Button(btns_frame, text="Read", command=self.leer_datos).grid(row=1, column=1, sticky="e", padx=16, pady=10)
        Button(btns_frame, text="Update", command=self.actualizar_datos).grid(row=1, column=2, sticky="e", padx=16, pady=10)
        Button(btns_frame, text="Delete", command=self.eliminar_datos).grid(row=1, column=3, sticky="e", padx=15, pady=10)

    # Métodos CRUD
    def conectar_base(self):
        conexion = sqlite3.connect("Usuarios")
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                CREATE TABLE DATOSUSUARIOS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    NOMBRE_USUARIO VARCHAR(20),
                    APELLIDO VARCHAR(50),
                    DIRECCION VARCHAR(50),
                    PASSWORD VARCHAR(20),
                    COMENTARIOS VARCHAR(100))
            """)
            messagebox.showinfo("BBDD", "BBDD creada con éxito")
        except:
            messagebox.showwarning("Atención!", "La BBDD ya existe")
        finally:
            conexion.close()

    def salir_crud(self):
        valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
        if valor == "yes":
            self.root.destroy()

    def borrar_datos(self):
        self.cuadros_id.set("")
        self.cuadros_nombre.set("")
        self.cuadros_apellido.set("")
        self.cuadros_direccion.set("")
        self.cuadros_password.set("")
        self.texto_comentario.delete(1.0, END)

    def crear_datos(self):
        conexion = sqlite3.connect("Usuarios")
        cursor = conexion.cursor()

        datos = (
            self.cuadros_nombre.get(),
            self.cuadros_apellido.get(),
            self.cuadros_direccion.get(),
            self.cuadros_password.get(),
            self.texto_comentario.get("1.0", END)
        )

        cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", datos)
        conexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con éxito")
        conexion.close()

    def leer_datos(self):
        conexion = sqlite3.connect("Usuarios")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + self.cuadros_id.get())
        el_usuario = cursor.fetchall()

        for usuario in el_usuario:
            self.cuadros_nombre.set(usuario[1])
            self.cuadros_apellido.set(usuario[2])
            self.cuadros_direccion.set(usuario[3])
            self.cuadros_password.set(usuario[4])
            self.texto_comentario.insert(1.0, usuario[5])

        conexion.commit()
        conexion.close()

    def actualizar_datos(self):
        conexion = sqlite3.connect("Usuarios")
        cursor = conexion.cursor()

        datos = (
            self.cuadros_nombre.get(),
            self.cuadros_apellido.get(),
            self.cuadros_direccion.get(),
            self.cuadros_password.get(),
            self.texto_comentario.get("1.0", END)
        )

        cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,APELLIDO=?,DIRECCION=?,PASSWORD=?,COMENTARIOS=? " +
                       "WHERE ID=" + self.cuadros_id.get(), datos)
        conexion.commit()
        messagebox.showinfo("BBDD", "Datos actualizados correctamente")
        conexion.close()

    def eliminar_datos(self):
        conexion = sqlite3.connect("Usuarios")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + self.cuadros_id.get())
        conexion.commit()
        messagebox.showinfo("BBDD", "Registro borrado con éxito")
        conexion.close()

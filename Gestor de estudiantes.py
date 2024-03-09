import tkinter as tk
from tkinter import simpledialog, messagebox

class Estudiante:
    def __init__(self, cedula, nombre, apellido, edad, nota1, nota2, nota3):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota_final = (nota1 + nota2 + nota3) / 3
        self.historial = []

    def obtener_datos(self):
        return f"No. Cedula: {self.cedula} - {self.nombre} {self.apellido} - Nota Final: {self.nota_final:.2f}"

    def editar_notas(self, nota1, nota2, nota3):
        self.nota1, self.nota2, self.nota3 = nota1, nota2, nota3
        self.nota_final = (nota1 + nota2 + nota3) / 3
        return "Registro Exitoso!"

    def incluir_evento(self, nota1, nota2, nota3):
        return f"Modificación - Nota_1: {nota1} Nota_2: {nota2} Nota_3: {nota3}"

    def obtener_historial(self):
        return f"No. Cedula: {self.cedula} - {self.nombre} {self.apellido}"

class Gestor_Estudiantes:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Estudiantes")
        self.master.geometry("800x200")
        self.master.configure(bg="#aa91c2")

        self.lista_estudiantes = []

        self.menu_frame = tk.Frame(self.master, bg="#aa91c2")
        self.menu_frame.pack(pady=20)

        opciones = [
            ("Registrar Estudiante", self.registrar_estudiante),
            ("Mostrar Estudiantes", self.listado_estudiantes),
            ("Buscar Estudiante", self.buscar_estudiante),
            ("Modificar Notas", self.modificar_notas),
            ("Consultar Historial", self.consultar_historial),
            ("Salir", self.salir)
        ]

        for texto, comando in opciones:
            tk.Button(self.menu_frame, text=texto, command=comando, bg="#4CAF50", fg="white", padx=10, pady=20).pack(side=tk.LEFT, padx=10,fill=tk.BOTH)

    def registrar_estudiante(self):
        cedula = simpledialog.askinteger("Registro de Estudiantes", "Ingrese el numero de cedula:")
        nombre = simpledialog.askstring("Registro de Estudiantes", "Ingrese el nombre:")
        apellido = simpledialog.askstring("Registro de Estudiantes", "Ingrese el apellido:")
        edad = simpledialog.askinteger("Registro de Estudiantes", "Ingrese su edad:")
        nota1 = simpledialog.askfloat("Registro de Estudiantes", "Ingrese nota 1:")
        nota2 = simpledialog.askfloat("Registro de Estudiantes", "Ingrese nota 2:")
        nota3 = simpledialog.askfloat("Registro de Estudiantes", "Ingrese nota 3:")
        obj_alumno = Estudiante(cedula, nombre, apellido, edad, nota1, nota2, nota3)
        self.lista_estudiantes.append(obj_alumno)

    def listado_estudiantes(self):
        result = "\n".join([obj_alumno.obtener_datos() for obj_alumno in self.lista_estudiantes])
        messagebox.showinfo("Listado de Estudiantes", result)

    def buscar_estudiante(self):
        cedula = simpledialog.askinteger("Buscar Estudiante", "Ingrese el numero de cedula a buscar:")
        result = ""
        for obj_alumno in self.lista_estudiantes:
            if cedula == obj_alumno.cedula:
                result = obj_alumno.obtener_datos()
        messagebox.showinfo("Buscar Estudiante", result)

    def modificar_notas(self):
        cedula = simpledialog.askinteger("Modificar Notas", "Ingrese el numero de cedula a buscar:")
        result = ""
        for obj_alumno in self.lista_estudiantes:
            if cedula == obj_alumno.cedula:
                nota1 = simpledialog.askfloat("Modificar Notas", "Ingrese nueva nota 1:")
                nota2 = simpledialog.askfloat("Modificar Notas", "Ingrese nueva nota 2:")
                nota3 = simpledialog.askfloat("Modificar Notas", "Ingrese nueva nota 3:")
                result = obj_alumno.editar_notas(nota1, nota2, nota3)
                obj_alumno.obtener_datos()
                recepcion_mensaje = obj_alumno.incluir_evento(nota1, nota2, nota3)
                obj_alumno.historial.append(recepcion_mensaje)
        messagebox.showinfo("Modificar Notas", result)

    def consultar_historial(self):
        cedula = simpledialog.askinteger("Consultar Historial", "Ingrese el numero de cedula a buscar:")
        result = ""
        for obj_alumno in self.lista_estudiantes:
            if cedula == obj_alumno.cedula:
                result = "\n".join(obj_alumno.historial)
        messagebox.showinfo("Consultar Historial", result)

    def salir(self):
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = Gestor_Estudiantes(root)
    root.mainloop()

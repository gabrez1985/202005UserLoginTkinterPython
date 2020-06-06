from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from SqliteDefinitions4TkinterUserLoginV01 import *
import re

root = Tk()
root.title("Private File System")
root.geometry('400x400')

EntryUsuario = StringVar()
EntryClave1 = StringVar()
EntryClave2 = StringVar()
treeviewfilesusuario = StringVar()
EntryCrear = StringVar
EntryAbrir = StringVar
EntryEliminar = StringVar
usuarioingresado = StringVar
EditorDeTexto = StringVar
filedetails = StringVar
nombrefile = StringVar


def callback(event):
    global treeviewfilesusuario
    global EntryAbrir
    global EntryEliminar
    EntryAbrir.delete(0, END)
    EntryEliminar.delete(0, END)
    fileselection = treeviewfilesusuario.selection()[0]
    EntryAbrir.insert(0, fileselection)
    EntryEliminar.insert(0, fileselection)


def IrAPantallaDeInicioPrograma():
    global EntryUsuario
    global EntryClave1

    for widget in root.winfo_children():
        widget.destroy()

    LabelTextoInicial = Label(root, text='Introduzca su usuario y Contraseña')
    LabelTextoInicial.grid(row=0, column=0, columnspan=2)

    LabelUsuario = Label(root, text='Usuario')
    LabelUsuario.grid(row=1, column=0)

    LabelClave1 = Label(root, text='Contraseña')
    LabelClave1.grid(row=2, column=0)

    EntryUsuario = Entry(root)
    EntryUsuario.grid(row=1, column=1)

    EntryClave1 = Entry(root)
    EntryClave1.grid(row=2, column=1)

    BotonCrearUsuario = Button(root, text='Crear Usuario',
                               command=IrAPantallaCreacionDeUsuario)
    BotonCrearUsuario.grid(row=4, column=0)

    BotonIngresar = Button(root, text='Ingresar', command=InicioUsuario)
    BotonIngresar.grid(row=3, column=1)


def CrearUsuario():
    usuarioingresado = EntryUsuario.get()
    claveingresada1 = EntryClave1.get()
    claveingresada2 = EntryClave2.get()

    try:
        queryuserpassword(usuarioingresado)
        usuarioexiste = 'SI'
    except:
        usuarioexiste = 'NO'

    if claveingresada1 != claveingresada2:
        messagebox.showinfo('Error en Clave',
                            "Verifique que haya ingresado la clave"
                            + " correctamente en las dos casillas")
    elif usuarioexiste == "SI":
        messagebox.showinfo('Error en Usuario',
                            "Nombre de Usuario ya existe, "
                            + "por favor escoger otro nombre de usuario")
    elif usuarioingresado == "" or claveingresada1 == "":
        messagebox.showinfo('Error en Datos Ingresados',
                            "No dejar vacio nombre de usuario "
                            + "ni clave")
    else:
        insertnewuserpassword(usuarioingresado, claveingresada1)
        messagebox.showinfo('Usuario Creado',
                            "Usuario Creado Correctamente")
        IrAPantallaDeInicioPrograma()


def IrAPantallaCreacionDeUsuario():
    global EntryUsuario
    global EntryClave1
    global EntryClave2

    for widget in root.winfo_children():
        widget.destroy()

    LabelTextoInicial = Label(root, text='Introduzca nombre de usuario y clave')
    LabelTextoInicial.grid(row=0, column=0, columnspan=2)

    LabelUsuario = Label(root, text='Usuario')
    LabelUsuario.grid(row=1, column=0)

    LabelClave1 = Label(root, text='Contraseña')
    LabelClave1.grid(row=2, column=0)

    LabelClave2 = Label(root, text='Repita Contraseña')
    LabelClave2.grid(row=3, column=0)

    EntryUsuario = Entry(root)
    EntryUsuario.grid(row=1, column=1)

    EntryClave1 = Entry(root)
    EntryClave1.grid(row=2, column=1)

    EntryClave2 = Entry(root)
    EntryClave2.grid(row=3, column=1)

    BotonCrearUsuario = Button(root, text='Crear Usuario', command=CrearUsuario)
    BotonCrearUsuario.grid(row=4, column=1)


def InicioUsuario():
    usuarioingresado = EntryUsuario.get()
    claveingresada1 = EntryClave1.get()

    try:
        clavedeusuarioregistrada = queryuserpassword(usuarioingresado)
        if claveingresada1 == clavedeusuarioregistrada:
            insertusernewtimelog(usuarioingresado, 'Ingreso Usuario', 'Clave Correcta')
            IrAPantallaDeInicioDeUsuario()
        else:
            messagebox.showinfo('Clave Incorrecta',
                                "Clave no es correcta, volver a intentar")
            insertusernewtimelog(usuarioingresado, 'Intento de Acceso', 'Clave Incorrecta')
    except:
        messagebox.showinfo('Usuario No Existe',
                            "Nombre de Usuario No existe")


def IrAPantallaDeInicioDeUsuario():
    global treeviewfilesusuario
    global EntryCrear
    global EntryAbrir
    global EntryEliminar
    global usuarioingresado

    try:
        usuarioingresado = EntryUsuario.get()
    except:
        pass

    for widget in root.winfo_children():
        widget.destroy()

    LabelTextoInicial = Label(
                              root, text='Hola ' + usuarioingresado +
                              ', bienvenido a tus archivos seguros')
    LabelTextoInicial.grid(row=0, column=0, columnspan=2)

    LabelCrear = Label(root, text='Ingrese Nombre de Archivo')
    LabelCrear.grid(row=1, column=0)

    LabelAbrir = Label(root, text='Seleccionar de lista')
    LabelAbrir.grid(row=2, column=0)

    LabelEliminar = Label(root, text='Seleccionar de lista')
    LabelEliminar.grid(row=3, column=0)

    EntryCrear = Entry(root)
    EntryCrear.grid(row=1, column=1)

    EntryAbrir = Entry(root)
    EntryAbrir.grid(row=2, column=1)

    EntryEliminar = Entry(root)
    EntryEliminar.grid(row=3, column=1)

    BotonCrear = Button(root, text='Crear', command=CrearFile)
    BotonCrear.grid(row=1, column=2)

    BotonAbrir = Button(root, text='Abrir', command=AbrirFile)
    BotonAbrir.grid(row=2, column=2)

    BotonEliminar = Button(root, text='Eliminar', command=EliminarFile)
    BotonEliminar.grid(row=3, column=2)

    BotonHistoricoLogeos = Button(root, text='Historico Logeos',
                                  command=IrAPantallaDeHistoricoLogeos)
    BotonHistoricoLogeos.grid(row=0, column=3)

    treeviewfilesusuario = ttk.Treeview(root)
    treeviewfilesusuario.grid(row=5, column=0)
    listafilesusuario = queryuserfiles(usuarioingresado)

    for files in listafilesusuario:
        treeviewfilesusuario.insert('', 'end', files[0], text=files[0])

    treeviewfilesusuario.bind('<<TreeviewSelect>>', callback)


def CrearFile():
    global filedetails
    global nombrefile
    nombrefile = EntryCrear.get()
    filedetails = queryuserfiledetails(usuarioingresado, nombrefile)

    if len(filedetails) == 0 and nombrefile != "" and nombrefile != " ":
        filedetails = ""
        insertusernewfile(usuarioingresado, nombrefile, filedetails)
        insertusernewtimelog(usuarioingresado, "Creacion File", nombrefile)
        IrAPantallaEditorDeFile()
    elif nombrefile == "" or nombrefile == " ":
        messagebox.showinfo('Error Nombre',
                            "Nombre no valido")
    else:
        messagebox.showinfo('Error Nombre',
                            "Nombre repetido, por favor cambiar nombre")


def AbrirFile():
    global filedetails
    global nombrefile
    nombrefile = EntryAbrir.get()
    filedetails = queryuserfiledetails(usuarioingresado, nombrefile)

    if len(filedetails) == 0:
        filedetails = ""
        messagebox.showinfo('Error Nombre',
                            "File Ingresado No Existe")
    else:
        insertusernewtimelog(usuarioingresado, "Acceso File", nombrefile)
        filedetails = filedetails[0][0]
        IrAPantallaEditorDeFile()


def GrabarArchivo():
    filedetails = EditorDeTexto.get('1.0', 'end')
    updateuserfile(usuarioingresado, nombrefile, filedetails)
    insertusernewtimelog(usuarioingresado, "Edicion File", nombrefile)
    messagebox.showinfo('File Grabado',
                        "Sus cambios han sido grabados")


def EliminarFile():
    nombrefile = EntryEliminar.get()
    resultadoquery = queryuserfiledetails(usuarioingresado, nombrefile)

    if len(resultadoquery) == 0:
        messagebox.showinfo('Error Nombre',
                            "No cuenta con un File con el nombre indicado")
    else:
        deleteuserfile(usuarioingresado, nombrefile)
        insertusernewtimelog(usuarioingresado, 'File Eliminado',
                             nombrefile)
        messagebox.showinfo('File Eliminado',
                            "File Eliminado, su lista de file se ha actualizado")
        IrAPantallaDeInicioDeUsuario()


def IrAPantallaEditorDeFile():
    global EditorDeTexto
    for widget in root.winfo_children():
        widget.destroy()
    EditorDeTexto = Text(root)
    EditorDeTexto.insert(END, filedetails)
    EditorDeTexto.grid(row=0, column=0, padx=50, pady=100)

    BotonGrabar = Button(root, text='Grabar', command=GrabarArchivo)
    BotonGrabar.grid(row=1, column=0)

    BotonVolver = Button(root, text='Volver',
                         command=IrAPantallaDeInicioDeUsuario)
    BotonVolver.grid(row=1, column=1)


def IrAPantallaDeHistoricoLogeos():
    for widget in root.winfo_children():
        widget.destroy()

    BotonVolver = Button(root, text='Volver',
                         command=IrAPantallaDeInicioDeUsuario)
    BotonVolver.grid(row=0, column=4)

    treeviewhistoricologeos = ttk.Treeview(root, columns=('Usuario',
                                           'TipoLog', 'DetallesLog',
                                                          'FechaHoraLog'))
    treeviewhistoricologeos.grid(row=1, column=0)
    treeviewhistoricologeos.config(height=20)
    treeviewhistoricologeos.heading('Usuario', text='Usuario')
    treeviewhistoricologeos.heading('TipoLog', text='TipoLog')
    treeviewhistoricologeos.heading('DetallesLog', text='DetallesLog')
    treeviewhistoricologeos.heading('FechaHoraLog', text='FechaHoraLog')

    userhistoriclogs = queryuserhistoriclogs(usuarioingresado)

    for log in userhistoriclogs:
        treeviewhistoricologeos.insert('', '0', log[0], text=log[0])
        treeviewhistoricologeos.set(log[0], 'Usuario', log[1])
        treeviewhistoricologeos.set(log[0], 'TipoLog', log[2])
        treeviewhistoricologeos.set(log[0], 'DetallesLog', log[3])
        treeviewhistoricologeos.set(log[0], 'FechaHoraLog', log[4])


# -------------------- Aca inicia el programa --------------------
try:
    createuserspasswordtable()
    createusersfilestable()
    createuserslogintimestable()
except:
    pass

IrAPantallaDeInicioPrograma()


root.mainloop()

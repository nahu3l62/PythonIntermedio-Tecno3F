import tkinter as tk
from tkinter import ttk
from Servicios.ServiciosPropietario import *
from Clases.Propietario import *


def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu=barra, width=300, height=300)
    menu_inquilino = tk.Menu(barra, tearoff=0)
    menu_propietario = tk.Menu(barra, tearoff=0)
    menu_contrato = tk.Menu(barra, tearoff=0)

    barra.add_cascade(label='Inquilino', menu=menu_inquilino)
    barra.add_cascade(label='Propietario', menu=menu_propietario)
    barra.add_cascade(label='Contrato', menu=menu_contrato)
    
    #submenu
    menu_inquilino.add_command(label='CRUD Inquilino')
    menu_propietario.add_command(label='CRUD Propietario')
    menu_contrato.add_command(label='CRUD Contrato', command= root.destroy)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=1000, height=1000)
        self.root = root
        self.pack()
        self.config(bg='white')
        self.id_inquilino = None
        
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.config(font=('Arial', 12, 'bold'))
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)

        self.label_dni = tk.Label(self, text="DNI: ")
        self.label_dni.config(font=('Arial', 12, 'bold'))
        self.label_dni.grid(row=2, column=0, padx=10, pady=10)

        self.label_cuil = tk.Label(self, text="CUIL: ")
        self.label_cuil.config(font=('Arial', 12, 'bold'))
        self.label_cuil.grid(row=3, column=0, padx=10, pady=10)

        self.label_domicilio = tk.Label(self, text="Domicilio: ")
        self.label_domicilio.config(font=('Arial', 12, 'bold'))
        self.label_domicilio.grid(row=4, column=0, padx=10, pady=10)

        self.label_email = tk.Label(self, text="Email: ")
        self.label_email.config(font=('Arial', 12, 'bold'))
        self.label_email.grid(row=5, column=0, padx=10, pady=10)

    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10,
                               pady=10, columnspan='2')

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self, textvariable=self.apellido)
        self.entry_apellido.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_apellido.grid(
            row=1, column=1, padx=10, pady=10, columnspan='2')

        self.dni = tk.StringVar()
        self.entry_dni = tk.Entry(self, textvariable=self.dni)
        self.entry_dni.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_dni.grid(
            row=2, column=1, padx=10, pady=10, columnspan='2')

        self.cuil = tk.StringVar()
        self.entry_cuil = tk.Entry(self, textvariable=self.cuil)
        self.entry_cuil.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_cuil.grid(
            row=3, column=1, padx=10, pady=10, columnspan='2')

        self.domicilio = tk.StringVar()
        self.entry_domicilio = tk.Entry(self, textvariable=self.domicilio)
        self.entry_domicilio.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_domicilio.grid(
            row=4, column=1, padx=10, pady=10, columnspan='2')

        self.email = tk.StringVar()
        self.entry_email = tk.Entry(self, textvariable=self.email)
        self.entry_email.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_email.grid(
            row=5, column=1, padx=10, pady=10, columnspan='2')


    def botones_principales(self):
        self.btn_alta = tk.Button(
            self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B',
                             cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=8, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83',
                             cursor='hand2', activebackground='#7594F5', activeforeground='#000000', state='disabled')
        self.btn_modi.grid(row=8, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(
            self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A',
                              cursor='hand2', activebackground='#F35B5B', activeforeground='#000000', state='disabled')
        self.btn_cance.grid(row=8, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_cuil.config(state='normal')
        self.entry_domicilio.config(state='normal')
        self.entry_email.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_cuil.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        self.entry_email.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.nombre.set('')
        self.apellido.set('')
        self.dni.set('')
        self.cuil.set('')
        self.domicilio.set('')
        self.email.set('')
        self.btn_alta.config(state='normal')

    def mostrar_tabla(self):
        self.lista_inquilinos = consultaInquilino()

        self.lista_inquilinos.reverse()

        self.tabla = ttk.Treeview(self, columns=(
            'Nombre', 'Apellido', 'DNI', 'CUIL', 'Domicilio', 'Email'))
        self.tabla.grid(row=9, column=0, columnspan=4, sticky='nse')

        self.scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=9, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Apellido')
        self.tabla.heading('#3', text='DNI')
        self.tabla.heading('#4', text='CUIL')
        self.tabla.heading('#5', text='Domicilio')
        self.tabla.heading('#6', text='Email')

        for i in self.lista_inquilinos:
            self.tabla.insert('', 0, text=i[0],
                              values=(i[1], i[2], i[3], i[4], i[5], i[6])

                              )

        self.btn_editar = tk.Button(
            self, text='Editar', command=self.editar_registro)
        self.btn_editar.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B',
                               cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=10, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(
            self, text='Borrar', command=self.eliminar_registro)
        self.btn_delete.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A',
                               cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_delete.grid(row=10, column=1, padx=10, pady=10)

    def guardar_campos(self):
        inquilino = Inquilino(
            self.nombre.get(),
            self.apellido.get(),
            self.dni.get(),
            self.cuil.get(),
            self.domicilio.get(),
            self.email.get(),
        )

        if self.id_inquilino == None:
            guardarInquilino(inquilino)
        else:
            actualizarInquilino(inquilino, self.id_inquilino)

        self.mostrar_tabla()
        self.bloquear_campos()

    def editar_registro(self):
        try:
            self.id_inquilino = self.tabla.item(self.tabla.selection())['text']

            self.nombre_inqui = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.apellido_inqui = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.dni_inqui = self.tabla.item(
                self.tabla.selection())['values'][2]
            self.cuil_inqui = self.tabla.item(
                self.tabla.selection())['values'][3]
            self.domicilio_inqui = self.tabla.item(
                self.tabla.selection())['values'][4]
            self.email_inqui = self.tabla.item(
                self.tabla.selection())['values'][5]

            self.habilitar_campos()
            
            self.nombre.set(self.nombre_inqui)
            self.apellido.set(self.apellido_inqui)
            self.dni.set(self.dni_inqui)
            self.cuil.set(self.cuil_inqui)
            self.domicilio.set(self.domicilio_inqui)
            self.email.set(self.email_inqui)
            
        
            #actualizarInquilino(inquilino2, self.id_inquilino)
            
        except:
            pass

    def eliminar_registro(self):
        try:
            self.id_inquilino = self.tabla.item(self.tabla.selection())['text']
            borrarInquilino(int(self.id_inquilino))
            self.mostrar_tabla()
            self.id_inquilino = None #reseteanis el id luego de eliminar
        except:
            pass

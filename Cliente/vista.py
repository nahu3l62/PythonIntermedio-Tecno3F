import tkinter as tk
from tkinter import ttk
from Servicios.ServiciosInquilino import *
from Clases.Inquilino import *
from Clases.Propietario import *
from Servicios.ServiciosPropietario import *
from Servicios.ServiciosContrato import *




       
def iniciar():
    window = tk.Tk()
    
    notebook = ttk.Notebook(window)
    
    tab1 = Frame(notebook)
    tab2 = Frame(notebook)
    tab3 = Frame(notebook)
    
    notebook.add(tab1, text="CRUD Inquilino")
    tab1.iniciarInquilino()
    notebook.add(tab2, text="CRUD Propietario")
    tab2.iniciarPropietario()
    notebook.add(tab3, text="CRUD Contrato")
    tab3.iniciarContrato()
    notebook.pack()
    
    window.mainloop()
    
    
    
    

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=800, height=800)
        self.root = root
        self.pack()
        self.config(bg='white')
        
    def iniciarInquilino(self):
        self.id_inquilino = None
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()     
        
    def iniciarPropietario(self):
        self.id_propietario = None
        self.label_form_propietario()
        self.input_form_propietario()
        self.botones_principales_propietario()
        self.mostrar_tabla_propietario()      
        
    def iniciarContrato(self):
        self.id_contrato = None
        self.label_form_contrato()
        self.input_form_contrato()
        self.botones_principales_contrato()
        self.mostrar_tabla_contrato()    
        
 
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
            
        except:
            pass
        
    def eliminar_registro(self):
        try:
            self.id_inquilino = self.tabla.item(self.tabla.selection())['text']
            borrarInquilino(int(self.id_inquilino))
            self.mostrar_tabla()
            self.id_inquilino = None 
        except:
            pass    
        
        
        
    def habilitar_campos_prope(self):
        self.entry_nombre_prope.config(state='normal')
        self.entry_apellido_prope.config(state='normal')
        self.entry_dni_prope.config(state='normal')
        self.entry_cuil_prope.config(state='normal')
        self.entry_domicilio_prope.config(state='normal')
        self.entry_email_prope.config(state='normal')
        self.btn_modi_prope.config(state='normal')
        self.btn_cance_prope.config(state='normal')
        self.btn_alta_prope.config(state='disabled')

    def bloquear_campos_prope(self):
        self.entry_nombre_prope.config(state='disabled')
        self.entry_apellido_prope.config(state='disabled')
        self.entry_dni_prope.config(state='disabled')
        self.entry_cuil_prope.config(state='disabled')
        self.entry_domicilio_prope.config(state='disabled')
        self.entry_email_prope.config(state='disabled')
        self.btn_modi_prope.config(state='disabled')
        self.btn_cance_prope.config(state='disabled')
        self.nombre_prope.set('')
        self.apellido_prope.set('')
        self.dni_prope.set('')
        self.cuil_prope.set('')
        self.domicilio_prope.set('')
        self.email_prope.set('')
        self.btn_alta_prope.config(state='normal')    
        
       
    def label_form_propietario(self):
        self.label_nombre_prope = tk.Label(self, text="Nombre: ")
        self.label_nombre_prope.config(font=('Arial', 12, 'bold'))
        self.label_nombre_prope.grid(row=0, column=0, padx=10, pady=10)

        self.label_apellido_prope = tk.Label(self, text="Apellido: ")
        self.label_apellido_prope.config(font=('Arial', 12, 'bold'))
        self.label_apellido_prope.grid(row=1, column=0, padx=10, pady=10)

        self.label_dni_prope = tk.Label(self, text="DNI: ")
        self.label_dni_prope.config(font=('Arial', 12, 'bold'))
        self.label_dni_prope.grid(row=2, column=0, padx=10, pady=10)

        self.label_cuil_prope = tk.Label(self, text="CUIL: ")
        self.label_cuil_prope.config(font=('Arial', 12, 'bold'))
        self.label_cuil_prope.grid(row=3, column=0, padx=10, pady=10)

        self.label_domicilio_prope = tk.Label(self, text="Domicilio: ")
        self.label_domicilio_prope.config(font=('Arial', 12, 'bold'))
        self.label_domicilio_prope.grid(row=4, column=0, padx=10, pady=10)

        self.label_email_prope = tk.Label(self, text="Email: ")
        self.label_email_prope.config(font=('Arial', 12, 'bold'))
        self.label_email_prope.grid(row=5, column=0, padx=10, pady=10)

    def input_form_propietario(self):
        self.nombre_prope = tk.StringVar()
        self.entry_nombre_prope= tk.Entry(self, textvariable=self.nombre_prope)
        self.entry_nombre_prope.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_nombre_prope.grid(row=0, column=1, padx=10,
                               pady=10, columnspan='2')

        self.apellido_prope = tk.StringVar()
        self.entry_apellido_prope = tk.Entry(self, textvariable=self.apellido_prope)
        self.entry_apellido_prope.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_apellido_prope.grid(
            row=1, column=1, padx=10, pady=10, columnspan='2')

        self.dni_prope = tk.StringVar()
        self.entry_dni_prope = tk.Entry(self, textvariable=self.dni_prope)
        self.entry_dni_prope.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_dni_prope.grid(
            row=2, column=1, padx=10, pady=10, columnspan='2')

        self.cuil_prope = tk.StringVar()
        self.entry_cuil_prope = tk.Entry(self, textvariable=self.cuil_prope)
        self.entry_cuil_prope.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_cuil_prope.grid(
            row=3, column=1, padx=10, pady=10, columnspan='2')

        self.domicilio_prope = tk.StringVar()
        self.entry_domicilio_prope = tk.Entry(self, textvariable=self.domicilio_prope)
        self.entry_domicilio_prope.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_domicilio_prope.grid(
            row=4, column=1, padx=10, pady=10, columnspan='2')

        self.email_prope = tk.StringVar()
        self.entry_email_prope = tk.Entry(self, textvariable=self.email_prope)
        self.entry_email_prope.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_email_prope.grid(
            row=5, column=1, padx=10, pady=10, columnspan='2') 
       
       
    def editar_registro_propietario(self):
        try:
            self.id_propietario = self.tabla_prope.item(self.tabla_prope.selection())['text']
            
            print(self.id_propietario)

            self.nombre_prope_edit = self.tabla_prope.item(
                self.tabla_prope.selection())['values'][0]
            self.apellido_prope_edit  = self.tabla_prope.item(
                self.tabla_prope.selection())['values'][1]
            self.dni_prope_edit  = self.tabla_prope.item(
                self.tabla_prope.selection())['values'][2]
            self.cuil_prope_edit = self.tabla_prope.item(
                self.tabla_prope.selection())['values'][3]
            self.domicilio_prope_edit  = self.tabla_prope.item(
                self.tabla_prope.selection())['values'][4]
            self.email_prope_edit  = self.tabla_prope.item(
                self.tabla_prope.selection())['values'][5]

            self.habilitar_campos_prope()
            
            self.nombre_prope.set(self.nombre_prope_edit )
            self.apellido_prope.set(self.apellido_prope_edit )
            self.dni_prope.set(self.dni_prope_edit)
            self.cuil_prope.set(self.cuil_prope_edit )
            self.domicilio_prope.set(self.domicilio_prope_edit )
            self.email_prope.set(self.email_prope_edit)
            
        except:
            pass   
       
        
    def botones_principales_propietario(self):
        self.btn_alta_prope = tk.Button(
            self, text='Nuevo', command=self.habilitar_campos_prope)
        self.btn_alta_prope.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B',
                             cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta_prope.grid(row=8, column=0, padx=10, pady=10)

        self.btn_modi_prope = tk.Button(self, text='Guardar', command=self.guardar_campos_propietario)
        self.btn_modi_prope.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83',
                             cursor='hand2', activebackground='#7594F5', activeforeground='#000000', state='disabled')
        self.btn_modi_prope.grid(row=8, column=1, padx=10, pady=10)

        self.btn_cance_prope = tk.Button(
            self, text='Cancelar', command=self.bloquear_campos_prope)
        self.btn_cance_prope.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A',
                              cursor='hand2', activebackground='#F35B5B', activeforeground='#000000', state='disabled')
        self.btn_cance_prope.grid(row=8, column=2, padx=10, pady=10)    
        
        
    def guardar_campos_propietario(self):
        propietario = Propietario(
            self.nombre_prope.get(),
            self.apellido_prope.get(),
            self.dni_prope.get(),
            self.cuil_prope.get(),
            self.domicilio_prope.get(),
            self.email_prope.get(),
        )

        if self.id_propietario == None:
            guardarPropietario(propietario)
        else:
            actualizarPropietario(propietario, self.id_propietario)

        self.mostrar_tabla_propietario()
        self.bloquear_campos_prope()


    def mostrar_tabla_propietario(self):
        self.lista_propietario = consultaPropietario()

        self.lista_propietario.reverse()

        self.tabla_prope = ttk.Treeview(self, columns=(
            'Nombre', 'Apellido', 'DNI', 'CUIL', 'Domicilio', 'Email'))
        self.tabla_prope.grid(row=9, column=0, columnspan=4, sticky='nse')

        self.scroll_prope = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla_prope.yview)
        self.scroll_prope.grid(row=9, column=4, sticky='nse')
        self.tabla_prope.configure(yscrollcommand=self.scroll_prope.set)

        self.tabla_prope.heading('#0', text='ID')
        self.tabla_prope.heading('#1', text='Nombre')
        self.tabla_prope.heading('#2', text='Apellido')
        self.tabla_prope.heading('#3', text='DNI')
        self.tabla_prope.heading('#4', text='CUIL')
        self.tabla_prope.heading('#5', text='Domicilio')
        self.tabla_prope.heading('#6', text='Email')

        for i in self.lista_propietario:
            self.tabla_prope.insert('', 0, text=i[0],
                              values=(i[1], i[2], i[3], i[4], i[5], i[6])

                              )

        self.btn_editar_prope = tk.Button(
            self, text='Editar', command=self.editar_registro_propietario)
        self.btn_editar_prope.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B',
                               cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar_prope.grid(row=10, column=0, padx=10, pady=10)

        self.btn_delete_prope = tk.Button(
            self, text='Borrar', command=self.eliminar_registro_propietario)
        self.btn_delete_prope.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A',
                               cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_delete_prope.grid(row=10, column=1, padx=10, pady=10)



    def eliminar_registro_propietario(self):
        try:
            self.id_propietario = self.tabla_prope.item(self.tabla_prope.selection())['text']
            borrarPropietario(int(self.id_propietario))
            self.mostrar_tabla_propietario()
            self.id_propietario = None 
        except:
            pass

    def guardar_campos_propietario(self):
        propietario = Propietario(
            self.nombre_prope.get(),
            self.apellido_prope.get(),
            self.dni_prope.get(),
            self.cuil_prope.get(),
            self.domicilio_prope.get(),
            self.email_prope.get(),
        )

        if self.id_propietario == None:
            guardarPropietario(propietario)
        else:
            actualizarPropietario(propietario, self.id_propietario)

        self.mostrar_tabla_propietario()
        self.bloquear_campos_prope()
        
    
    def input_form_contrato(self):
        self.plazomeses = tk.StringVar()
        self.entry_plazomeses= tk.Entry(self, textvariable=self.plazomeses)
        self.entry_plazomeses.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_plazomeses.grid(row=0, column=1, padx=10,
                               pady=10, columnspan='2')

        self.idinquilino = tk.StringVar()
        self.entry_idinquilino = tk.Entry(self, textvariable=self.idinquilino)
        self.entry_idinquilino.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_idinquilino.grid(
            row=1, column=1, padx=10, pady=10, columnspan='2')

        self.idpropietario = tk.StringVar()
        self.entry_idpropietario = tk.Entry(self, textvariable=self.idpropietario)
        self.entry_idpropietario.config(
            width=50, state='disabled', font=('Arial', 12))
        self.entry_idpropietario.grid(
            row=2, column=1, padx=10, pady=10, columnspan='2')    
           
    def habilitar_campos_contrato(self):
        self.entry_plazomeses.config(state='normal')
        self.entry_idinquilino.config(state='normal')
        self.entry_idpropietario.config(state='normal')
        self.btn_modi_contrato.config(state='normal')
        self.btn_cance_contrato.config(state='normal')
        self.btn_alta_contrato.config(state='disabled')

    def bloquear_campos_contrato(self):
        self.entry_plazomeses.config(state='disabled')
        self.entry_idinquilino.config(state='disabled')
        self.entry_idpropietario.config(state='disabled')
        self.btn_modi_contrato.config(state='disabled')
        self.btn_cance_contrato.config(state='disabled')
        self.plazomeses.set('')
        self.idinquilino.set('')
        self.idpropietario.set('')
        self.btn_alta_contrato.config(state='normal')        
        
        
    def botones_principales_contrato(self):
        self.btn_alta_contrato = tk.Button(
            self, text='Nuevo', command=self.habilitar_campos_contrato)
        self.btn_alta_contrato.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B',
                             cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta_contrato.grid(row=8, column=0, padx=10, pady=10)

        self.btn_modi_contrato = tk.Button(self, text='Guardar', command=self.guardar_campos_contrato)
        self.btn_modi_contrato.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83',
                             cursor='hand2', activebackground='#7594F5', activeforeground='#000000', state='disabled')
        self.btn_modi_contrato.grid(row=8, column=1, padx=10, pady=10)

        self.btn_cance_contrato = tk.Button(
            self, text='Cancelar', command=self.bloquear_campos_contrato)
        self.btn_cance_contrato.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A',
                              cursor='hand2', activebackground='#F35B5B', activeforeground='#000000', state='disabled')
        self.btn_cance_contrato.grid(row=8, column=2, padx=10, pady=10)        
        
    
    def label_form_contrato(self):
        self.label_plazomeses_contrato = tk.Label(self, text="Plazo Meses: ")
        self.label_plazomeses_contrato.config(font=('Arial', 12, 'bold'))
        self.label_plazomeses_contrato.grid(row=0, column=0, padx=10, pady=10)

        self.label_idinquilino_contrato = tk.Label(self, text="ID Inquilino: ")
        self.label_idinquilino_contrato.config(font=('Arial', 12, 'bold'))
        self.label_idinquilino_contrato.grid(row=1, column=0, padx=10, pady=10)

        self.label_idpropietario_contrato = tk.Label(self, text="ID Propietario")
        self.label_idpropietario_contrato.config(font=('Arial', 12, 'bold'))
        self.label_idpropietario_contrato.grid(row=2, column=0, padx=10, pady=10)
        
    def mostrar_tabla_contrato(self):
        self.lista_contrato = consultaContrato()

        self.lista_contrato.reverse()

        self.tabla_contrato = ttk.Treeview(self, columns=(
            'ID', 'Plazo Meses', 'ID Inquilino', 'ID Propietario'))
        self.tabla_contrato.grid(row=9, column=0, columnspan=4, sticky='nse')

        self.scroll_contrato = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla_contrato.yview)
        self.scroll_contrato.grid(row=9, column=4, sticky='nse')
        self.tabla_contrato.configure(yscrollcommand=self.scroll_contrato.set)

        self.tabla_contrato.heading('#0', text='ID')
        self.tabla_contrato.heading('#1', text='Plazo Meses')
        self.tabla_contrato.heading('#2', text='ID Inquilino')
        self.tabla_contrato.heading('#3', text='ID Propietario')

        for i in self.lista_contrato:
            self.tabla_contrato.insert('', 0, text=i[0],
                              values=(i[1], i[2], i[3])
                              )

        self.btn_delete_contrato = tk.Button(
            self, text='Borrar', command=self.eliminar_registro_contrato)
        self.btn_delete_contrato.config(width=10, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A',
                               cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_delete_contrato.grid(row=10, column=1, padx=10, pady=10)    
        
    def guardar_campos_contrato(self):
        contrato = Contrato(
            self.plazomeses.get(),
            self.idinquilino.get(),
            self.idpropietario.get(),
        )

        if self.id_contrato == None:
            guardarContrato(contrato)
        else:
            actualizarContrato(contrato, self.id_contrato)

        self.mostrar_tabla_contrato()
        self.bloquear_campos_contrato()    
        
    def eliminar_registro_contrato(self):
        try:
            self.id_contrato = self.tabla_contrato.item(self.tabla_contrato.selection())['text']
            borrarContrato(int(self.id_contrato))
            self.mostrar_tabla_contrato()
            self.id_contrato = None 
        except:
            pass    
        
        
        
        
        
        
        
        
        
        
        

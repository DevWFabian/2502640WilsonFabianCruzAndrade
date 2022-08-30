from calendar import c
import tkinter as tk
from tkinter import CENTER, N, ttk, messagebox

class Payroll(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Nomina')
        self.create_tabs()
    
    def createEmployee(self,tabulador):
        frame= tk.LabelFrame(tabulador,text='Ingresar nuevo empleado',font=15)
        frame.grid(row = 0 ,column = 1, columnspan = 3,pady = 20, padx=100)
        # nombre
        tk.Label(frame , text = 'Nombres: ',font=15,padx=40,justify="left").grid(row=1,column=0,padx=20,pady=10)
        self.firstName= tk.Entry(frame, width=40,font=15)
        self.firstName.grid(row = 1 , column = 1, padx=20)
        # Apellidos
        tk.Label(frame , text = 'Apellidos: ',font=15,padx=40).grid(row=2,column=0,padx=20,pady=10)
        self.lastName= tk.Entry(frame, width=40,font=15)
        self.lastName.grid(row = 2 , column = 1, padx=20)
        # lista tipo documneto
        tk.Label(frame , text = 'Tipo de documento: ',font=15,padx=40).grid(row=3,column=0,padx=20,pady=10)
        type_document_list=[x for x in ['Seleccione','Cedula','Cedula extranjera']]
        combobox=ttk.Combobox(frame,width=57 ,values=type_document_list)
        combobox.grid(row=3, column=1, padx=20, pady=10)
        combobox.current(0)
        def saveCombobox():
            self.typeDocumnet=combobox.get()
        # Numero documento
        tk.Label(frame, text='Numero de documento',font=15, padx=40).grid(row=4,column=0,padx=20,pady=10)
        self.documentNumber= tk.Entry(frame, width=40,font=15)
        self.documentNumber.grid(row = 4 , column = 1, padx=20)
        # Salario base
        tk.Label(frame, text='Salario Base:',font=15, padx=40).grid(row=5,column=0,padx=20,pady=10)
        self.baseSalary= tk.Entry(frame, width=40,font=15)
        self.baseSalary.grid(row = 5 , column = 1, padx=20)
        boton1 = ttk.Button(tabulador, text='Registrar')
        boton1.grid(row=1, column=2)
    def readEmployees(self,tabulador):
        self.tree=ttk.Treeview(tabulador,height=15,columns=("Nombres","Apellidos","Tipo de documento","Numero de documento","Salario base"))
        self.tree.heading("#0",text="ID_Empleado");self.tree.column("#0",width=100,anchor=CENTER)
        self.tree.heading("Nombres",text="Nombres");self.tree.column("Nombres",width=150,anchor=CENTER)
        self.tree.heading("Apellidos",text="Apellidos");self.tree.column("Apellidos",width=150,anchor=CENTER)
        self.tree.heading("Tipo de documento",text="Tipo de documento");self.tree.column("Tipo de documento",width=150,anchor=CENTER)
        self.tree.heading("Numero de documento",text="Numero de documento");self.tree.column("Numero de documento",width=150,anchor=CENTER)
        self.tree.heading("Salario base",text="Salario base");self.tree.column("Salario base",width=150,anchor=CENTER)
        self.tree.grid(row=0,column=0,columnspan=1,padx=20,pady=20)
        
        
    def create_tabs(self):
        control_tab = ttk.Notebook(self)
        tab1 = ttk.Frame(control_tab)
        # Agregamos el tabulador al control de tabuladores
        control_tab.add(tab1, text='Registrar Empleado')
        # Mostramos el tabulador
        control_tab.pack(fill='both')
        self.createEmployee(tab1)
        tab2 = ttk.Frame(control_tab)
        control_tab.add(tab2, text='Mostrar Registros')
        self.readEmployees(tab2)
        






if __name__ == '__main__':
    application = Payroll()
    application.mainloop()

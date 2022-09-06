from distutils.filelist import findall
import tkinter as tk
import re
from tkinter import CENTER,ttk, messagebox
import sqlite3
class Payroll(tk.Tk):
    db_name = 'payrollAppGUI/database.db'
    def __init__(self):
        super().__init__()
        self.title('Nomina')
        self.create_tabs()
    
    def employee(self,tabulador):
        self.formEmployee(tabulador)
        self.table_employees(tabulador)
        self.tree.bind('<<TreeviewSelect>>',self.selectRows)
    def payroll(self,tabulador):
        self.form_payrool(tabulador)
        
    def selectRows(self,e):
        self.firstName.delete(0,tk.END)
        self.lastName.delete(0,tk.END)
        self.typeDocument.delete(0,tk.END)
        self.documentNumber.delete(0,tk.END)
        self.baseSalary.delete(0,tk.END)
        selected=self.tree.focus()
        row=self.tree.item(selected,'values')
        self.id_employees= self.tree.item(selected,'text')
        self.firstName.insert(0,row[0])
        self.lastName.insert(0,row[1])
        self.typeDocument.insert(0,row[2])
        self.documentNumber.insert(0,row[3])
        self.baseSalary.insert(0,row[4])
    def create_tabs(self):
        control_tab = ttk.Notebook(self)
        tab1 = ttk.Frame(control_tab)
        # Agregamos el tabulador al control de tabuladores
        control_tab.add(tab1, text='Registrar Empleado')
        # Mostramos el tabulador
        control_tab.pack(fill='both')
        self.employee(tab1)
        tab2 = ttk.Frame(control_tab)
        control_tab.add(tab2, text='Mostrar Registros')
        self.payroll(tab2)
    def formEmployee(self,tabulador):
        frame= tk.LabelFrame(tabulador,text='Empleados',font=15)
        frame.grid(row = 0 ,column = 1, columnspan = 3,pady = 20, padx=20)
        # nombre
        tk.Label(frame , text = 'Nombres: ',font=15,padx=40,justify="left").grid(row=1,column=0,padx=5,pady=10,sticky=tk.W)
        self.firstName= tk.Entry(frame, width=30,font=15)
        self.firstName.grid(row = 1 , column = 1, padx=10)
        
        # Apellidos
        tk.Label(frame , text = 'Apellidos: ',font=15,padx=40).grid(row=2,column=0,padx=2,pady=10,sticky=tk.W)
        self.lastName= tk.Entry(frame, width=30,font=15)
        self.lastName.grid(row = 2 , column = 1, padx=10)
        # lista tipo documneto
        tk.Label(frame , text = 'Tipo de documento: ',font=15,padx=40).grid(row=3,column=0,padx=5,pady=10,sticky=tk.W)
        type_document_list=[x for x in ['Cedula','Cedula extranjera']]
        self.typeDocument=ttk.Combobox(frame,width=41 ,values=type_document_list)
        self.typeDocument.grid(row=3, column=1, padx=10, pady=10)
        # Numero documento
        tk.Label(frame, text='Numero de documento',font=15, padx=40).grid(row=4,column=0,padx=5,pady=10,sticky=tk.W)
        self.documentNumber= tk.Entry(frame, width=30,font=15)
        self.documentNumber.grid(row = 4 , column = 1, padx=10)
        # Salario base
        tk.Label(frame, text='Salario Base:',font=15, padx=40).grid(row=5,column=0,padx=5,pady=10,sticky=tk.W)
        self.baseSalary= tk.Entry(frame, width=30,font=15)
        self.baseSalary.grid(row = 5 , column = 1, padx=10)
            
        boton1 = ttk.Button(tabulador, text='Registrar', command=self.insert_employees)
        boton1.grid(row=1, column=1)
        boton2 = ttk.Button(tabulador, text='Actualizar', command=self.update_employees)
        boton2.grid(row=1, column=2,pady=5)
        boton3 = ttk.Button(tabulador, text='Eliminar', command=self.delete_employees)
        boton3.grid(row=1, column=3,pady=5)
    def form_payrool(self,tabulador):
        frame= tk.LabelFrame(tabulador,text='Nomina',font=15)
        frame.grid(row = 0 ,column = 1, columnspan = 3,pady = 20, padx=20)
        filt = tk.LabelFrame(frame , text = 'Filtrar: ',font=15,padx=20)
        filt.grid(row=0,column=1,padx=5,pady=10,sticky=tk.W)
        self.filter_option=ttk.Combobox(filt,width=41 ,values=('Seleccione','id empleado','Numero Documento','Nombre','Apellido'))
        self.filter_option.grid(row=1, column=2, padx=10, pady=10)
        def option_combobox(self,e):
            pass
    def run_query(self,query,parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor=conn.cursor()
            result=cursor.execute(query, parameters)
            conn.commit()
        return result
    def table_employees(self,tabulador):
        self.tree=ttk.Treeview(tabulador,height=11,columns=("Nombres","Apellidos","Tipo de documento","Numero de documento","Salario base"))
        self.tree.heading("#0",text="ID_Empleado");self.tree.column("#0",width=100,anchor=CENTER)
        self.tree.heading("Nombres",text="Nombres");self.tree.column("Nombres",width=125,anchor=CENTER)
        self.tree.heading("Apellidos",text="Apellidos");self.tree.column("Apellidos",width=125,anchor=CENTER)
        self.tree.heading("Tipo de documento",text="Tipo de documento");self.tree.column("Tipo de documento",width=125,anchor=CENTER)
        self.tree.heading("Numero de documento",text="Numero de documento");self.tree.column("Numero de documento",width=135,anchor=CENTER)
        self.tree.heading("Salario base",text="Salario base");self.tree.column("Salario base",width=125,anchor=CENTER)
        self.tree.grid(row=0,column=4,columnspan=1,padx=5,pady=20)
        self.select_employees()
    def select_employees(self):    
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #ejecutar sentencia
        query= "select * from empleados order by idEmpleados desc"
        db_rows=self.run_query(query)
        for row in db_rows:
            self.tree.insert('',0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
    def validationsForm(self,input_text:str,atribute_name:str,type_data:str,character_match:str,min_len:int,max_len:int,limit=False,limit_range=0,):
        validation= re.findall(character_match,input_text)
        if limit:
            if validation:
                messagebox.showwarning(f"Advertencia",f"La entrada de {atribute_name} solo puede contener {type_data}")
                return False
            elif input_text == '':
                messagebox.showwarning(f"advertencia",f"Los espacios de {atribute_name} no pueden quedar en blanco")
                return False
            elif len(input_text) < min_len:
                messagebox.showwarning("Advertencia",f"El numero minimo de caracteres para el campo {atribute_name} es {min_len}")
                return False
            elif len(input_text) > max_len:
                messagebox.showwarning("Advertencia",f"El numero maximo de caracteres para el campo {atribute_name} es {max_len}")
                return False
            elif int(input_text)> limit_range:
                messagebox.showwarning("Advertencia",f"El valor ingresado en el campo {atribute_name} no puede ser mayor a {limit_range}")
                return False
            else:
                return True
        else:
            if validation:
                messagebox.showwarning(f"Advertencia",f"La entrada de {atribute_name} solo puede contener {type_data}")
                return False
            elif input_text == '':
                messagebox.showwarning(f"advertencia",f"Los espacios de {atribute_name} no pueden quedar en blanco")
                return False
            elif len(input_text) < min_len:
                messagebox.showwarning("Advertencia",f"El numero minimo de caracteres para el campo {atribute_name} es {min_len}")
                return False
            elif len(input_text) > max_len:
                messagebox.showwarning("Advertencia",f"El numero maximo de caracteres para el campo {atribute_name} es {max_len}")
                return False
            else:
                return True
    def insert_employees(self):
        try:
            validation_name= self.validationsForm(self.firstName.get(),'Nombres','Letras','[^a-zñ A-ZÑ]',2,30)
            validation_last_name= self.validationsForm(self.lastName.get(),'Apellidos','Letras','[^a-zñ A-ZÑ]',2,30)
            validation_type_document= self.validationsForm(self.typeDocument.get(),'Tipo de Documento','Opciones','[^a-zñ A-ZÑ]',2,30)
            validation_document_number= self.validationsForm(self.documentNumber.get(),'Numero de documento','Numeros',"[^0-9]",7,15)
            validation_base_salary= self.validationsForm(self.baseSalary.get(),'Salario','Numeros con o sin decimales','[^\\d.\\d]',6,12)
            if validation_name==True and validation_last_name==True and validation_type_document==True and validation_document_number==True and validation_base_salary==True:
                query= "insert into empleados(empNombre,empApellido,empTipoDocumento,empNumeroDocumento,empSalarioBase)"
                query+=" values(?,?,?,?,?)"
                
                parameters=(self.firstName.get(),self.lastName.get(),self.typeDocument.get(),self.documentNumber.get(),float(self.baseSalary.get()))            
                self.run_query(query,parameters)
                messagebox.showinfo('Exito','Se registro exitosamente el empleado')
                #limipiar Espacios
                self.firstName.delete(0,tk.END)
                self.lastName.delete(0,tk.END)
                self.typeDocument.delete(0,tk.END)
                self.documentNumber.delete(0,tk.END)
                self.baseSalary.delete(0,tk.END)
        except ValueError as e:
            messagebox.showerror('Error','No se registro el empleado')
            self.select_employees()
    def update_employees(self):
        try:
            idEmployeed=self.tree.item(self.tree.selection())['text']
            basSalary=self.tree.item(self.tree.selection())['values'][4]
            try:
                query= f"update empleados set empNombre=?,empApellido=?,empTipoDocumento=?,empNumeroDocumento=?,empSalarioBase=? WHERE idEmpleados= ?"
                parameters = (self.firstName.get(),self.lastName.get(),self.typeDocument.get(),self.documentNumber.get(),basSalary,idEmployeed)     
                self.run_query(query,parameters)
                messagebox.showinfo('Exito','Se pudo actualizar correctamente')
                #limipiar Espacios
                self.firstName.delete(0,tk.END)
                self.lastName.delete(0,tk.END)
                self.typeDocument.delete(0,tk.END)
                self.documentNumber.delete(0,tk.END)
                self.baseSalary.delete(0,tk.END)
            except sqlite3.ProgrammingError as e:
                messagebox.showerror('Error','No se Actualizo el registro,  Seleccione un registro de la tabla')
        except IndexError as e:
            messagebox.showerror("Error","Seleccione un registro de la tabla")
        self.select_employees()
    def delete_employees(self):
        try:
            idEmployeed=self.tree.item(self.tree.selection())['text']
            name=self.tree.item(self.tree.selection())['values'][0]
            try:
                query=f"DELETE FROM empleados WHERE idEmpleados= ? " 
                parameters=(idEmployeed,)
                self.run_query(query,parameters)
                messagebox.showinfo(f"Exito",f"Se elimino el registro del empleado {name}")
                self.firstName.delete(0,tk.END)
                self.lastName.delete(0,tk.END)
                self.typeDocument.delete(0,tk.END)
                self.documentNumber.delete(0,tk.END)
                self.baseSalary.delete(0,tk.END)
                self.id_employees = ''
            except sqlite3.ProgrammingError as e: 
                messagebox.showerror(f"Error",f"No se elimino el registro del empleado {self.firstName.get()}, Seleccione un registro de la tabla")
        except IndexError as e:
            messagebox.showerror("Error","Seleccione un registro de la tabla")
        self.select_employees()
if __name__ == '__main__':
    application = Payroll()
    application.mainloop()

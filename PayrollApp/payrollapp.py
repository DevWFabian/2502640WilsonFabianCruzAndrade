from datetime import datetime
import re
def create_user(document_number,first_name,last_name,days_worked,base_salary):
    user={"id":document_number,"first_name":first_name,"last_name":last_name,"days_worked":days_worked,"salary":base_salary}
    return user
def check_input(attribute_name:str,character_match:str,min_length:int,max_length:int,limit=False,limit_range=0):
    flag_closing= True
    if limit:
        while flag_closing:
            input_text=input(f"Ingrese {attribute_name}: ")    
            if re.findall(character_match,input_text):
                print("La entrada contiene uno o varios caracteres incorrectos")
            else:
                if not input_text:
                    print("El espacio es obligatorio no puede quedar en blanco")
                else:
                    if len(input_text)< min_length: 
                        print(f"El numero de caracteres tiene que ser de mas de {min_length}")
                    elif len(input_text) > max_length:
                        print(f"El numero de caracteres tiene que ser de menos de {max_length}")
                    else:
                        if int(input_text) > limit_range:
                            print(f"El valor ingresado es mayor a {limit_range}")
                        else:
                            flag_closing=False
                            return input_text                
    else:
        while flag_closing:
            input_text=input(f"Ingrese {attribute_name}: ")    
            primera_ecepcion= re.findall(character_match,input_text)
            if primera_ecepcion:
                print("La entrada contiene uno o varios caracteres incorrectos")
            else:
                if not input_text:
                    print("El espacio es obligatorio no puede quedar en blanco")
                else:
                    if len(input_text)< min_length: 
                        print(f"El numero de caracteres tiene que ser de mas de {min_length}")
                    elif len(input_text) > max_length:
                        print(f"El numero de caracteres tiene que ser de menos de {max_length}")
                    else:
                        flag_closing=False
                        return input_text
def salary_calculator(base_salary,days_worked):
        daily_salary=float(base_salary)/30
        health_and_pension_discount= (daily_salary* 0.08)*int(days_worked)
        if float(base_salary) <=2000000:
            transportation_subsidy = (117100/30)*int(days_worked)
            earned_income = ((daily_salary*int(days_worked))+transportation_subsidy)-health_and_pension_discount
            summary={"daily_salary":round(daily_salary,2),"discount":round(health_and_pension_discount,2),"transportation":round(transportation_subsidy,2),"earned_income":round(earned_income,2)}
        else:
            earned_income = daily_salary*int(days_worked)-health_and_pension_discount
            summary={"daily_salary":round(daily_salary,2),"discount":round(health_and_pension_discount,2),"transportation":0,"earned_income":round(earned_income,2)}
        return summary
def show_all_records(record_list:list):
    output_message=""
    for i in record_list:
        value_list=[]
        output_message+=f"\n\t\t\t*****Nomina*****\n"
        for v in i.values():
            value_list.append(v)
        output_message+=f"\tFecha: {datetime.today()}\n\tNumero de documento: {value_list[0]}\n"
        output_message+=f"\tNombre: {value_list[1]}\n\tApellido: {value_list[2]}\n"
        output_message+=f"\t\t\t***resumen***\n"
        output_message+=f"\tDias trabajados: {value_list[3]}\n\tSalario base: ${value_list[4]}\n"
        output_message+=f"\tSalario Diario: ${value_list[5]}\n\tAportes Salud 4% y Pension 4%: -${value_list[6]}\n"
        output_message+=f"\tSubsidio de transporte: ${value_list[7]}\n\tTotal: ${value_list[8]}\n"
        output_message+=f"\n***********************************************\n"
        value_list.clear()
    return output_message    
def save_in_text_document(text_to_save:str):
    try:
        with open("PayrollApp/payroll.txt","a+",encoding="utf-8")as pr:
            pr.write(text_to_save)
            print("se ha guardado los registros en el archivo")
    except:
        print("No se ha podido guardar el archivo")
def run_program():
    payroll=[]
    option=0
    while option < 4:
        options_menu=f"\t***Bienvenido***\n"
        options_menu+=f"Opciones:\n"
        options_menu+=f"1. Agregar empleado\n"
        options_menu+=f"2. Visualizar todos los registros\n"
        options_menu+=f"3. Imprimir todos los registros en archivo .txt\n"
        options_menu+=f"4. Salir\n"
        print(options_menu)
        option=int(check_input("opcion","[^0-9]",1,1,True,4))
        if option == 1:
            document_number=check_input("Numero de documento","[^0-9]",10,15)
            first_name=check_input("nombre","[^a-zñA-ZÑ]",2,30)
            last_name=check_input("apellido","[^a-zñA-ZÑ]",2,30)
            days_worked=check_input("dias trabajados","[^0-9]",1,2,True,31)
            base_salary=check_input("salario base","[^0-9]",6,9)
            user=create_user(document_number,first_name,last_name,days_worked,base_salary)
            summary=salary_calculator(base_salary,days_worked)
            user.update(summary)
            payroll.append(user)
        elif option == 2:
            print(show_all_records(payroll))  
        elif option == 3:
            save_in_text_document(show_all_records(payroll))  
    pass
run_program()
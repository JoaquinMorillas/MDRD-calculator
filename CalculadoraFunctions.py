from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import datetime

mdrd_flag = False
clearence_flag = False

def mdrd(win):
    global mdrd_flag
   

    edad = win.edad.get()
    creatinina = win.creatinina.get()
    sexo = win.sexo.get()

    
    if not type(edad) == int or edad <= 0:
        msg.showerror(title="Error", message="Solo se permiten números enteros mayores a 0 en 'Edad'")
        win.mdrd.set("Error en el parametro 'Edad'")
        mdrd_flag = False
        return False
    if not type(creatinina) in [int, float] or creatinina <=0:
        msg.showerror(title="Error", message="Solo se permiten números mayores a 0 en 'Creatinina'")
        win.mdrd.set("Error en el parametro 'Creatinina'")
        mdrd_flag = False
        return False

    else:
        if sexo == 0:
            mdrd = int(175*(creatinina**-1.154)*(edad**-0.203)*0.742)
            win.mdrd.set(mdrd)
            mdrd_flag = True
            return True
            

        elif sexo == 1:
            mdrd = int(175*(creatinina**-1.154)*(edad**-0.203))
            win.mdrd.set(mdrd)
            mdrd_flag = True
            return True


            
    



def clearence(win):
    global clearence_flag
    
    
    creatinina_s = win.creatinina.get()
    creatinina_o = win.creatinina_o.get()
    diuresis = win.diuresis.get()

    if not type(creatinina_s) in [int, float] or creatinina_s <= 0:
        msg.showerror(title="Error", message="Solo se permiten números mayores a 0 en 'Creatinina'")
        win.clearence.set("Error en el parametro 'creatinina'")
        clearence_flag = False
        return False
    
    if not type(creatinina_o) in [int, float] or creatinina_o <= 0:
        msg.showerror(title="Error", message="Solo se permiten números mayores a 0 en 'Creatinina en orina'")
        win.clearence.set("Error en el parametro 'Creatinina en orina'")
        clearence_flag = False
        return False
        
    if not type(diuresis) == int or diuresis <= 0:
        msg.showerror(title="Error", message="Solo se permiten números Enteros mayores a 0 en 'Diuresis'")
        win.clearence.set("Error en el parametro 'Diuresis'")
        clearence_flag = False
        return False

    else:
        creatinina_o_24= creatinina_o*diuresis/100000

        clearence = int((creatinina_o_24/(creatinina_s*10))*694)
        win.clearence.set(clearence)
        clearence_flag = True
        return True
    
def upload(win):
    
    global mdrd_flag
    global clearence_flag
    if mdrd_flag == True and clearence_flag == True:
        conn = sqlite3.connect(MDRD.db)
        curr = conn.cursor()

        edad = win.edad.get()
        sexo = win.sexo.get()
        creatinina = win.creatinina.get()
        creatinina_o = win.creatinina_o.get()
        diuresis = win.diuresis.get()
        creati_24 = creatinina_o*diuresis/100000
        clearence = win.clearence.get()
        mdrd = win.mdrd.get()
        day = datetime.date.today()

        curr.execute("INSERT INTO datos VALUES(?,?,?,?,?,?,?,?,?)",
                     (edad, sexo,creatinina,creatinina_o,diuresis,creati_24,clearence,mdrd,day))
        

        conn.commit()
        clearence_flag = False
        mdrd_flag = False
def resultado(win):
    mdrd(win)
    
    clearence(win)
    
    upload(win)
    
    
def limpiar(win):
    win.edad.set(0)
    win.creatinina.set(0)
    win.creatinina_o.set(0)
    win.diuresis.set(0)
    win.clearence.set(0)
    win.mdrd.set(0)
    

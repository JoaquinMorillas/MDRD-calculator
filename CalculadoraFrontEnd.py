from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from CalculadoraFunctions import mdrd, clearence, resultado, limpiar

WIDTH = 400
HEIGHT = 800



class Win(Frame):
    def __init__(self, root, width, height ):
        super().__init__()
        self.root = root
        self.width = width
        self.height = height
        self.root.title("Calculadora de MDRD")
        self.root.geometry(f"{self.height}x{self.width}")

        self.numero_muestra = IntVar()

        self.sexo = IntVar()
        self.creatinina = DoubleVar()
        self.edad = IntVar()

        self.diuresis= IntVar()
        self.creatinina_o= DoubleVar()

        self.mdrd= DoubleVar()
        self.clearence = DoubleVar()

        self.bg_1 = "midnight blue"
        self.bg_2 = "Grey5"
        self.fg = "white"
        self.font = "comicsans"


    def input_frame(self):

       
        inputs_frame = Frame(self.root, bd=5, padx= 10, bg=self.bg_1, height = self.height//2, width= self.width//2, relief="groove")
        inputs_frame.pack(side = LEFT, fill=BOTH, expand=True, pady=10)

        title = Label(inputs_frame,fg=self.fg, bg=self.bg_1,text= "Datos del paciente",font=("arial", 15))
        title.grid(row=0, column=0, columnspan=4)

        #label_numero_muestra = Label(inputs_frame,fg=self.fg,bg=self.bg_1, font=self.font, text = "Número de Muestra").grid(column= 0, row=1)
        #numero_muestra_entry = Entry(inputs_frame,fg=self.fg,bg=self.bg_2, font=self.font, textvariable= self.numero_muestra)
        #numero_muestra_entry.grid(row=1, column=1)
        
        label_creatinina = Label(inputs_frame,fg=self.fg,bg=self.bg_1,font=self.font,  text = "creatinina en suero(mg/dl)").grid(column= 0, row=4)
        creatinina_entry = Entry(inputs_frame,fg=self.fg,bg=self.bg_2,font=self.font,  textvariable= self.creatinina)
        creatinina_entry.grid(column= 1, row=4)

        label_edad = Label(inputs_frame,fg=self.fg,bg=self.bg_1, font=self.font, text="Edad(años)").grid(column=0, row =5)
        edad_entry = Entry(inputs_frame,fg=self.fg,bg=self.bg_2,font=self.font,  textvariable=self.edad)
        edad_entry.grid(column= 1, row=5)

        label_sexo = Label(inputs_frame,fg=self.fg,bg=self.bg_1, font=self.font,text="Sexo:").grid(column=0, row= 2)
        radio_button_f = Radiobutton(inputs_frame,fg=self.fg, bg=self.bg_1,selectcolor="black", font=self.font,text= "Femenino", variable= self.sexo, value=0).grid(column=1, row=2)
        radio_button_m = Radiobutton(inputs_frame,fg=self.fg,bg=self.bg_1,selectcolor="black", font=self.font,text= "Masculino", variable= self.sexo, value=1).grid(column=1, row=3)

        label_diuresis=Label(inputs_frame,fg=self.fg,bg=self.bg_1, font=self.font,text="Diuresis(ml/24hrs):")
        label_diuresis.grid(column=0, row=6)

        diuresis_entry=Entry(inputs_frame,fg=self.fg,bg=self.bg_2, font=self.font,textvariable= self.diuresis)
        diuresis_entry.grid(column=1, row=6)


        label_creatinina_o=Label(inputs_frame,fg=self.fg,bg=self.bg_1, font=self.font,text="Creatinina en Orina(mg/dl):")
        label_creatinina_o.grid(column=0, row=7)

        creatinina_o_entry=Entry(inputs_frame,fg=self.fg,bg=self.bg_2,font=self.font, textvariable= self.creatinina_o)
        creatinina_o_entry.grid(column=1, row=7)

        boton_resultado = Button(inputs_frame,fg="white",bg="blue",font=self.font,text= "Calcular Resultado", command= lambda: resultado(self))
        boton_resultado.grid(column=0, row=8, columnspan= 4,ipady= 10)

        boton_limpiar = Button(inputs_frame,fg="white",bg="red", font=self.font,text= "Limpiar Datos", command= lambda: limpiar(self))
        boton_limpiar.grid(column=0, row=9, columnspan= 4, ipady= 10)

    
    
    def results_frame(self):

        results_frame = Frame(self.root, bd=5,padx = 10,bg=self.bg_1, height = self.height//2, width= self.width//2, relief="groove")
        results_frame.pack(side= RIGHT, fill=BOTH, expand=True, pady=10)

        label= Label(results_frame,pady = 30,fg=self.fg, bg=self.bg_1,text= "MDRD: ", font=(self.font, 20))
        label.pack()
        label_resultado_mdrd= Label(results_frame,fg=self.fg, bg=self.bg_1,textvariable= self.mdrd, font=(self.font, 20))
        label_resultado_mdrd.pack()

        label= Label(results_frame,pady = 30, fg=self.fg, bg=self.bg_1,text= "Clearence Medido:", font=(self.font, 20))
        label.pack()
        label_resultado_cl= Label(results_frame,pady = 10,fg=self.fg, bg=self.bg_1, textvariable = self.clearence, font=(self.font, 20))
        label_resultado_cl.pack()

                                 



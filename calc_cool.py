# -*- coding: utf-8 -*-
import tkinter as tk
import CoolProp as cp
import numpy as np
import prop_fluidos
from prop_fluidos import fluido

#
lista_fluidos = cp.CoolProp.FluidsList()


ventana = tk.Tk()
ventana.title('CoolProp Calculator')
ventana.geometry("+300+200")

fluido1 = fluido('Air')


#Start Menu

label_fluid = tk.StringVar() #Variable que guarda el texto del label
label_fluid.set("Fluid") #Cambia el texto de la variable
#Se crea el label y se conecta con variable1
label = tk.Label(ventana,textvariable=label_fluid)
label.grid(row=0,column=0)


# Seleccion Fluido
selec_fluido = tk.Listbox ( ventana, selectmode='single',height=1,width=15,highlightcolor='#a8acfd',selectbackground='#a8acfd'
)
 # to insert items in the list
for index, str_fluido in enumerate(lista_fluidos):
    selec_fluido.insert(index, str_fluido)
selec_fluido.grid(row=1,column=0)
selec_fluido.selection_set(2)
selec_fluido.see(2)

#Densidad

text_density = tk.StringVar() #Variable que guarda el texto del label
text_density.set("Density") #Cambia el texto de la variable
density_value = tk.Label(ventana,textvariable=text_density,bd = 5,width=5)
density_value.grid(row=0,column=2)


variable_density = tk.StringVar() #Variable que guarda el texto del label
#Se crea el label y se conecta con variable1
output_density = tk.Entry(ventana,textvariable=variable_density,bd = 5,width=5)

#text_density = f'{fluido1.rho:.2f}'
#output_density.insert(0,text_density)
output_density.grid(row=1,column=2)

#Temperatura
variable1 = tk.StringVar() #Variable que guarda el texto del label
variable1.set("Temperature") #Cambia el texto de la variable
#Se crea el label y se conecta con variable1
label_temperatura = tk.Label(ventana,textvariable=variable1)
label_temperatura.grid(row=0,column=1)

variable_temp = tk.StringVar() #Variable que guarda el texto del entry
#Se crea el entry y se conecta con variable
entrada_temp = tk.Entry(ventana,textvariable=variable_temp,bd = 5,width=5)
entrada_temp.grid(row=1,column=1)
entrada_temp.insert(0,'25')
fluido1.temperatura = np.float(entrada_temp.get())
variable_density.set(f'{fluido1.rho:.2f}')



def selected_fluid():    
    print(selec_fluido.selection_get() )
    fluido1 = fluido(selec_fluido.selection_get())
    fluido1.temperatura = np.float(entrada_temp.get())
    fluido1.propiedades()
    variable_density.set(f'{fluido1.rho:.2f}')
    
    



#Calcular
boton1 = tk.Button(ventana, text='Calculate',pady=5,padx=52,activebackground='#a8acfd',
height=1,width=15,justify='center',command = selected_fluid)
boton1.grid(row=2, column=0)


ventana.mainloop()




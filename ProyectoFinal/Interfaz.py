import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2

def Calibrar(): 
    print("Calibrando!!")

def Inicio(): 
    print("Iniciando!!")

#Ventana principal
pantalla= Tk()
pantalla.title("Sistema de Reconocimiento Facial")
pantalla.geometry("1280x720")

#Fondo
imagenF=PhotoImage(file='C:/Users/morin/OneDrive - Universidad de Guanajuato/UG/Inteligencia Artificial/ProyectoEquipo_03/SepUp/Inicio.png')
background=Label(image=imagenF,text="Inicio")
background.place(x=0,y=0, relheight=1, relwidth=1)
botonCalibrar = tk.Button(pantalla, text="Calibrar",fg="white", bg="#3E0248", relief="flat",
                      cursor="hand2", width=7, height=1, font=("DM Sans", 33),command=Calibrar)
botonCalibrar.place(x=850, y=295)

botonInicio = tk.Button(pantalla, text="Inicio",fg="white", bg="#3E0248", relief="flat",
                      cursor="hand2", width=7, height=1, font=("DM Sans", 33), command=Inicio) 
botonInicio.place(x=850, y=460)

#Entradas
#Numero 1
InputNum1=Entry(pantalla, width=75)
InputNum1.place(x=195,y=365)

#Numero 2
InputNum2=Entry(pantalla, width=75)
InputNum2.place(x=195,y=585)



pantalla.mainloop()
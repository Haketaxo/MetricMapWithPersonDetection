import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2 as cv

# Distance constants 
KNOWN_DISTANCE = 45 #cm
PERSON_WIDTH = 60 #cm

# Object detector constant 
CONFIDENCE_THRESHOLD = 0.4
NMS_THRESHOLD = 0.3

# colors for object detected
COLORS = [(255,0,0),(255,0,255),(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
GREEN =(0,255,0)
BLACK =(0,0,0)
# defining fonts 
FONTS = cv.FONT_HERSHEY_COMPLEX
PINK = (147, 20, 255)
ORANGE = (0, 69, 255)
Z = 0
X = 0
Y = 0
# getting class names from classes.txt file 
class_names = []
with open("classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
#  setttng up opencv net
yoloNet = cv.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

yoloNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
yoloNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)

model = cv.dnn_DetectionModel(yoloNet)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

# object detector funciton /method
def object_detector(image):
    classes, scores, boxes = model.detect(image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    # creating empty list to add objects data
    data_list =[]
    for (classid, score, box) in zip(classes, scores, boxes):
        # define color of each, object based on its class id 
        color= COLORS[int(classid) % len(COLORS)]
    
        label = "%s : %f" % (class_names[classid], score)

        # draw rectangle on and label on object
        cv.rectangle(image, box, color, 2)
        cv.putText(image, label, (box[0], box[1]-14), FONTS, 0.5, color, 2)
    
        # getting the data 
        # 1: class name  2: object width in pixels, 3: position where have to draw text(distance)
        if classid ==0: # person class id 
            data_list.append([class_names[classid], box[2], (box[0], box[1]-2)])
        elif classid ==67:
            data_list.append([class_names[classid], box[2], (box[0], box[1]-2)])
        # if you want inclulde more classes then you have to simply add more [elif] statements here
        # returning list containing the object data. 
    return data_list


def focal_length_finder (measured_distance, real_width, width_in_rf):
    focal_length = (width_in_rf * measured_distance) / real_width

    return focal_length

# distance finder function 
def distance_finder(focal_length, real_object_width, width_in_frmae):
    distance = (real_object_width * focal_length) / width_in_frmae
    return distance 

# reading the reference image from dir 
ref_person = cv.imread('ReferenceImages/image1.png')


person_data = object_detector(ref_person)
person_width_in_rf = person_data[0][1]

print(f"Person width in pixels : {person_width_in_rf} ")

# finding focal length 
focal_person = focal_length_finder(KNOWN_DISTANCE, PERSON_WIDTH, person_width_in_rf)


def Iniciar():
    print("iniciando")
    cap = cv.VideoCapture(0)
    Coordenadas=[]
    while True:
        ret, frame = cap.read()    
        data = object_detector(frame) 
        for d in data:
            if d[0] =='person':
                distance = distance_finder(focal_person, PERSON_WIDTH, d[1])
                x, y = d[2]
            cv.rectangle(frame, (x, y-3), (x+700, y+35),BLACK,-1 )
            cv.putText(frame, f'Dis: {round(distance,2)} cm', (x+5,y+13), FONTS, 0.48, GREEN, 2)
            cv.putText(frame, f'Cordenadas x: ({x}), y:{y-3})', (x+5,y+26), FONTS, 0.48, GREEN, 2)

        cv.imshow('frame',frame)
        key = cv.waitKey(1)
        if key ==ord('q'):
            break

        if key == ord('c'):
            orignal = frame.copy()
            cv.imwrite(f'ImagenesEvaluacion/Evaluacion.png', orignal)
    cv.destroyAllWindows()
    cap.release()
    

def Evaluar(): 
    print("Iniciando!!")
    Alto = float(ALTO.get())
    Ancho = float(ANCHO.get())
    Distancia = float(DISTANCIA.get())

    Evaluar= cv.imread('ImagenesEvaluacion/Evaluacion.png')
    data = object_detector(Evaluar)
    for d in data:
        if d[0] =='person':
            distance = distance_finder(focal_person, PERSON_WIDTH, d[1])
            x, y = d[2]
    print("Tus errores Calculados son:")
    EvaluarX = 100 - (x * 100)/Ancho
    EvaluarY = 100 - (y * 100)/Alto
    EvaluarZ = 100 - (distance * 100)/Distancia
    Promedio = abs((EvaluarX + EvaluarY + EvaluarZ )/3)
    print(f"{EvaluarX} % ")
    print(f"{EvaluarY} % ")
    print(f"{EvaluarZ} % ")

    Evaluacion = tk.Button(pantalla, text=f"La presicion es: {Promedio} %",fg="white", bg="#3E0248", relief="flat",
                      cursor="hand2", width=30, height=1, font=("DM Sans", 23)) 
    Evaluacion.place(x=195, y=50)

#Ventana principal
pantalla= Tk()
pantalla.title("Sistema de Reconocimiento Facial")
pantalla.geometry("1280x720")

#Fondo
imagenF=PhotoImage(file='C:/Users/PRIDE OMEGA/Downloads/Proyecto Final IA/ProyectoFinal/Inicio.png') 
background=Label(image=imagenF,text="Inicio")
background.place(x=0,y=0, relheight=1, relwidth=1)
botonCalibrar = tk.Button(pantalla, text="Iniciar",fg="white", bg="#3E0248", relief="flat",
                      cursor="hand2", width=8, height=3, font=("DM Sans", 33),command=Iniciar)
botonCalibrar.place(x=850, y=200)

botonInicio = tk.Button(pantalla, text="Evaluar",fg="white", bg="#3E0248", relief="flat",
                      cursor="hand2", width=17, height=1, font=("DM Sans", 33), command=Evaluar) 
botonInicio.place(x=195, y=200)

#Entradas
#Numero 1
ALTO=Entry(pantalla, width=75)
ALTO.place(x=195,y=350)

ANCHO=Entry(pantalla, width=75)
ANCHO.place(x=195,y=450)

DISTANCIA=Entry(pantalla, width=75)
DISTANCIA.place(x=195,y=550)

pantalla.mainloop()
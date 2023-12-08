# MetricMapWithPersonDetection
Este es un proyecto el cual generara un mapa metrico al detectar a una persona en tiempo real

---------------------------------------------------------------------------------
	        |		Proyecto Final: Mapa métrico identificando personas		|
	        |				Equipo: ABMODEL					                          |
	        |	Integrantes: *Jesús Everardo MArtínez González			  	|
	        |		     *Omar Giovanni Merino Montiel				            |
	        |	     	     *Sandra Yazmin Morin Morales			          	|
	        |		     *Kathia Michelle Villegas Mosqueda			        	|
	---------------------------------------------------------------------------------
Este programa realiza una interfaz mediante la cual por medio de una cámara permite la identificacion de personas y sus coordenadas. 
Su objetivo principal es identificar personas que se encuentren de pie mediante una cámara con una caja (en pixeles) que envuelva a la persona detectada y que la silueta que detecte las convierta en coordenadas X, Y y Z de su ubicación con respecto a la cámara.   

		--------------------------------------------------------
		          |		  Requisitos del sistema 		|
		--------------------------------------------------------

	1.-Python o algún editor de archivos de extención .ipynb
	2.- Bibliotecas de python:
		-NumPy
		-tkinder
		-cv2
		-time
		-PIL
	3.- Que su computadora en donde va a ejecutar el programa tenga una cámara.

Si usted desea calibrar su programa a sus mediciones dirigase al apartado "Calibración del programa", si no lo desea, dirijase al apartado "Ejecutar".  

		--------------------------------------------------------
		          |		Calibración del programa		|
		--------------------------------------------------------

**Nota : El programa ya esta calibrado, es decir ya tiene una referencia, por lo que se puede ejecutar. 

	Ejecute las siguientes instrucciones si usted desea calibrar el programa:

	** Se recomienda que para la calibración se encuentre en un espacio donde solo se 	encuentre usted, para que solo detecte una persona y en base a ello se tome como 	referencia. 
		1.- Descomprima la carpeta .zip
		2.- Abra su editor de archivos y cargue la carpeta que previamente 			descomprimio.
		Puede observar que en la carpeta hay varios archivos, dirijase al archivo 		con el 	nombre "CaptureReferenceImage". 
		3.- Una vez abierto el archivo ejecute el programa.
		Puede observar que le abre una ventana de la cámara, alejese una distancia 		considerable, pero que usted tenga noción de a que distancia esta respecto 		a la cámara. 
		4.- Presione la letra "c" para capturar la imagen de referencia.
		5.- Presione la letra "q" para salir de la ventana.
		Dentro de la carpeta del proyecto se le creará un archivo .png, que 			corresponde a su imagen capturada de referencia. 
		6.- Abra la imagen, y visualice la distancia a la que le indica que esta 		detectando a la persona.
		7.- Abra el archivo "Proyecto Final", en la línea de codigo 8 ingrese la 		distancia a la que se detecto su imagen de referencia. 
		Y ¡Listo! su programa ya esta calibrado.  			

		--------------------------------------------------------
		                  |			Ejecutar			|
		--------------------------------------------------------

Para la ejecución de nuestro programa:
	1.- Descarge y descomprima la carpeta .zip
	2.- Abra su editor de archivos y abra la carpeta descomprimida
	    Ejemplo: File >> Open Folder >> Descargas>> "Proyecto Final"
	3.- Observe que la carpeta tiene varios archivos, dirijase al archivo con el nombre 	"Proyecto Final IA" y ejecutelo. 
	4.- Se le desplegará una interfaz, de clic en "Iniciar" para que se abra una 	ventana con su cámara.
	5.- Presione "q" para salir. 
	6.- En la interfaz contiene un apartado de evaluación de la presición, ingrese las 	coordenadas que detecto la camara al momento de la ejecución del programa y de 	click en "Evaluar", se le desplegara la presión que se obtuvo con respecto a la 	referencia que se tiene. 


 Para referencias de YoloV4 visite el siguiente sitio:
 
https://github.com/kiyoshiiriemon/yolov4_darknet

 Para la estimacion de distancias visite el siguiente sitio:

 https://barcelonageeks.com/estimacion-de-distancia-en-tiempo-real-usando-opencv-python/

# adptado de: http://www.galirows.com.br/meublog/opencv-python/opencv2-python27/capitulo2-deteccao/reconhecimento-face/
import cv2
from agnes import Agnes

class detectFace():
	
	def startWeb(self):
		arqCasc1 = 'haar-xml/haarcascade_frontalface_default.xml'
		arqCasc2 = 'haar-xml/haarcascade_eye.xml'
		faceCascade1 = cv2.CascadeClassifier(arqCasc1) #classificador para o rosto
		faceCascade2 = cv2.CascadeClassifier(arqCasc2) #classificador para os olhos

		agnes = Agnes()
		cont = 0
		hello = 0

		webcam = cv2.VideoCapture(0)  #instancia o uso da webcam

		while True:
		    s, imagem = webcam.read() #pega efeticamente a imagem da webcam
		    imagem = cv2.flip(imagem,180) #espelha a imagem

		    faces = faceCascade1.detectMultiScale(
		        imagem,
		        minNeighbors=20,
		        minSize=(30, 30),
			maxSize=(300,300)
		    )

		    if len(faces) > 0:
		    	if cont == 0 and hello <= 2:
		    		agnes.speak("hello")
		    		hello +=1

		    	if cont < 18:
		    		cont += 1
		    		
		    else:
		    	if cont > 0 :
		    		cont = cont - 1
		    		
		    	if hello > 0:
		    		hello = hello - 1


def main():
	d = detectFace()
	d.startWeb()

if __name__ == "__main__":
    main()
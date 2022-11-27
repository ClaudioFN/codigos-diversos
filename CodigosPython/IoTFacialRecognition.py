# -*- coding: utf-8 -*-

# Codigo elaborado com apoio de video aula da Dio - O Novo Mundo das Cidades Inteligentes com Tecnologia de IoT
# CODIGO DESENVOLVIDO NO COLAB DA GOOGLE. CERTAS PARTES TALVEZ NAO OPEREM COMO DEVERIA.

import imutils # Redimencionamento | Rotacao
import numpy as np
import cv2 # OpenCV
from google.colab.patches import cv2_imshow
from IPython.display import display, Javascript # Webcam Leitura
from google.colab.output import eval_js #Webcam Leitura
from base64 import b64decode # Pacote para codificar dados binarios

def take_photos(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
  ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename,'wb') as f:
    f.write(binary)
  return filename

# Executa a chamada que pega a imagem da webcam
image_file = take_photos()

image = cv2.imread(image_file)

# Redimensiona para ter uma largura maxima de 400 pixels
image = imutils.resize(image, width=400)
(h, w) = image.shape[:2]
print(w, h)
cv2_imshow(image)

!wget -N https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
!wget -N https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel

print("[INFO] loading model...")
prototxt = 'deploy.prototxt'
model = 'res10_300x300_ssd_iter_140000.caffemodel' # Baixou
net = cv2.dnn.readNetFromCaffe(prototxt, model) # Inseriu no modelo de treinamento

# Redimensionar para ter uma largura maxima de 400 pixels - janela onde fica a face da pessoa
image = imutils.resize(image, width=400)
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

# Print informando que a analise foi feita
print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()

for i in range(0, detections.shape[2]):

	# Extrair a probabilidade associada a previsao
	confidence = detections[0, 0, i, 2]

	# Filtra deteccoes fracas garantindo que a "confianca" seja
	# Maior que o limite minimo de confianca
	if confidence > 0.5: # Nossa deteccao deve ter no minimo 50% de certeza
		# Calcula as coordenadas (x, y) da caixa delimitadora do objeto
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")
		# Desenha a caixa delimitadora da face junto com a probabilidade associada
		text = "{:.2f}%".format(confidence * 100)
		y = startY - 10 if startY - 10 > 10 else startY + 10
		cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
		cv2.putText(image, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

# Mostra o resultado, confirmando se tem uma face na imagem e o quanto essa face foi detectada
cv2_imshow(image)
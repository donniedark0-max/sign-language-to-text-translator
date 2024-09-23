# Traductor de Lenguaje de Señas a Texto

Este proyecto implementa un sistema de reconocimiento de gestos en tiempo real para traducir el lenguaje de señas al lenguaje hablado. Utiliza un enfoque de deep learning para procesar videos y extraer características relevantes de los gestos.

## Tecnologías Utilizadas
* **TensorFlow/PyTorch:** Framework de aprendizaje profundo para la construcción y entrenamiento de modelos.
* **OpenCV:** Biblioteca de visión por computadora para el procesamiento de imágenes y videos.
* **MediaPipe:** Framework para la detección de puntos clave en tiempo real.
* **Keras:** API de alto nivel para construir y entrenar modelos de deep learning.

## Proceso Detallado

* **Captura de video:** Se captura un video en tiempo real del usuario realizando un gesto.
* **Preprocesamiento:** El video se preprocesa para mejorar la calidad de la imagen y resaltar las características relevantes de los gestos. Esto puede incluir tareas como reescalado, normalización y eliminación de ruido.
* **Extracción de características:** Se utilizan técnicas de visión por computadora, como la detección de puntos clave de las manos mediante MediaPipe, para extraer características clave de los gestos. Estas características se utilizan como entrada para el modelo de deep learning.
* **Modelo de clasificación:** Se emplea una red neuronal profunda, típicamente una combinación de redes convolucionales (CNN) y recurrentes (RNN), para clasificar los gestos y asignarles la palabra o frase correspondiente. Las CNN son excelentes para extraer características espaciales de las imágenes, mientras que las RNN son capaces de modelar la secuencia temporal de los gestos.
* **Traducción a texto:** El resultado de la clasificación, que es una representación numérica de la clase, se convierte en una palabra o frase legible en lenguaje natural.
Modelo

* **Arquitectura:** Se utiliza una arquitectura híbrida que combina redes neuronales convolucionales (CNN) para extraer características espaciales de los gestos y redes neuronales recurrentes (RNN) como LSTM o GRU para modelar la secuencia temporal de los gestos.
* **Entrenamiento:** El modelo se entrena en un conjunto de datos de videos de gestos etiquetados, utilizando una función de pérdida de entropía cruzada y un optimizador Adam. Se aplican técnicas de aumento de datos, como rotaciones, escalado y cambios de brillo, para mejorar la generalización del modelo.
* **Evaluación:** El rendimiento del modelo se evalúa utilizando métricas como precisión, recall y F1-score. Se realiza una validación cruzada para obtener una estimación más robusta del rendimiento.
* **Conjunto de Datos**

* **Descripción:** El conjunto de datos consiste en videos de personas realizando gestos en lenguaje de señas, etiquetados con la palabra o frase correspondiente.
* **Formato:** Los videos están en formato [formato] y las etiquetas están en formato [formato].
* 
### Resultados

Precisión: [Valor] %

Recall: [Valor] %

F1-score: [Valor] %

[Incluir aquí una tabla o gráfico que muestre los resultados de la evaluación del modelo]

### Demostración

[Incluir un enlace a un video o GIF que muestre el modelo en funcionamiento]


## Contribuidores

* [José](https://github.com/JoseZaravia17) 
* [Luis]()
* [Jheanpierre]()
* [Juan José](https://github.com/donniedark0-max)

## Gracias

![screen](https://64.media.tumblr.com/6ef336942b8244de073f3a1d8f4227f1/27692d7c9a9ba2cf-de/s640x960/74e032925e7da4f108880d39890897b594cf1c15.jpg)


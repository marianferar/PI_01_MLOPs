# RecomendadorMovies
# Proyecto individual 1 - MLOps

Hice un sistema de recomendación de películas o series en el cual se ingresa el número de usuario junto con el título de la película/serie deseada, y el sistema devuelve si la recomienda o no. 
En el rol de *Data Engineer* realicé una exploración de los datasets aportados en formato csv para corroborar cantidad de valores nulos y duplicados. Luego realicé las transformaciones solicitadas como reemplazar datos nulos por str, modificar el formato de las fechas, crear una nueva columna con la inicial de la plataforma y el id de la película/serie, cambiar a minúsculas todos los campos y texto, y finalmente, crear dos nuevas columnas donde se diferencie el tiempo y el tipo de duración, respectivamente.
Para aplicar *Machine learning*, realicé un EDA para visualizar el comportamiento de las variables. Como hallazgos más relevantes, encontré que si una persona desea ver una película antigua (desde 1920) tendría más posibilidades de encontrarla en la plataforma Amazon o Disney Plus; y además, si una persona desea ver una serie, sería más probable encontrar mayores opciones en la plataforma Hulu. Otro hallazgo fue, que no hay diferencia de rating por plataforma ni por tipo(serie o película)… en otras palabras, se podría inferir que no hay una plataforma con ‘mejores películas/series puntuadas’.

# Consultas API
Puedes hacer las siguientes consultas a la API:

    o Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
    o	Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
    o	Cantidad de películas por plataforma con filtro de PLATAFORMA
    o	Actor que más se repite según plataforma y año.

# Modelo de Machine Learning
Puedes acceder a una recomendación de película o serie ingresando un número de usuario y el título que deseas ver. El sistema te responderá si te la recomienda o no.

## Estructura del proyecto

    o API: contiene las funciones
    o DATA: contiene los datasets finales, resultado de las distintas transformaciones que aportan información a la API y al modelo de Machine Learning.
    o GRADIO: contiene la interfaz de usuario
    o IMAGES: contiene una imagen para la interfaz
    o NOTEBOOKS: contiene los notebooks realizados para las etapas del proyecto.

## Empezando
Para empezar a ejecutar este proyecto, clona este repositorio en tu máquina:

`git clone https://github.com/your-username/your-repo.git`

## Tecnologías utilizadas
Pandas, NumPy, Seaborn, Scikit-learn, FastAPI, Gradio, Requests, Docker, Gradio, Surprise

## Prerrequisitos
Para correr este proyecto necesitarás **uvicorn** , **FastAPI**, **Gradio**, **Docker** , **Docker Compose** y **Surprise** instalados en tu máquina.

## Corriendo la app
Para correr la app, usa los comandos:
- En `./api`:
`uvicorn main:app --host 0.0.0.0 --port 8000`

- En `./gradio`:
`py app.py`

La API fue construida usando FastAPI, la cual genera documentación interactiva de manera automática. Puedes acceder a ella copiando este link en tu navegador: http://localhost:8000/docs 

Esto inicia la API y Gradio app en contenedores Docker por separado, con la API corriendo en el puerto 8000 y Gradio en el puerto 7860. Puedes acceder a Gradio app con este link en tu navegador: http://localhost:7860 .


## Marianela Fernández - DATA 08
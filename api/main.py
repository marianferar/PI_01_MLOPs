from fastapi import FastAPI
import pandas as pd
import datetime

# Cargamos el archivo con los datos procesados
streaming = pd.read_csv(r'..\data\streaming_api.csv' , delimiter =',', encoding= 'utf-8')

# Listas de valores disponibles
platforms = ['amazon', 'disney plus', 'hulu', 'netflix']
duration_types = ['min', 'season', 'seasons']

# API

app = FastAPI()

# Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN
@app.get("/max_duration/")
async def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    max_duration_movie = max_duration(year, platform, duration_type)
    return {"movie": max_duration_movie}

# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/score_count/")
async def get_score_count(platform: str, scored: int, year: int):
    # print('===DEBUG===',scored, year, platform)
    count = score_count(platform, scored, year)
    return {"count": count}

# Cantidad de películas por plataforma con filtro de PLATAFORMA
@app.get("/count_platform/")
async def get_count_platform(platform: str):
    # print('===DEBUG===',platform)
    count = count_platform(platform)
    return {"count": count}

# Actor que más se repite según plataforma y año
@app.get("/actor/")
async def get_actor(platform: str, year: int):
    # print('===DEBUG===', year, platform)
    actor_count = actor(platform, year)
    return {"actor": actor_count}

# FUNCIONES LOCALES

#Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
#(la función debe llamarse get_max_duration(year, platform, duration_type))

def max_duration(year=None, platform=None, duration_type=None):
    today = datetime.date.today()

    if platform not in platforms: 
        return 'platform incorrect'
    if duration_type not in duration_types:
        return 'duration_type incorrect'
    if year > today.year:
        return 'year incorrect'
    
    # filtrar el DataFrame de películas en función de los parámetros de entrada
    filtered = streaming.copy()
    
    if year is not None:
        filtered = filtered[filtered['release_year'] == year]
    if platform is not None:
        filtered = filtered[filtered['platform'] == platform]
    if duration_type is not None:
        filtered = filtered[filtered['duration_type'].str.contains(duration_type)]
       
    # obtener la película con la duración más larga
    max_duration = filtered['duration_int'].max()
    longest_movies = filtered[filtered['duration_int'] == max_duration]['title'].tolist()
    
    # devolver la lista de películas con la duración más larga
    return longest_movies


#Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año 
#(la función debe llamarse get_score_count(platform, scored, year))

def score_count(platform, score, year):
    today = datetime.date.today()

    if platform not in platforms: 
        return 'platform incorrect'
    if year > today.year:
        return 'year incorrect'
    if score > 5 or score < 1:
        return 'score incorrect'
    
    # Filtrar el dataframe por plataforma y año
    filtered = streaming[(streaming['platform'] == platform) & (streaming['release_year'] == year)]
    
    # Contar la cantidad de películas con puntaje mayor al valor especificado
    count = int(filtered[filtered['score'] > score]['title'].count())
    
    # Devolver el resultado
    return count


#Cantidad de películas por plataforma con filtro de PLATAFORMA. 
#(La función debe llamarse get_count_platform(platform))

def count_platform(platform):
    if platform not in platforms: 
        return 'platform incorrect'
    
    filtered = streaming[(streaming['platform'] == platform)]
    count = int(filtered['title'].count())

    return count


# Actor que más se repite según plataforma y año. 
# (La función debe llamarse get_actor(platform, year))

def actor(platform, year):
    filtered = streaming[(streaming['platform'] == platform) & (streaming['release_year'] == year) & (streaming['cast'] != 'NaN')]
    
    actor_count = filtered['cast'].value_counts()
    
    if actor_count.empty:
        return 'Not Found'
    
    return actor_count.idxmax()

import os
import gradio as gr
import requests

# Definir la lista de valores para los dropdown
DURATION_TYPES = ['min', 'season', 'seasons']
PLATFORMS = ['amazon', 'disney plus', 'hulu', 'netflix']

API_BASE_URL = "http://localhost:8000"

# bkg = os.path.join(os.path.dirname(__file__), "../images/theoffice.jpg")

# Definir las funciones para llamar a los endpoints de la API
def max_duration(duration, year, plataform):
    # print('===DEBUG===',duration, year, plataform)
    response = requests.get(f"{API_BASE_URL}/max_duration?duration_type={duration}&year={int(year)}&platform={plataform}")
    return response.json()['movie']

def score_count(platform, score, year):
    # print('===DEBUG===',score, year, platform)
    response = requests.get(f"{API_BASE_URL}/score_count?platform={platform}&scored={int(score)}&year={int(year)}")
    return response.json()['count']

def count_platform(platform):
    # print('===DEBUG===',platform)
    response = requests.get(f"{API_BASE_URL}/count_platform?platform={platform}")
    return response.json()['count']

def actor(platform, year):
    # print('===DEBUG===', year, platform)
    response = requests.get(f"{API_BASE_URL}/actor?platform={platform}&year={int(year)}")
    return response.json()['actor']

def recommendation(userId, title):
    response = requests.get(f"{API_BASE_URL}/recommendation?userId={int(userId)}&title={title}")
    return response.json()

# Definir la interfaz y las opciones
with gr.Blocks() as iface:
    gr.Markdown("# Consulta tus peliculas favoritas!")
    # gr.Image(type="pil", value=bkg, interactive=False)

    with gr.Tab("get_max_duration"):
        duration_type = gr.inputs.Dropdown(DURATION_TYPES, label="Duration Type")
        year = gr.inputs.Number(default=2021, label="Year")
        platform = gr.inputs.Dropdown(PLATFORMS, label="Platform")
        get_max_duration_button = gr.Button("Enviar")
    
    with gr.Tab("get_score_count"):
        scored = gr.inputs.Slider(1, 5, step=0.5, default=3, label="Score")
        year_score_count = gr.inputs.Number(default=2021, label="Year")
        platform_score_count = gr.inputs.Dropdown(PLATFORMS, label="Platform")
        score_count_button = gr.Button("Enviar")

    with gr.Tab("get_count_platform"):
        platform_count = gr.inputs.Dropdown(PLATFORMS, label="Platform")
        count_platform_button = gr.Button("Enviar")
    
    with gr.Tab("get_actor"):
        platform_actor = gr.inputs.Dropdown(PLATFORMS, label="Platform")
        year_actor = gr.inputs.Number(default=2021, label="Year")
        actor_button = gr.Button("Enviar")

    text_output = gr.Textbox(label="Result")

    get_max_duration_button.click(max_duration, inputs=[duration_type,year,platform], outputs=text_output)
    score_count_button.click(score_count, inputs=[platform_score_count,scored,year_score_count], outputs=text_output)
    count_platform_button.click(count_platform, inputs=[platform_count], outputs=text_output)
    actor_button.click(actor, inputs=[platform_actor,year_actor], outputs=text_output)

# Ejecutar la interfaz
iface.launch()
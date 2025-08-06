import os
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig

# --- ENVIRONMENT SETUP INSTRUCTIONS ---
# 1. Install the Google Cloud AI Platform SDK:
#    pip install google-cloud-aiplatform
#
# 2. Authenticate your Codespace:
#    In your Codespaces terminal, run:
#    gcloud auth application-default login
#
# 3. Set the project id as an environment variable in your Codespaces settings:
#    GOOGLE_CLOUD_QUOTA_PROJECT = "arched-curve-464100-c9"
# ------------------------------------

# --- Configuration ---
PROJECT_ID = "arched-curve-464100-c9"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.5-flash"

# File and folder paths
ONTOLOGY_FILE_PATH = "quantum_mindfulness (2).md"
OUTPUT_ARTICLE_FOLDER = "Texts/"

print("[*] Script started.")
print(f"[*] Using Project ID: {PROJECT_ID}, Location: {LOCATION}, Model: {MODEL_NAME}")
print(f"[*] Ontology File: {ONTOLOGY_FILE_PATH}")
print(f"[*] Output Folder: {OUTPUT_ARTICLE_FOLDER}")

# Ensure the output directory exists
os.makedirs(OUTPUT_ARTICLE_FOLDER, exist_ok=True)

# --- Define the list of top subclasses ---
top_subclass_topics = [
    "Prácticas",
    "Sin Categorizar",
    "Fenómeno",
    "Prácticas y Metodologías Avanzadas",
    "Conceptos Centrales",
    "Dimensión Psicodinámica",
    "Capacidad Cognitiva",
    "Optimización y Refinamiento Cognitivo",
    "Tensión y Disfunción Cognitiva",
    "Mecanismo Cognitivo",
    "Factor Influyente",
    "Percepción",
    "Arquitectura Formal",
    "Estrategias Principales",
    "Objetivos",
    "Práctica de Influencia del Colapso",
    "Colapso de Onda Psicodinámica",
    "Influencias de Activación Dimensional",
    "Modalidad Secundaria",
    "Desafíos Epistemológicos"
]

# Set the number of articles to generate for each topic
articles_per_topic = 5

# --- Define the Spanish Prompt Template ---
SPANISH_PROMPT_TEMPLATE = f"""---
Eres un escritor de blogs experto, especializado en el marco de la Mindfulness Cuántica. Tu tarea es generar una publicación de blog de alta calidad a partir de la ontología proporcionada, enfocándote en el siguiente tema: {{topic_name}}.

**INSTRUCCIONES CRÍTICAS PARA EL FORMATO Y CONTENIDO DE SALIDA:**

1.  **IDIOMA DE SALIDA:** El idioma de salida DEBE ser **ÚNICAMENTE español**.

2.  **ESTRUCTURA EXACTA de Salida:** Tu respuesta DEBE consistir en dos partes, en este orden preciso:
    * **YAML Front Matter:** Un bloque de YAML encerrado en `---` líneas al principio del archivo.
    * **Cuerpo del Artículo:** Inmediatamente después del `---` de cierre del YAML, el encabezado principal H3, seguido del contenido expandido del artículo.
    * **NO** incluyas ningún texto introductorio, preámbulos o comentarios conversacionales antes de la apertura `---` del YAML Front Matter.
    * **NO** incluyas ningún texto entre el `---` de cierre del YAML y el encabezado H3, excepto por una sola línea en blanco para mayor legibilidad.

3.  **Propiedades del Front Matter YAML (Adherencia Estricta a la Muestra de Git it Write):**
    * `title`: El título principal del artículo. Este DEBE ser idéntico al encabezado H3 en el cuerpo del artículo. **ASEGÚRATE de que este valor esté entre comillas dobles.** Ejemplo: `title: "Tu Título de Artículo con Dos Puntos: Subtítulo"`
    * `menu_order`: Establece este valor en `1`.
    * `post_status`: Establece este valor en `publish`.
    * `post_excerpt`: Un resumen conciso de 2-3 oraciones del artículo. **ASEGÚRATE de que este valor esté entre comillas dobles.**
    * `taxonomy`: Esta clave contendrá tus categorías y etiquetas.
        * `category`: Una lista YAML de 1 a 3 categorías. **DEBES seleccionar ÚNICAMENTE de la siguiente lista predefinida:** ["Core Concepts", "Framework Principles", "Psychodynamic Dimensions", "Prime Modality", "Secondary Modality", "Formal Architecture", "Emergent Properties", "Therapeutic Strategies", "Challenges and Limitations", "Advanced Practices", "Mindfulness Approaches", "Human Capacities", "Goals", "Perception", "Practices"]. **Cada elemento de categoría en la lista DEBE estar entre comillas dobles.** Ejemplo: `  - "Category One"`
        * `post_tag`: Una lista YAML de 3 a 7 etiquetas relevantes. Estas pueden ser más específicas y no necesitan estar en una lista predefinida, pero deben derivarse del contenido del artículo y de la ontología de Mindfulness Cuántica. **Cada elemento de etiqueta en la lista DEBE estar entre comillas dobles.** Ejemplo: `  - "tag-one"`
    * `custom_fields`: Un mapa YAML vacío: {{}}.

4.  **Contenido del Cuerpo del Artículo (Adherencia Estricta):**
    * **Longitud:** Expande el artículo para que tenga entre 700 y 1000 palabras.
    * **Tono:** Mantén un tono claro, atractivo e informativo, adecuado para una audiencia general interesada en la mindfulness y la psicología.
    * **Profundidad:** Crea un artículo completo sobre el tema {{topic_name}}, utilizando la ontología como tu material de origen.
    * **Encabezados:** El ÚNICO encabezado de nivel superior en el cuerpo del artículo debe ser el encabezado principal H3 (`### Tu Título de Artículo`).
    * **LIMPIEZA:** ABSOLUTAMENTE NO incluyas ningún encabezado `##` de nivel dentro del cuerpo del artículo.
    * **Sin Títulos Redundantes:** Asegúrate de que el encabezado H3 esté presente solo una vez al principio del cuerpo del artículo, inmediatamente después del YAML.

**Referencia de la Ontología de Mindfulness Cuántica (para contexto y terminología):**
{{ontology_content}}

**Tu Tarea:**
Crea un artículo de blog completo en **español** basándote en esta ontología, específicamente sobre el tema de **{{topic_name}}**. El resultado debe seguir las reglas de formato YAML y Markdown exactamente como se ha descrito.

**Tu Artículo Generado (con YAML Front Matter):**
"""

try:
    # Initialize Vertex AI
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = GenerativeModel(MODEL_NAME)

    # --- Read the Ontology File ---
    ontology_content = ""
    with open(ONTOLOGY_FILE_PATH, 'r', encoding='utf-8') as f:
        ontology_content = f.read()

    # --- Loop through each topic to generate multiple articles ---
    for topic in top_subclass_topics:
        for i in range(articles_per_topic):
            print(f"\n[*] Generating article {i+1} for topic: {topic}")

            final_prompt = SPANISH_PROMPT_TEMPLATE.format(
                topic_name=topic,
                ontology_content=ontology_content
            )

            # Generate content
            try:
                # Use the provided generation configuration
                generation_config = GenerationConfig(
                    temperature=0.7,
                    top_p=1.0,
                    top_k=32.0,
                    max_output_tokens=4096,
                    stop_sequences=[]
                )

                response = model.generate_content(
                    contents=[{"role": "user", "parts": [{"text": final_prompt}]}],
                    generation_config=generation_config
                )

                # --- Process and save the generated article ---
                if response and response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
                    generated_text = response.candidates[0].content.parts[0].text
                    if generated_text:
                        safe_topic_name = topic.replace(" ", "_").replace("/", "_")
                        output_filename = f"generated_qm_article_ES_{safe_topic_name}_{i+1}.md"
                        output_filepath = os.path.join(OUTPUT_ARTICLE_FOLDER, output_filename)

                        generated_text = generated_text.strip()

                        with open(output_filepath, 'w', encoding='utf-8') as f:
                            f.write(generated_text)
                        print(f"[*] Successfully generated and saved article to: {output_filepath}")
                    else:
                        print(f"[ERROR] Generated text was empty for topic: {topic}. Skipping...")
                else:
                    print(f"[ERROR] No valid response or no candidates received for topic: {topic}. Skipping...")
            except Exception as e:
                print(f"[ERROR] An API error occurred for topic: {topic}. Details: {e}. Skipping...")

except FileNotFoundError:
    print(f"Error: The file {ONTOLOGY_FILE_PATH} was not found.")
except Exception as e:
    print(f"\n[FATAL ERROR] An unexpected error occurred: {e}")

print("\n[*] Script finished.")
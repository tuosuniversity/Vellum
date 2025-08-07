import os
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig

# --- ENVIRONMENT SETUP INSTRUCTIONS ---
# 1. Install the Google Cloud AI Platform SDK:
#    pip install google-cloud-aiplatform
#
# 2. Authenticate your Codespace:
#    In your Codespaces terminal, run:
#    gcloud auth application-default login
#
# 3. Set the project id as an environment variable in your Codespaces settings:
#    GOOGLE_CLOUD_QUOTA_PROJECT = "arched-curve-464100-c9"
# ------------------------------------

# --- Configuration ---
PROJECT_ID = "arched-curve-464100-c9"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.5-flash"

# File and folder paths
ONTOLOGY_FILE_PATH = "quantum_mindfulness.md"
OUTPUT_ARTICLE_FOLDER = "Texts-es/"

print("[*] Script started.")
print(f"[*] Using Project ID: {PROJECT_ID}, Location: {LOCATION}, Model: {MODEL_NAME}")
print(f"[*] Ontology File: {ONTOLOGY_FILE_PATH}")
print(f"[*] Output Folder: {OUTPUT_ARTICLE_FOLDER}")

# Ensure the output directory exists
os.makedirs(OUTPUT_ARTICLE_FOLDER, exist_ok=True)

# --- Define the list of top subclasses ---
top_subclass_topics = [
"Experiencia Interna Abstracta",
"Inteligencia Accionable",
"Visión de Fuerza Constitutiva Activa",
"Conocimiento Activo",
"Maestría Activa",
"Proceso de Reencuadre Activo",
"Investigación Estructural Activa",
"Proceso de Actualización",
"Experiencia Actualizada",
"Prácticas y Metodologías Avanzadas",
"Principio Estético",
"Resolución Estética",
"Ansiedad",
"Significado Asignado",
"Escultura de la Atención",
"Sintonización",
"Valencia Promedio del Estado Anterior",
"Manifestación Conductual",
"Formación de Creencias",
"Sistema de Anulación Biológica",
"Huesos de la Realidad",
"Compasión Delimitada",
"Desafíos y Limitaciones",
"Patrón de Conserje del Caos",
"Mindfulness Clásico",
"Agencia Cognitiva",
"Anclaje Cognitivo",
"Componente de Anclaje Cognitivo",
"Consecuencia del Fallo del Anclaje Cognitivo",
"Valoración Cognitiva",
"Sesgo de Valoración Cognitiva",
"Componente de Valoración Cognitiva",
"Componentes (C = wΨ ⋅ Valencia(Ψ) + wS ⋅ ValenciaProm(S_t-1) + Sesgo_M1)",
"Sesgo Cognitivo",
"Capacidad Cognitiva",
"Decoherencia Cognitiva",
"Destilación Cognitiva",
"Campo de Emergencia Cognitiva",
"Herencia de Patrones Cognitivo-Emocionales",
"Resistencia Cognitiva",
"Mejora Cognitiva",
"Deriva Entrópica Cognitiva",
"Manipulación del Campo Cognitivo",
"Mecanismo de Filtrado Cognitivo",
"Flujo Cognitivo",
"Fluidez Cognitiva",
"Influencia Cognitiva",
"Mapeo Cognitivo",
"Medición Cognitiva",
"Mecanismo Cognitivo",
"Modalidad Cognitiva",
"Conciencia de Múltiples Estados Cognitivos",
"Optimización y Refinamiento Cognitivo",
"Sobrecarga Cognitiva",
"Proceso Cognitivo",
"Recursos Cognitivos",
"Tensión y Disfunción Cognitiva",
"Enfoques de Estructuración Cognitiva",
"Superposición Cognitiva",
"Disfunción del Colapso",
"Fatiga del Colapso",
"Práctica de Influencia en el Colapso",
"Modo de Colapso",
"Intervenciones en el Punto de Colapso",
"Mecanismo de Condicionamiento",
"Ciclo de Sesgo de Confirmación y Construcción de la Realidad",
"Atención Consciente",
"Conciencia Consciente",
"Observación Consciente",
"Construcción Consciente de la Realidad",
"Creación Consciente de la Realidad / Reencuadre Perceptual",
"Pila Consciente",
"Gestión Consciente del Estado",
"Fortificación de la Conciencia",
"Refinamiento de la Conciencia",
"Función de Onda de la Conciencia",
"Realidad Construida",
"Interferencia Constructiva",
"Experimentación Contemplativa",
"Indagación Contemplativa",
"Modelo de Mentación Continua",
"Concepto Central",
"Artesanía del Colapso",
"Génesis Creativa",
"Parálisis Creativa",
"Potencial Creativo",
"Método de Cultivo",
"Narrativa Cultural",
"Arquitectura de Decisión",
"Atraso de Decoherencia",
"Trauma Psicológico Profundo",
"Interferencia Destructiva",
"Patrón de Interferencia en el Desarrollo",
"Activación Dimensional",
"Influencia de Activación Dimensional",
"Influencias (Kj = I_Sj + I_Cj + I_Tj + I_Ψj + εj)",
"Sintonización Dimensional",
"Cristalización Dimensional",
"Desalineación Dimensional",
"Compromiso Cognitivo Dirigido",
"Estado Disociativo",
"Red Dinámica e Interconectada",
"Patrón Disfuncional",
"Mindfulness Encarnado",
"Propiedades Emergentes",
"Escultura del Colapso Emocional",
"Creatividad Emocional",
"Apertura Emocional",
"Entrelazamiento Cuántico Emocional",
"Patrón de Reactividad Emocional",
"Regulación Emocional / Modulación Afectiva",
"Respuesta Emocional",
"Resilvestración Emocional",
"Teoría de la Tormenta Emocional",
"Ausencia Empírica",
"Estilo de Compromiso",
"Toma de Decisiones Mejorada",
"Influencia Ambiental",
"Resonancia Ambiental",
"Desafíos Epistemológicos",
"Discernimiento Epistemológico",
"Límites Éticos",
"Ejemplos",
"Entrenamiento de la Función Ejecutiva",
"Disonancia Existencial",
"Realidad Experimentada",
"Límite Experiencial",
"Influencia Externa",
"Intensidad Final",
"Dinámicas de Flujo en la Conciencia",
"Arquitectura Formal",
"Testimonio Formal",
"Principio del Marco",
"Principios del Marco",
"Libre Albedrío",
"Sustrato Energético Fundamental",
"Conciencia General",
"Dimensiones Geométricas de la Conciencia",
"Abandono de Metas",
"Metas",
"Función de Anclaje",
"Impronta Histórica / Impronta de Trauma",
"Capacidades Humanas",
"Humor como Tecnología Cognitiva",
"Identidad",
"Proceso de Transformación de la Identidad",
"Impacto del Ahora",
"Síndrome del Impostor",
"Reactividad Impulsiva",
"Impulso hacia el Compartir Generativo",
"Tensión por Proceso Incompleto",
"Inercia del Pasado",
"Epistemología Inferencial",
"Factores Influyentes",
"Disposición Inherente",
"Guion Heredado",
"Guiones Heredados",
"Imposición de la Arquitectura Institucional",
"Enfoques Terapéuticos Integrados",
"Colapso Intencional",
"Patrón de Interferencia",
"Patrones de Interferencia",
"Cartografía Interna",
"Resolución de Conflictos Internos",
"Mapa Interno del Funcionamiento Psicológico",
"Experiencia de Relación Interpersonal",
"Realidad Intersubjetiva",
"Resonancia Intersubjetiva",
"Cognición Intuitiva",
"Celos",
"Adquisición de Conocimiento",
"Repertorio Conductual Aprendido",
"Liberación de Guiones Heredados",
"Proceso de Liberación",
"Limitación de la Observación Directa",
"Estrategias Principales",
"Manejo de la Tensión y Disfunción Cognitiva",
"Manipulación de la Realidad Construida",
"Memoria (Explícita e Implícita)",
"Organización del Sistema de Archivos Mentales",
"Flexibilidad Mental",
"Interfaz Mente-Cuerpo",
"Cuantos Mentales",
"Estado Mental",
"Principio de la Mente Controla el Cerebro",
"Comparación de Enfoques de Mindfulness",
"Terapia Cognitiva Basada en Mindfulness (TCBM)",
"Reducción del Estrés Basada en Mindfulness (MBSR)",
"Meta de Mindfulness",
"Intervención de Mindfulness",
"Escaneo Multidimensional",
"Gestión de Narrativas",
"Desarrollo Natural",
"Incrustación Neurológica por Repetición",
"Cognición No Local",
"Fenómeno No Material",
"Observación No Reactiva",
"Estado Meta No Local",
"Restricciones Objetivas",
"Efecto Observable",
"Observación (Ψ)",
"Componentes (Ψ = α(β + 1)(A + f))",
"Influencia de la Observación",
"Valencia de la Observación",
"Paradoja del Efecto Observador",
"Función del Observador",
"Dinámica Observador-Participante",
"Rol Observador-Participante",
"Teoría del Observador-Participante",
"Rol del Observador",
"Teoría del Campo Ontológico",
"Cortafuegos Ontológico",
"Desalineación Ontológica",
"Reestructuración Ontológica",
"Inanición Ontológica",
"Estadismo Ontológico",
"Otros Conceptos Clave",
"Estado Mental General",
"Tolerancia a la Paradoja",
"Maestría Pasiva",
"Visión de Receptor Pasivo",
"Presencia Pautada",
"Limitación Percibida",
"Significado/Intención Percibida",
"Problema Percibido",
"Percepción",
"Agilidad Perceptual",
"Teoría de la Construcción Perceptual",
"Contrato Perceptual",
"Distorsión Perceptual",
"Encuadre Perceptual",
"Libertad Perceptual",
"Meta Perceptual",
"Maestría Perceptual",
"Reencuadre Perceptual",
"Técnica de Moldeamiento Perceptual",
"Sofisticación Perceptual",
"Superposición Perceptual",
"Tendencia Personal",
"Tendencia Personal (Sensibilidad Cognitiva)",
"Tendencia Personal (Persistencia del Estado de Ánimo)",
"Tendencia Personal (Persistencia Dimensional)",
"Tendencia Personal (Reactividad a Nuevos Eventos)",
"Tendencia Personal (Expresión del Rasgo)",
"Organización de la Personalidad",
"Fenómeno",
"Ingeniería de Plausibilidad",
"Limitaciones Prácticas de la Aplicación de QM",
"Sabiduría Práctica",
"Prácticas",
"Modalidad Principal",
"Modalidad Principal (Tríada Cognitivo-Ejecutiva)",
"Principio de Equilibrio",
"Principio de Límite",
"Principio de Medida",
"Principio de Contención",
"Principio de Simetría",
"Receptividad a los Principios",
"Influencia del Estado Anterior",
"Autorregulación Proactiva",
"Campo Probabilístico",
"Estado Mental Probabilístico",
"Dirección Probabilística",
"Mecanismo de Procesamiento",
"Sistema de Ansiedad Proyectada",
"Principio Protector",
"Proto-Impulso",
"Proxy",
"Arquitectura Psíquica",
"Dimensión Psico-Estética",
"Dimensión Psico-Conceptiva",
"Dimensión Psico-Empática",
"Dimensión Psico-Fundacional",
"Codificación Psico-Fundacional",
"Colapso Psico-Meditativo",
"Dimensión Psico-Meditativa",
"Estructuración Psico-Meditativa",
"Dimensión Psico-Motivacional",
"Impulso Psico-Motivacional",
"Dimensión Psico-Protectora",
"Dimensión Psico-Receptiva",
"Dimensión Psico-Transpersonal",
"Dimensión Psico-Volitiva",
"Dinámicas Psico-Volitivas",
"Campo Psico-Volitivo",
"Restauración del Equilibrio Psicodinámico",
"Colapso Psicodinámico",
"Dimensión Psicodinámica",
"Dimensiones Psicodinámicas",
"Fricción Psicodinámica",
"Alineación Armónica Psicodinámica",
"Navegación Psicodinámica",
"Colapso de la Onda Psicodinámica",
"Desarmonía Psicológica",
"Disfunción y Desequilibrio Psicológico",
"Entrelazamiento Psicológico",
"Corazón Psicológico",
"Fenómeno Psicológico",
"Autocirugía Psicológica",
"Estado Psicológico",
"Estructura Psicológica",
"Transformación Psicológica Vía Reasignación Ontológica",
"Tríada Psicosocial Emotiva",
"Potencialidad Pura",
"Redefinición del Propósito",
"Diplomacia Cuántica",
"Mindfulness Cuántico (Activo)",
"Observador Cuántico",
"Percepción Cuántica",
"Principio Cuántico",
"Huella Perceptual Bruta",
"Datos Sensoriales Brutos",
"Re-Convergencia",
"Fase 1: Reconocimiento y Distinción Perceptual",
"Conciencia Relacional",
"Salud Relacional",
"Mindfulness Relacional",
"Función de Relevancia",
"Fluidez Religiosa",
"Reputación",
"Entrenamiento y Desarrollo de Capacidades Requeridos",
"Fatiga de Resolución",
"Re-patronaje de Respuesta",
"Ingeniería Inversa de Patrones de Colapso",
"Ingeniería Inversa de Estados Emocionales",
"Modalidad Secundaria",
"Experiencia de Segunda Mano",
"Permeabilidad Selectiva",
"El Ser como Observador-Participante Dinámico",
"Construcción del Autoconcepto",
"Integridad del Ser",
"Realidad Compartida",
"Alfabetización Somática",
"Arquitectura Soberana",
"Protocolo Estandarizado",
"Influencia Estocástica",
"Gestión Estratégica de la Atención",
"Manipulación Estratégica de la Trayectoria Cognitiva",
"Arquitectura Estratégica de la Forma de Onda",
"Conciencia Estructural",
"Introspección Estructural",
"Comprensión Estructurada",
"Interferencia Sub-dinámica",
"Infraestructura Subconsciente",
"Método de Cultivo de la Superposición",
"Cognición Superposicional",
"Ingeniería Cognitiva Superposicional",
"Acción Sostenida",
"Mecanismo de Acción Sostenida",
"Deconstrucción de Sistemas",
"Conocimiento Tácito",
"Intervención Terapéutica para el Malestar y la Disfunción",
"Estrategia Terapéutica",
"Fase 2: Rastreo de Orígenes",
"Influencia del Rasgo",
"Variable de Rasgo",
"Modalidades de Transición",
"Desafío de la Traducción en Psicología",
"Fatiga de Traducción",
"Colapso Traumático",
"Colapso Reactivo Inconsciente",
"Consecuencia de Superposición no Resuelta",
"Alineación de Valores",
"Conciencia Vectorizada",
"Visión de la Percepción",
"Compromiso Volitivo",
"Continuidad Volitiva",
"Impulso Volitivo",
"Estructura de Vulnerabilidad",
"Voluntad",
"Voluntad de Conexión",
"Conciencia Testigo",
"Efecto Zeigarnik"
]

# Set the number of articles to generate for each topic
articles_per_topic = 1  # Change this number to generate more or fewer articles per subclass

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

            final_prompt = f"""---
Eres un escritor de blogs experto, especializado en el marco de la Mindfulness Cuántica. Tu tarea es reescribir y expandir el contenido del artículo proporcionado en una publicación de blog de alta calidad.

**INSTRUCCIONES CRÍTICAS PARA EL FORMATO Y CONTENIDO DE SALIDA:**

1.  **ESTRUCTURA EXACTA de Salida:** Tu respuesta DEBE consistir en dos partes, en este orden preciso:
    * **Front Matter YAML:** Un bloque de YAML encerrado entre líneas `---` al principio del archivo.
    * **Cuerpo del Artículo:** Inmediatamente después del `---` de cierre del YAML, el encabezado principal H3, seguido del contenido expandido del artículo.
    * **NO** incluyas ningún texto introductorio, preámbulos o comentarios conversacionales antes de la apertura `---` del Front Matter YAML.
    * **NO** incluyas ningún texto entre el `---` de cierre del YAML y el encabezado H3, excepto una sola línea en blanco para mayor legibilidad.

2.  **Propiedades del Front Matter YAML (Adherencia Estricta a la Muestra de Git it Write):**
    * `title`: El título principal del artículo. Este DEBE ser idéntico al encabezado H3 en el cuerpo del artículo. **ASEGÚRATE de que este valor esté entre comillas dobles.** **IMPORTANTE: El título DEBE ser un título único de una sola frase. No uses dos puntos o un subtítulo.** Ejemplo: `title: "Tu Título de Artículo Único"`
    * `menu_order`: Establece este valor en `1`.
    * `post_status`: Establece este valor en `publish`.
    * `post_excerpt`: Un resumen conciso de 2-3 oraciones del artículo. **ASEGÚRATE de que este valor esté entre comillas dobles.**
    * `taxonomy`: Esta clave contendrá tus categorías y etiquetas.
        * `category`: Una lista YAML de 1 a 3 categorías. **DEBES seleccionar ÚNICAMENTE de la siguiente lista predefinida:** ["Core Concepts", "Framework Principles", "Psychodynamic Dimensions", "Prime Modality", "Secondary Modality", "Formal Architecture", "Emergent Properties", "Therapeutic Strategies", "Challenges and Limitations", "Advanced Practices", "Mindfulness Approaches", "Human Capacities", "Goals", "Perception", "Practices"]. **Cada elemento de categoría en la lista DEBE estar entre comillas dobles.** Ejemplo: `  - "Categoría Uno"`
        * `post_tag`: Una lista YAML de 3 a 7 etiquetas relevantes. Estas pueden ser más específicas y no necesitan estar en una lista predefinida, pero deben derivarse del contenido del artículo y de la ontología de Mindfulness Cuántica. **Cada elemento de etiqueta en la lista DEBE estar entre comillas dobles.** Ejemplo: `  - "etiqueta-uno"`
    * `custom_fields`: Un mapa YAML vacío `{{}}`.

3.  **Contenido del Cuerpo del Artículo (Adherencia Estricta):**
    * **Longitud:** Expande el artículo para que tenga entre 700 y 1000 palabras.
    * **Tono:** Mantén un tono claro, atractivo e informativo, adecuado para una audiencia general interesada en la mindfulness y la psicología.
    * **Profundidad:** Asegúrate de que el contenido reescrito sea coherente, fluya bien y profundice en los conceptos presentados, basándose en los principios y la terminología que se encuentran en la Ontología de Mindfulness Cuántica proporcionada a continuación.
    * **NUEVA INSTRUCCIÓN: Cuando utilices terminología de la ontología, no encierres los términos entre comillas. Intégralos fluidamente en la prosa como si fueran lenguaje natural para el tema.**
    * **Encabezados:** El ÚNICO encabezado de nivel superior en el cuerpo del artículo debe ser el encabezado principal H3 (`### Tu Título de Artículo`).
    * **LIMPIEZA:** ABSOLUTAMENTE NO incluyas ningún encabezado `## ARTICLES`, `## Article N`, `## Articulo N`, o cualquier otro encabezado de nivel `##` dentro del cuerpo del artículo. Elimina cualquier encabezado de este tipo del contenido original.
    * **Sin Títulos Redundantes:** Asegúrate de que el encabezado H3 esté presente solo una vez al principio del cuerpo del artículo, inmediatamente después del YAML.

**Referencia de la Ontología de Mindfulness Cuántica (para contexto y terminología):**
{ontology_content}

**Tu Artículo Reescribido (con Front Matter YAML):**
"""
            # Generate content
            try:
                response = model.generate_content(
                    contents=[{"role": "user", "parts": [{"text": final_prompt}]}],
                    generation_config=GenerationConfig(
                        temperature=0.7,
        top_p=1.0,
        top_k=32.0,
                        #max_output_tokens=2048,
                        stop_sequences=[] # This prevents the model from stopping on "---"
                    )
                )

                # --- Process and save the generated article ---
                if response and response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
                    generated_text = response.candidates[0].content.parts[0].text
                    if generated_text: # Ensure the generated text is not empty
                        # Create a clean filename from the topic name
                        safe_topic_name = topic.replace(" ", "_").replace("/", "_")
                        output_filename = f"generated_qm_article_{safe_topic_name}_{i+1}.md"
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
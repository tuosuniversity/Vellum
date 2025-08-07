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
OUTPUT_ARTICLE_FOLDER = "Texts/"

print("[*] Script started.")
print(f"[*] Using Project ID: {PROJECT_ID}, Location: {LOCATION}, Model: {MODEL_NAME}")
print(f"[*] Ontology File: {ONTOLOGY_FILE_PATH}")
print(f"[*] Output Folder: {OUTPUT_ARTICLE_FOLDER}")

# Ensure the output directory exists
os.makedirs(OUTPUT_ARTICLE_FOLDER, exist_ok=True)

# --- Define the list of top subclasses ---
top_subclass_topics = [
"Abstract Internal Experience",
"Actionable Intelligence",
"Active Constitutive Force View",
"Active Knowing",
"Active Mastery",
"Active Reframing Process",
"Active Structural Investigation",
"Actualization Process",
"Actualized Experience",
"Advanced Practices and Methodologies Category",
"Aesthetic Principle",
"Aesthetic Resolution",
"Analytical Reasoning",
"Anxiety",
"Assigned Meaning",
"Attention Sculpting",
"Attunement",
"Average Valence of Prior State (AvgValence(S_t-1))",
"Behavioral Manifestation",
"Belief Formation",
"Biological Override System",
"Bones of Reality",
"Bounded Compassion",
"Chaos Concierge Pattern",
"Challenges and Limitations",
"Challenges and Limitations Category",
"Classical Mindfulness",
"Cognitive Agency",
"Cognitive Anchoring",
"Cognitive Anchoring Component",
"Cognitive Anchoring Failure",
"Cognitive Anchoring Failure Consequence",
"Cognitive Appraisal",
"Cognitive Appraisal Bias (Bias_M1)",
"Cognitive Appraisal Component",
"Cognitive Appraisal Components Category",
"Cognitive Bias",
"Cognitive Capacity",
"Cognitive Collapse",
"Cognitive Decoherence",
"Cognitive Distillation",
"Cognitive Emergence Field",
"Cognitive-Emotional Pattern Inheritance",
"Cognitive Endurance",
"Cognitive Enhancement",
"Cognitive Entropic Drift",
"Cognitive Field Manipulation",
"Cognitive Filtering Mechanism",
"Cognitive Flow",
"Cognitive Fluency",
"Cognitive Influence",
"Cognitive Mapping",
"Cognitive Measurement",
"Cognitive Mechanism",
"Cognitive Modality",
"Cognitive Multi-State Awareness",
"Cognitive Optimization",
"Cognitive Optimization and Refinement",
"Cognitive Overwhelm",
"Cognitive Process",
"Cognitive Resources",
"Cognitive Strain and Dysfunction",
"Cognitive Structuring Approaches",
"Cognitive Superposition",
"Collapse Dysfunction",
"Collapse Fatigue",
"Collapse Influence Practice",
"Collapse Mode",
"Collapse Point Interventions",
"Conditioning Mechanism",
"Confirmation Bias and Reality Construction Cycle",
"Conscious Attention",
"Conscious Awareness",
"Conscious Observation",
"Conscious Reality Construction",
"Conscious Reality Creation / Perceptual Reframing",
"Conscious Stack",
"Conscious State Management",
"Consciousness Fortification",
"Consciousness Refinement",
"Consciousness Wave Function",
"Constructed Reality",
"Constructive Interference",
"Contemplation",
"Contemplative Experimentation",
"Contemplative Inquiry",
"Continuous Mentation Model",
"Core Concepts Category",
"Craftsmanship of Collapse",
"Creative Genesis",
"Creative Paralysis",
"Creative Potential",
"Cultivation Method",
"Cultural Narrative",
"Decision Architecture",
"Decoherence Backlog",
"Decoupling Phase",
"Deep Psychological Trauma",
"Destructive Interference",
"Developmental Interference Pattern",
"Dimensional Activation (Kj)",
"Dimensional Activation Influence",
"Dimensional Activation Influences Category",
"Dimensional Attunement",
"Dimensional Crystallization",
"Dimensional Literacy",
"Dimensional Misalignment",
"Directed Cognitive Engagement (f)",
"Dissociative State",
"Dynamic and Interconnected Network",
"Dysfunctional Pattern",
"Embodied Mindfulness",
"Emergent Properties Category",
"Emotional Collapse Sculpting",
"Emotional Creativity",
"Emotional Openness",
"Emotional Quantum Entanglement",
"Emotional Reactivity Pattern",
"Emotional Regulation / Affective Modulation",
"Emotional Response",
"Emotional Rewilding",
"Emotional Storm Theory",
"Empirical Absence",
"Engagement Style",
"Enhanced Decision-Making",
"Environmental Influence",
"Environmental Resonance",
"Epistemological Challenges",
"Epistemological Discernment",
"Ethical Boundaries",
"Examples",
"Executive Function Training",
"Existential Dissonance",
"Experienced Reality",
"Experiential Limit",
"External Influence",
"Final Intensity (xj)",
"Flow Dynamics in Consciousness",
"Formal Architecture Category",
"Formal Testimony",
"Framework Principle",
"Framework Principles Category",
"Free Will",
"Fundamental Energetic Substrate",
"General Awareness (A)",
"Geometric Dimensions of Awareness",
"Goal Abandonment",
"Goals Category",
"Grounding Function",
"Historical Imprint / Trauma Imprint",
"Human Capacities Category",
"Humor as Cognitive Technology",
"Identity",
"Identity Transformation Process",
"Impact of the Now",
"Imposter Syndrome",
"Impulse Reactivity",
"Impulse Toward Generative Sharing",
"Incomplete Process Tension",
"Inertia of the Past",
"Inferential Epistemology",
"Influential Factor",
"Inherent Disposition (Bias_M1)",
"Inherited Script",
"Inherited Scripts",
"Institutional Architecture Imposition",
"Integrated Therapeutic Approaches",
"Intentional Collapse",
"Interference Pattern",
"Interference Patterns",
"Internal Cartography",
"Internal Conflict Resolution",
"Internal Map of Psychological Functioning",
"Interpersonal Relationship Experience",
"Intersubjective Reality",
"Intersubjective Resonance",
"Intuitive Cognition",
"Jealousy",
"Knowledge Acquisition",
"Learned Behavioral Repertoire",
"Liberation from Inherited Scripts",
"Liberation Phase",
"Liberation Process",
"Limitation of Direct Observation",
"Main Strategies Category",
"Management of Cognitive Strain and Dysfunction",
"Manipulation of Constructed Reality",
"Mental Filesystem Organization",
"Mental Flexibility",
"Mental-Physical Interface",
"Mental Quanta",
"Mental State",
"Mind Controls Brain Principle",
"Mindfulness Approaches Comparison Category",
"Mindfulness Based Cognitive Therapy (MBCT)",
"Mindfulness Based Stress Reduction (MBSR)",
"Mindfulness Goal",
"Mindfulness Intervention",
"Multidimensional Scanning",
"Narrative Management",
"Natural Development",
"Neurological Embedding",
"Non-Local Cognition",
"Non-Material Phenomenon",
"Non-Reactive Observation",
"Nonlocal Goal State",
"Objective Constraints",
"Observable Effect",
"Observation (Ψ)",
"Observation Components Category",
"Observation Influence (IΨj)",
"Observation Valence (Valence(Ψ))",
"Observer Effect Paradox",
"Observer Function",
"Observer-Participant Dynamic",
"Observer-Participant Role",
"Observer-Participant Theory",
"Observer Role",
"Ontological Field Theory",
"Ontological Firewall",
"Ontological Misalignment",
"Ontological Reassignment",
"Ontological Restructuring",
"Ontological Starvation",
"Ontological Statecraft",
"Optimal Cognitive State",
"Osmotic Integration",
"Other Key Concepts",
"Overall Mental State (S)",
"Paradox Tolerance",
"Passive Mastery",
"Passive Recipient View",
"Patterned Presence",
"Perceived Limitation",
"Perceived Meaning/Intent (β)",
"Perceived Problem",
"Perception",
"Perceptual Agility",
"Perceptual Construction Theory",
"Perceptual Contract",
"Perceptual Distortion",
"Perceptual Framing",
"Perceptual Freedom",
"Perceptual Goal",
"Perceptual Mastery",
"Perceptual Reframing",
"Perceptual Shaping Technique",
"Perceptual Sophistication",
"Perceptual Superposition",
"Personal Tendency (w)",
"Personal Tendency (Cognitive Responsiveness - wCj)",
"Personal Tendency (Mood Persistence - wS)",
"Personal Tendency (Dimensional Persistence - wSj)",
"Personal Tendency (Reactivity to New Events - wΨ)",
"Personal Tendency (Reactivity - wΨ)",
"Personal Tendency (Trait Expression - wTj)",
"Personality Organization",
"Phenomenon",
"Plausibility Engineering",
"Practical Limitations of QM Application",
"Practical Wisdom",
"Practices Category",
"Prime Modality (M1)",
"Prime Modality Category",
"Principle of Balance",
"Principle of Limit",
"Principle of Measure",
"Principle of Restraint",
"Principle of Symmetry",
"Principle Receptivity",
"Prior State Influence (ISj)",
"Proactive Self-Regulation",
"Probabilistic Field",
"Probabilistic Mental State",
"Probabilistic Steering",
"Processing Mechanism",
"Projected Anxiety System",
"Protective Principle",
"Proto-Impulse",
"Proxy",
"Psychic Architecture",
"Psycho-Aesthetic Dimension (Pd6)",
"Psycho-Conceptive Dimension (Pd2)",
"Psycho-Empathic Dimension (Pd4)",
"Psycho-Foundational Dimension (Pd9)",
"Psycho-Foundational Encoding",
"Psycho-Meditative Collapse",
"Psycho-Meditative Dimension (Pd3)",
"Psycho-Meditative Structuring",
"Psycho-Motivational Dimension (Pd7)",
"Psycho-Motivational Momentum",
"Psycho-Protective Dimension (Pd5)",
"Psycho-Receptive Dimension (Pd8)",
"Psycho-Transpersonal Dimension (Pd10)",
"Psycho-Volitional Dimension (Pd1)",
"Psycho-Volitional Dynamics",
"Psycho-Volitional Field",
"Psychodynamic Balance Restoration",
"Psychodynamic Collapse",
"Psychodynamic Dimension (Pdj)",
"Psychodynamic Dimensions Category",
"Psychodynamic Friction",
"Psychodynamic Harmonic Alignment",
"Psychodynamic Navigation",
"Psychodynamic Wave Collapse",
"Psychological Disharmony",
"Psychological Dysfunction and Imbalance",
"Psychological Entanglement",
"Psychological Heart",
"Psychological Phenomenon",
"Psychological Self-Surgery",
"Psychological State",
"Psychological Structure",
"Psychological Transformation via Ontological Reassignment",
"Psychosocial Emotive Triad",
"Pure Potentiality",
"Purpose Redefinition",
"Quantum Diplomacy",
"Quantum Mindfulness Application",
"Quantum Observer",
"Quantum Perception",
"Quantum Principle",
"Raw Perceptual Imprint (α)",
"Raw Sensory Data",
"Re-Convergence",
"Recognition Phase",
"Relational Consciousness",
"Relational Health",
"Relational Mindfulness",
"Relevance Function (Relevance(Ψ, Pd_j))",
"Religious Fluidity",
"Reputation",
"Required Training and Capacity Development",
"Resolution Fatigue",
"Response Re-Patterning",
"Reverse Engineering Collapse Patterns",
"Reverse Engineering Emotional States",
"Secondary Modality (M2)",
"Secondary Modality Category",
"Secondhand Experience",
"Selective Permeability",
"Self as Dynamic Observer-Participant",
"Self-Concept Construction",
"Self Integrity",
"Shared Reality",
"Sigmoid Function",
"Social Influence",
"Somatic Literacy",
"Sovereign Architecture",
"Standardized Protocol",
"Stochastic Influence (εj)",
"Strategic Attention Management",
"Strategic Cognitive Trajectory Manipulation",
"Strategic Waveform Architecture",
"Structural Awareness",
"Structural Introspection",
"Structured Understanding",
"Sub-dynamic Interference",
"Subconscious Infrastructure",
"Superposition Cultivation Method",
"Superpositional Cognition",
"Superpositional Cognitive Engineering",
"Sustained Action",
"Sustained Action Mechanism",
"System Deconstruction",
"Tacit Knowledge",
"Therapeutic Intervention for Distress and Dysfunction",
"Therapeutic Strategy",
"Tracing Origins Phase",
"Trait Influence (ITj)",
"Trait Variable (Tj)",
"Transitional Modalities",
"Translation Challenge in Psychology",
"Translation Fatigue",
"Traumatic Collapse",
"Unconscious Reactive Collapse",
"Unresolved Superposition Consequence",
"Value Alignment",
"Vectorized Awareness",
"View of Perception",
"Volitional Commitment",
"Volitional Continuity",
"Volitional Impulse",
"Vulnerability Structure",
"Will",
"Will-to-Connection",
"Witness Consciousness",
"Zeigarnik Effect"
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
You are an expert blog writer, specializing in the Quantum Mindfulness framework. Your task is to rewrite and expand the provided article content into a high-quality blog post.

**CRITICAL INSTRUCTIONS FOR OUTPUT FORMAT & CONTENT:**

1.  **EXACT Output Structure:** Your response MUST consist of two parts, in this precise order:
    * **Front Matter YAML:** A block of YAML enclosed by `---` lines at the beginning of the file.
    * **Article Body:** Immediately following the closing `---` of the YAML, the main H3 heading, followed by the expanded article content.
    * **DO NOT** include any introductory text, preambles, or conversational remarks before the opening `---` of the Front Matter YAML.
    * **DO NOT** include any text between the closing `---` of the YAML and the H3 heading, except for a single blank line for readability.

2.  **Front Matter YAML Properties (Strict Adherence to Git it Write Sample):**
    * `title`: The main title of the article. This MUST be identical to the H3 heading in the article body. **ENSURE this value is enclosed in double quotes.** **IMPORTANT: The title MUST be a unique, single-phrase title. Do not use a colon or a subtitle.**
    * `menu_order`: Set this value to `1`.
    * `post_status`: Set this value to `publish`.
    * `post_excerpt`: A concise 2-3 sentence summary of the article. **ENSURE this value is enclosed in double quotes.**
    * `taxonomy`: This key will contain your categories and tags.
        * `category`: A YAML list of 1 to 3 categories. **You MUST select ONLY from the following predefined list:** ["Core Concepts", "Framework Principles", "Psychodynamic Dimensions", "Prime Modality", "Secondary Modality", "Formal Architecture", "Emergent Properties", "Therapeutic Strategies", "Challenges and Limitations", "Advanced Practices", "Mindfulness Approaches", "Human Capacities", "Goals", "Perception", "Practices"]. **Each category item in the list MUST be enclosed in double quotes.** Example: `  - "Category One"`
        * `post_tag`: A YAML list of 3 to 7 relevant tags. These can be more specific and do not need to be in a predefined list, but should be derived from the content of the article and the Quantum Mindfulness ontology. **Each tag item in the list MUST be enclosed in double quotes.** Example: `  - "tag-one"`
    * `custom_fields`: A blank YAML map `{{}}`.

3.  **Article Body Content (Strict Adherence):**
    * **Length:** Expand the article to be between 700 and 1000 words.
    * **Tone:** Maintain a clear, engaging, and informative tone, suitable for a general audience interested in mindfulness and psychology.
    * **Depth:** Ensure the rewritten content is coherent, flows well, and expands on the concepts presented, drawing upon the principles and terminology found in the Quantum Mindfulness Ontology provided below.
    * **NEW INSTRUCTION: When using terminology from the ontology, do not enclose the terms in quotation marks. Integrate them smoothly into the prose as if they were natural language for the topic.**
    * **Headings:** The ONLY top-level heading in the article body must be the main H3 heading (`### Your Article Title`).
    * **CLEANLINESS:** ABSOLUTELY DO NOT include any `## ARTICLES`, `## Article N`, `## Articulo N`, or any other `##` level headings within the article body. Remove any such headings from the original content.
    * **No Redundant Titles:** Ensure the H3 heading is present only once at the very beginning of the article body, immediately after the YAML.

**Quantum Mindfulness Ontology Reference (for context and terminology):**
{ontology_content}

**Your Rewritten Article (with Front Matter YAML):**
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
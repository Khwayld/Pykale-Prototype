# ==========================
# General Configuration
# ==========================
N_SAMPLES = 200
DEFAULT_SEED = 29118

# ==========================
# UI styling constants
# ==========================
PRIMARY_COLOR = "#16a085"
SUBHEADING_COLOR = "#2980b9"

# ==========================
# Routes metadata
# ==========================
PAGE_MAP = {
    "[HOME_LINK]": ("Home Page", "home"),
    "[HUB_LINK]": ("Hub Page", "hub"),
    "[VIDEO_EXAMPLE_LINK]": ("Video Demo", "video_example"),
    "[DOMAIN_ADAPTATION_LINK]": ("Domain Adaptation", "domain_adaptation"),
    "[INTRODUCTION_LINK]": ("Introduction", "introduction"),
    "[KALE_API_LINK]": ("Kale API Guide", "kale_api"),
    "[CHATBOT_PAGE_LINK]": ("Chatbot", "chatbot_page"),
    "[LOADDATA_PAGE_LINK]": ("Load Data", "loaddata_page"),
    "[PREPDATA_PAGE_LINK]": ("Prep Data", "prepdata_page"),
    "[EMBED_PAGE_LINK]": ("Embed Page", "embed_page"),
    "[PREDICT_PAGE_LINK]": ("Predict Page", "predict_page"),
    "[EVALUATE_PAGE_LINK]": ("Evaluate Page", "evaluate_page"),
    "[INTERPRET_PAGE_LINK]": ("Interpret Page", "interpret_page"),
    "[PIPELINE_PAGE_LINK]": ("Pipeline Page", "pipeline_page"),
    "[BUILD_FIRST_MODEL_PAGE_LINK]": ("Build First Model", "build_first_model_page")
}

# ==========================
# Hub section cards
# Used to render the main dashboard/hub page
# ==========================
HUB = [
    {
        "name": "Getting Started with PyKale",
        "description": "An introduction to PyKale, its purpose, and how to use it.",
        "image": "https://avatars.githubusercontent.com/u/63680111?s=200&v=4",
        "nav": "introduction",
        "category": "Guides"
    },
    {
        "name": "The KALE API",
        "description": "A detailed breakdown of how the PyKale API works.",
        "image": "https://avatars.githubusercontent.com/u/63680111?s=200&v=4",
        "nav": "kale_api",
        "category": "Guides"
    },
    {
        "name": "Domain Adaptation on Toy Data",
        "description": "An interactive tutorial & demo of domain adaptation with PyKale.",
        "image": "https://avatars.githubusercontent.com/u/63680111?s=200&v=4",
        "nav": "domain_adaptation",
        "category": "Demo"
    },
    {
        "name": "Video Dataset Loading & Augmentation",
        "description": "An interactive demonstration on video preprocessing using PyKale.",
        "image": "https://avatars.githubusercontent.com/u/63680111?s=200&v=4",
        "nav": "video_example",
        "category": "Demo"
    },
    {
        "name": "Build Your First PyKale Model",
        "description": "A quick-start guide on building and running your first PyKale model",
        "image": "https://avatars.githubusercontent.com/u/63680111?s=200&v=4",
        "nav": "build_first_model_page",
        "category": "Tutorial"
    }
]

MODULES = [
    {"name": "📂 Data Handling (loaddata)", "desc": "Load and manage datasets (images, videos, graphs).", "nav": "loaddata_page"},
    {"name": "⚙️ Data Preprocessing (prepdata)", "desc": "Transform raw data for modeling.", "nav": "prepdata_page"},
    {"name": "📑 Feature Extraction (embed)", "desc": "Extract feature representations using embeddings.", "nav": "embed_page"},
    {"name": "🔍 Model Prediction (predict)", "desc": "Build and apply ML models for predictions.", "nav": "predict_page"},
    {"name": "📊 Evaluation (evaluate)", "desc": "Measure performance using evaluation metrics.", "nav": "evaluate_page"},
    {"name": "🔎 Interpretation (interpret)", "desc": "Visualize and explain model decisions.", "nav": "interpret_page"},
    {"name": "🔗 Pipeline (pipeline)", "desc": "Combine all steps into a unified workflow.", "nav": "pipeline_page"},
]

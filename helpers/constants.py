DEFAULT_SEED = 29118
N_SAMPLES = 200

PRIMARY_COLOR = "#16a085"
SUBHEADING_COLOR = "#2980b9"

EXAMPLES = [
    {
        "name": "Video Loading Example",
        "description": "Load frames from short clips and display them in Streamlit for quick analysis.",
        "image": "",
        "nav": "video_example",
        "category": "Video Processing"
    },
    
    {
        "name": "Domain Adaptation Example",
        "description": "Learn to adapt models across related domains for more robust predictions.",
        "image": "",
        "nav": "domain_adaptation",
        "category": "Domain Adaptation",
    },

    {
        "name": "Third Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation",
        "category": "Other Transfer Learning"
    },

    {
        "name": "Fourth Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation",
        "category": "Multi-Modal"
    },

    {
        "name": "Fifth Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation",
        "category": "Domain Adaptation"
    },

    {
        "name": "Sixth Example",
        "description": "Some Description",
        "image": "",
        "nav": "domain_adaptation",
        "category": "Video Processing"
    }
]


SYSTEM_PROMPT = """
You are PyKale Assistant, an AI specialized in the PyKale library.
Here is some information about PyKale:
- PyKale is a library built on PyTorch for multimodal learning and transfer learning from multiple data sources.
- It includes modules for domain adaptation, video loading and transforms, and more.
- We have examples like 'Video Loading Example', 'Domain Adaptation Example', etc.
Please guide the user step by step to use PyKale if they need, or point them to specific examples.
Always greet them politely and remain helpful.
"""

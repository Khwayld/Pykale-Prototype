# Core pages
from views.home_page import home_page
from views.hub_page import hub_page
from views.chatbot.chatbot_page import chatbot_page
from views.train_page import train_model_page

# Demos
from views.demos.video_demo.video_demo import video_demo_page
from views.demos.domain_demo.domain_adaptation_demo import domain_adaptation_page

# Guides
from views.guides.introduction_guide import introduction_page
from views.guides.kale_api_guide.kale_api_guide import kale_api_page
from views.guides.kale_api_guide.embed_page import embed_page
from views.guides.kale_api_guide.loaddata_page import loaddata_page
from views.guides.kale_api_guide.prepdata_page import prepdata_page
from views.guides.kale_api_guide.predict_page import predict_page
from views.guides.kale_api_guide.evaluate_page import evaluate_page
from views.guides.kale_api_guide.interpret_page import interpret_page
from views.guides.kale_api_guide.pipeline_page import pipeline_page



ROUTES = {
    "home": home_page,
    "hub": hub_page,
    "chatbot_page": chatbot_page,
    "train_page": train_model_page,
    "video_example": video_demo_page,
    "domain_adaptation": domain_adaptation_page,
    "introduction": introduction_page,
    "kale_api": kale_api_page,
    "loaddata_page": loaddata_page,
    "prepdata_page": prepdata_page,
    "embed_page": embed_page,
    "predict_page": predict_page,
    "evaluate_page": evaluate_page,
    "interpret_page": interpret_page,
    "pipeline_page": pipeline_page,
}



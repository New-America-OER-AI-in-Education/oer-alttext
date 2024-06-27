from typing import List
from fdllm import get_caller
from fdllm.chat import ChatController
from PIL import Image
import fitz
from io import BytesIO
from tqdm import tqdm

# dotenv
from dotenv import load_dotenv
load_dotenv()

# load image
# image = Image.open("image.png")

# chatter = ChatController(Caller=get_caller("gpt-4o"))

# languages = []
# text_length = None
# inmsg, outmsg = chatter.chat(f"ONLY SAY THE ANSWER. Give me good standard of alt text for these images, leave a new line between each language. Generate it in these languages ${languages}. Make sure the text length is no larger than ${text_length}", images=[image], detail='high')

# print(outmsg.Message)

chatter = ChatController(Caller=get_caller("gpt-4o"))



def process_image(image: any, languages: List[str], verbosity: int, grade: str, robustness: str, subject: str, text_length: int, feedback="", additional_prompt=""):
    inmsg, outmsg = chatter.chat("Image: ONLY GIVE THE ANSWER. Give me a good standard alt text for the image inputted." + 
                                 "Be sure to leave a blank line between each language output " + 
                                 "(if it is only one language output, make sure all the content is in one line). " +
                                 f"Generate it in these languages: ${languages} (if no language is selected, leave it in English) " +
                                 f"If a subject is selected: ${subject}, give the alt text in the context of the subject selected (if there is no subject, " +
                                 f"give the alt text in a general context).  If an education level is selected: ${grade}, give the alt text in the context of the education level " + 
                                 "(if there is no education level, give the alt text in a general context). " +
                                 f"The verbosity should like ${verbosity} (if no verbosity is selected, default to medium). " +
                                 f"The length of the alt text: ${text_length} should default to no longer than 125 characters, unless otherwise selected.)" + 
                                 f"Additional prompt info: ${additional_prompt}." + 
                                 f"Feedback from previous prompts: ${feedback}", detail=robustness.lower(), images=[image])
    
    return outmsg.Message

def process_pdf(pdf, languages: List[str], verbosity: int, grade: str, robustness: str, subject: str, text_length: int, feedback="", additional_prompt=""):
    f = fitz.open(stream=pdf, filetype="pdf")
    npages = f.page_count
    text = []
    images = []
    
    for pagen in tqdm(range(npages)):
        page = f.load_page(pagen)
        text_ = page.get_text()
        image_list = page.get_images(full=True)
        images_ = [
            Image.open(BytesIO(f.extract_image(img_[0])["image"])) for img_ in image_list
        ]

        text.append(text_)
        images.extend(images_)  # Flatten the list of images

    inmsg, outmsg = chatter.chat("PDF: ONLY GIVE THE ANSWER. Give me a good standard alt text for all of the images inputted." + 
                                 "Be sure to leave a blank line between each language output " + 
                                 "(if it is only one language output, make sure all the content is in one line). " +
                                 f"Generate it in these languages: ${languages} (if no language is selected, leave it in English) " +
                                 f"If a subject is selected: ${subject}, give the alt text in the context of the subject selected (if there is no subject, " +
                                 f"give the alt text in a general context).  If an education level is selected: ${grade}, give the alt text in the context of the education level " + 
                                 "(if there is no education level, give the alt text in a general context). " +
                                 f"The verbosity should like ${verbosity} (if no verbosity is selected, default to medium). " +
                                 f"The length of the alt text: ${text_length} should default to no longer than 125 characters, unless otherwise selected.)" + 
                                 f"Additional prompt info: ${additional_prompt}." + 
                                 f"Feedback from previous prompts: ${feedback}", detail=robustness.lower(), images=images)
    
    return outmsg.Message
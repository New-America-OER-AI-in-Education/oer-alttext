from typing import List
from fdllm import get_caller
from fdllm.chat import ChatController
from PIL import Image

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
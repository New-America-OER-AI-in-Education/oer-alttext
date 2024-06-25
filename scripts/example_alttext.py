# %%
from io import BytesIO
from pathlib import Path

import fitz
from dotenv import load_dotenv
load_dotenv(override=True)

from fdllm import get_caller
from fdllm.chat import ChatController
from PIL import Image
from tqdm import tqdm

from project import DATADIR

# %% Read images from a specified PDF
testfile = (
    DATADIR
    / "Flexbooks"
    / "Earth Science"
    / "CK-12-Earth-Science-For-Middle-School_b_v1_smr.pdf"
)
f = fitz.open(testfile)
npages = f.page_count
text = []
images = []
# load the text and images from each page of the pdf
for pagen in tqdm(range(npages)):
    page = f.load_page(pagen)
    text_ = page.get_text()
    image_list = page.get_images(full=True)
    images_ = [
        Image.open(BytesIO(f.extract_image(img_[0])["image"])) for img_ in image_list
    ]

    text.append(text_)
    images.append(images_)

# %%
# select an image-capable OpenAI model (any of these)
model = "gpt-4o"
# model = "gpt-4-turbo"
# model = "gpt-4-vision-preview"

# this instantiates a chat with the selected model
chatter = ChatController(Caller=get_caller(model))

# lets start with the simplest possible prompt
prompt = "Please describe these images"
# here we call the model passing in the image from page 16
inmsg, outmsg = chatter.chat(prompt, images=images[15])
print(outmsg.Message)
images[15][0]

# %% try a prompt to get a more concise description more suitable for an alt-text tag
chatter = ChatController(Caller=get_caller("gpt-4o"))
# here we suggest 20 words
prompt = """
Please describe these images for an alt-text to enable a blind person to
understand what is shown in the image. The description should be less than 20
words per image.
""".replace( "\n", " ").strip()
inmsg, outmsg = chatter.chat(
    prompt,
    images=images[15],
)
print(outmsg.Message)
images[15][0]

# %% 
# maybe 20 words is a bit too concise, here we try a different model with more words
chatter = ChatController(Caller=get_caller("gpt-4-turbo"))
max_words = 60
prompt = f"""
Please describe these images for an alt-text to enable a blind person to
understand what is shown in the image. The description should be less than {max_words} 
words per image.
""".replace( "\n", " ").strip()
inmsg, outmsg = chatter.chat(
    prompt,
    images=images[15],
)
print(outmsg.Message)
images[15][0]

# %%
# other parameters of interest:
# ChatController.chat function:
# detail = 'low' , 'high' (default 'low'). This sets the image resolution for OpenAI

# ChatController init:
#    Sys_Msg={
#        0: "This will appear at the start of the conversation"
#        -1: "This will appear at the end of the conversation, after the user chat input"
#        -2: "This will appear at the end of the conversation, before the user chat input"
#    }
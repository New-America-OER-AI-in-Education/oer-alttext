# %%
from pathlib import Path
from io import BytesIO

from dotenv import load_dotenv
load_dotenv(override=True)

from PIL import Image
import fitz
from tqdm import tqdm
from fdllm import get_caller
from fdllm.chat import ChatController

# %%
testfile = (
    Path(__file__).resolve().parent
    / "data"
    / "CK-12-Earth-Science-For-Middle-School_b_v1_smr.pdf"
)

# %%
f = fitz.open(testfile)
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
    images.append(images_)

# %%
chatter = ChatController(Caller=get_caller("gpt-4-vision-preview"))

inmsg, outmsg = chatter.chat("Describe these images", images=images[15])

# %%
print(outmsg.Message)
images[15][0]
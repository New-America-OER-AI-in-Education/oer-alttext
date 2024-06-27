from fdllm import get_caller
from fdllm.chat import ChatController
from PIL import Image

# load image
image = Image.open("image.png")

chatter = ChatController(Caller=get_caller("gpt-4o"))

languages = []
text_length = None
inmsg, outmsg = chatter.chat(f"ONLY SAY THE ANSWER. Give me good standard of alt text for these images, leave a new line between each language. Generate it in these languages ${languages}. Make sure the text length is no larger than ${text_length}", images=[image], detail='high')

print(outmsg.Message)
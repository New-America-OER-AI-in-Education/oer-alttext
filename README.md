
# Improving accessibility by automatically generating alt-text for images

## FabData LLM

This project uses the [FabData LLM](https://github.com/AI-for-Education/fabdata-llm) package, which provides a convenient chatbot-style API to a range of LLM models. You can find an overview of the package in the project [README](https://github.com/AI-for-Education/fabdata-llm/blob/main/README.md). This is provided as a framework with the tooling necessary to quickly start working on the problem, but please feel free to use other LLM frameworks if you prefer or are familiar with them. 

## OpenAI access keys

OpenAI are kindly supporting this event by providing access. You will need to download the `env` file from the [hackathon dropbox](https://www.dropbox.com/scl/fo/xcranzh6fora7nyyqu4wf/ANtNTFNr7nUHHaWi1agegVo?rlkey=lhjg2dg72oiecnwyke0u8x2q9&dl=0), and put it in this project folder named `.env`. 

## Data and Example

You can use whatever content you like from OER Commons. For example there is a large quantity of online courseware. You can use the metadata database from the other projects to investigate this if you like. However, to get you started we have included a number of [Flexbooks](https://www.ck12.org/fbbrowse/) from the CK-12 Foundation, which are textbooks curated from OERCommons hosted content. You can find the available Flexbooks in PDF format [here](https://www.dropbox.com/scl/fo/y67u4dgtdcc8b8qxqsr4m/AK_l7I3-Ac_lXiIbKX6qzqw?rlkey=0bm04kvv1od48xgugwa1m6r2j&dl=0). Download the `Flexbooks` folder and put it in a `data` sub-folder of this project. 

## Possible Tasks

- How to evaluate the generated alt-texts from different models and different prompts? What makes a good alt-text, and how does it differ from the captions the images currently have in the Flexbooks? Does this depend on the area (maybe scientific diagrams have different requirements in terms of useful level of detail than illustrations in a social science text). Is there a trade-off between conciseness vs detail, and what is better for accessibility? Is our idea of alt-text limited by current implementations (i.e. html alt-text). How could this be improved? Perhaps there could be two levels of description, concise (~20 words) and a more detailed description (>100 words).
- How can the prompts used for this task be optimized? Are the outputs improved by including more context, i.e. the title of that chapter or the abstract, goals and audience of that book? What shoudl we ask the model to do to optimize accessibility?
- Can we make a minimum viable product using this approach? ie convert the pdf content to a website with alt-text, perhaps with different levels of conciseness (buttons? mouseover?)
- Could you make a webapp (using streamlit or some other approach) that takes an arbitrary content page from the web, and produces a copied version with alt-text added. 
# imports

import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI


# GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

# google_api_key = os.getenv("GOOGLE_API_KEY")
ollama_api_key = "ollama"

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key=ollama_api_key)

# if not google_api_key:
#     print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
# elif not google_api_key.startswith("AIz"):
#     print("An API key was found, but it doesn't start AIz")
# else:
#     print("API key found and looks good so far!")

# Define our system prompt

system_prompt = """
You are a office assistant that analyzes the contents of a website,
and provides a short, accurate summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""


# Define our user prompt

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""

# See how this function creates exactly the format above

def messages_for(url_content):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + url_content}
    ]


# And now: call the OpenAI API. You will get very familiar with this!

def summarize(url):
    url_content = fetch_website_contents(url)
    response = ollama.chat.completions.create(
        model = "llama3.2",
        messages = messages_for(url_content)
    )
    return response.choices[0].message.content


# A function to display this nicely in the output, using markdown

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))



url = input("Enter url or website address. The address you be in the format https://url.doman :")
url = f"https://{url}"
print("")
print(f"You entered {url}")
print("")

display_summary(url)

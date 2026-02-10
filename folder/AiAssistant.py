# accept voice input and turn it into text

import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from openai import OpenAI
from dotenv import dotenv_values
from pathlib import Path


#BASE_DIR = Path(__file__).resolve().parent.parent
#load_dotenv(BASE_DIR / ".env")

#api_key = os.environ["OPENAI_API_KEY"]  # force error if missing
#client = OpenAI(api_key=api_key)

#print("OpenAI client initialized")

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path='.env')

# print(dotenv_values(".env"))

# print("API KEY =", os.getenv("OPENAI_API_KEY"))
# openai.api_key = os.environ.get("OPENAI_API_KEY")



def speech_to_text():

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 2.0  # wait 2 seconds of silence

    ''' recording the sound '''

    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Done recording")

    ''' Recorgnizing the Audio '''
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="en-US"
            )
        #print("Decoded Text : {}".format(text))

        return text
    
    except Exception as ex:
        print(ex)

# output_of_speech = speech_to_text()
# print("This is what I said: ", output_of_speech)

# output_of_speech to LLM and get response

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    reasoning={"effort": "low"},
    input=[
        {
            "role": "developer",
            "content": "You are a helpfull assistant. You speak a classy english.Your name is Vex. A legendary artifact that dedicates his life to his master."
        },
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(response.output_text)
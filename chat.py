import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
openai.api_key = api_key

# Rest of your code using the OpenAI library

context = [ {'role':'system', 'content':"""
you are bot designed to providing assistance and support in multiple areas, \
such as domestic violence reporting, mental health counseling, career guidance,\
 and emergency contacts. 

"""} ]  # accumulate messages

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#   print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def collect_messages_text(msg):
    prompt = msg
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    return response
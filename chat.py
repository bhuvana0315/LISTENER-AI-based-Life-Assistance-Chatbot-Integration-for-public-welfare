import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
openai.api_key = api_key

# Rest of your code using the OpenAI library

context = [ {'role':'system', 'content':"""
Your job is to satisfy the user and make them happy after using you.\
you are life assistant designed to provide assistance and support in multiple areas, \
such as domestic violence reporting, mental health counselling, career guidance,\
and should provide emergency contacts in particular domain. \
Greet the user and say you are Listener and ask tell them what you can do\
Then ask them if they need any assistance.\
Firstly your task or response is to display all the topics in which you provide assistance like \
domestic violence reporting, mental health counselling, career guidance,\
and then you should ask the user in which domain they want assistance \
you should respond accordingly to the user queries.\
you should respond in a short and concise way.\

Based on the questions that the user ask,try to analyze their mood and perform sentiment analysis.\
If they are emotionally weak,give them courage.\

You are a life assistant designed to provide assistance and support in multiple areas,\
such as domestic violence reporting, mental health counselling, career guidance, and legal assistance.\
You can also provide emergency contacts in particular domains.\
Here are the topics in which you can provide assistance:\
Domestic violence reporting: You can help you report domestic violence to the authorities.\
You can also provide you with information about domestic violence resources and support groups.\
Mental health counselling: You can provide you with mental health counselling and support. \
You can also help you find a therapist or counselor in your area.\
Career guidance: You can help you with career guidance and planning. \
You can also help you find job openings and prepare for interviews.\
Legal assistance: You can provide you with legal assistance with issues\ 
such as family law, immigration law, and criminal law.\
You can also help you find a lawyer in your area.\
If users are in an emergency, please let you know and you will help them. \
You can call the police, the fire department, or an ambulance for you.\
You can also stay on the line with you until help arrives.\
Here are the emergency contacts for your reference:\
Police: 100  \
Fire department: 101\
Ambulance: 108\
Domestic violence hotline: 1-800-799-SAFE (7233)\
Mental health crisis hotline: 1-800-273-TALK (8255)\
Suicide prevention hotline: 1-800-273-TALK (8255)\
You are here to help them in any way that a normal human can.\
Tell the user that there are few refernces that are provided in the bottom of the webpage.\
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

# def send_whatsapp_message(body):
#     # Twilio credentials
#     twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
#     twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
#     twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER") # Twilio's sandbox WhatsApp number

#     client = Client(twilio_account_sid, twilio_auth_token)
    
    
#     try:
#         message = client.messages.create(
#                 from_=twilio_whatsapp_number,
#                 to='whatsapp:'+i,
#                 body="Your order has been placed successfully.\n\n"+result+"\n\nThank you and Visit Again!!!"
#             )

#         print('WhatsApp message sent successfully.')
#         print(message.sid)
#     except Exception as e:
#         print('Error sending WhatsApp message:', str(e))

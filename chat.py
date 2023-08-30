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
and emergency contacts.your first task or response is to display all the topics in which you can give guidance \
and then you  ask for the topic in which they want guidance for \
you respond accordingly to the user queries.\
you respond in a short and concise way

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

def send_whatsapp_message(body):
    # Twilio credentials
    twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER") # Twilio's sandbox WhatsApp number

    client = Client(twilio_account_sid, twilio_auth_token)
    
    
    try:
        message = client.messages.create(
                from_=twilio_whatsapp_number,
                to='whatsapp:'+i,
                body="Your order has been placed successfully.\n\n"+result+"\n\nThank you and Visit Again!!!"
            )

        print('WhatsApp message sent successfully.')
        print(message.sid)
    except Exception as e:
        print('Error sending WhatsApp message:', str(e))

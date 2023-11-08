# load environment variables from .env file
from dotenv import load_dotenv # using 'pip install python-dotenv'
load_dotenv()

import os
import asyncio
import json
from supabase import create_client

# Set up SupaBase client
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# Invoke 'hello-world' Edge Function
async def invoke_hello_world(username):
    response = supabase.functions.invoke("hello-world", invoke_options={'body': {
        'name': username
    }})

    return response

def greet_user(uname):
    # Invoke the HackerHot edge function to calculate the score
    loop = asyncio.new_event_loop()

    invoke_resp_bytes = loop.run_until_complete(invoke_hello_world(uname))
    resp_str = invoke_resp_bytes.decode('utf-8')
    resp_json = json.loads(resp_str)
    print(resp_json['message'])

    loop.close()

greet_user('Crystal')
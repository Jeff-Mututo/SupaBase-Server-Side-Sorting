# load environment variables from .env file
from dotenv import load_dotenv # uses 'pip install python-dotenv'
load_dotenv()

import os, asyncio, json
from supabase import create_client
from datetime import datetime, timedelta

# Set up SupaBase client
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

async def invoke_hacker_hot(gravity, upVotes, created_at):
    response = supabase.functions.invoke("hackerhot-single", invoke_options={"body": {
        'gravity': gravity,
        'upVotes': upVotes,
        'created_at': created_at
    }})

    return response

def update_scores(gravity):
    # mark the cutoff date 6 months earlier from today
                    # (4weeks/month * 6months = 24 weeks)
    month_cutoff = (datetime.now() - timedelta(weeks=24)).strftime('%Y-%m-%d') # yyyy-mm-dd

    # query all rows that are within that 6 month cutoff
    query = supabase.table("services").select("*").gte("created_at", month_cutoff).execute()

    for row in query.data:
        # invoke the edge function
        loop = asyncio.new_event_loop()

        # pass the rows of data and store the resulting list
        resp_bytes = loop.run_until_complete(invoke_hacker_hot(gravity, row['upvotes'], row['created_at']))

        # convert bytes data into regular json dictionary
        resp_json = json.loads(resp_bytes.decode('utf-8'))
        currScore = resp_json['score']
        # UPDATE services SET iscore = scoresDict[key] WHERE id = key
        data = supabase.table("services").update({"iscore": currScore}).eq("id", row['id']).execute()

        loop.close()

# update_scores(gravity)
# update_scores(1.4)
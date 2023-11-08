# SupaBase-Server-Side-Sorting

you can see the implementation for task 1 in these different files

## Libraries/Packages

* decay (npm)
* supabase (pip)
* asyncio (pip)
* datetime (pip)
* python_dotenv (pip)
* json (pip)

## Python Files

### main.py (look inside before running)

runs the hackerhot sorting algorithm at 10 minute intervals using the 'asyncio' library

### hackerhot_many.py

This queries the DB and passes all the rows to the 'hackerhot-many' Edge Function. Their scores are calculated and returned a dictionary {row_id, iScore} and then the python function updates all of the rows with their new iScore value

### hackerhot_single.py

Similar to hackerhot_many.py except the python function only passes one row to the edge function, 'hackerhot-single', receives the new iScore and updates the row in the DB.

It repeats this for each row

## Edge Functions

Check inside the folde supabase/functions/ to find the .ts files for each of the edge functions used.
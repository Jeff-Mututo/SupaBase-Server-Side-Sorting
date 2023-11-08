import asyncio
import hackerhot_single as hack_single
import hackerhot_many as hack_many

gravity = 1.4

# run the function every 10 minutes
async def periodic():
    while True:
        hack_many.update_scores(gravity)
        await asyncio.sleep(1 * 60 * 10) # sleep for 10 minutes (1sec * 60sec/min * 10min)

scheduler = asyncio.new_event_loop()
scheduler.create_task(periodic())
scheduler.run_forever() # run the event loop forever or until some coroutine or callback invokes scheduler.stop()
# it might be better to use a cron job?
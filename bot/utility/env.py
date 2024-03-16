from dotenv import load_dotenv, find_dotenv
import os

class Env:
    '''
        Utility class for getting data from `.env`
    '''
    def __init__(self):
        # Setup env
        load_dotenv(find_dotenv())
        
        self.discord_token: str = str(os.getenv("DISCORD_TOKEN"))
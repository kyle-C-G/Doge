from dotenv import load_dotenv, find_dotenv
import os

class Env:

    def __init__(self):
        # Setup env
        load_dotenv(find_dotenv())
        self.discord_token: str = str(os.getenv("DISCORD_TOKEN"))
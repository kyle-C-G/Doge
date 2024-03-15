import yaml #type: ignore
from utility.logger import Logger
import os

# Initialise Logger
logger: Logger = Logger()

class Config:

    def __init__(self) -> None:

        # Initilisation
        self.check_emoji_reply: bool = False
        self.emoji_replies: list[str] = []
        self.jimin: bool = False
        self.check_discord_status: bool = False
        self.discord_status: str = ""
        self.command_prefix: str = ""
        self.vxtwitter: bool = False

        # Get path
        script_dir = os.path.dirname(os.path.realpath(__file__))
        yaml_path = os.path.join(script_dir, "../../config.yaml")
        
        with open(yaml_path, "r") as file:
            # Load Config File
            try:
                data = yaml.load(file, Loader=yaml.BaseLoader)
            except Exception as e:
                logger.log("Config: Issue loading config.yaml", error=True, )
                quit()

            # Get Command Prefix
            try:
                self.command_prefix = data["command-prefix"]
            except:
                logger.log("Config: Issue loading command-prefix")
                quit()

            # Get Discord Status
            try:
                if "discord-status" in data:
                    self.discord_status = data["discord-status"]
                    self.check_discord_status = True
            except:
                logger.log("Config: Issue loading discord-status", error=True)
                quit()
            
             # Get Jimin
            try:
                if "jimin" in data:
                    if bool(data["jimin"]):
                        self.jimin = True
            except Exception as e:
                logger.log("Config: Issue loading jimin", error=True)
                quit()
            
            # Get Emoji Replies
            try:
                if "emoji-reply" in data:
                    self.emoji_replies = data["emoji-reply"]
                    self.check_emoji_reply= True
            except Exception as e:
                logger.log("Config: Issue loading emoji-reply", error=True)
                quit()

            # Get vxwitter
            try:
                if "vxtwitter" in data:
                    if bool(data["vxtwitter"]):
                        self.vxtwitter = True
            except:
                logger.log("Config: Issue loading vxtwitter", error=True)

    # Returns list of emoji replies if they exist
    def get_emoji_reply_list(self) -> list[str]:
        if self.check_emoji_reply:
            return self.emoji_replies
        else:
            return []

config = Config()
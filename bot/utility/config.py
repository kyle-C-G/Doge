import yaml #type: ignore
from utility.logger import Logger #type: ignore
import os
from typing import Any

# Initialise Logger
logger: Logger = Logger()

class Config:
    '''
        Utility class for getting values from `config.yaml`
    '''
    def __init__(self) -> None:

        # Variable Initilisation
        self.__detect_messages: list[dict[str, Any]] = [] # private
        self.__discord_status: str = "" # private
        self.__emoji_replies: list[str] = [] # private
        self.check_detect_messages: bool = False
        self.check_discord_status: bool = False
        self.check_emoji_reply: bool = False
        self.command_prefix: str = ""
        self.jimin: bool = False
        self.vxtwitter: bool = False

        # Get path of config.yaml
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
                    self.__discord_status = data["discord-status"]
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
                    self.__emoji_replies = data["emoji-reply"]
                    self.check_emoji_reply= True
            except Exception as e:
                logger.log("Config: Issue loading emoji-reply", error=True)
                quit()

            # Get Detect Messages
            try:
                if "detect-message" in data:
                    self.__detect_messages = data["detect-message"]
            except:
                logger.log("Config: Issue loading detect-message", error=True)
                quit()

            # Get vxwitter
            try:
                if "vxtwitter" in data:
                    if bool(data["vxtwitter"]):
                        self.vxtwitter = True
            except:
                logger.log("Config: Issue loading vxtwitter", error=True)
                quit()

    
    def get_emoji_reply_list(self) -> list[str]:
        '''
            Get the list of emojis defined by `emoji-reply` in `config.yaml`
            :return: List of emojis, if set. Empty list. if not.
            :rtype: list[str]
        '''
        if self.check_emoji_reply:
            return self.__emoji_replies
        else:
            return []

    def get_discord_status(self) -> str:
        '''
            Get the Discord RP status defined by `discord-status` in `config.yaml`
            :return: Discord RP Status, if set. Empty string, if not.
            :rtype: str  
        '''
        if self.check_discord_status:
            return self.__discord_status
        else:
            return ""
    
    def get_detect_message_array(self) -> list[dict[str, Any]]:
        '''
            Get the `detect-message` array in `config.yaml`
            :return: `detect-message` array, if set. Empty list, if not.
            :rtype: list[dict[str, `Any`]]
        '''
        if self.check_detect_messages:
            return self.__detect_messages
        else:
            return []
    
    def get_detect_messages(self) -> list[str]:
        '''
            Gets all detection messages defined by `detect` in `config.yaml`
            :return: List of detection messages, if set. Empty list, if not. 
            :rtype: list[str]
        '''
        if self.check_detect_messages:
            output_array: list[str] = []
            for message_dict in self.__detect_messages:
                output_array.append(message_dict["detect"])
            return output_array
        else:
            return []
    
    def get_replies(self, detect_message: str) -> list[str]:
        '''
            Gets all possible replies defined by `replies` in `config.yaml`
            :param detect_message: Detection message defined in `config.yaml` to get `replies` for.
            :type detect_message: str
            :return: List of possible replies, if set. Empty array, if not.
            :rtype: list[str]
        '''
        if self.check_detect_messages:
            try:
                output_array: list[str]
                for message in self.__detect_messages:
                    if message["detect"] == detect_message: 
                        output_array = message["replies"]
                if len(output_array) == 0:
                    raise Exception
                else:
                    return output_array
            except:
                logger.log("Config: Issue with get_replies", error=True)
                exit()
        else:
            return []

config = Config()
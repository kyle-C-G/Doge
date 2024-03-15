import os
from systemd.journal import JournalHandler #type: ignore
import logging
import yaml #type: ignore

class Logger:

    def __init__(self) -> None:
        self.journal_type: str = ""

        # Get config
        script_dir = os.path.dirname(os.path.realpath(__file__))
        yaml_path = os.path.join(script_dir, "../../config.yaml")
        with open(yaml_path, "r") as file:
            try:
                data = yaml.load(file, Loader=yaml.BaseLoader)
            except Exception as e:
                print("\033[31m"  + "Logger: Issue loading config.yaml" + "\033[0m")
                quit()
            try:
                self.journal_type = str(data["journal-type"])
            except:
                print("\033[31m"  + "Logger: Couldn't Load journal_type" + "\033[0m")

        # Journal Setup
        if (self.journal_type == "systemctl"):
            self.systemd_log = logging.getLogger('Logger')
            self.systemd_log.addHandler(JournalHandler())
            self.systemd_log.setLevel(logging.DEBUG)
    
    def log(self, message: str, error: bool = False) -> None:
        if (self.journal_type == "systemctl"):
            self.systemd_log.warning(message)
        else:
            if error:
                output_message = "\033[31m" + message + "\033[0m"
            else:
                output_message = message
            print(output_message)
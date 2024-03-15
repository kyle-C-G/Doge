import os
from systemd.journal import JournalHandler #type: ignore
import logging

class Logger:

    def __init__(self, journal_type: str) -> None:
        # Journal Setup
        self.journal_type = journal_type
        if (self.journal_type == "systemctl"):
            self.systemd_log = logging.getLogger('Logger')
            self.systemd_log.addHandler(JournalHandler())
            self.systemd_log.setLevel(logging.DEBUG)
    
    def log(self, message: str) -> None:
        if (self.journal_type == "systemctl"):
            self.systemd_log.warning(message)
        else:
            print(message)
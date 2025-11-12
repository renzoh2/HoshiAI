import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

class Contants(str, Enum):
    
    APPLICATION_NAME = os.getenv('APPLICATION_NAME')
    LANGUAGE_OPTIONS_FILE = os.getenv('LANGUAGE_OPTIONS_FILE')

    def __str__(self):
        return str(self.value)
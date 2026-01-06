import os
import time

class Utils:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

import os
import logging
from pathlib import Path
from functools import reduce

logger = logging.getLogger()
logging.getLogger().setLevel(logging.INFO)

class MarkCalulator:
    """
    Some Simple Operators
    """

    def __init__(self):
        logger.info("Calulator Class Initialised!")

    @staticmethod
    def rating(_mark_list: list) -> str:

        avg = sum(_ for _ in _mark_list) / len(_mark_list)

        if avg>=91 and avg<=100:
            rating =  "A1"
        elif avg>=81 and avg<91:
            rating = "A2"
        elif avg>=71 and avg<81:
            rating = "B1"
        elif avg>=61 and avg<71:
            rating = "B2"
        elif avg>=51 and avg<61:
            rating = "C1"
        elif avg>=41 and avg<51:
            rating = "C2"
        elif avg>=33 and avg<41:
            rating = "D"
        elif avg>=21 and avg<33:
            rating = "E1"
        elif avg>=0 and avg<21:
            rating = "E2"

        return rating



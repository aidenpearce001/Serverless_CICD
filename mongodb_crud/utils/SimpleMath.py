import os
import sys
import logging
from pathlib import Path
from functools import reduce

logger = logging.getLogger()
logging.getLogger().setLevel(logging.INFO)

class Basic:
    """
    Some Simple Operators
    """

    def __init__(self):
        logger.info("Number Logic Class Initialised!")

    @staticmethod
    def simple_sum(a: int, b:int) -> int:
        return a + b

    @staticmethod
    def multiple(a: int, b:int) -> int:
        return a * b

    @staticmethod
    def square_root(a: int) -> float:
        return a ** (1/2)


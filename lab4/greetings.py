from colorama import Fore, Style
from rich import print
from emoji import emojize


def greet():
    print(Fore.GREEN + "Привіт! Це консольний помічник студента!" + Style.RESET_ALL)
    print(emojize("Навчайся та розвивайся :books:"))
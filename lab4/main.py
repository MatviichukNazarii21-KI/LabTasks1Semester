from greetings import greet
from calculator import calculate
from randomizer import random_number
from date_tools import show_date
from text_tools import analyze_text
from validation import check_email
from formatting import show_color
from ascii_art import show_art
from table_tools import show_table
from qr_tools import create_qr
from animal import show_animal
from file_tools import save_text
from system_info import show_system
from math_tools import square
from statistics_tools import average


def main():
    greet()
    calculate()
    random_number()
    show_date()
    analyze_text()
    check_email()
    show_color()
    show_art()
    show_table()
    create_qr()
    show_animal()
    save_text()
    show_system()
    square()
    average()


if __name__ == "__main__":
    main()
import re

def get_yn(prompt: str) -> bool:
    yn = None
    while True:
        yn = input(prompt + "[y/n]: ").lower()
        if yn == "y":
            return True
        elif yn == "n":
            return False
        

def get_choice(choices: list):
    choice = None
    while True:
        try:
            choice = int(input(f"Enter choice [{1}-{len(choices)}]: "))
        except ValueError as e:
            continue
        if choice is not None and (1 <= choice <= len(choices)):
            return choices[choice - 1]




def get_str(prompt: str, min_len=1) -> str:
    while True:
        s = input(prompt + " ")
        s = re.sub("\s+", "", s)
        if len(s) >= min_len:
            return s
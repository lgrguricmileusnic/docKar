

def get_yn(prompt: str) -> bool:
    yn = None
    while True:
        yn = input(prompt + "[y/n]").lower()
        if yn == "y":
            return True
        elif yn == "n":
            return False
        

def get_choice(min: int, max: int) -> int:
    choice = None
    while True:
        try:
            choice = int(input(f"Enter choice [{min}-{max}]: "))
        except ValueError as e:
            pass
        if choice is not None and (1 <= choice <= 3):
            return choice

def get_str(prompt: str, min_len=1) -> str:
    while True:
        s = input(prompt)
        if len(s) >= min_len:
            return
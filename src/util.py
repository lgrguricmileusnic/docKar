

def get_yn(prompt: str) -> bool:
    yn = None
    while True:
        yn = input().lower()
        if

def get_choice(min: int, max: int) -> int:
    choice = None
    while True:
        try:
            choice = int(input(f"Enter choice [{min}-{max}]: "))
        except ValueError as e:
            pass
        if choice is not None and (1 <= choice <= 3):
            return choice

def get_str(prompt: str, min_len=1: int) -> str:
    while True:
        s = input(prompt)
        if len(s) >= min_len:
            return
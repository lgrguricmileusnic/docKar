from src.args import parse_args
from src.menu import menu
def print_banner():
    print(r"""
   ___  ____  _______ _____   ___ 
  / _ \/ __ \/ ___/ //_/ _ | / _ \
 / // / /_/ / /__/ ,< / __ |/ , _/
/____/\____/\___/_/|_/_/ |_/_/|_|     
    """)


def main():
    args = parse_args()
    print_banner()
    menu(args.out_dir)

if __name__ == "__main__":
    main()
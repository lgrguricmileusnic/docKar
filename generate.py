from src.args import parse_args
from src.menu import menu
def print_banner():
    print(r"""
   ___  ____  _______ _____   ___ 
  / _ \/ __ \/ ___/ //_/ _ | / _ \
 / // / /_/ / /__/ ,< / __ |/ , _/
/____/\____/\___/_/|_/_/ |_/_/|_| 
    
    A script for creating Docker Compose based ECU networks.
    """)


def main():
    parse_args()
    print_banner()
    menu()

if __name__ == "__main__":
    main()
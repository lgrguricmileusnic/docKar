import compose as cmp
import os
from .util import get_yn, get_choice, get_str

def print_menu_header(path: str):
    print(f"""
    Code, Dockerfiles and compose.yml will be stored in:
    {path}
    """)

def print_choices():
    print(r"""
    1) Add CAN bus
    2) Add ECU
    3) Add instrument cluster TUI to an ECU
    """)


def configure_net_driver():
    driver = "lovrogm/dockercan:latest"
    use_default_driver = get_yn(f"Use default CAN docker network driver ({driver}) [y/n]")

    if not use_default_driver:
        driver = get_str("Enter custom driver name: ")
        return

    # dockercan options
    # TODO print dockercan options header
    create_host_if = get_yn("[dockercan] Create host virtual CAN interface for this bus? [y/n]")
    if create_host_if:
        if_name = get_str("Enter interface name: ")
        # TODO finish

    # TODO centralised, CAN FD
    centralised = get_yn()

def choice_add_can_bus(compose: cmp.Compose):
    name = get_str("Enter bus name: ")



    network = cmp.Network(name, driver=driver)
    compose.add_network(network)


def choice_add_ecu(compose: cmp.Compose):
    pass

def choice_add_ic_tui(compose: cmp.Compose):
    pass
def menu(path: str):
    compose = cmp.Compose(os.path.join(path), "compose.yml")

    print_choices()
    choice = get_choice()

    if choice == 1:
        choice_add_can_bus()
    elif choice == 2:
        choice_add_ecu()
    elif choice == 3:
        choice_add_ic_tui()
    
    compose.save_to_file()

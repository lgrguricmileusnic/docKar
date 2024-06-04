import compose as cmp
import os
from .util import get_yn, get_choice, get_str

networks = []


def print_menu_header(path: str):
    print(f"""
    Code, Dockerfiles and compose.yml will be stored in:
    {path}
    """)

def print_choices():
    print(r"""
    1) Add CAN bus
    2) Add ECU
    """)


def create_network(name: str):
    default_driver = "lovrogm/dockercan:latest"

    if get_yn(f"Use default CAN docker network driver ({default_driver})"):
        driver = get_str("Enter custom driver name: ")
        network = cmp.Network(name, driver=driver)
        return network

    network = cmp.Network(name, driver=default_driver)


    opts = {}
    if get_yn("[dockercan] Connect host to this bus over vcan interface?"):
        if_name = get_str("Enter interface name: ")
        opts["host_if"] = if_name
    
    if get_yn("[dockercan] Use CAN FD?"):
        opts["canfd"] = "true"
    if len(opts.keys()) > 0:
        network.add_driver_opts(opts)

def choice_add_can_bus(compose: cmp.Compose):
    name = get_str("Enter bus name: ")
    net = create_network(name)
    compose.add_network(net)


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

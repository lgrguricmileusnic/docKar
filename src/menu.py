import os
from .car import CANBus, ECU, ECUType
from .util import get_yn, get_choice, get_str
from .compose import create_compose


buses = []
path = None


def print_menu_header(path: str):
    print(f"""
    Code, Dockerfiles and compose.yml will be stored in:
    {path}
    """)

def print_layout():
    global buses

    if len(buses) == 0:
        return
    
    print("\n ========= NETWORK LAYOUT =========")
    w = 15
    for bus in buses:
        print("{name:{w}}".format(name=bus.name, w=w), end=" ")
    print()

    for _ in range(len(buses)):
        print("{divider:{w}}".format(divider='│', w=w), end=" ")
    print()
    
    max_ecus = 0
    for bus in buses:
        max_ecus = max(max_ecus, len(bus.ecus))

    for i in range(max_ecus):
        for bus in buses:
            try:
                ecu = bus.ecus[i]
                print("{name:{w}}".format(name='├ '+ ecu.name, w=w), end=" ")
            except IndexError:
                print("{divider:{w}}".format(divider='│', w=w), end=" ")

        print()
        for _ in range(len(buses)):
            print("{divider:{w}}".format(divider='│', w=w), end=" ")
        print()
    print("\n ========= NETWORK LAYOUT ========= \n")
    # print("\n\n", end="")
        




def print_choices():
    print(r"""
    Select option:

    1) Add CAN bus
    2) Add ECU
    3) Done
    4) Exit
    """)

def print_bus_choices():
    s = ""
    i = 1
    for bus in buses:
        s += f"""{i}) {bus.name}\n """
        i += 1
    print(s)

def create_bus():
    name = get_str("Enter bus name: ")

    if_name = None
    if get_yn("[dockercan] Connect host to this bus over vcan interface?"):
        if_name = get_str("Enter interface name: ")
    
    canfd = False
    if get_yn("[dockercan] Use CAN FD?"):
        canfd = True

    bus = CANBus(name=name,canfd=canfd, host_if=if_name)

    if get_yn("Add random CAN frame generation to this bus?"):
        bus.add_ecu(ECU("noise_gen", ECUType.cangen, False))

    if get_yn("Attach cannelloni container?"):
        bus.add_ecu(ECU("cannelloni", ECUType.cannelloni, False))

    return bus


def create_ecu():
    name = get_str("Enter ECU name:")
    if get_yn("Use ECU template?"):
        ecu_type = ECUType.ecu_template
    else:
        ecu_type = ECUType.custom

    ic = get_yn("Connect ECU to IC-TUI?")

    return ECU(name=name, type=ecu_type, ic=ic)


def choice_add_can_bus():
    global buses
    buses.append(create_bus())


def choice_add_ecu():
    global buses

    def print_question():
        print("Connect ECU to which buses? (e.g. 1,3)")
        print_bus_choices()
    
    if len(buses) <= 0:
        print("Add a CAN bus first.")
        return
    ecu = create_ecu()

    while True:
        try:
            print_question()
            selected_buses = [buses[int(num) - 1] for num in get_str("Enter choice: ").split(",")]
            break
        except Exception as e:
            pass
    for bus in selected_buses:
        bus.add_ecu(ecu)
    
def choice_done():
    global path, buses
    compose_path = os.path.join(path, "compose.yml")
    
    
    
    with open(compose_path, "w") as f:
        yaml.dump(create_compose(buses=buses), f)
    




    # TODO copy templates


def menu(out_dir: str):
    global path
    path = out_dir
    while True:
        print_layout()
        print_choices()
        choice = get_choice([
            choice_add_can_bus,
            choice_add_ecu,
            choice_done,
            exit
        ])
        choice()

from enum import Enum, auto

class CANBus:
    def __init__(self, name: str, canfd: bool, host_if: str):
        self.name = name
        self.ecus = []
        self.canfd = canfd
        self.host_if = host_if

    def add_ecu(self, ecu):
        self.ecus.append(ecu)

    def remove_ecu(self, ecu):
        self.ecus.pop(ecu)



class ECUType(Enum):
    cangen = auto()
    cannelloni = auto()
    ecu_template = auto()
    custom = auto()

class ECU:
    def __init__(self, name: str, type: ECUType, ic: bool):
        self.name = name
        self.type = type
        self.ic = ic

import yaml
from .car import CANBus, ECU, ECUType

    
_SERVICES = "services"
_NETWORKS = "networks"
    
def create_compose(buses: list[CANBus]) -> dict:
    content = {Compose._SERVICES : {}, Compose._NETWORKS : {}} 


    

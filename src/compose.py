import yaml
import shutil
import os
from .car import CANBus, ECU, ECUType

    
_SERVICES = "services"
_NETWORKS = "networks"

_DRIVER      = "driver"
_DRIVER_OPTS = "driver_opts"

_DEFAULT_DRIVER = "lovrogm/dockercan:latest"
_HOST_IF        = "host_if"
_CAN_FD         = "canfd"

def create_project(path: str, buses: list[CANBus]) -> dict:
    content = {_SERVICES : {}, _NETWORKS : {}} 
    cg_count = 0
    cnl_count = 0
    ic_tui_count = 0

    for bus in buses:
        # create network
        content[_NETWORKS][bus.name] = {
            _DRIVER : _DEFAULT_DRIVER,
        }
            
        opts = {}
        if bus.host_if is not None:
            opts[_HOST_IF] = f"{bus.host_if}"
        opts[_CAN_FD] = f"{str(bus.canfd).lower()}"        
        
        content[_NETWORKS][bus.name][_DRIVER_OPTS] = opts

        for ecu in bus.ecus:
            if ecu.type == ECUType.cangen:
                dest = os.path.join(path, "cangen")
                if not os.path.isdir(dest):
                    shutil.copytree("./ecus/cangen", dest)

                content[_SERVICES][f"cangen{cg_count}"] = {
                    "build" : "./cangen",
                    "networks" : [bus.name]
                }
                cg_count += 1

            elif ecu.type == ECUType.cannelloni:
                dest = os.path.join(path, "cannelloni")
                if not os.path.isdir(dest):
                    shutil.copytree("./ecus/cannelloni", dest)

                content[_SERVICES][f"cannelloni{cnl_count}"] = {
                    "build" : "./cannelloni",
                    "networks" : [bus.name],
                    "ports" : f"{20000 + cnl_count}:20000"
                }
                cnl_count += 1
            
            elif ecu.type == ECUType.ecu_template:
                if ecu.name in content[_SERVICES].keys():
                    content[_SERVICES][ecu.name][_NETWORKS].append(bus.name)
                    continue

                dest = os.path.join(path, ecu.name)

                shutil.copytree("./ecus/ecu-template", dest)

                content[_SERVICES][ecu.name] = {
                    "build" : f"./{ecu.name}",
                    "networks" : [bus.name],
                }
                if ecu.ic:
                    add_ic_tui(content, path, ecu.name, ic_tui_count)
                    ic_tui_count += 1
            elif ecu.type == ECUType.custom:
                if ecu.name in content[_SERVICES].keys():
                    content[_SERVICES][ecu.name][_NETWORKS].append(bus.name)
                    continue

                content[_SERVICES][ecu.name] = {
                    "image" : "alpine:latest",
                    "networks" : [bus.name]
                }
                if ecu.ic:
                    add_ic_tui(content, path, ecu.name, ic_tui_count)
                    ic_tui_count += 1


    compose_path = os.path.join(path, "compose.yml")
    
    with open(compose_path, "w") as f:
        yaml.dump(content, f)
    
def add_ic_tui(compose: dict, path: str, service_name: str, index: int):
    if compose[_SERVICES][service_name]["networks"] is None:
        compose[_SERVICES][service_name]["networks"] = []


    tui_name = f"ic-tui{index}"
    net_name = f"tui_api{index}"

    dest = os.path.join(path, tui_name)
    shutil.copytree("./ecus/ic-tui", dest)
    
    compose[_SERVICES][service_name]["networks"].append(net_name) 

    compose[_SERVICES][tui_name] = {
        "build" : f"./{tui_name}",
        "networks":[net_name]
    }

    compose[_NETWORKS][net_name] = {
        _DRIVER : "bridge"
    }
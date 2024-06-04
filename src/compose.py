import yaml




class Network:
    
    _DRIVER      = "driver"
    _DRIVER_OPTS = "driver_opts"
    
    def __init__(self, name: str, driver: str):
        self.name = name
        self._content = {
            Network._DRIVER : driver     
        }

    def add_driver_opts(self, opts: dict):
        self._content[Network._DRIVER_OPTS] = opts

class Service:
    
    _BUILD    = "build"
    _NETWORKS = "networks"
    _PORTS    = "ports"
    
    def __init__(self, name: str, build_path: str):
        self.name = name
        self._content = {
            Service._BUILD : build_path,
        }
    def add_network(self, network_name: str):
        if Service._NETWORKS not in self._content.keys():
            self._content[Service._NETWORKS] = []
        self._content[Service._NETWORKS].append(network_name)
    def add_port_mapping(self, host_port, container_port):
        if Service._PORTS not in self._content.keys():
            self._content[Service._PORTS] = []
        self._content[Service._PORTS].append(f"{host_port}:{container_port}")


class Compose:
    
    _SERVICES = "services"
    _NETWORKS = "networks"
    
    def __init__(self, path: str):
        self._content = {Compose._SERVICES : {}, Compose._NETWORKS : {}}
        self.path = path
    def add_service(self, service: Service):
        self._content[Compose._SERVICES][service.name] = service._content

    def add_network(self, network: Network):
        self._content[Compose._NETWORKS][network.name] = network._content
    
    def save_to_file(self):
        with open(self.path, "w") as f:
            yaml.dump(self._content, f)

    

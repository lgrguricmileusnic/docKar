import yaml

banner = r"""
   ___  ____  _______ _____   ___ 
  / _ \/ __ \/ ___/ //_/ _ | / _ \
 / // / /_/ / /__/ ,< / __ |/ , _/
/____/\____/\___/_/|_/_/ |_/_/|_| 
"""

compose = {"services": {}, "networks": {}}

def main():
    print(banner)
    compose["services"]["serv1"] = None
    compose["services"]["serv2"] = None
    compose["networks"]["net1"] = None
    compose["networks"]["net2"] = None
    with open("compose.yml", "w") as f:
        yaml.dump(compose, f, )

main()
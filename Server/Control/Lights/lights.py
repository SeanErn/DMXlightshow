import lifxlan
import json
from lifxlan import RED

#load config
with open('config.json') as json_file:
    config = json.load(json_file)
    print(config)
    json_file.close()


# Create light objects
overheadLight = lifxlan.light(config.lightMacAdresses.overheadLight, config.lightIPs.overheadLight) # Overhead light
lifxZ = lifxlan.light(config.lightMacAdresses.lifxZ, config.lightIPs.lifxZ) # Lifx Z strip
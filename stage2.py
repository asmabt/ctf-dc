from utils.auth import IntersightAuth, get_authenticated_aci_session
import requests
import json
from env import config
import csv

aci_session = get_authenticated_aci_session(
    config['ACI_USER'], config['ACI_PASSWORD'], config['ACI_BASE_URL'])

headers = {
    "Content-Type": "Application/json"
}


url = f"{config['ACI_BASE_URL']}/api/class/fabricHealthTotal.json"
resp = aci_session.get(url, headers=headers)
results = resp.json()['imdata']

# Retrieve the total health information for the fabric


def getHealthInfo():
    for result in results:
        print("---------------")
        print(
            f" total health score = {result['fabricHealthTotal']['attributes']['twScore']}")
        print(
            f" maximum severity = {result['fabricHealthTotal']['attributes']['maxSev']}")
        print("---------------")


getHealthInfo()

# Write the health score information


def CreateHealthFile():
    with open('Health_Info.csv', 'w', newline='') as healthFile:
        for result in results:
            writer = csv.writer(healthFile)
            writer.writerow([f"timestamp={result['fabricHealthTotal']['attributes']['updTs']}",
                             f"total health score={result['fabricHealthTotal']['attributes']['twScore']}", f"maximum severity={result['fabricHealthTotal']['attributes']['maxSev']}"])


CreateHealthFile()

from utils.auth import IntersightAuth
import requests
import json
from env import config
import pprint


auth = IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

BASE_URL = 'https://www.intersight.com/api/v1'


def getAlarms():
    url = f"{BASE_URL}/cond/Alarms"
    response = requests.get(url, auth=auth)
    alarms_res = response.json()['Results']
    print("######Alarms########### ")
    for alarm in alarms_res:
        print(alarm['Description'])


# retreive Alarms
 getAlarms()


def getPhysicalInfra():
    infra_url = f"{BASE_URL}/compute/PhysicalSummaries"
    infra_resp = requests.get(infra_url, auth=auth)
    print("###### PhysicalSummaries ########### ")
    results = infra_resp.json()['Results']
    for result in results:
        print(json.dumps(
            f" ** Name : {result['Name']}", indent=4))
        print(json.dumps(
            f" - Management IP address : {result['MgmtIpAddress']}", indent=4))
        print(json.dumps(
            f" - Management Mode : {result['ManagementMode']}", indent=4))
        print(json.dumps(
            f" - CPUs : {result['NumCpus']}", indent=4))
        print(json.dumps(
            f" - NumCpuCores : {result['NumCpuCores']}", indent=4))
        print(json.dumps(
            f" - Power State : {result['OperPowerState']}", indent=4))
        print(json.dumps(
            f" - Firmware : {result['Firmware']}", indent=4))
        print(json.dumps(
            f" - Model : {result['Model']}", indent=4))
        print(json.dumps(
            f" - Serial : {result['Serial']}", indent=4))
        for tag in result['Tags']:
            if tag['Key'] == "Intersight.LicenseTier":
                print(f" - License Tier : {tag['Value']}")
    print("-------------------------")


# retreive physical infrastructure summary
 getPhysicalInfra()


# Hardware Compatibility List
def getHCL():
    hcl_url = f"{BASE_URL}/cond/HclStatuses"
    hcl_resp = requests.get(hcl_url, auth=auth)
    print("###### Hardware Compatibility List ########### ")
    results = hcl_resp.json()['Results']
    for result in results:
        print(f" - OS Vendor: {result['HclOsVendor']}")
        print(f" - OS Version: {result['HclOsVersion']}")
        print("-------------------------")


 getHCL()


# retreive kubernetes clusters running
def getkubernetes():
    kubernetes_url = f"{BASE_URL}/kubernetes/Clusters"
    kubernetes_resp = requests.get(kubernetes_url, auth=auth)
    print("###### kubernetes clusters running ########### ")
    results = kubernetes_resp.json()['Results']
    for result in results:
        print(f" - Cluster Name: {result['Name']}")
        print("-------------------------")


 getkubernetes()

# GET all kubernetes deployments on the cluster

def getkubernetesDeployments():
    # filter for kubernetes deployments
    kubernetes_deployments_url = f"{BASE_URL}/kubernetes/Deployments?$filter=ObjectType eq 'kubernetes.Deployment'"
    kubernetes_deployments_resp = requests.get(
        kubernetes_deployments_url, auth=auth)
    print("###### kubernetes deployments on the cluster ########### ")
    results = kubernetes_deployments_resp.json()['Results']
    count = 0

    for result in results:
        ObjectType.append(result['ObjectType'])
        count += 1
    print(f"number of kubernetes deployments : {count}")


getkubernetesDeployments()

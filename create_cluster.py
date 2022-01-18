import os
import argparse
import json

def checkRG( rgName):
  RGList = json.loads(os.popen("az group list").read())
  for rg in RGList:
    if rg["name"] == rgName:
      return True
  return False

parser = argparse.ArgumentParser(description="Deploy Kubernetes Cluster on Azure")
parser.add_argument("--rgName", "-r", required=True, help="Enter Resource Group")
args = parser.parse_args()

print("Proceeding with eastus as default zone")
zone = "eastus"

if not checkRG(args.rgName):
  print("Given Resource Group doesn't exist. Creating a new Resource group: %s"%(args.rgName))
  RGStatus = json.loads(os.popen("az group create -l %s -n %s"%(zone, args.rgName)).read())["properties"]["provisioningState"]
  if RGStatus == "Succeeded":
    print("Successfully created RG: %s"%(args.rgName))
  else:
    print("Failed creating RG: %s"%(args.rgName))

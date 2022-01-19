import os
import argparse
import json

def checkRG( rgName):
''' Check if given Resource Group exists
    Return True if yes, False if not
'''

  RGList = json.loads(os.popen("az group list").read())
  for rg in RGList:
    if rg["name"] == rgName:
      return True
  return False

def createCluster(rgName, clusterName, nodeCount):
''' Create a cluster on the fly with given clusterName and in given resource group
    Return True if cluster creation is successful and Flase if cluster creation fails
'''

  print("Creating a cluster %s in group %s"%(clusterName, rgName))
  print("This might take few minutes")
  clusterStatus = json.loads(os.popen("az aks create --resource-group %s --name %s --node-count %d --enable-addons monitoring --generate-ssh-keys"%(rgName, clusterName, nodeCount)).read())["provisioningState"]
  if clusterStatus == "Succeeded":
    print("\nSuccessfully created cluster")
    return True
  else:
    print("\nFailed creating cluster")
    return False

def setDefaultCluster(rgName, clusterName):
''' Set the cluster create above as default
'''
  print("Setting up %s as default cluster"%(clusterName))
  if os.system("az aks get-credentials --resource-group %s --name %s"%(rgName, clusterName)) == 0:
    print("Configured %s as default cluster"%(clusterName))
  else:
    print("Failed configuring %s as default cluster"%(clusterName))

parser = argparse.ArgumentParser(description="Deploy Kubernetes Cluster on Azure")
parser.add_argument("--rgName", "-r", required=True, help="Enter Resource Group")
parser.add_argument("--clusterName", "-c", required=True, help="Enter Cluster Name")
parser.add_argument("--nodeCount", "-n", required=True, help="Enter Node Count")
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

if createCluster(args.rgName, args.clusterName, int(args.nodeCount)):
  setDefaultCluster(args.rgName, args.clusterName)

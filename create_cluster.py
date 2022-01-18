import os
import argparse

parser = argparse.ArgumentParser(description="Deploy Kubernetes Cluster on Azure")
parser.add_argument("-r", "--resourceGroup", required=True, help="Enter Resource Group")
parser.add_argument("-z", "--zone", default="us-west", help="Enter Zone", required=False)
args = parser.parse_args()


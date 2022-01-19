## Problem statement 1: 
- Script create_cluster.py takes input arguments such as cluster Name, resource group and node Count and creates a Kubernetes cluster 
- Run "kubectl apply -f templates/nodejs.yaml" to create a deployment with one replica

##Problem statement 2:
- Run "kubectl apply -f templates/" to create a Horizontal Pod Autoscaling which scales the Pods between 1 to 4 bsaed on the CPU utilization
- The above command deploys a secret with API keys and places them in environmental variables. In the given yaml, 2 environmental variables will be created in the POD - API_USER and API_TOKEN
- The script check_autoscale.py creates a new pod which sends multiple requests to the nodejs application. This in turn results in the POD auto scaling based on the CPU utilization
- The above command also creates an SSL certificatee and places it in the /tmp/ directory of the POD

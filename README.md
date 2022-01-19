# ATC Round 1 - Kubernetes

## Environment
- The current setup is run on Azure cloud shell
- Code is present in ATC_round1 repository 
- Scripts are developed in Python3 
- Manifest files are developed in YAML

## Step-01: Cluster creation
- Clone the repository and go to the ATC_round1 directory
- Execute the script with help option to see required arguments

```
  python3 create_cluster.py --help
  usage: create_cluster.py [-h] --rgName RGNAME --clusterName CLUSTERNAME
                         --nodeCount NODECOUNT

  Deploy Kubernetes Cluster on Azure

  optional arguments:
    -h, --help            show this help message and exit
    --rgName RGNAME, -r RGNAME
                          Enter Resource Group
    --clusterName CLUSTERNAME, -c CLUSTERNAME
                          Enter Cluster Name
    --nodeCount NODECOUNT, -n NODECOUNT
                          Enter Node Count
```

- Execute python with above arguments to mention the resource group, cluster name and node count to be deployed

```
  python3 create_cluster.py -r kubecluster -c cluster1 -n 1
```

- The script will take around 5-10 minutes to execute and once complete, will create a cluster with given number of nodes in the mentioned resource group and will set it to default

## Step-02: Create deployment and service
- Run kubectl apply command on the templates directory to create deployment and a service

```
  kubectl apply -f templates/
```

- templates/nodejs.yml will create a nodejs deployment

- templates/nodejs-hpa.yml will create a nodejs service which scales upto 4 pods based on the CPU utilization. If CPU utilization is more than 5%, a new pod is created automatically

- templates/nodejs-svc.yml will create a Load Balancer service which exposes port 8081

- templates/nodejs-secret.yml will create a secret with environment variables called api_user and api_token in the POD 

- templates/ingress.yml will create an Ingress controller to provide an SSL Termination

- templates/tls_secret.yml will create a secret with SSL generated keys and added them to the pod at /tmp/ directory

## Step-03: Test auto scaling

- Wait till the service had a public IP assigned
- 
- Execute the script check_autoscale.py

```
  python3 check_autoscale.py
```

- This will create a POD and sends multiple requests to the node JS application to test the autoscaling feature

- Below is the sample output of the script

```
harsha@Azure:~/ATC_round1$ python3 check_autoscale.py
Fetching IP address of nodejs service
Created Load to test service scalability
pod/load-generator created
Current Node Count/min Replica: 1/1
Current CPU/Target CPU: 0/5
Current Node Count/min Replica: 1/1
Current CPU/Target CPU: 90/5
Current Node Count/min Replica: 4/1
Current CPU/Target CPU: 26/5
Node count increased to 4
Deleting Load
pod "load-generator" deleted
Current Node Count/min Replica: 4/1
Current CPU/Target CPU: 26/5
Current Node Count/min Replica: 4/1
Current CPU/Target CPU: 15/5
Current Node Count/min Replica: 4/1
Current CPU/Target CPU: 0/5
Current Node Count/min Replica: 4/1
Current CPU/Target CPU: 0/5
Current Node Count/min Replica: 4/1
Current CPU/Target CPU: 0/5
Current Node Count/min Replica: 4/1
Current CPU/Target CPU: 0/5
Current Node Count/min Replica: 4/1
Current CPU/Target CPU: 0/5
Current Node Count/min Replica: 1/1
Current CPU/Target CPU: 0/5
Node count decreased to 1
```

## Problem statement 1: 
- Script create_cluster.py takes input arguments such as cluster Name, resource group and node Count and creates a Kubernetes cluster 
- Run "kubectl apply -f templates/nodejs.yaml" to create a deployment with one replica

## Problem statement 2:
- Run "kubectl apply -f templates/" to create a Horizontal Pod Autoscaling which scales the Pods between 1 to 4 bsaed on the CPU utilization using templates/nodejs-hpa.yml
- The above command deploys a secret with API keys and places them in environmental variables. In the given yaml, 2 environmental variables will be created in the POD - API_USER and API_TOKEN using templates/nodejs-secret.yml
- Once the service gets a public IP, the script check_autoscale.py creates a new pod which sends multiple requests to the nodejs application. This in turn results in the POD auto scaling based on the CPU utilization 
- The above command also creates an SSL certificatee and places it in the /tmp/ directory of the POD using templates/tls_secret.yml

## CI/CD Pipeline
- Create namespaces for dev, qa, staging and prod stages
- Create Azure pipelines in all the stages with required testing
- Dev Pipeline: Creates a image with the changes, runs baisc tests and pushes the images to private registry or Azure Container Registry's dev folder
- QA Pipeline: Creates PODs with the image pushed as part of Dev pipeline and runs feature testing to verify the functionality and promote the image to ACR's QA folder
- Staging Pipeline: Create the PODs with the images pushed as part of QA pipeline and run production tests and performance tests and promote the image to staging folder in ACR
- Production Pipeline: Move the Image to production on demand
- Reviews can be added at every stage and hooks can be integrated to trigger the pipelines automatically at every stage
- Notifications can be integrated in Azure to keep everyone in the team in sync with the status of changes


import os
import time

def fetchSvcIp():
  print("Fetching IP address of nodejs service")
  return(os.popen("kubectl get svc nodejs-svc -o=jsonpath='{.status.loadBalancer.ingress[*].ip}'").read())

def createLoad(svcIP):
  print("Created Load Generator POD to test service scalability")
  os.system('kubectl run load-generator --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.00001; do wget -q -O- http://' + svcIP + ':8081/; done"')

def monitorLoad(stage):
  for iteration in range(0,25):
    currentNodeCount, currentCPU, targetCPU, minReplicas = (os.popen("kubectl get hpa nodejs -o=jsonpath='{.status.currentReplicas}{\"\t\"}{.status.currentCPUUtilizationPercentage}{\"\t\"}{.spec.targetCPUUtilizationPercentage}{\"\t\"}{.spec.minReplicas}'").read().split("\t"))
    print("Current Node Count/min Replica: %s/%s"%(currentNodeCount, minReplicas))
    print("Current CPU/Target CPU: %s/%s"%(currentCPU, targetCPU))
    if stage == "before":
      if minReplicas != currentNodeCount:
        print("NodeJS POD count increased to %s"%(currentNodeCount))
        break
      time.sleep(60)
    if stage == "after":
      if minReplicas == currentNodeCount:
        print("NodeJS POD count decreased to %s"%(currentNodeCount))
        break
      time.sleep(60)

def deleteLoad():
  print("Deleting Load Generator POD")
  os.system("kubectl delete pod load-generator")

svcIP = fetchSvcIp()
createLoad(svcIP)
monitorLoad("before")
deleteLoad()
monitorLoad("after")

# Creating out First App

## Check the health of Cluster
```
kubectl get nodes 
```

## Deploy Nginx App
```
kubectl run hello-k8s --image=nginx --port=80
```

## Check the status of PODs 
```  
kubectl get pods 
kubectl describe pods hello-k8s
```

## Let's Deploy our newly built PythonWeb App.
```
kubectl run mypythonwebapp --image=amitvashist7/mypywebapp:v3 --port=8081
```
```
kubectl get pods
NAME             READY   STATUS    RESTARTS   AGE
hello-k8s        1/1     Running   0          6m22s
mypythonwebapp   1/1     Running   0          4m58s
```


## Note : In case you are getting dockerlimit error while deploying your pod, then below is the workaround:
```
docker login 
ls -ltr /root/.docker/config.json
```

## Create Image Pull Secrets in K8s Cluster:
```
kubectl create secret generic regcred --from-file=.dockerconfigjson=/root/.docker/config.json --type=kubernetes.io/dockerconfigjson
```

## Now update your deployment file with your pull secret name under container section:
```
imagePullSecrets:
   - name: regcred
```

## Sample Pod Deployment file is avalible with name: k8s-hello-2.yaml
```
kubectl apply -f k8s-hello-2.yaml
```


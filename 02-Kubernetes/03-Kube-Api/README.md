``` 

  133  kubectl cluster-info
  134  kubectl api-versions
  135  kubectl api-resources
  136  kubectl proxy --address='172.31.0.10' --port=8001 --accept-hosts='.' --accept-paths='.' &
  
144  curl http://172.31.0.10:8001/api/v1/secrets
  145  curl http://172.31.0.10:8001/api/v1/pods
  146  curl http://172.31.0.10:8001/api/v1/pods  | grep -A10 "hey"
```

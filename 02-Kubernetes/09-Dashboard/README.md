# Setting up the dashboard

## Start dashboard

Create dashboard:
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
```

## Create user

Create sample user (if using RBAC - on by default on new installs with kops / kubeadm):
```
kubectl create -f sample-user.yaml

```

## Get login token:
```
kubectl -n kubernetes-dashboard  get secret | grep admin-user-1
kubectl -n kubernetes-dashboard  describe secret admin-user-1-token-j4vkv

```
Note: Expose dashboard svc to node port & try to access the same : https::<nodeip>:<nodeport>


helm uninstall kibana -n tracking
helm uninstall elasticsearch -n tracking
kubectl delete ns tracking

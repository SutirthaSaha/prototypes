kubectl config use-context dev
kubectl apply -f namespace.yaml

helm repo add elastic https://helm.elastic.co
helm repo update

helm upgrade --install elasticsearch -n tracking -f elastic-search-values.yaml elastic/elasticsearch
helm upgrade --install kibana -n tracking -f kibana-values.yaml elastic/kibana

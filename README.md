# Kubernetes Manager CLI

## 🚀 Features
- Connect to a K8s cluster and install Helm and KEDA
- Deploy containerized apps with KEDA-based autoscaling
- Get real-time health status

## 📦 Prerequisites
- Python 3.8+
- `kubectl` installed
- kubeconfig configured

## 🛠 Usage

```bash
# Connect
python main.py connect

# Deploy
python main.py deploy -name demo --namespace demo

# Health Check
python main.py health --name demo --namespace demo
```
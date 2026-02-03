# ⚙️ Installation & Setup

1) Clone the repository

``` bash
git clone https://github.com/xusniya/argo-pro.git
```

2) Create and activate virtual environment

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

3) Install dependencies

``` bash
pip install -r requirements.txt
```

4) Run the development server

``` bash
python manage.py runserver
```

# Run with Docker

Build and start containers

``` bash
docker-compose up --build
```

# Install Helm
helm install agriculture agriculture/ -n agriculture
![img.png](img.png)

# Argocd
Register and Checking
```bash
kubectl apply -f application.yaml
kubectl get applications -n argocd
```
![img_1.png](img_1.png)
![img_2.png](img_2.png)
![img_3.png](img_3.png)

# Grafana Dashboard
Custom Metrics
![img_4.png](img_4.png)
![img_5.png](img_5.png)
![img_6.png](img_6.png)

# Loki Logs
![logs.png](logs.png)
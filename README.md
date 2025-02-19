# app-chatbot-react-fastapi

## Link to Demo

<https://test1.agreeablesky-0f350fca.australiaeast.azurecontainerapps.io/>
![image](https://github.com/user-attachments/assets/492f88c4-b18e-41f8-89a6-5a1b6c771020)

## Build and Run

```bash
docker build -t raychung/app-chatbot-react-fastapi:latest .

docker run -p 8000:8000 raychung/app-chatbot-react-fastapi:latest
```

## GitHub Actions

<https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust-user-assigned-managed-identity?pivots=identity-wif-mi-methods-azp>

```bash
az ad sp create-for-rbac \
  --name my-app-credentials \
  --role contributor \
  --scopes /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP_NAME>
```

```bash
git config user.email "ray.chunkit.chung@gmail.com"
git config user.name "Ray Chung"
```

## Dev Environment

```bash
# cd backend
# rmdir /s /q static
# xcopy ..\frontend\out static /e /i
# uvicorn main:app --port 8000 --reload --reload-dir static
python3.12 -m venv .venv
.venv\Scripts\activate
cd backend
rmdir /s /q static
xcopy ..\frontend\out static /e /i
pip install --upgrade -r requirements.txt
pip install --upgrade  -r dev-requirements.txt
# uvicorn main:app --port 8000 --reload
python main.py
```

```bash
cd frontend
npm install
npm run dev
################
cd frontend
npm run reinstall
npm run dev
```

## Fastapi starter

<https://github.com/itacode/fastapi-starter/blob/main/app/main.py>

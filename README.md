# app-chatbot-react-fastapi

## Link

<https://test1.agreeablesky-0f350fca.australiaeast.azurecontainerapps.io/>

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
pip install -r requirements.txt
pip install -r dev-requirements.txt
uvicorn main:app --port 8000 --reload
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


# Azure RAG Web App (gpt-4o-mini)

## Environment Variables
AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_API_KEY
AZURE_OPENAI_DEPLOYMENT_NAME
AZURE_OPENAI_API_VERSION

## Run locally
docker build -t rag-webapp .
docker run -p 8000:8000 rag-webapp

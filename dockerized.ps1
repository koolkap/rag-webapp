# Login to Azure
#az login

# Set subscription (optional)
# az account set --subscription "SUBSCRIPTION_ID"

# ===== EDIT THESE VALUES =====
$RESOURCE_GROUP = "rg-email-reminder"
$ACR_NAME       = "dockercicd"        # no .azurecr.io
$IMAGE_NAME     = "rag-webapp"
$IMAGE_TAG      = "v1"
# =============================

# Login to ACR
az acr login --name $ACR_NAME
az acr update --name $ACR_NAME --admin-enabled true
# Build image (optional – skip if already built)
docker build -t $IMAGE_NAME .

# Tag image for ACR
docker tag ${IMAGE_NAME}:latest `
    dockercicd.azurecr.io/${IMAGE_NAME}:${IMAGE_TAG}

# Push image to ACR
docker push dockercicd.azurecr.io/${IMAGE_NAME}:${IMAGE_TAG}




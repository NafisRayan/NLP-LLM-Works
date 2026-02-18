import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")
deployment_name = os.getenv("DEPLOYMENT_NAME")

# Extract the endpoint from the base URL (remove the path)
# The base URL format is like: https://endpoint.openai.azure.com/openai/responses?api-version=...
# We need just: https://endpoint.openai.azure.com
if base_url:
    azure_endpoint = base_url.split("/openai")[0]
    # Extract api_version from base_url
    if "api-version=" in base_url:
        api_version = base_url.split("api-version=")[1].split("&")[0]
    else:
        api_version = "2024-08-01-preview"
else:
    azure_endpoint = None
    api_version = "2024-08-01-preview"

print(f"Using deployment: {deployment_name}")
print(f"Using azure_endpoint: {azure_endpoint}")
print(f"Using api_version: {api_version}")

client = AzureOpenAI(
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version=api_version
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message)

# Use the official vLLM image as the base image
FROM vllm/vllm-openai:latest

# Expose port 8000
EXPOSE 8000

# Command to run the vLLM server with the specified model and parameters
# we set the model name to the model we want to use
# we set our unique api key, so requests will be safe
# we set the data type (dtype) to half precision
# we set the maximum model length to 2048 tokens which means we will use less resources
# we set the swap space to 2.0 GB
CMD ["NousResearch/Meta-Llama-3-8B-Instruct", "--api-key", "my-unique-api-key", "--swap-space", "2.0", "--dtype", "half", "--max-model-len", "2048", "--port", "8000"]
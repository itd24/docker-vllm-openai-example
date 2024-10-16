from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="my-unique-api-key")

# Make a request to the model
response = client.chat.completions.create(
    model="NousResearch/Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! What do you recommend I do when it is snowing?",
         },
    ],
    max_tokens=100,
)

# Print the response
print("Response:", response.choices[0].message.content)
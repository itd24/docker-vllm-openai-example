FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install vllm

CMD ["python3", "-m", "vllm.entrypoints.openai.api_server", "--model", "google/gemma-2b-it", "--swap-space","2.0", "--dtype", "half"]
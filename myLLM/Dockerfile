FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install vllm

CMD ["python3", "-m", "vllm.entrypoints.openai.api_server", "--model", "facebook/opt-125m","--swap-space","2.0"]
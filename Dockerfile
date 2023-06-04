FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

COPY ./config.yaml /app/config.yaml

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app/app
FROM public.ecr.aws/lambda/python:3.9

COPY ./requirements.txt /app/requirements.txt

# COPY ./config.yaml /app/config.yaml

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /var/task
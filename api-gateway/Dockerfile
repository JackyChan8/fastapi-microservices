FROM bitnami/python:3.11

EXPOSE 8000
WORKDIR /app

RUN apt-get update && apt-get install git -y && \
    apt-get install libgl1 libgl1-mesa-glx libglib2.0-0 libsm6 libxrender1 libxext6 -y

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

COPY . .
ENV PYTHONPATH app

HEALTHCHECK --interval=21s --timeout=3s --start-period=10s CMD curl --fail http://localhost:8000/ping || exit 1

CMD ["uvicorn", "web:app", "--host", "0.0.0.0", "--port", "8000"]
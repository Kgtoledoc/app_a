FROM public.ecr.aws/docker/library/python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el archivo .proto de app_b y compilarlo
COPY proto/image_processor.proto .
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_processor.proto

COPY . .

CMD ["python", "app.py"]
# App A

App A actúa como el frontend o API Gateway para el servicio de procesamiento de imágenes. Recibe imágenes y las envía al microservicio App B para su procesamiento.

## Características

- Recibe imágenes a través de una API HTTP.
- Envía imágenes al backend gRPC para su procesamiento.
- Devuelve la imagen procesada al cliente.

## Requisitos

- Python 3.9+
- Docker

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Kgtoledoc/app_a.git
cd app_a

```
   
2. Instala las dependencias:
```bash
pip install -r requirements.txt

```
   

3. Ejecuta la aplicación:
```bash
python app.py

```

   
## Despliegue
App A se despliega en un clúster de Kubernetes. El despliegue se gestiona a través de AWS CodeBuild y Amazon EKS.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.
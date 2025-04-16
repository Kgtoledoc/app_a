from flask import Flask, request, Response
import grpc
import image_processor_pb2
import image_processor_pb2_grpc

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_image():
    # Leer la imagen del request
    image = request.files['image'].read()
    
    # Crear un canal gRPC
    channel = grpc.insecure_channel('app-b:50051')
    stub = image_processor_pb2_grpc.ImageProcessorStub(channel)
    
    # Enviar la imagen al servicio gRPC
    response = stub.ProcessImage(image_processor_pb2.ImageRequest(image=image))
    
    # Devolver la imagen procesada como respuesta
    return Response(response.image, mimetype='image/jpeg')  # Cambia el mimetype según el formato de la imagen

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
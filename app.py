from flask import Flask, request
import grpc
import app_b_pb2
import app_b_pb2_grpc

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_image():
    image = request.files['image'].read()
    channel = grpc.insecure_channel('app_b:50051')
    stub = app_b_pb2_grpc.ImageProcessorStub(channel)
    response = stub.ProcessImage(app_b_pb2.ImageRequest(image=image))
    return response.image

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
from app import app, model
from flask import jsonify
from flask import request, Response
import base64
import cv2
import numpy as np

@app.route("/predict", methods=["POST"])
def predict():
    img = request.files['file'].read()  # read the file
    npimg = np.fromstring(img, np.uint8)  # convert to numpy array
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)  # convert numpy array to image

    count = model.people_count_by_img(img)
    return jsonify(count=count)

@app.route("/cap", methods=["GET"])
def capp():
    return Response(model.video_cap() , mimetype='multipart/x-mixed-replace; boundary=frame')


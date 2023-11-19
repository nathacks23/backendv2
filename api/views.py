from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework import status
import cv2
import numpy as np
import keras
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

class UploadImageView(APIView):
    parser_classes = (MultiPartParser,)
    def post(self, request, *args, **kwargs):
        uploaded_image = request.FILES.get('image')

        if not uploaded_image:
            return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the uploaded file to a temporary file
        file_path = default_storage.save('temp_image.jpg', ContentFile(uploaded_image.read()))

        # Load the pre-trained stroke predictor
        model = keras.models.load_model('api/stroke_recognition.h5')

        # Read the image using OpenCV
        image = cv2.imread(file_path)
        image = cv2.resize(image, (150, 150))

        # Reshape and normalize the image
        image = np.expand_dims(image, axis=0)
        image = image.astype('float32') / 255.0

        # Make the prediction
        prediction = model.predict(image)

        # Determine the class based on the prediction
        if prediction[0][0] >= 0.5:
            prediction_label = "Stroke"
            return Response({'prediction': 1, 'label': prediction_label})
        else:
            prediction_label = "Not Stroke"
            return Response({'prediction': 0, 'label': prediction_label})
         


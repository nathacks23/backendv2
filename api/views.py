from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework import status

class UploadImageView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        uploaded_image = request.FILES.get('image')

        if uploaded_image:
            # Process the image (you can replace this with your own logic)
            # Here, we are just returning a success message
            return Response({'message': 'Image uploaded successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No image file provided.'}, status=status.HTTP_400_BAD_REQUEST)


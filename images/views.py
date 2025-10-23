from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import ImageItem
from .serializers import ImageItemSerializer
from .services import upload_image_to_cloud


class ImageItemViewSet(viewsets.ModelViewSet):
    queryset = ImageItem.objects.all().order_by('-uploaded_at')
    serializer_class = ImageItemSerializer
    parser_classes = (MultiPartParser, FormParser)  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data.pop('image')
        upload = upload_image_to_cloud(file)  # {'url': ..., 'public_id': ...}

        item = ImageItem.objects.create(
            image_url=upload['url'],
            cloudinary_public_id=upload['public_id'],
            **serializer.validated_data
        )

      
        out = self.get_serializer(item)
        return Response(out.data, status=status.HTTP_201_CREATED)
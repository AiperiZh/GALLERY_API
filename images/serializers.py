from rest_framework import serializers

from .models import ImageItem

class ImageItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required = True)
    class Meta:
        model = ImageItem
        fields = '__all__'
        read_only_fields = ["id", "image_url", "cloudinary_public_id", "uploaded_at"]


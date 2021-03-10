from rest_framework import serializers

from .models import Gltf_json, Gltf_buffer, Gltf_buffer2

class Gltf_json_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Gltf_json
		fields = '__all__'

class Gltf_buffer_Serializer(serializers.ModelSerializer):
	buffer = serializers.JSONField(binary=True)

	class Meta:
		model = Gltf_buffer
		fields = '__all__'

class Gltf_buffer2_Serializer(serializers.ModelSerializer):

	class Meta:
		model = Gltf_buffer2
		fields = '__all__'


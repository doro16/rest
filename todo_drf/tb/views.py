import base64
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.settings import api_settings
from rest_framework.renderers import BaseRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .serializers import Gltf_json_Serializer, Gltf_buffer_Serializer, Gltf_buffer2_Serializer

from .models import Gltf_json, Gltf_buffer, Gltf_buffer2
import json
from rest_framework import parsers, status


# Create your views here.

class BinaryRenderer(BaseRenderer):
    media_type = 'application/*'
    format = 'binary'
    charset = None
    render_style = 'binary'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'BufferList':'/buffer-list/',
		'BufferDetail View':'/buffer-detail/<str:pk>/',
		'BufferCreate':'/buffer-create/',
		'BufferUpdate':'/buffer-update/<str:pk>/',
		'BufferDelete':'/buffer-delete/<str:pk>/',
		'BufferList2': '/buffer-list2/',
		'BufferDetail View2': '/buffer-detail2/<str:pk>/',
		'BufferCreate2': '/buffer-create2/',
		'BufferUpdate2': '/buffer-update2/<str:pk>/',
		'BufferDelete2': '/buffer-delete2/<str:pk>/',
		'BufferDownload2': '/buffer-download2/<str:pk>/',
		'JsonList': '/json-list/',
		'JsonDetail View': '/json-detail/<str:pk>/',
		'JsonCreate': '/json-create/',
		'JsonUpdate': '/json-update/<str:pk>/',
		'JsonDelete': '/json-delete/<str:pk>/',
		}

	return Response(api_urls)

# tb_gltf_buffer CRUD


@api_view(['GET'])
def bufferList(request):
	tasks = Gltf_buffer.objects.all().order_by('-id')
	serializer = Gltf_buffer_Serializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def bufferDetail(request, pk):
	tasks = Gltf_buffer.objects.get(id=pk)
	serializer = Gltf_buffer_Serializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def bufferCreate(request):
	serializer = Gltf_buffer_Serializer(data=json.loads(request.body.decode('utf-8')))
	if serializer.is_valid():
		serializer.save()

	print("serialize.data는 ", serializer.data)					# 찍기만하고 안들어감. 왜냐면 키:값 형태가 아니잔ㅇㅎ아,..
	return Response(serializer.data)

@api_view(['POST'])
def bufferUpdate(request, pk):
	task = Gltf_buffer.objects.get(id=pk)
	serializer = Gltf_buffer2_Serializer(instance=task, data=json.loads(request.body.decode('utf-8')))


	if serializer.is_valid():
		serializer.save()

	print("data는", json.loads(request.body.decode('utf-8')))	#
	print("serialize.data는 ", serializer.data)					#

	return Response(serializer.data)


@api_view(['DELETE'])
def bufferDelete(request, pk):
	task = Gltf_buffer.objects.get(id=pk)
	task.delete()

	return Response('삭제되었습니다.')



# tb_gltf_buffer2 CRUD TYPE이 BYTEA일때 직렬화가 안됨


@api_view(['GET'])
def bufferList2(request):
	tasks = Gltf_buffer2.objects.all().order_by('-id')
	serializer = Gltf_buffer2_Serializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def bufferDetail2(request, pk):
	tasks = Gltf_buffer2.objects.get(id=pk)
	serializer = Gltf_buffer2_Serializer(tasks, many=False)
	return Response(serializer.data)


class FileUploadView(APIView):
	parser_class = (FileUploadParser,)

	def post(self, request, *args, **kwargs):

		file_serializer = Gltf_buffer2_Serializer(data=request.data)

		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def bufferCreate2(request):
	serializer = Gltf_buffer2_Serializer(data=request.data)

	if serializer.is_valid():
		nu2 = serializer.save()
		nu2.buffer = base64.b64encode(request.data['buffer']) # a bytes-like object is required, not 'str'
		nu2.save()

	print(nu2.paint_data, "base64.b64encode(request.data['buffer']였음")
	print(request.data, "data였음")
	print(serializer.data, "serialize.data였음")

	return Response(serializer.data)

@api_view(['POST'])
def bufferUpdate2(request, pk):
	task = Gltf_buffer2.objects.get(id=pk)
	serializer = Gltf_buffer2_Serializer(instance=task, data=request.data)

	if serializer.is_valid():
		nu2 = serializer.save()
		if 'buffer' in request.data.keys():
			nu2.paint_data = base64.b64encode(request.data['buffer'])
			nu2.save()

	print(request.data, "data였음")								# 가져옴
	print(serializer.data, "serialize.data였음")					# 못가져옴


	return Response(serializer.data)


@api_view(['DELETE'])
def bufferDelete2(request, pk):
	task = Gltf_buffer2.objects.get(id=pk)
	task.delete()

	return Response('삭제되었습니다.')


@api_view(['GET'])
@renderer_classes([BinaryRenderer])
def bufferDownload2(request):
	tasks = Gltf_buffer2.objects.all()
	serializer = Gltf_buffer2_Serializer(tasks, many=True)
	return Response(serializer.data)

# tb_gltf_json CRUD


@api_view(['GET'])
def jsonList(request):
	tasks = Gltf_json.objects.all().order_by('-id')
	serializer = Gltf_json_Serializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def jsonDetail(request, pk):
	tasks = Gltf_json.objects.get(id=pk)
	serializer = Gltf_json_Serializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def jsonCreate(request):
	serializer = Gltf_json_Serializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def jsonUpdate(request, pk):
	task = Gltf_json.objects.get(id=pk)
	serializer = Gltf_json_Serializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def jsonDelete(request, pk):
	task = Gltf_json.objects.get(id=pk)
	task.delete()

	return Response('삭제되었습니다.')



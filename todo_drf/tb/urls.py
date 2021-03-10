from django.urls import path
from . import views
from .views import FileUploadView

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('buffer-list/', views.bufferList, name="buffer-list"),
	path('buffer-detail/<str:pk>/', views.bufferDetail, name="buffer-detail"),
	path('buffer-create/', views.bufferCreate, name="buffer-create"),
	path('buffer-update/<str:pk>/', views.bufferUpdate, name="buffer-update"),
	path('buffer-delete/<str:pk>/', views.bufferDelete, name="buffer-delete"),
	path('buffer-list2/', views.bufferList2, name="buffer-list2"),
	path('buffer-detail2/<str:pk>/', views.bufferDetail2, name="buffer-detail2"),
	path('buffer-create3/', FileUploadView.as_view()),
	path('buffer-create2/', views.bufferCreate2, name="buffer-create2"),
	path('buffer-update2/<str:pk>/', views.bufferUpdate2, name="buffer-update2"),
	path('buffer-delete2/<str:pk>/', views.bufferDelete2, name="buffer-delete2"),
	path('buffer-download2/', views.bufferDownload2, name="buffer-download2"),
	path('json-list/', views.jsonList, name="json-list"),
	path('json-detail/<str:pk>/', views.jsonDetail, name="json-detail"),
	path('json-create/', views.jsonCreate, name="json-create"),
	path('json-update/<str:pk>/', views.jsonUpdate, name="json-update"),
	path('json-delete/<str:pk>/', views.jsonDelete, name="json-delete"),
]

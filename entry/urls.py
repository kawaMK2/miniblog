from django.urls import path
from .views import EntryListAPIView


urlpatterns = [
	path('entries/', EntryListAPIView.as_view()),
]

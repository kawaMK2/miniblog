from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Entry
from .serializers import EntrySerializer


class EntryListAPIView(generics.ListAPIView):
	permission_classes = (AllowAny,)
	serializer_class = EntrySerializer
	queryset = Entry.objects.all()

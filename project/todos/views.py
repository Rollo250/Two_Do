from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework_simplejwt.authentication import JWTAuthentication


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

"""class SnippetDetails(APIView):
    authentication_classes = [BasicAuthentication, JWTAuthentication]
    permission_classes = [Isauthenticated]
    
    def _get_object(self, pk):
        try:
            return Snippet.object.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self._getobject(pk)
        serializer = SnippetSerializer(snippet)"""
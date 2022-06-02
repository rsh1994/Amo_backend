from .models import Board
from .serializers import BoardSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class BoardViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
   
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
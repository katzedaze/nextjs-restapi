from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from .models import Post, Task
from .serializers import PostSerializer, TaskSerializer, UserSerializer


# ユーザー作成
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # ユーザー作成直後はアクセスを許可
    permission_classes = (AllowAny,)


# ポストの一覧取得
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


# IDに基づく特定のポスト取得
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


# タスクの一覧取得
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


# IDに基づく特定のタスク取得
class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


# タスクの作成・更新・削除
# JWTトークンによるアクセス許可が必要
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

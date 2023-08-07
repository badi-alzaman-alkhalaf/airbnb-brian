from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response  import Response



@api_view(['GET'])
def post_list_api(request):
    posts = Post.objects.all()
    data = PostSerializer(posts, many=True, context={"request":request}).data
    return Response({"data":data})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail_api(request, id):
    post = get_object_or_404(Post, id=id)
    data = PostSerializer(post, context={"request":request}).data
    return Response({"data":data})



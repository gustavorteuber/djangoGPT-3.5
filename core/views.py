from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from .utils import get_gpt3_response  

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user_message = serializer.validated_data['content']
        gpt3_response = get_gpt3_response(user_message)

        response_message = ChatMessage.objects.create(content=gpt3_response)

        headers = self.get_success_headers(serializer.data)
        return Response(ChatMessageSerializer(response_message).data, status=status.HTTP_201_CREATED, headers=headers)

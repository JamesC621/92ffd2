from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, JsonResponse
from messenger_backend.models import Conversation
from rest_framework.views import APIView

class ReadMessages(APIView):
    """
    expect { recipientId, conversationId } in body (conversationId will be null if no conversation exists yet)
    """
    def put(self, request):
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)

            sender_id = user.id
            body = request.data
            conversation_id = body.get("conversationId")
            recipient_id = body.get("recipientId")

            conversation = Conversation.find_conversation(sender_id, recipient_id)
            if conversation.user1 and conversation.user1.id == user_id:
                conversation.user1_unread = 0
                conversation.user1_last_read_id = conversation.user1_last_unread_id or conversation.user1_last_read_id
                conversation.user1_last_unread_id = 0
            elif conversation.user2 and conversation.user2.id == user_id:
                conversation.user2_unread = 0
                conversation.user2_last_read_id = conversation.user2_last_unread_id or conversation.user2_last_read_id
                conversation.user2_last_unread_id = 0
            conversation.save()
            return JsonResponse({ "success": True })

        except Exception as e:
            return HttpResponse(status=500)
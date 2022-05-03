from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, JsonResponse
from messenger_backend.models import Conversation
from rest_framework.views import APIView

class ReadMessages(APIView):
    """
    expect { recipientId } in body
    """
    def put(self, request):
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)

            user_id = user.id
            body = request.data
            recipient_id = body.get("recipientId")

            conversation = Conversation.find_conversation(user_id, recipient_id)
            if conversation:
                if conversation.user1 and conversation.user1.id == user_id:
                    conversation.user1_unread = 0
                    conversation.user1_last_read_id = conversation.user1_last_unread_id
                    reader_last_read = conversation.user1_last_read_id
                    other_last_read = conversation.user2_last_read_id
                elif conversation.user2 and conversation.user2.id == user_id:
                    conversation.user2_unread = 0
                    conversation.user2_last_read_id = conversation.user2_last_unread_id
                    reader_last_read = conversation.user2_last_read_id
                    other_last_read = conversation.user1_last_read_id
                conversation.save()
                return JsonResponse({ 
                    "conversationId": conversation.id,
                    "readerId": user_id,
                    "otherUserId": recipient_id,
                    "readerLastRead": reader_last_read,
                    "otherUserLastRead": other_last_read,
                })
            return JsonResponse({})
        except Exception as e:
            return HttpResponse(status=500)
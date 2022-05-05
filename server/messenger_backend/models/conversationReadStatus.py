from django.db import models

from . import utils

class ConversationReadStatus(utils.CustomModel):

    conversation_id = models.IntegerField(default=-1)
    user_id = models.IntegerField(default=-1)
    last_read_id = models.IntegerField(default=-1)
    last_unread_id = models.IntegerField(default=-1)
    unread = models.IntegerField(default=0)


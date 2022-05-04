from django.db import models

from . import utils

class ConversationReadStatus(utils.CustomModel):

    conversation_id = models.IntegerField()
    user_id = models.IntegerField()
    last_read_id = models.IntegerField(default=-1)
    last_unread_id = models.IntegerField(default=-1)
    unread = models.IntegerField(default=0)
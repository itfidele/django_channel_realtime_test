from channels.layers import get_channel_layer
from django.db.models.signals import post_save, post_delete
from .models import Data
from django.dispatch import receiver
from asgiref.sync import async_to_sync

@receiver(post_delete,sender=Data)
@receiver(post_save, sender=Data)
def change_data(sender, instance, *args, **kwargs):
	count=Data.objects.count()
	async_to_sync(get_channel_layer().group_send)('well',{
        "type":"data_update",
        "event":'update_integer',
        'message':count,
        'data':'welcome',
    })
    
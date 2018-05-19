from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from django.contrib.auth import hashers
from django.conf import settings

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    CharField
)

from rent.models import ParkingForRent

class ParkingForRentSerializer(ModelSerializer):
    class Meta:
        model = ParkingForRent
        fields = [
            'db_property',
            'db_area',
            'db_type',
            'db_reserved',
            'db_period',
            'db_price',
            'db_status',
            'timestamp',
            'serial_no',
        ]

    def validate(self,data):
        unique_id  = get_random_string(length=10)
        data["serial_no"] = '#' + unique_id
#       ENCODED_PASSWORD = settings.EMAIL_HOST_PASSWORD
#       DECODED_PASSWORD = hashers.encode(ENCODED_PASSWORD)
#       settings.EMAIL_HOST_PASSWORD = DECODED_PASSWORD
#       email = EmailMessage('Subject', 'abc' , to=['jaoernwong@parkitmy.com'])
#       email.send()        
        return data
          
""""
from posts.models import Post
from posts.api.serializers import PostDetailSerializer


data = {
    "title": "Yeahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug": "yeah-buddy",
    
}

obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


"""
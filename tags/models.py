from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    lable = models.CharField(max_length=255)\
    
# generic class for tagging items
class TaggedItems(models.Model):
    # type of tag applied
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)

    # get the id and type of the item
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
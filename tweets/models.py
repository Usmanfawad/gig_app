from django.db import models


class Tweet(models.Model):
    # The id in django is automatically created so there is no need to put in the field.
    content= models.TextField(blank=True,null=True)
    image= models.FileField(upload_to='images/',blank=True,null=True)

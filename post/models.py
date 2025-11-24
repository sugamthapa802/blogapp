from django.db import models
from django.conf import settings


class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posts')
    body=models.TextField(max_length=1000)
    relevant_pic=models.ImageField(upload_to='posts/',blank=True,null=True)

    def __str__(self):
        return self.title

class Interactions(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    class Meta:
        abstract=True
    
class Comment(Interactions):
    comment_text=models.TextField(max_length=500)
    def __str__(self):
        return self.comment_text[:50]+'.....'
    class Meta:
        default_related_name='comments'
    
class Like(Interactions):
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['user','post'],name='unique_like')
        ]
        default_related_name='likes'
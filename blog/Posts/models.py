from django.db import models


class Topic(models.Model):
    topicName = models.CharField(max_length = 250)



class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE, default = "null")
    postTitle = models.CharField(max_length = 250)
    publisher = models.CharField(max_length = 250)
    datePub = models.DateTimeField(auto_now=False, auto_now_add=True)
    lastMod = models.DateTimeField(auto_now=True, auto_now_add=False)
    text = models.TextField()

    def __str__(self):
        return (str(self.postTitle) + ":" + str(self.id))



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, default = "null")
    name = models.CharField(max_length = 250)
    commentText = models.TextField()

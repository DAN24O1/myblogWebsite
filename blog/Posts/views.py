from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Post, Comment
from django.template import loader
from .forms import CommentForm


def index(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():

        form.save()
        form = CommentForm()

    allTopics = Topic.objects.all()
    allComments = Comment.objects.all()
    context = {
    'allComments' : allComments,
    'allTopics' : allTopics,
    'form' : form

    }
    return render(request, 'blog.html', context)





def detail(request, topic, postId=None):
    if postId:
        text = request.POST['text']
        post = Post.objects.get(id=int(postId))
        post.comment_set.create(name='dan', commentText=text)



    allTopics = Topic.objects.all()
    topic = Topic.objects.get(id = topic)
    allPosts = topic.post_set.all()
    allComments = []

    for eachPost in allPosts:
        allComments.append(eachPost.comment_set.all())


    context = {
        'allTopics' : allTopics,
        'topicId' : topic.id,
        'allPosts' : allPosts,
        'allComments' : allComments,
        'range': range(len(allComments)),


    }

    return render(request, 'blog.html', context)




def cv(request):
    context = {
    }
    return render(request, 'cv.html', context)


# Create your views here.

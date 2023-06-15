from django.shortcuts import render, redirect
from .models import Author, Post
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
    return render(request, 'home.html')


def author_new(request):
    if request.method == 'POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        a1 = Author()
        a1.name = my_name
        a1.email = my_email
        a1.password = my_password
        a1.save()
        return redirect('/')
    else:
        return render(request, 'author/author_new.html')
    
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors':authors})

def author_detail(request, my_id):
    author = Author.objects.get(id=my_id)
    return render(request, 'author/author_detail.html', {'author':author})

def author_update(request, my_id):
    author = Author.objects.get(id=my_id)
    if request.method == 'POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        author.name = my_name
        author.email = my_email
        author.password = my_password
        author.save()
        return redirect('/')
    else:
        return render(request, 'author/author_update.html', {'author':author})

def post_list(request):
    # order_by하고 -컬럼명 이렇게 주면 내림차순정렬
    posts = Post.objects.filter().order_by('-created_at')
    return render(request, 'post/post_list.html', {"posts":posts})

def post_new(request):
    if request.method == 'POST':
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        my_email = request.POST['my_email']
        p1 = Post()
        if my_email:
            try:
                a1 = Author.objects.get(email = my_email)
                # 장고에서 a1객체에서 id값만 빼서, db에 저장할때는 author_id에 id값을 저장
                p1.author = a1 #{id:1, name:"hong", email:"hong@naver" ...}
            except Author.DoesNotExist:
                # HttpResponse는 200 정상
                return HttpResponseNotFound("존재하지 않는 이메일입니다.")
        p1.title = my_title
        p1.contents = my_contents
        p1.save()
        return redirect('/')
    else:
        return render(request, 'post/post_new.html')


def post_detail(request, my_id):
    post = Post.objects.get(id=my_id)
    return render(request, 'post/post_detail.html', {'post': post})

def post_update(request, my_id):
    post = Post.objects.get(id=my_id)
    if request.method == 'POST':
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        post.title = my_title
        post.contents = my_contents
        post.save()
        return redirect('/')
    else:
        return render(request, 'post/post_update.html', {'post':post})


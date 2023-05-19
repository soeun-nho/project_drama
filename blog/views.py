from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostModelForm
from .models import Post


# Create your views here.
# 세번째 인자 주목!

def bloghome(request):
    return render(request, "blogIndex.html")

#create
def create(request):
    if request.method =='POST':
        form =PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=PostModelForm()
    return render(request,"form_create.html", {'form': form})

#read?
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,"post_list.html",{'posts':posts})

def post_detail(request):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post
    }
    return render(request,"post_detail.html", context)

def post_update(request,id):
    post = get_object_or_404(Post, pk=id)
    if request.method=='POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)
        return render(request, "form_create.html", {'form':form})
    

def post_delete(request, id):
    post= Post.objects.get(pk=id)
    post.delete()
    return redirect('post_list')
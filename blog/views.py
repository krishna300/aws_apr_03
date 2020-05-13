from django.shortcuts import render,redirect,reverse
from .forms import NoteForm
from .models import Post
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView


posts = [

    {
        'title': 'post1',
        'content': 'pst1 Lorem ipsum, dolor sit amet consectetur adipisicing elit. Vitae excepturi suscipit in!'
    },

    {
        'title': 'post2',
        'content': 'pst2 sit amet consectetur adipisicing elit. Vitae excepturi suscipit in!'
    },
    {
        'title': 'post3',
        'content': '3 ipsum, dolor sit amet consectetur adipisicing elit. Vitae excepturi suscipit in!'
    },
]


def a1(request):
    return HttpResponse('<h2> using HttpResponse </h2>')


def a2(request):
    return render(request, 'blog/a2.html')


def a3(request):
    return render(request, 'blog/a3.html', {'posts': posts})


def a4(request):
    return render(request, 'blog/a4.html')


def a5(request):
    return render(request, 'blog/a5.html')



def list1(request):
    posts=Post.objects.all()
    return render(request,'blog/list.html',{'posts':posts})



def create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect('a1')
    return render(request, 'blog/create.html', {'form': form})




class PostListView(ListView):
    model=Post
    template_name='blog/list.html'
    context_object_name='posts'



class PostUpdateView(UpdateView):
    model=Post
    template_name='blog/create.html'
    fields = ['title', 'url', 'description']


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

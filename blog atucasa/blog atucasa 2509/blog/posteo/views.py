from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from posteo.models import Posteo, posteoView, Comment, Like, Dislike
from posteo.forms import posteoForm

class posteoListViews(ListView):
    model = Posteo

class posteoDetailViews(DetailView):
    model = Posteo
    template_name = "posteo/posteo_Detail.html"

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        #if self.request.user.is_authenticated:
        posteoView.objects.get_or_create(user=self.request.user, posteo=object)

        return object
    
class posteoCreateViews(CreateView):
    form_class = posteoForm
    model = Posteo
    success_url = '/'
    template_name = "posteo/posteo_create.html"

    def get_context_data(self, *args, **kwargs):
        context = super(posteoCreateViews,self).get_context_data(*args, **kwargs)
        context.update({
            'view_type': 'create'
        })
        print(context)
        print(context["form"])
        print(context["form"].fields)
        return context

class posteoUpdateViews(UpdateView):

    from_class = posteoForm
    model = Posteo
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context
#   fields = (
#   'title',
#   'content',
#   'thumbmail',
#   'autor', 
    #'slug'
    
#    )

class posteoDeleteViews(DeleteView):
    model = Posteo
    success_url = '/'

def lista_post(request):
    return HttpResponse("post")

def like(request,slug,int):
    posteo = get_object_or_404(posteo,slug=slug)
    like_qs = like.object.filter(user=request.user, posteo=posteo)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    like.object.create(user=request.user, posteo=posteo)
    return redirect('detail', slug=slug)



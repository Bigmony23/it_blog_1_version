from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
# Create your views here.

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_view.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title','summary','body','photo']
    success_url = reverse_lazy('article_list')
    template_name = 'article_edit.html'

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title','summary','body','photo','author']
    success_url = reverse_lazy('article_list')
    template_name = 'article_new.html'
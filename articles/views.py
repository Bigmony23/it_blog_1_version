from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
# Create your views here.

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_view.html'

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author or self.request.user.is_superuser

class ArticleUpdateView( LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = ['title','summary','body','photo']
    success_url = reverse_lazy('article_list')
    template_name = 'article_edit.html'
    def test_func(self):
        obj = self.get_object()
        return obj.author==self.request.user or self.request.user.is_superuser

class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Article
    fields = ['title','summary','body','photo']
    success_url = reverse_lazy('article_list')
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser
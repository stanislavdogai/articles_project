from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import CommentForm
from webapp.models import Comment, Article


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/create.html"
    permission_required = "webapp.add_article"

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.article = article
        comment.save()
        return redirect('webapp:article_view', pk=article.pk)


class CommentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Comment
    template_name = 'comments/update.html'
    form_class = CommentForm
    permission_required = "webapp.change_comment"

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})


class CommentDeleteView(PermissionRequiredMixin, DeleteView):
    model = Comment
    permission_required = "webapp.delete_comment"

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:article_view", kwargs={"pk": self.object.article.pk})


class LikeComment(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        user = self.request.user
        if user in comment.users.all():
            comment.users.remove(user)
            comment.save()
            return JsonResponse({'comment' : comment.users.count()})
        else:
            comment.users.add(user)
            comment.save()
            return JsonResponse({'comment': comment.users.count()})

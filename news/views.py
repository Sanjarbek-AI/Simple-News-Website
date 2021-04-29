from math import ceil

from django.db.models import Q
from django.views.generic import ListView, DetailView

from news.models import NewsModel


class NewsListView(ListView):
    template_name = 'news_list.html'
    model = NewsModel
    paginate_by = 6

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        q = self.request.GET.get('q', '')

        qs = NewsModel.objects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(category__title__icontains=q)
        ).order_by('-pk')

        if pk:
            qs = qs.filter(category_id=pk)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ceil(NewsModel.objects.count() / self.paginate_by)
        context['range'] = range(x)

        return context


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    model = NewsModel

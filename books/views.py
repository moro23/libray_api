from django.utils import timezone
from django.views.generic.list import ListView
# Create your views here.

from .models import Book
class BookListView(ListView):

    model = Book 
    paginate_by = 100
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now() 
        return context 
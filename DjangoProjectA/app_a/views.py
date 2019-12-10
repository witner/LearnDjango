from django.shortcuts import render
from django.http import HttpResponse
from app_a.models import Author
# Create your views here.


def first_view(request):
    author_list = Author.objects.all()
    print(author_list)
    return render(request, 'first.html', {'authors': author_list})



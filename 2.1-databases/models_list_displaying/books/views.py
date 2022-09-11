from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import Book


def validate_date(date):
    try:
        if len(date) != 10:
            return HttpResponseNotFound('Incorrect data format, should be YYYY-MM-DD')
        date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return HttpResponseNotFound('Incorrect data format, should be YYYY-MM-DD')
    return date.date()


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def books_by_date(request, date):
    date = validate_date(date)
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=date)
    pub_dates = Book.objects.values('pub_date').order_by('pub_date').distinct()
    paginator = Paginator(pub_dates, 1)
    page_number = 1
    for pub_date in pub_dates:
        if date == pub_date['pub_date']:
            break
        page_number += 1
    page = paginator.page(page_number)
    prev_date = None
    next_date = None
    if page.has_previous():
        prev_date = paginator.page(page_number-1).object_list[0]['pub_date']
    if page.has_next():
        next_date = paginator.page(page_number+1).object_list[0]['pub_date']
    print(prev_date)
    print(next_date)
    context = {
        'books': books,
        'page': page,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, template, context)

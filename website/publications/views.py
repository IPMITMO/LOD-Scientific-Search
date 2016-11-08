from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Publication
from django.db.models import Q
from .forms import SearchForm


def index(request):
    all_publications = Publication.objects.all()
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data
            return HttpResponseRedirect('/publications/search/' + search_query['text_for_search'])
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
    context = {'all_publications': all_publications,
               'form': form}
    return render(request, 'publications/index.html', context)


def search(request, search_query):
    results = Publication.objects.filter(Q(name__icontains=search_query) |
                                         Q(author__icontains=search_query) |
                                         Q(year__icontains=search_query) |
                                         Q(publisher__icontains=search_query))
    context = {'all_results': results}
    return render(request, 'publications/search.html', context)


def detail(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    context = {'name': publication.name,
               'year': publication.year,
               'author': publication.author,
               'publisher': publication.publisher}
    return render(request, 'publications/detail.html', context)

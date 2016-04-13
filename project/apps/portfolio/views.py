# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404

from portfolio.models import PortfolioItem


def index(request):
    items = PortfolioItem.objects.all()
    return render(request, 'portfolio/index.html', {'object_list': items})


def single(request, pk):
    try:
        obj = PortfolioItem.objects.get(pk=pk)
    except PortfolioItem.DoesNotExist:
        raise Http404

    obj.new_visit()

    return render(request, 'portfolio/single.html', {'object': obj})

from django.core.paginator import Paginator


def custom_paginator(request, object_list):
    paginator = Paginator(object_list, 6)
    page_obj = paginator.get_page(request.get('pageNumber', 1))

    return page_obj, paginator.num_pages, paginator.count

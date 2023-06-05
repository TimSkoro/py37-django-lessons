from django.shortcuts import render


def id_view(requests, id):
    return render(requests, 'slug_page.html', context={"data": id, "tag": "ID"})


def slug_view(requests, name_of_news):
    return render(requests, 'slug_page.html', context={"data": name_of_news, 'tag': "SLUG"})

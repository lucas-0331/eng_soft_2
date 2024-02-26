from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        return render(request, "index.html")


def OrderView(request, order_items, username):
        return render(request, "order.html")
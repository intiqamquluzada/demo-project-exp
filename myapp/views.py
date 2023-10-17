from django.shortcuts import render
from myapp.models import MyModel


def index_view(request):
    my_datas = MyModel.objects.all()
    # print(my_datas)

    context = {
        "my_datas": my_datas,
    }
    return render(request, "index.html", context)


def detail_view(request, id):
    my_obj = MyModel.objects.get(id=id)
    context = {
        "my_obj": my_obj,
    }
    return render(request, "detail.html", context)

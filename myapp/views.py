from django.shortcuts import render
from myapp.models import MyModel


def index_view(request):
    my_datas = MyModel.objects.all()
    # print(my_datas)

    context = {
        "my_datas": my_datas,
    }
    return render(request, "index.html", context)

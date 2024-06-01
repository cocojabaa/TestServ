import json
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Items

# Create your views here.
@csrf_exempt
def index(req: HttpRequest):
    if (len(dict(req.POST.items())) > 0):
        print(req.POST["message"])
    return render(req, "app/index.html")

def send_all_items(req: HttpRequest):
    data = {"all_items": []}
    for item in Items.objects.all():
        data["all_items"].append(item.get_dict())
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json")

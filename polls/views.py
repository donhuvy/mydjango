from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Chào Minh Thu. Bạn đang ở trang chủ của ứng dụng Bình chọn.")

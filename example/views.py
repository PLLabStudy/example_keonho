from django.shortcuts import render

# Create your views here.
def index(request):
    a = "안녕하세요 인덱스 페이지입니다."
    send_varilbe = {
        'B': "안녕하세요 인덱스 사이지입니다.",
        'a': a
    }
    return render(request, "index.html", send_varilbe)

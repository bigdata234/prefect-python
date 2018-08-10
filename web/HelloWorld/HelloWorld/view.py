from django.http import HttpResponse
from django.shortcuts import render
import jwt


def test(request):
    return render(request, 'test.html')


def hello(request):
    context = {}
    context['hello'] = 'Hello World,templates'
    # return render(request,'hello.html',context)
    # return HttpResponse("Hello,Django!")

    METABASE_SITE_URL = "http://192.168.85.130:3000"
    METABASE_SECRET_KEY = "e82a275d9788d1d03b09aa272a8f6fb735f855d67affb7c53a32a513426b8b42"

    payload = {
        "resource": {"question": 16},
        "params": {

        }
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframeUrl = METABASE_SITE_URL + "/embed/question/" + token.decode("utf8") + "#bordered=true&titled=true"
    print(iframeUrl)
    context['iframeUrl'] = iframeUrl

    return render(request, 'index.html', context)

from series import model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from series.models import Serie
from series.serializers import SerieSerializer



class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def serie_list(request):
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        # return JSONResponse(request, status=201)
        data = JSONParser().parse(request)
        serializer = SerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def serie_detail(request, pk):
    try:
        serie = Serie.objects.get(pk=pk)
    except Serie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerieSerializer(serie)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SerieSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        serie.delete()
        return HttpResponse(status=204)

@csrf_exempt
def modelPredict(request):
    #return "Hola"
    return model.predict("Que visaje la vida parce....")

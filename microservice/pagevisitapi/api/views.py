from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from pagevisitapi.models import PageVisit
from .serializers import PageVisitSerializer

class PageVisitApiView(APIView):

    def get(self,request):
        pagevisits = PageVisit.objects.all()
        serializer = PageVisitSerializer(pagevisits,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PageVisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)




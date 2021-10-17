from rest_framework import serializers, status
from rest_framework import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer


# @api_view(["GET", "POST"])
# def job_list_create_api_view(request):

#     if request.method == "GET":
#         joboffers = JobOffer.objects.filter(available=True)
#         serializer = JobOfferSerializer(joboffers, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = JobOfferSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def job_detail_api_view(request, pk):
#     try:
#         joboffer = JobOffer.objects.filter(pk=pk)
#     except JobOffer.DoesNotExist:
#         return Response({"error" : {
#                     "code" : 404,
#                     "message" : "JobOffer not found!"
#                 }}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = JobOfferSerializer(joboffer)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = JobOfferSerializer(joboffer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         joboffer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class JobListCreateAPIView(APIView):
    
    def get(self, request):
        joboffers = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(joboffers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobDetailAPIView(APIView):

    def get_object(self,pk):
        joboffer = get_object_or_404(JobOffer, pk=pk)
        return joboffer

    def get(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(joboffer)
        return Response(serializer.data)

    def put(self, request, pk):
        joboffer = self.get_object(pk)
        serializer = JobOfferSerializer(joboffer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        joboffer = self.get_object(pk)
        joboffer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
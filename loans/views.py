import logging
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .serializers import LoanSerializer
from .services import LoanServices
# Create your views here.

class EmiView(GenericAPIView):
    serializer_class = LoanSerializer
    loan_services = LoanServices()
    logger = logging.getLogger(__name__)
    
    """
    API for generating EMI details
    """
    def post(self,request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            self.logger.info('Invalid Parameters',serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        try:
            data = self.loan_services.emi_calculator(request.data)
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            self.logger.error("GENERATE EMI API FAILED",e)
            data = {'message':'Something went wrong. Please try again later'}
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)
    
    
    """
    API for returning the status of Generate EMI details API
    """
    def get(self,request):
        try:
            data = self.loan_services.generate_emi_details_api_status()
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            self.logger.error("GENERATE EMI API FAILED",e)
            data = {'message':'Something went wrong. Please try again later'}
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)

import logging
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoanSerializer
from .services import LoanServices

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
            return Response(data,status=status.HTTP_201_CREATED)
        except Exception as e:
            self.logger.error("GENERATE EMI API FAILED",e)
            data = {'message':'Something went wrong. Please try again later'}
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)
    
    
    """
    API for fetching the status of the above POST API
    """
    def get(self,request):
        try:
            data = self.loan_services.emi_api_status()
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            self.logger.error("GENERATE EMI API FAILED",e)
            data = {'message':'Something went wrong. Please try again later'}
            return Response(data,
                            status=status.HTTP_400_BAD_REQUEST)

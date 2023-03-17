from datetime import datetime
import calendar
import json
from django.db.models import Count,Avg
from .models import Loan

class LoanServices():

    # For calculating the EMI amount applicable
    def calculate_emi(self,data):
        P = data['loan_amount']
        n = data['tenure']
        interest = data['interest']
        r = (interest/12)/100
        emi = P * r * (pow(1+r,n)/(pow(1+r,n)-1))
        return round(emi,2)

    # For finding the instalment details for every month
    def calculate_balance(self,data):
        
        balance = []
        tenure = data['tenure']
        current_month = datetime.now().month
        current_year = datetime.now().year

        # Calculates instalment details for every month and adds it to a list
        for i in range(tenure):
            d = {}
            d['instalment'] = i+1

            # finding the instalment month
            instalment_month = (current_month +i) % 12
            if instalment_month == 0:
                instalment_month =12
            d['month'] = calendar.month_name[instalment_month]

            # finding the instalment year
            d['year'] = current_year + ((current_month-1+i)//12)

            # loan percentage paid till date
            loan_paid_till_date = round(((i+1)/tenure)*100,2)
            d['loan_paid_till_date'] = str(loan_paid_till_date)+' %'
            
            balance.append(d)
        return balance

    # Calculates the total interest payable
    def get_total_interst(self, data, emi_amount):
        loan_amount = data['loan_amount']
        tenure = data['tenure']
        total_payable = emi_amount*tenure
        total_interst = round(total_payable - loan_amount,2)
        return total_interst

    # All EMI details 
    def emi_calculator(self,data):

        res = {}
        emi_amount = self.calculate_emi(data)
        res['emi_amount'] = emi_amount
        res['total_interest'] = self.get_total_interst(data,emi_amount)
        res['balance'] = self.calculate_balance(data)
        
        # res['total_interest'] = total_interest
        # res['balance'] = balance
        return res
    

    # Aggrgate values of loan attributes fetched from DB
    def generate_emi_details_api_status(self):
        api_status = Loan.objects.filter(is_deleted=False).aggregate(
            total_hits = Count('id'),
            loan_avg=Avg('loan_amount'),
            interest_avg=Avg('interest'),
            tenure_avg=Avg('tenure'))
        return api_status
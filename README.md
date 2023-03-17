# Loans - EMI Details Generator

urls : [POST,GET] http:<localhost>/api/loans/emi/
payload : 
{
    "loan_amount": 5000000,
    "interest": 9,
    "tenure":12
}
'tenure' should be given as the number of months.
Swagger documentation included in the home page.

DB used: Sqlite

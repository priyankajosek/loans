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

Directions:
clone and open this project 
run 'pip install pipenv'
run 'pipenv shell'
run 'pipenv install'
run 'python manage.py makemigrations'
run 'python manage.py makemigrations loans'
run 'python manage.py migrate'
run 'python manage.py runserver'

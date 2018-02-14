# backenddevtest
1. Clone project.
2. cd backenddevtest/
3. virtualenv .env -p python3.5
4. source .env/bin/activate
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver
9. open another terminal and run: cd ui/
10. python -m SimpleHTTPServer 8001

# rio-lists
Web service for lists of different kind. Like, shopping lists, to-do lists or else.
### current state
Semi functional: items can be added or deleted
### todo
- deploy somewhere for others to test
- add user login
- make lists private
- add static handling
- add css styles
- add pictures and icons
- make amount changeable
### development: docker
To deploy - from the root folder:
```Linux Kernel Module
docker-compose up -d --build
```
Then go to http://127.0.0.1:5000 <br>
To switch containers off:
```Linux Kernel Module
docker-compose down -v
```
### production: nginx, gunicorn, docker
To deploy - from the root folder:
```Linux Kernel Module
docker-compose -f docker-compose.prod.yml up -d --build
```
To build the data base with initial tables & values:
```Linux Kernel Module
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
```
To switch containers off:
```Linux Kernel Module
docker-compose -f docker-compose.prod.yml down -v
```

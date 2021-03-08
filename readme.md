### Overview
A veterinary app for building an API using Django Rest Framework and Polymorphic Model.

------------

### Installation
- Create and activate a virtualenv
 
- Install all packages from requirements.txt

`$ pip install -r requirements.txt`

- Migrate app and create superuser

`$ python manage.py makemigrations`

`$ python manage.py migrate`

`$ python manage.py createsuperuser`

- Run server

`$ python manage.py runserver`


------------

### API Documentation
| Endpoint  | HTTP Method  | CRUD Method  | Description  |
| ------------ | ------------ | ------------ | ------------ |
| /animals/  | GET  | READ  | Show the list of animals  |
| /animals/<:id>/ |  GET |  READ | Show the animal with matching id  |
| /cats/  | GET  |  READ | Show the list of cats  |
| /cats/  | POST  | CREATE  | Create a new cat  |
| /cats/<:id>/  |  GET | READ  | Show the cat with matching id  |
| /cats/<:id>/  | PUT  | UPDATE  | Update a cat specified by id  |
| /cats/<:id>/  | DELETE  | DELETE  | Delete a cat specified by id  |
| /dogs/  | GET  |  READ | Show the list of dogs  |
| /dogs/  | POST  | CREATE  | Create a new dog |
| /dogs/<:id>/  |  GET | READ  | Show the dog with matching id  |
| /dogs/<:id>/  | PUT  | UPDATE  | Update a dog specified by id  |
| /dogs/<:id>/  | DELETE  | DELETE  | Delete a dog specified by id  |
| /cows/  | GET  |  READ | Show the list of cows  |
| /cows/  | POST  | CREATE  | Create a new cow |
| /cows/<:id>/  |  GET | READ  | Show the cow with matching id  |
| /cows/<:id>/  | PUT  | UPDATE  | Update a cow specified by id  |
| /cows/<:id>/  | DELETE  | DELETE  | Delete a cow specified by id  |
| /appointment/  | GET  |  READ | Show the list of appointments |
| /appointment/  | POST  | CREATE  | Create a new appointment  |
| /appointment/<:id>/  |  GET | READ  | Show the appointments with matching animal_id  |
| /appointment/<:id>/  | PUT  | UPDATE  | Update a appointment specified by id  |
| /appointment/<:id>/  | DELETE  | DELETE  | Delete a appointment specified by id |

https://documenter.getpostman.com/view/10306840/Tz5jg1pL











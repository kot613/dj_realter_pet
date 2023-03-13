# Real estate agency site(pet project)
***
This project is not intended for commercial use.
The project was implemented with the help of Django

The RealEstate has got 3 apps, the different apps and their purpose are described here:

### Agents app
Сreated Agent and MessageAgent models. Implemented form for sending a message and controllers to display a list of agents and details about each.

#### Agent
The Agent model contains information about the agent, such as the agent's name, description, profile picture, e-mail address and phone number, whether he is a top seller, and the creation date.

+ name: CharField(max_length=255)
+ slug: SlugField(max_length=255, unique=True, db_index=True)
+ photo: ImageField(upload_to='agents_photo/%Y/%m/%d/')
+ description: models.TextField(blank=True)
+ email: CharField(max_length=50)
+ phone: CharField(max_length=20)
+ hire_date: DateTimeField(default=datetime.now, blank=True)
+ is_best: BooleanField(default=False)

For test use fixture agent.json

#### MessageAgent
All users will be able to send a message to an agent for further communication.

+ name: CharField(max_length=255)
+ email: CharField(max_length=50)
+ comment: TextField()
+ is_read: BooleanField(default=False)
+ agent: ForeignKey(Agent)
 
### Houses app
Created House models. Controllers have been implemented to display the list of houses, house details, and search according to the given parameters.

#### House
The House model contains information about the house: city, lat and lng, description, image, number of bathrooms and bedrooms, year of construction, total area, overall quality and overall condition. There is also a link to the agent who represents this home.
+ realtor: ForeignKey(Agent)
+ title: CharField
+ city: CharField
+ lat: FloatField
+ lng: FloatField
+ description: TextField
+ price: IntegerField
+ bedrooms: IntegerField
+ bathrooms: IntegerField
+ area: IntegerField
+ year_build: IntegerField
+ total_room: IntegerField
+ building_type: CharField
+ overall_quality: SmallIntegerField(choices)
+ overall_condition: SmallIntegerField(choices)
+ list_date: DateTimeField
+ photo_main:ImageField
+ photo: ImageField

For test use fixture houses.json

### Pages app
Controllers have been implemented to display the home and about page.
***
Modified admin panel.

## Project setup


### Setting up a virtual environment
At the root of the project, create a virtual environment using the command:
```shell
python -m venv venv
```
Activate it:
```shell
venv\Scripts\activate
```

Then we install all the dependencies from the `req.txt` file into the virtual environment:

```shell
pip install -r req.txt
```

### Migrations
**Postgres must be enabled for migration**

If all the previous steps are completed successfully, all that remains for you is to apply the migrations, for this we use this command:

```shell
python manage.py migrate
```

### Launch of the project
After successful configuration, you need to write the following command to run the django app:
Write the data from the file to your database
```shell
python.exe -Xutf8 manage.py loaddata agents/fixture/agents.json
python.exe -Xutf8 manage.py loaddata houses/fixture/houses.json
```
Create superuser
```shell
python manage.py createsuperuser
```
Launch of the project
```shell
python manage.py runserver
```
***


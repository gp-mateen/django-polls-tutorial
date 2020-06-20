# Django Polls Tutorial
Django polls tutorial with materialize css.

## Setup

### Make migrations
Make migrations with the below command to be applied to the database.

`python manage.py makemigrations`

### Migrate
Migrate all the migrations that are created in the above step to the local SQLite database.

`python manage.py migrate`

### Run Django (dev) server

`python manage.py runserver`

At this point you'll see no active polls, so let's go ahead and add some data. We've create `load.py` to specifically take care of loading some intitial data to work with.

`python load.py`

Now go back and check the polls page, and go ahead and vote.

### Demo
This app is live [here](http://gpmateen.pythonanywhere.com/polls/).

A big thanks to [pythonanywhere](https://www.pythonanywhere.com/)
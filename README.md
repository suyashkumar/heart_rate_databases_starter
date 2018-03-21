# heart_rate_databases_starter
Starter codebase for BME590 Databases Assignment (which can be found [here](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/databases/main.md#mini-projectassignment)). 

To get started with this sample code, you first need to get the mongodb program running. To do this, simply run 
```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```

either on your local machine (if you have docker installed there) or on a virtual machine you have access to where you can first install docker.

:eyes: if you are running your mongodb database on a virtual machine, you need to replace the `connect` URI string in `main.py`. Replace `localhost` with a VM address, like so:

```py
connect("mongodb://vcm-0000.vm.duke.edu:27017/heart_rate_app") # open up connection to db
```

once your database is running and your connection string is set, you can run the starter program by running `main.py` after activating your `virtualenv` and installing all the dependencies listed in `requirements.txt`.

```
python main.py
```

## The Assignment + Hints

This starter code _is not_ a flask server like you need to build in your assignment--`main.py` is an example module that contains several useful functions for creating a `User` (`create_user`) and updating a `User` with a new heart rate and heart rate timestamp (`add_heart_rate`). 

`models.User` is a data model that represents the entity we want to store and retreive from the database. You can see that `User` is just a python class with some properties. 

:eyes: When writing the `POST /api/heart_rate` endpoint, you need to first check if the user with the given email already exists in the database. If so, then you can use `add_heart_rate` to append a heart rate measurement to that user. If not, then you would want to `create_user`. I did not explicitly show you how to check if a user already exists in the database, but this is something you should be able to figure out based on the sample code + google + office hours! 

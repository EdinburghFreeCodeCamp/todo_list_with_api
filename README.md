# todo_list_with_api

Hey Edinburgh folks!

I've started this off in django, if you are unfamiliar with Django please try the django project tutorial - I thought it was fab.

To run:
* Clone this repo. 
* `python manage.py migrate`
* `python manage.py runserver`
* Open localhost:8000 in your fav. browser, appricate the lack of css!
* Go back to the console and ctrl-c to stop the server. Create a user for yourself using  `python manage.py createsuperuser`
* Start the server and go to localhost:8000/admin and start exploring the models. Create some lists and elements...
* Go to localhost:8000/todo and you should be able to see a list of the instances you just created.

#Contributing
Once you know what you want to do let others know about it by creating an issue and assigning your self to it.
For the sake of example, you want to improve the styling :)
* Create a branch for the issue `git checkout -b improve_styling`
 * The branch name should be short but descriptive.
* Commit regularly with descriptive commits. `git commit -m "add a folder for the css within todo/static/ with css files for a minimal design. Create a base.html template in todo_website/templates and import the css file in this base template. Add {% extends base.html %} to each of the existing templates for layout and styles."
 * This message might be on the long side but I hope you get what I mean...ur 
* Push often
* Once you are finished, create a pull request. I and others will review the work before merging with master.

Please write tests  :D


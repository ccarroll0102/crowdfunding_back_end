# Crowdfunding Back End
{{ SwimRise }}

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ A crowdfunding website designed to raise money for children, families swim or beach clubs to fund swimming lessons for children who cannot afford to attend swimming or surf safety (nippers) lessons }}

=> Log in
    - GET Log in details
    - GET Sign up details 
    - Log out

=> Homepage
    - GET list of available fundraisers

=> "My Profile"
    - GET details of currently-logged-in user account
    - PATCH/POST change details of user account
    - DELETE delete user account

=> Fundraiser page
    - GET fundraiser information
    - GET previously made pledge
    - IF logged in be able to POST a pledge
    - IF not logged in be prompted to log in to POST a pledge
    - POST a pledge 
    - GET the pledge I just in the front end


### Front End Pages/Functionality
- {{ The Homepage }}
    - {{ Show all of the fundraisers currently available }}
    - {{ Ability to login }}
    - {{ Ability to create a fundraiser if logged in }}
    - {{ Ability to make a pledge to any fundraise if logged in}}

- {{ Login Page}}
    - {{ Enter username and password to login }}
    - {{ Login success and error modals }}
    - {{ Potential 2FA screen? }}

- {{ A Fundraiser Page}}
    - {{ Page the shows the detail of a selected fundraited }}
    - {{ User to see:
                    1. Fundraiser details (title, descriptionl, image, goal, if open, created date, expiry date?)
                    2. Ability to add a pledge with associated pledge details
                    3. Post the pledge and then see it added to the fundraiser
                    4. view all of the previously made pledges }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
|     |             |         |              |                       |                              |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )




--- Method ---

create the model
running a migration will create the database table based on this model
creates a migration file that tells django what changes to make to the database
python manage.py migrate
 python manage.py makemigrations
 Then we create a serializer for our pledges and fundraisers so that we can convert the data to and from JSON format when sending and receiving API requests.
 Go to serializers.py to create the serializers and copy/paste and change fundraisers to pledges for the PledgeSerializer
 Then go to View
 Type in the class for the pledge
 Write in the Post/Get functions
 Then go to URLS folder in the fundraisers file 
 create a third path
 then go to pledged endpoint and it should be an empty list 
 http://127.0.0.1:8000/fundraisers/
 to interact with the database use the django shell
 python manage.py shell
 from fundraisers.models import Fundraiser, Pledge
 Fundraiser.objects.all()
 Fundraiser.objects.create(title="Save the Whales", description="We need to save the whales", goal=10000, image="http://example.com/whale.jpg", is_open=True)
 Fundraiser.objects.all()


model serializer view URL
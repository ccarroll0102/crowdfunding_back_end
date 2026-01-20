# crowdfunding_back_end
""" A crowdfunding website designed to raise money for children, families swim or beach clubs to fund swimming lessons for children who cannot afford to attend swimming or surf safety (nippers) lessons """

--- Method ---

# create the model
# running a migration will create the database table based on this model
# creates a migration file that tells django what changes to make to the database
# python manage.py makemigrations
# python manage.py migrate


# Then we create a serializer for our pledges and fundraisers so that we can convert the data to and from JSON format when sending and receiving API requests.
# Go to serializers.py to create the serializers and copy/paste and change fundraisers to pledges for the PledgeSerializer

# Then go to View
# Type in the class for the pledge
# Write in the Post/Get functions

# Then go to URLS folder in the fundraisers file 
# create a third path

# then go to pledged endpoint and it should be an empty list 
# http://127.0.0.1:8000/fundraisers/

# to interact with the database use the django shell
# python manage.py shell
# from fundraisers.models import Fundraiser, Pledge
# Fundraiser.objects.all()
# Fundraiser.objects.create(title="Save the Whales", description="We need to save the whales", goal=10000, image="http://example.com/whale.jpg", is_open=True)
# Fundraiser.objects.all()


model serializer view URL
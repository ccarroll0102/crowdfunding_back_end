# Crowdfunding Back End  
**Claudia Carroll**

## Planning:
**🏊‍♀️ SwimRise** is a crowdfunding platform designed to help children and families access swimming and surf safety lessons.
Swim clubs, surf clubs, and families can raise funds for children who cannot afford swimming or nippers (surf life-saving) programs.

This backend provides:

- User authentication (token-based)
- Fundraiser creation and management
- Pledge creation
- Fundraiser state management (Open, Closed, Archived)
- Ownership-based permissions

### Intended Audience/User Stories

My crowdfunding back end project enables:

- Creation of fundraisers
- Public viewing of active fundraisers
- Secure pledge submissions
- Fundraiser lifecycle management (open → closed → archived)

## 🔐 Authentication

- As a user, I can sign up for an account.
- As a user, I can log in and receive a token.
- As a logged-in user, I can access protected endpoints.
- As a user, I can log out.

---

## 🏠 Homepage / Public View

- As a visitor, I can view all active fundraisers.
- As a visitor, I can view details of an open or closed fundraiser.
- As a visitor, I cannot see archived fundraisers.
- As a visitor, I must log in to create a pledge.

---

## 👤 My Dashboard

- As a logged-in user, I can:
  - View all fundraisers I own (including archived).
  - Create a fundraiser.
  - Close a fundraiser.
  - Reopen a fundraiser.
  - Archive a fundraiser (must be closed first).
  - Unarchive a fundraiser (remains closed).

---

## 💰 Pledging

- As a logged-in user, I can pledge to an open fundraiser.
- I cannot pledge to a closed fundraiser.
- I cannot pledge to an archived fundraiser.
- If the fundraiser does not exist, I receive a 404 error.

---

# 🔄 Fundraiser States

Fundraisers have three states:

- **Open** → Accepting pledges  
- **Closed** → Visible but not accepting pledges  
- **Archived** → Hidden from public but available to the owner  

---

## 🔁 State Transitions

| From | Action | To |
|------|--------|----|
| Open | Close | Closed |
| Closed | Open | Open |
| Closed | Archive | Archived |
| Archived | Unarchive | Closed |

## 📋 Business Rules

- Only the owner can modify fundraiser state.
- Fundraiser must be closed before archiving. 
- Unarchiving does not automatically reopen the fundraiser.
- Archived fundraisers are hidden from non-owners.
- Closed fundraisers remain publicly visible.
- Cannot pledge to closed or archived fundraisers.


### API Spec
# 🌐 API Specification

| URL | Method | Purpose | Request Body | Success Code | Authentication |
|-----|--------|---------|--------------|--------------|---------------|
| `/fundraisers/` | GET | Get all non-archived fundraisers | – | 200 | Public |
| `/fundraisers/?owner=me` | GET | Get all fundraisers owned by current user (including archived) | – | 200 | Authenticated |
| `/fundraisers/?owner=<id>` | GET | Get non-archived fundraisers for a specific user | – | 200 | Public |
| `/fundraisers/` | POST | Create a fundraiser | Fundraiser fields | 201 | Authenticated |
| `/fundraisers/<id>/` | GET | Get fundraiser details | – | 200 | Public (archived hidden from non-owner) |
| `/fundraisers/<id>/` | PATCH | Edit fundraiser | Partial fields | 200 | Owner only |
| `/fundraisers/<id>/close/` | PATCH | Close fundraiser | – | 200 | Owner only |
| `/fundraisers/<id>/open/` | PATCH | Reopen closed fundraiser | – | 200 | Owner only |
| `/fundraisers/<id>/archive/` | PATCH | Archive fundraiser (must be closed) | – | 200 | Owner only |
| `/fundraisers/<id>/unarchive/` | PATCH | Unarchive fundraiser (remains closed) | – | 200 | Owner only |
| `/pledges/` | GET | List pledges | – | 200 | Public |
| `/pledges/` | POST | Create pledge | Pledge fields | 201 | Authenticated |
| `/api-token-auth/` | POST | Obtain authentication token | Username & password | 200 | Public |

---

# 🔐 Permissions Model

- **Public users**:
  - Can view open and closed fundraisers
  - Cannot see archived fundraisers
  - Cannot create pledges without authentication

- **Authenticated users**:
  - Can create pledges
  - Can create fundraisers

- **Fundraiser owners**:
  - Can edit their fundraisers
  - Can close/open fundraisers
  - Can archive/unarchive fundraisers

  # 🚀 Future Improvements

Potential future enhancements:

- Expiry date for fundraisers
- Frontend integration


### DB Schema
![]( {{ https://ibb.co/tpw1qDRB}} )
![]( {{ https://ibb.co/qYhj0KP2}} )
![]( {{ https://ibb.co/hJn4CK6B}} )




--- Method personal notes---

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
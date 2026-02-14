from django.urls import path
from . import views
 
urlpatterns = [
   path('fundraisers/', views.FundraiserList.as_view()),
   path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()),
   path('fundraisers/<int:pk>/archive/', views.FundraiserArchive.as_view()),
   path('pledges/', views.PledgeList.as_view()),
   path('fundraisers/<int:pk>/unarchive/', views.FundraiserUnarchive.as_view()),
   path('fundraisers/<int:pk>/close/', views.FundraiserClose.as_view()),
   path('fundraisers/<int:pk>/open/', views.FundraiserOpen.as_view()),

 ]
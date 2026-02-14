
# Create your views here.
from urllib import request
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from .models import Fundraiser
from .serializers import FundraiserDetailSerializer, FundraiserSerializer
from .models import Pledge
from .serializers import PledgeSerializer


class FundraiserList(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get(self, request):
        owner_filter = request.query_params.get("owner")

        if owner_filter == "me":
            if not request.user.is_authenticated:
                return Response(
                    {"detail": "Authentication required."},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            fundraisers = Fundraiser.objects.filter(owner=request.user)

        elif owner_filter is not None:
            if not owner_filter.isdigit():
                return Response(
                    {"detail": "owner must be a number or 'me'."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            fundraisers = Fundraiser.objects.filter(
                owner_id=owner_filter,
                is_archived=False
            )

        else:
            fundraisers = Fundraiser.objects.filter(is_archived=False)

        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    
class FundraiserDetail(APIView):

    permission_classes = [
      permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get_object(self, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        if fundraiser.is_archived and self.request.user != fundraiser.owner:
            raise Http404
        self.check_object_permissions(self.request, fundraiser)
        return fundraiser

    def get(self, request, pk):
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data)
    
    def put(self, request, pk):
        forbidden_fields = {'owner', 'date_created'}
        if any(field in request.data for field in forbidden_fields):
            return Response(
                {"detail": "You cannot edit owner or date_created."},
                status=status.HTTP_400_BAD_REQUEST
            )
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(
            instance = fundraiser,
            data = request.data, 
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def patch(self, request, pk):
        forbidden_fields = {'owner', 'date_created'}
        if any(field in request.data for field in forbidden_fields):
            return Response(
                {"detail": "You cannot edit owner or date_created."},
                status=status.HTTP_400_BAD_REQUEST
            )
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetailSerializer(
            instance=fundraiser,
            data=request.data,
            partial=True
    )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, pk):
        fundraiser = self.get_object(pk)
        fundraiser.delete()
        return Response (
            {"detail": "Fundraiser deleted successfully."},
            status=status.HTTP_200_OK
        )
    
class FundraiserArchive(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self,pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        if fundraiser.is_archived and self.request.user != fundraiser.owner:
            raise Http404
        self.check_object_permissions(self.request, fundraiser)
        return fundraiser
    
    def patch (self, request, pk):
        fundraiser = self.get_object(pk)
        if fundraiser.is_archived:
            return Response(
                {"detail": "Fundraiser is already archived"},
                status=status.HTTP_400_BAD_REQUEST
            )
        fundraiser.is_open = False
        fundraiser.is_archived = True
        fundraiser.save()
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FundraiserUnarchive(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_object(self,pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        if fundraiser.is_archived and self.request.user != fundraiser.owner:
            raise Http404
        self.check_object_permissions(self.request, fundraiser)
        return fundraiser
    
    def patch (self, request, pk):
        fundraiser = self.get_object(pk)
        if fundraiser.is_archived == False:
            return Response(
                {"detail": "Fundraiser is not archived"},
                status=status.HTTP_400_BAD_REQUEST
            )
        fundraiser.is_archived = False
        fundraiser.save()
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FundraiserClose(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_object(self,pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        if fundraiser.is_archived and self.request.user != fundraiser.owner:
            raise Http404
        self.check_object_permissions(self.request, fundraiser)
        return fundraiser
    
    def patch (self, request, pk):
        fundraiser = self.get_object(pk)
        if fundraiser.is_archived == True:
            return Response(
                {"detail": "Fundraiser is archived and cannot be closed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if fundraiser.is_open == False:
            return Response(
                {"detail": "Fundraiser is already closed."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        fundraiser.is_open = False
        fundraiser.save()
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        fundraiser_id = request.data.get('fundraiser')

        if fundraiser_id is None:
            return Response(
            {"detail": "fundraiser field is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

        fundraiser = get_object_or_404(Fundraiser, pk=fundraiser_id)

        if fundraiser.is_archived:
            return Response(
            {"detail": "Cannot pledge to an archived fundraiser."},
            status=status.HTTP_400_BAD_REQUEST
        )

        if not fundraiser.is_open:
            return Response(
            {"detail": "Cannot pledge to a closed fundraiser."},
            status=status.HTTP_400_BAD_REQUEST
        )

        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
        )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
    )
    
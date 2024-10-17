from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # Allow access without authentication
from .models import Component, Vehicle, Issue, Transaction
from .serializers import ComponentSerializer, VehicleSerializer, IssueSerializer, TransactionSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    permission_classes = [AllowAny]  # Optional: Change to IsAuthenticated if needed

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [AllowAny]  # Allow access without authentication

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [AllowAny]  # Optional: Change to IsAuthenticated if needed

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]  # Optional: Change to IsAuthenticated if needed
from rest_framework import viewsets , permissions
from .models import User, Address
from .serializers import UserSerializer, AddressSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Только просмотр своего профиля и списка users (для admins)
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class AddressViewSet(viewsets.ModelViewSet):
    """
    CRUD для адресов текущего пользователя
    """
    
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

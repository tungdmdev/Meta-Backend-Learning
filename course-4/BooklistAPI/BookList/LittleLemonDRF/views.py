from .models import Book, MenuItem, Category
from .serializers import BookSerializer, MenuItemSerializer, CategorySerializer
from rest_framework import generics
from rest_framwork import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from django.core.paginator import Paginator, EmptyPage
from rest_framework import viewsets

from reset_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, throttle_classes

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import Rating
from .serializers import RatingSerializer

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']

    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = [AnonRateThrottle, UserRateThrottle]
        return [throttle() for throttle in throttle_classes]

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    

@api_view(['GET'],['POST'])
def menu_items(request):
    if(request.method=='GET'):
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', defaults = 1)
        if category_name:
            items = items.filter(category__title = category_name)
        if to_price:
            items = items.filter(price = to_price)    
        if search:
            items = items.filter(title__contains=search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        paginator = Paginator.page(number=page)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []                   
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif request.method=='POST':
        serializerd_item = MenuItemSerializer(data=request.data)
        serializerd_item.is_valid(raise_exception=True)
        serializerd_item.save()
        return Response(serializerd_item.validated_data,status.HTTP_201_CREATED)
    
@api_view()
def single_item(request,id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)
    

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"secrets"})


@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response(request.user.email)

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Manager see this"})
    else:
        return Response({"message":"Not Auth"}, 403)
    

@api_view()
def throttle_check(request):
    return Response({"message":"successful"})


class RatingsView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if(self.request.method=='GET'):
            return []

        return [IsAuthenticated()]
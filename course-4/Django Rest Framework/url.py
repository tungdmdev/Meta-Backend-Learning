class Orders():
	@staticmethod
	@api_view()
	def listOrders(request):
	    return Response({'message':'list of orders'}, 200)
	
class BookView(APIView):
	def get(self, request, pk):
		return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
	def put(self, request, pk):
		return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
	
class BookView(viewsets.ViewSet):
	def list(self, request):
		return Response({"message":"All books"}, status.HTTP_200_OK)
	def create(self, request):
		return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
	def update(self, request, pk=None):
		return Response({"message":"Updating a book"}, status.HTTP_200_OK)
	def retrieve(self, request, pk=None):
		return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
	def partial_update(self, request, pk=None):
		return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
	def destroy(self, request, pk=None):
		return Response({"message":"Deleting a book"}, status.HTTP_200_OK)


from rest_framework.routers import SimpleRouter
router = SimpleRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
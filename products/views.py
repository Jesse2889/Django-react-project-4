# pylint: disable=no-member
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.status import HTTP_404_NOT_FOUND
from .models import Product
from .serializers import ProductSerializer 


class ProductListView(APIView): 

    def get(self, _request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data) 

class ProductDetailView(APIView):
    def get(self, _request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serialized_product = ProductSerializer(product)
            return Response(serialized_product.data)
        except product.DoesNotExist:
            return  Response({'message': 'Not Found'}, status=HTTP_404_NOT_FOUND)


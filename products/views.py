# pylint: disable=no-member
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_204_NO_CONTENT, HTTP_202_ACCEPTED
from .models import Product
from .serializers import ProductSerializer, BasketSerializer 


class ProductListView(APIView): 

    def get(self, _request):
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)

        return Response(serialized_products.data) 

class ProductDetailView(APIView):
    def get(self, _request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serialized_product = ProductSerializer(product)
            return Response(serialized_product.data)
        except product.DoesNotExist:
            return  Response({'message': 'Not Found'}, status=HTTP_404_NOT_FOUND)
def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            updated_product = ProductSerializer(product, data=request.data)
            if updated_product.is_valid():
                updated_product.save()
                return Response(updated_product.data, status=HTTP_202_ACCEPTED)
            return Response(updated_product.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)
        except Product.DoesNotExist:
            return  Response({'message': 'Not Found'}, status=HTTP_404_NOT_FOUND)

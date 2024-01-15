from django.shortcuts import render
from .models import Product,DestinationCharge,Order,ContactUs,ShoppingCart,HomePageVideo,Store,ProductVariation
from django.contrib.auth import get_user_model
from .serializers import (DestinationChargeSerializer,OrderSerializer,
        ContactUsSerializer,ShoppingCartSerializer,HomePageVideoSerializer,ProductVariationSerializer)
from django.db.models import Sum
from django.core.mail import EmailMultiAlternatives
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


User=get_user_model()


def home(request):
    return render(request,'index.html')




@api_view(['GET'])
def giveaway_api(request):
    if request.method=='GET':
        products=ProductVariation.objects.filter(in_stock=True,product__is_active=True).order_by('-updated')
        serializer=ProductVariationSerializer(products,many=True)
        return Response(serializer.data,content_type='application/json')


@api_view(['PUT','GET'])
def remove_from_cart(request):
    data=request.data
    if request.method == "PUT":
        item=ShoppingCart.objects.get(id=data['product_id'],shopper=data['email'],status='in-cart')
        prod=item.product
        refill=item.quantity
        product=ProductVariation.objects.get(id=prod.id)
        product.quantity=refill+product.quantity
        product.save(update_fields=['quantity'])
        item.delete()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def get_destination(request):
    data=request.data
    unordered_cart_items=ShoppingCart.objects.filter(shopper=data['email'],status='in-cart')
    amount=unordered_cart_items.aggregate(total=Sum('cost'))
    if request.method== 'PUT':
        destinations=DestinationCharge.objects.all()
        serializer=DestinationChargeSerializer(destinations,many=True)
        return Response({"areas":serializer.data,'amount':amount})


@api_view(['PUT'])
def update_cart_items(request):
    data=request.data
    if request.method == "PUT":
        product=ProductVariation.objects.get(id=data['product_id'])
        cart_data={
            "shopper":data['email'],
            "product":product,
            "quantity": int(data['quantity']),
            "cost": int(data['quantity'])*product.price
        }

        if product.in_stock and product.product.is_active:
            if int(data['quantity']) > product.quantity:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            ShoppingCart.objects.create(**cart_data)
            stock_balance=product.quantity - int(data['quantity'])
            product.quantity = stock_balance
            product.save(update_fields=['quantity'])
            return Response(status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_multi_cart_items(request):
    data=request.data
    if request.method == "PUT":
        product_quantity_pair= zip(data['product_id'],data['quantity'])

        for i,qty in product_quantity_pair:
            product=ProductVariation.objects.get(id=i)

            cart_data={
                "shopper":data['email'],
                "product":product,
                "quantity": qty,
                "cost": qty*product.price
            }

            if product.in_stock and product.product.is_active:
                if qty > product.quantity:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                ShoppingCart.objects.create(**cart_data)
                stock_balance=product.quantity - qty
                product.quantity = stock_balance
                product.save(update_fields=['quantity'])
        return Response(status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def display_cart_items(request):
    data=request.data

    if request.method == "PUT":
        unordered_cart_items=ShoppingCart.objects.filter(shopper=data['email'],status='in-cart')
        count=unordered_cart_items.aggregate(total=Sum('quantity'))
        serializer=ShoppingCartSerializer(unordered_cart_items,many=True)
        return Response({"products":serializer.data,"count":count})


@api_view(['POST'])
def initiate_payment(request):
    from .utility import remove
    data=request.data
    order_serializer=OrderSerializer(data=data)
    if order_serializer.is_valid():
        order_serializer.save()
        items=data['item'].split(',')
        products=remove(items)

        product_ids= []
        for prod,var in products:
            if var=='':
                var=None
            product_ids.append(ProductVariation.objects.get(product__description=prod,variant=var).id)

        ordered=ShoppingCart.objects.filter(shopper=data['ordered_by'],product__in=product_ids,status='in-cart')
        for j in ordered:
            store=Store.objects.get(variant=j.product.id)
            store.unit_sold+=j.quantity
            store.save(update_fields=['unit_sold'])
        ordered.update(status='ordered')
        return Response(status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def client_orders(request):
    from .utility import remove
    if request.method == 'PUT':
        data=request.data
        orders=Order.objects.filter(ordered_by=data['email']).order_by('-ordered_on')
        categories=[]
        for order in orders:
            items=order.item.split(',')
            products=remove(items)
            for prod,var in products:
                if var=='':
                    var=None
                category=ProductVariation.objects.get(product__description=prod,variant=var).product.category
                if category not in categories:
                    categories.append(category)
        products=ProductVariation.objects.filter(product__category__in=categories)
        product_serializer=ProductVariationSerializer(products,many=True)
        serializer=OrderSerializer(orders,many=True)

        return Response({"orders":serializer.data,"products":product_serializer.data})
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def contact_us(request):
    data=request.data
    serializer=ContactUsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def recently_added(request):
    recent = HomePageVideo.objects.all().order_by('-updated')
    cart=ShoppingCart.objects.filter(status='ordered').order_by('-quantity')[:6]
    cart_items=[i.product.id for i in cart]
    top_selling=ProductVariation.objects.filter(id__in=cart_items,product__is_active=True)
    sales=ProductVariation.objects.filter(product__on_sales=True,product__is_active=True,in_stock=True)
    all_products=ProductVariation.objects.filter(product__is_active=True,in_stock=True)
    all_products_serializer=ProductVariationSerializer(all_products,many=True)
    sales_serializer=ProductVariationSerializer(sales,many=True)
    top_selling_serializer=ProductVariationSerializer(top_selling,many=True)
    serializer=HomePageVideoSerializer(recent,many=True)
    return Response({'recent':serializer.data,'top':top_selling_serializer.data,'sales':sales_serializer.data,'all':all_products_serializer.data})








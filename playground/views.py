from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, DecimalField
from django.db.models.aggregates import Count, Max, Min
from django.db.models import Value, F, ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection


from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    # product = Product.objects.all() # Get all product
    # product = Product.objects.filter(pk=0).first()  # filter product and fetch only one that matches the pk
    # exist = Product.objects.filter(pk=0).exists()  # filter product and fetch only one that exist with the pk
    # exist = Product.objects.filter(unit_price__gt=1.0)  # GREATER THAN 20
    # exist = Product.objects.filter(unit_price__range=(20, 50))  # WITHIN THE RANGE
    # contains = Product.objects.filter(title__contains='m')  # That contains a letter base on case sensitive
    # contains = Product.objects.filter(title__icontains='Coffee')  # That contains a letter base on case insensitive
    # contains = Product.objects.filter(last_update__year=2021)  # Product that was update 2021
    # contains = Product.objects.filter(description__isnull=True)  # Product that id null
    # contains = Product.objects.filter(inventory__lt=10, unit_price__lt=20) # Product inventory < 10 AND unit_price < 20
    # contains = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20) # Product inventory < 10 AND unit_price < 20
    # contains = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20)) # Product inventory < 10 AND unit_price < 20 USING Q
    # contains = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20)) # Product inventory < 10 OR unit_price < 20 USING Q
    # contains = Product.objects.filter(unit_price__lt=10).order_by('title')  # Sorting Product ASCENDING
    # contains = Product.objects.filter(unit_price__lt=10).order_by('-title')  # Sorting Product DESCENDING
    # contains = Product.objects.filter(collection__id=1).order_by('unit_price')  # Filtering and Sorting Product
    # contains = Product.objects.earliest('unit_price')  # Filtering product and selecting the first index in DESCENDING
    # contains = Product.objects.latest('unit_price')  # Filtering product and selecting the first index in ASCENDING
    # contains = Product.objects.all()[:5]  # limiting record to 5
    # contains = Product.objects.all()[5:10]  # limiting record to 5 and skipping five
    # contains = Product.objects.all()[:5]  # limiting record to 5
    # contains = Product.objects.values('id', 'title')  # Getting values base on field
    # contains = Product.objects.values('id', 'title', 'collection__title')  # Getting values base on related_field, this return the result as dic
    # contains = Product.objects.values_list('id', 'title', 'collection__title')  # Getting values base on related_field, this return the result as tuple
    # contains = OrderItem.objects.values('product_id')  # Getting related (product_id) item from OrderItem which is from Product
    # contains = OrderItem.objects.values('product_id').distinct()  # Getting distinct related (product_id) item from OrderItem which is from Product
    # contains = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())  # Getting distinct id from OrderItem and fetching the whole product details from Product Table
    # contains = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')  # Getting distinct id from OrderItem and fetching the whole product details from Product Table and then order_by their title
    # contains = Product.objects.only('id', 'title')  # This only work when working with only one field to be rendered
    # contains = Product.objects.defer('id', 'title')  # Except the mentioned field: This only work when working with only one field to be rendered
    # contains = Product.objects.select_related('collection')  # Get data in table with a related_field that has only one related
    # contains = Product.objects.prefetch_related('promotions').select_related('collection')  # Get data in table with a related_field that has many related
    # contains = Order.objects.select_related('customer').order_by('-placed_at')[:5]  # Getting the latest five customers and order_descending order (base on  related_field)
    # contains = Order.objects.select_related('customer').prefetch_related('orderitem_set__product')  # Getting related customer together with product from Ordeitem based on (orderItem_set)
    # contains = Order.objects.aggregate(Count('id'))  # Counting objects.
    # contains = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))  # Count of product and Min unit_price.
    # contains = Product.objects.aggregate(count=Count('id'), min_price=Max('unit_price'))  # Count of product and Max unit_price.
    # contains = Product.objects.aggregate(count=Count('id'), min_price=Avg('unit_price'))  # Count of product and Average unit_price.
    # contains = Product.objects.annotate(isNew=Value(True))  # Annotate helps to add extra field to a query_set from DB. In this example, we appends isNew with help of Value function.
    # contains = Product.objects.annotate(new_id=F('id'))  # Annotate by referencing to related field

    # contains = Customer.objects.annotate(
    #     # CALLING CONCAT
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )  # Annotate by concatenation of two fields

    # contains = Customer.objects.annotate(
    #     # CALLING CONCAT
    #     order_count=Count('order')
    # )  # Annotate and Counting customer's order

    # # This help to reference field using F and also, its help to add discount with an output_field of Decimal
    # discount_price = ExpressionWrapper(
    #     F('unit_price' * 0.8), output_field=DecimalField()
    # )
    # contains = Product.objects.annotate(
    #     # CALLING discount_price
    #     discounted_price=discount_price
    # )  # Annotate and Counting customer's order

    # This help to reference field using Content-type base on Product
    # content_type = ContentType.objects.get_for_model(Product)
    # contains = TaggedItem.objects.select_related('tag').filter(
    #     content_type=content_type,
    #     object_id=1
    # )  # Annotate and Counting customer's order

    # Calling method for working with content_type
    # contains = TaggedItem.objects.get_tag_for(Product, 1)

    # # Creating object
    # contains = Collection()
    # contains.title = 'Basic Math'
    # contains.featured_product = Product(pk=1)
    # contains.save()

    # # Updating object 1
    # contains = Collection.objects.get(pk=12)
    # contains.featured_product = None
    # contains.save()

    # # Updating object 2
    # contains = Collection.objects.filter(pk=11).update(title='Learning')

    # # Deleting object 1
    # contains = Collection(pk=11)
    # contains.delete()

    # # Deleting object 2
    # contains = Collection.objects.filter(id__gt=5).delete()

    # # Transaction roleback using transaction.atomic for wrapping only needed part (1)
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()
    #
    #     order_item = OrderItem()
    #     order_item.order = order
    #     order_item.product_id = 1
    #     order_item.quantity = 10
    #     order_item.unit_price = 10
    #     order_item.save()

    # The second is to call @transacction.atomic() before declaring the function (2)

    # # Calling SQL PROCEDURE USING RAW SQL WITHOUT ORM
    # with connection.cursor() as cursor:
    #     cursor.callproc('get_customers', [1, 2, 'a'])

    # Fetching data from DB without ORM rather using RAW SQL
    queryset = Customer.objects.raw('SELECT * FROM store_customer')

    return render(request, 'hello.html', {'name': 'Abdulmutallib', 'product': queryset})
    # return render(request, 'hello.html', {'name': 'Abdulmutallib', 'product': list(contains)})

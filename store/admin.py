from django.contrib import admin, messages
from django.db.models import QuerySet
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from . import models


# Custom filer: For seeing low inventory
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),
            ('>10', 'Okay')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        if self.value() == '>10':
            return queryset.filter(inventory__gt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    # adding auto populated
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    lis_per_page = 10
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_select_related = ['collection']
    search_fields = ['title__istartswith']

    def collection_title(self, product):
        return product.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'

    # Method for clearing data from a db table field
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        data_updated = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{data_updated} product were updated successfully.',
            messages.SUCCESS
        )


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_product', 'products_count']
    lis_per_page = 10
    list_select_related = ['featured_product']
    search_fields = ['title__istartswith']

    # Getting the count of product collection
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
            'collection__id': str(collection.id)
        }))

        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name__istartswith']
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    lis_per_page = 10


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'unit_price', 'order', 'product']
    list_editable = ['unit_price']
    lis_per_page = 10

    def order(self, order):
        return order.placed_at

    def order(self, product):
        return product.title

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    list_display = ['id', 'placed_at', 'customer']
    lis_per_page = 10

@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'discount']
    list_editable = ['description']
    lis_per_page = 10


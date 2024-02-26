from django.contrib import admin
from .establishment_models import (
    Address,
    Establishment,
    Phone,
    Order,
    OrderItem,
)
from .product_models import (
    Available,
    Category,
    Product,
    # Subcategory,
    UnitMeasurement,
)


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = [
        "establishment_name",
        "establishment_legal_name",
        "establishment_cnpj",
        "establishment_description",
        "establishment_address_pk",
        "establishment_phone_pk",
    ]
    search_fields = [
        "establishment_name",
    ]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "address_street",
        "address_neighborhood",
        "address_number",
        "address_city",
        "address_state",
        "address_postal_code",
        "address_latitude",
        "address_longitude",
        "address_created_at",
    ]
    search_fields = [
        "address_street",
        "address_neighborhood",
        "address_postal_code",
        "address_city",
    ]


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


# class SubcategoryInline(admin.TabularInline):
#     model = Subcategory
#     extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "category_name",
    ]
    search_fields = [
        "category_name",
    ]
    inlines = [
        ProductInline,
        # SubcategoryInline,
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "product_name",
        "product_price",
        "product_code",
        "product_available_pk",
        "product_category_pk",
        "product_unitMeasurement",
    ]
    search_fields = [
        "product_name",
        "product_code",
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_user_pk",
        "order_establishment_pk",
        # "order_items_pk",
        "order_total_price",
        "order_created_at",
        "order_is_paid",
    ]
    search_fields = [
        "order_items_pk",
        "order_user_pk",
    ]

class Order_ItemAdmin(admin.ModelAdmin):
    list_display = [
        "order_item_pk",
        "order_item_product_pk",
        "order_item_quantity",
    ]
    search_fields = [
        "order_item_pk",
    ]
    inlines = [
        ProductInline,
    ]

admin.site.register(Establishment, EstablishmentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Available)
admin.site.register(UnitMeasurement)
admin.site.register(Phone)
admin.site.register(Address, AddressAdmin)
# admin.site.register(Subcategory)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)

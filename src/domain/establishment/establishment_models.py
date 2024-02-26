from django.db import models
from django.contrib.auth.models import User
from .product_models import Product


class Address(models.Model):
    address_street = models.CharField(
        max_length=255,
        verbose_name="Rua",
    )
    address_neighborhood = models.CharField(
        max_length=255,
        verbose_name="Bairro",
    )
    address_number = models.CharField(
        max_length=15,
        verbose_name="Número",
    )
    address_city = models.CharField(
        max_length=255,
        verbose_name="Cidade",
    )
    address_state = models.CharField(
        max_length=127,
        verbose_name="Estado",
    )
    address_postal_code = models.CharField(
        max_length=8,
        verbose_name="CEP",
    )
    address_latitude = models.CharField(
        max_length=15,
        verbose_name="Latitude",
    )
    address_longitude = models.CharField(
        max_length=15,
        verbose_name="Longitude",
    )
    address_created_at = models.DateTimeField(
        verbose_name="Data de Criação",
    )

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.address_neighborhood}"


class Phone(models.Model):
    phone_ddd = models.CharField(
        max_length=3,
        verbose_name="DDD",
    )
    phone_number = models.CharField(
        max_length=9,
        verbose_name="Telefone",
    )

    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"

    def __str__(self):
        return f"({self.phone_ddd}) {self.phone_number}"


class Establishment(models.Model):
    establishment_name = models.CharField(
        max_length=45,
        verbose_name="Nome",
    )
    establishment_legal_name = models.CharField(
        max_length=45,
        verbose_name="Razão Social",
    )
    establishment_cnpj = models.CharField(
        max_length=14,
        verbose_name="CNPJ",
        unique=True,
    )
    establishment_description = models.CharField(
        max_length=255,
        verbose_name="Descrição do Estabelecimento",
    )
    establishment_address_pk = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name="Endereço",
    )
    establishment_phone_pk = models.ForeignKey(
        Phone,
        on_delete=models.CASCADE,
        verbose_name="Telefone",
    )

    class Meta:
        verbose_name = "Estabelecimento"
        verbose_name_plural = "Estabelecimentos"

    def __str__(self):
        return f"{self.establishment_cnpj}"


class Order(models.Model):
    order_user_pk = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Consumidor",
    )
    order_establishment_pk = models.ForeignKey(
        Establishment,
        on_delete=models.CASCADE,
        verbose_name="Estabelecimento",
    )
    order_items_pk = models.ManyToManyField(
        Product,
        through="OrderItem",
    )
    order_total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor Total",
    )
    order_created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data do Pedido",
    )
    order_is_paid = models.BooleanField(
        default=False,
        verbose_name="Pagamento",
    )

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"{self.order_establishment.establishment_name}"

class OrderItem(models.Model):
    order_item_pk = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Item",
    )
    order_item_product_pk = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Produto",
    )
    order_item_quantity = models.PositiveIntegerField(
        verbose_name="Quantidade",
    )

    def subtotal(self):
        return self.order_item_product.product_price * self.order_item_quantity

    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"

    def __str__(self):
        return f"{self.order_item_product}"


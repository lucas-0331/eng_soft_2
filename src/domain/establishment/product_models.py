from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=255,
        verbose_name="Categoria",
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f"{self.category_name}"


# class Subcategory(models.Model):
#     subcategory_name = models.CharField(
#         max_length=255,
#         verbose_name="Subcategoria",
#     )
#     subcategory_category_pk = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         verbose_name="Categoria",
#     )

#     class Meta:
#         verbose_name = "Subcategoria"
#         verbose_name_plural = "Subcategorias"

#     def __str__(self):
#         return f"{self.subcategory_name}"


class UnitMeasurement(models.Model):
    UnitMeasurement_type = models.CharField(
        max_length=8,
        verbose_name="Tipo de Unidade de Medida",
    )

    class Meta:
        verbose_name = ("Unidade de Medida",)
        verbose_name_plural = "Unidade de Medida"

    def __str__(self):
        return f"{self.UnitMeasurement_type}"


class Available(models.Model):
    available_name = models.CharField(
        max_length=255,
        verbose_name="Disponibilidade/Validade",
    )

    class Meta:
        verbose_name = "Disponibilidade"
        verbose_name_plural = "Disponibilidades"

    def __str__(self):
        return f"{self.available_name}"


class Product(models.Model):
    product_name = models.CharField(
        max_length=255,
        verbose_name="Produto",
    )
    product_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Valor",
    )
    product_code = models.CharField(
        max_length=255,
        verbose_name="Código",
    )
    product_available_pk = models.ForeignKey(
        Available,
        on_delete=models.CASCADE,
        verbose_name="Disponibilidade",
    )
    product_category_pk = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Categoria",
    )
    product_UnitMeasurement = models.ForeignKey(
        UnitMeasurement,
        on_delete=models.CASCADE,
        verbose_name="Unidade de Medida",
    )

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.product_name}"

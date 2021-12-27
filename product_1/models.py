from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product_in(models.Model):
    class Meta:
        verbose_name = 'продукт Ин'
        verbose_name_plural = 'продукты Ин'

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    data_created = models.DateField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order_in(models.Model):
    STATUS = (
        ('Оброватыются', 'Оброватыются'),
        ('Выехал', 'Выехал'),
        ('Доставлено', 'Доставлено')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='customer_in_order')
    product = models.ForeignKey(Product_in, on_delete=models.CASCADE,
                                related_name='product_in_order')
    data_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200,
                              choices=STATUS, default='Обробатывается')

    def __str__(self):
        return self.product.name

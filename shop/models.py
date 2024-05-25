from django.db import models




class ProductSet(models.Model):
    class SetType(models.TextChoices):
        VIP = 'vip', 'Vip'
        STANDART = 'standart', 'Standart'
        MINI = 'mini', 'Mini'
    product = models.ManyToManyField('shop.Product')
    type = models.CharField(max_length=55, choices=SetType.choices)
    discount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self) -> str:
        return f"{self.id}-{self.product}"


class PromoCode(models.Model):
    is_active = models.BooleanField(default=True)
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=55)

    def __str__(self) -> str:
        return f"{self.id}-{self.code}"
    


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'new', 'New'
        IN_PROGRESS = 'in_progress', 'In progress'
        DONE = 'done', 'Done'

    class DeliveryMethod(models.TextChoices):
        PICKUP = 'pickup', 'Pickup'
        DELIVERY = 'delivery', 'Delivery'

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=55)
    email = models.EmailField(null=True, blank=True)
    connect_type = models.CharField(max_length=55)
    comment = models.TextField(null=True, blank=True)
    delivery_method = models.CharField(max_length=55, choices=DeliveryMethod.choices)
    payment_method = models.CharField(max_length=55)
    promocode = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=55, choices=OrderStatus.choices, default=OrderStatus.NEW)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.id}-{self.full_name}"
    


class ProductInCart(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    product_color = models.ForeignKey('shop.ProductColor', on_delete=models.CASCADE)
    product_size = models.ForeignKey('shop.ProductSize', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey('shop.Order', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.id}-{self.product}"
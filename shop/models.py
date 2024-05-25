from django.db import models

class ProductImages(models.Model):
    product = models.ForeignKey(' ', on_delete=models.PROTECT)
    color = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='ProductImage')
    image_2 = models.ImageField(upload_to='ProductImage')
    image_3 = models.ImageField(upload_to='ProductImage')
    add_price = models.DecimalField(max_digits=10, decimal_places=10)

class ProductMemory(models.Model):
    product = models.ForeignKey('', on_delete=models.PROTECT)
    add_price = models.DecimalField(max_digits=10, decimal_places=10)
    memory  = models.CharField(max_length=100)

class Repair(models.Model):
    title = models.CharField(max_length=100)
    min_price = models.DecimalField(max_digits=10, decimal_places=10)
    repair_time = models.CharField(max_length=100)
    product = models.ForeignKey(' ', on_delete=models.PROTECT)


class RepairAppliction(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    repair = models.ForeignKey(Repair, on_delete=models.PROTECT)

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
class FAQ(models.Model):

    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=150)

class Email_account(models.Model):

    email = models.EmailField()

    def __str__(self) -> str:
        return self.email


class Category(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='CategoryImage/')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category)
    guarentee = models.CharField(max_length=50)
    support_time = models.CharField(max_length=50)
    pickup = models.CharField(max_length=100)
    available = models.BooleanField()
    delivery_time = models.CharField(max_length=50)
    delivery_cost = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


from django.db import models

class Repair(models.Model):
    title = models.CharField(max_length=100)
    min_price = models.DecimalField(max_digits=10, decimal_places=2,  null=True)
    repair_time = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey("shop.Category", on_delete=models.PROTECT)
    guarantee = models.CharField(max_length=50)
    support_time = models.CharField(max_length=50)
    pickup = models.CharField(max_length=100)
    available = models.BooleanField()
    delivery_time = models.CharField(max_length=50)
    delivery_cost = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    repair = models.ForeignKey(Repair, on_delete=models.PROTECT, null=True )

    def __str__(self) -> str:
        return self.name
    


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product_images")
    color = models.CharField(max_length=100)
    image_1 = models.ImageField(upload_to='products/')
    image_2 = models.ImageField(upload_to='products/')
    image_3 = models.ImageField(upload_to='products/')
    add_price = models.DecimalField(max_digits=10, decimal_places=2)


class ProductMemory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_memories')
    add_price = models.DecimalField(max_digits=10, decimal_places=2)
    memory = models.CharField(max_length=100)





class RepairApplication(models.Model):
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
    product_color = models.ForeignKey(ProductImages, on_delete=models.CASCADE)
    product_size = models.ForeignKey(ProductMemory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey('shop.Order', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.id}-{self.product}"


class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self) -> str:
        return f"{self.id}-{self.question}"


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


class ContactApplication(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id}-{self.full_name}"


class Discount(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()
    image = models.ImageField(upload_to='discount/')
    link = models.URLField()

    def __str__(self):
        return f"{self.id}-{self.title}"


class Client(models.Model):
    class ClientChoices(models.TextChoices):
        STARS = 'stars', 'Stars'
        COMPANY = 'company', "Company"

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='discount')
    type = models.CharField(max_length=50, choices=ClientChoices.choices, default=ClientChoices.STARS)

    def __str__(self):
        return f"{self.id}-{self.name}"



class Statiy(models.Model):
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='discount')

    def __str__(self):
        return f"{self.id}-{self.title}"
    


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_colors')
    add_price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.product.name



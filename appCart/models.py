from django.db import models
from appProduct.models import Product
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed


# Create your models here.
STATUS = [
    ('payment_waiting', 'Ödeme Bekliyor'),
    ('buyed', 'Ödeme Tamamlandı'),
    ('deleted', 'Silindi'),
]

class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    price = models.FloatField(("Fiyat"),default=0)
    is_delete = models.BooleanField(("Silindi"), default=False)
    created_date = models.DateTimeField(("Oluşturma"), auto_now_add=True)
    updated_date = models.DateTimeField(("Güncelleme"), auto_now=True)

    def __str__(self) :
        return f"{self.product.title } - price : {self.price} TL"

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, verbose_name=("Müşteri"), null=True, blank=True, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, blank=True, null= True)
    items = models.ManyToManyField(ShoppingCartItem, blank=True)
    total_price = models.FloatField(("Toplam Ücret"), default=0)
    status = models.CharField(default="payment_waiting", choices=STATUS, max_length=20)
    created_date = models.DateTimeField(("Oluşturma"), auto_now_add=True)
    updated_date = models.DateTimeField(("Güncelleme"), auto_now=True)

    class Meta:
        verbose_name = "Alışveriş Sepetleri"
        verbose_name_plural = "Alışveriş Sepeti"

    def __str__(self) :
        return f"PK: {self.pk} - Toplam: {self.total_price} - Durum: {self.status}"
    
    def total_price_update(self):
        if self.status == "payment_waiting":
            total_price = 0
            for item in self.items.all():       #* selfin için items ın içindeki herşey (sepetteki ürün ürünler)
                if item.is_delete == False:
                    total_price += item.price
            self.total_price = total_price
            self.save()  


#* Sepete ürün atılıp kaydet dediğimizde sepet içindeki ürünün fiyatı ürünün kendi fiyatına eşitliyor.

@receiver(post_save, sender=ShoppingCartItem)
def shopping_card_item_receiver(sender, instance, created, *args, **kwargs):
    if created:
        instance.price = instance.product.price
        instance.save()
        
    instance.shoppingcart_set.first().total_price_update()
    print(sender)
    print(kwargs)
    print(f"{'x'*30}\nShoppingCartItem\n{'x'*30}")
    print(instance.shoppingcart_set.first().total_price)


#* shoppingcart içindeki items değiştiğinde
@receiver(m2m_changed, sender=ShoppingCart.items.through)    
def shopping_card_receiver(sender, instance, *args, **kwargs):
    instance.total_price_update()
    print(args)
    print(kwargs)
    print(f"{'x'*30}\nShoppingCart\n{'x'*30}")

from django.core.mail import send_mail
from django.db import models

from apps.shop.models import Product


# Create your models here.
class Order(models.Model):
    name = models.CharField(verbose_name="Customer Name", max_length=150)
    email = models.CharField(verbose_name="Customer Email", max_length=150)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(
        Product, related_name="order_item", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id}"

    def send_email(self):
        subject = "Order on Akun.dev"
        message = f"Dear {self.name}!\n\nThank you for ordering {self.product}.\nWe will contact you shortly!\n\nBest regards,\nAlmaz Kunpeissov"
        from_email = "hello@akun.dev"
        recipient_list = [self.email, "hello@akun.dev"]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=True,
        )

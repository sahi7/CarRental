from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('standard', 'Standard'),
        ('standard_plus', 'Standard Plus'),
        ('premium', 'Premium'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='client')
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()  # Duration of the subscription plan in months

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    payment_status = models.BooleanField(default=False)
    
    # Additional fields for payment method.
    payment_method = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    def renew_subscription(self):
        # Logic to renew subscription
        pass

    def __str__(self):
        return f"{self.user.username}'s {self.plan.name} Subscription"
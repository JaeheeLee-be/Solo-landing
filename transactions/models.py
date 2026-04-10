from django.db import models

from accounts.models import Account


class Transaction(models.Model):

    class TransactionType(models.TextChoices):
        DEPOSIT = 'deposit', '입금'
        WITHDRAWAL = 'withdrawal', '출금'

    class Category(models.TextChoices):
        FOOD = 'food', '식비'
        TRANSPORT = 'transport', '교통'
        SHOPPING = 'shopping', '쇼핑'
        CULTURE = 'culture', '문화'
        ETC = 'etc', '기타'

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    transaction_type = models.CharField(
        max_length=20,
        choices=TransactionType.choices
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    balance_after = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=200, blank=True)
    transacted_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transactions'
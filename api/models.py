from django.db import models


class Asset(models.Model):
    contract_address = models.CharField(max_length=50, null=False)
    token_id = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=50, null=True)
    decimals = models.IntegerField(null=True)
    thumbnail_url = models.URLField(null=True)
    animation_url = models.URLField(null=True)
    name = models.CharField(max_length=50, null=True)
    contract_name = models.CharField(max_length=50, null=True)
    symbol = models.CharField(max_length=50, null=True)
    is_verified = models.BooleanField(null=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("contract_address", "token_id")

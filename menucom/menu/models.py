from django.db import models

# CATEGORYの定義を追加
CATEGORY = [
    ('recommendation', 'おすすめ'),
    ('skewer', '串焼き'),
    ('onedish', '一品'),
    ('specialty', '名物'),
    ('friedfood', '揚げ物'),
    ('rice', 'ご飯'),
    ('dessert', 'デザート'),
    ('drink', 'ドリンク'),
]

class Menu(models.Model):
    tagline = models.CharField(max_length=100)
    menu = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )


from django.db import models

TYPE_CHOICES= {
    ('G','Граммы'),
    ('L','Литры'),
}
class GoodItem(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя продукта')
    created_at = models.DateTimeField(verbose_name='Дата поступления')
    price = models.DecimalField(verbose_name='Цена продукта', max_digits=8, decimal_places=2, default=0)
    units_of_measurement = models.CharField(max_length=40, verbose_name='Ед.измерения',choices=TYPE_CHOICES)
    vendor = models.CharField(max_length=128, verbose_name='Поставщик')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточка товара'

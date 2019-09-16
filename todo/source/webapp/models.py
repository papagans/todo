from django.db import models


status_choices = (
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')
)


class Todo(models.Model):
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name='Description')
    status = models.CharField(max_length=20, default=status_choices[0][0], verbose_name='Status', choices=status_choices)
    date = models.DateField(max_length=10, null=True, blank=False, verbose_name='Date')
    details = models.TextField(max_length=400, null=True, blank=False, verbose_name='Details')

    def __str__(self):
        return self.description

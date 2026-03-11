from django.db import models


class Todo(models.Model):

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    is_done = models.BooleanField(default=False)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    due_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)


class Category(models.Model):

    title = models.CharField(
        max_length=155,
        verbose_name="Название"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Type(models.Model):

    title = models.CharField(
        max_length=155,
        verbose_name="Название"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="types"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Articles(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


class Comments(MPTTModel):
    content = models.TextField("Текст комментария")

    article = models.ForeignKey(
        Articles,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="comment",
        verbose_name="Статья",

    )
    time_create = models.DateTimeField("Время создания комментария", auto_now_add=True)

    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class Meta:
        ordering = ("time_create",)

    class MPTTMeta:
        order_insertion_by = ['article']

    def __str__(self) -> str:
        return self.content

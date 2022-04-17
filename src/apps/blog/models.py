from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.CharField("Автор комментария", max_length=255)
    content = models.TextField("Текст комментария")
    id_kor = models.PositiveIntegerField("ID референта", default=0)
    level = models.PositiveIntegerField(
        "Уровень вложенности", blank=True, default=0
    )
    post = models.ForeignKey(
        Posts,
        on_delete=models.PROTECT,
        related_name="comment",
        verbose_name="Статья",
    )
    time_create = models.DateTimeField(
        "Время создания комментария", auto_now_add=True
    )

    class Meta:
        ordering = ("time_create",)

    def __str__(self) -> str:
        return f"Comment by {self.author} on {self.post} on {self.id_kor}"

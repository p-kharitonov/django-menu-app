from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=64, verbose_name="Name")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name="Name")
    url = models.CharField(max_length=127, verbose_name="URL")
    position = models.PositiveSmallIntegerField(default=0, verbose_name="Position")
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Parent Item")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("position",)
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

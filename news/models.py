from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    CATEGORY = (("0", "Politics"),("1", "Sports"),("2", "International"),("3","Entertainment"),("4", "Local News"),("5", "Valley News"))
    title = models.CharField(max_length=250)
    story = models.TextField(verbose_name='article')
    category = models.CharField(choices=CATEGORY, max_length=2)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(default=0)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    cover_image = models.ImageField(upload_to='uploads')
    class Meta:
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return reverse("detail_news", kwargs={"category": self.get_category_display().lower(),"pk": self.pk})

        

    def __str__(self):
        return self.title


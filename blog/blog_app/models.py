from django.db import models

# Create your models here.
class add_blog(models.Model):
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    catogery = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    post_body = models.TextField(blank=False, null=False)
    date_pub = models.DateField(auto_now=False)

    def __str__(self):
        return self.title



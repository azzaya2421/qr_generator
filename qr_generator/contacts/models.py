from django.db import models

class Contact(models.Model):
    image = models.ImageField(upload_to='contact_images', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    company_address = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qrcode', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

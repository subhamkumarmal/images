from django.db import models

# Create your models here.
class StudentsDeails(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    phone=models.CharField(max_length=11)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    img_filed=models.ImageField(upload_to='upload/images')

    def __str__(self):
        return self.name

    class Meta:
        db_table='studentdetial'



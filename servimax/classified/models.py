from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)


    class Meta:
        abstract = True


class Worker(User):
    type = models.CharField(max_length=20)
    hourly_rate = models.FloatField()

    def __str__(self):
        return self.first_name + ': ' + self.type

class Employer(User):
    def __str__(self):
        return self.first_name + ': Employer'
    
class Contract(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    rate = models.FloatField()

from django.db import models

class Client(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Lawyer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Case(models.Models):
    STATUS_CHOICES=(
        ('OPEN','Open'),
        ('CLOSED','Closed'),
        ('PENDING','Pending'),
    )

    title=models.CharField(max_length=200)
    description=models.TextField()
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='OPEN')
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    lawyer=models.ForeignKey(Lawyer,on_delete=models.CASCADE)
    created_on=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
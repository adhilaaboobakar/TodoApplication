from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    options=(
        ("pending","pending"),
        ("completed","completed"),
        ("In progress","In progress")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")
    created_date=models.DateField(auto_now_add=True,blank=True)


    def __str__(self):
        return self.title
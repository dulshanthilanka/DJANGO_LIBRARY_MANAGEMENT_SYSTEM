from django.db import models

# Create your models here.
class userdetails(models.Model):
    user_name = models.CharField(max_length=200)
    user_id = models.IntegerField()
    user_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_name} - {self.user_id}"


class bookdtails(models.Model):
    user = models.OneToOneField(userdetails, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    book_id = models.IntegerField()
    book_availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book_name} - {self.book_id}"
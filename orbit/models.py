from django.db import models

class About(models.Model):
    title=models.CharField(max_length=202)
    image=models.FileField(upload_to='about/')
    description=models.TextField()
    python=models.IntegerField()
    telegram=models.IntegerField()
    back_end=models.IntegerField()
    front_end=models.IntegerField()
    web_site=models.IntegerField()

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(max_length=202)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title=models.CharField(max_length=202)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="portfolio")
    image=models.FileField(upload_to='portfolio/')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    title=models.CharField(max_length=202)
    body=models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    job=models.CharField(max_length=202)
    company=models.CharField(max_length=202)
    location=models.CharField(max_length=202)
    time=models.CharField(max_length=202)
    date=models.CharField(max_length=202)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job

class Education(models.Model):
    akademy=models.CharField(max_length=202)
    title=models.CharField(max_length=202)
    location=models.CharField(max_length=202)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HappyClients(models.Model):
    full_name=models.CharField(max_length=202)
    job=models.CharField(max_length=202)
    image=models.FileField(upload_to='client/')
    body=models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name





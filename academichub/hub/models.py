from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    branches = models.ManyToManyField(Branch)

    def __str__(self):
        return self.name


# Category (Assignments, PPTs, Notes, etc.)
class FileCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class File(models.Model):

    title = models.CharField(max_length=200)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    category = models.ForeignKey(FileCategory, on_delete=models.CASCADE)

    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
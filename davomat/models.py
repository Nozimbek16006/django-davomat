from django.db import models
import uuid

class Dates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    course = models.ForeignKey('Courses', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.date)

class Courses(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)

        def __str__(self):
            return self.name

class Students(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    course = models.ForeignKey('Courses', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey('Students', on_delete=models.PROTECT)
    date = models.ForeignKey('Dates', on_delete=models.PROTECT)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name
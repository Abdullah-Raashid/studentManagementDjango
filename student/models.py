from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
# Create your models here.


class Club(models.Model):
    """Extra-curricular club that students may join (demonstrates Many-To-Many)."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class StudentManager(models.Manager):
    """Custom manager adding helper querysets."""

    def with_parent(self):
        """Return students with parent data pre-fetched (ORM optimisation)."""
        return self.select_related("parent")

    def search(self, term: str):
        """Case-insensitive search by first or last name."""
        return self.filter(models.Q(first_name__icontains=term) | models.Q(last_name__icontains=term))


class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.EmailField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='students/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    clubs = models.ManyToManyField(Club, blank=True, related_name="members")
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    # attach custom manager
    objects = StudentManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
        super(Student, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
import pytest
from student.models import Parent, Student
from django.utils import timezone

@pytest.mark.django_db
def test_student_str():
    parent = Parent.objects.create(
        father_name="Dad", father_mobile="08000000000", father_email="dad@example.com",
        mother_name="Mom", mother_mobile="07000000000", mother_email="mom@example.com",
        present_address="A St", permanent_address="B St"
    )
    student = Student.objects.create(
        first_name="John", last_name="Doe", student_id="S1", gender="Male",
        date_of_birth="2010-01-01", student_class="1A", religion="None",
        joining_date=timezone.now().date(), mobile_number="08011111111",
        admission_number="ADM1", section="A", parent=parent
    )
    assert str(student) == "John Doe (S1)" 
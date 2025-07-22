from django.core.management.base import BaseCommand
from django.utils import timezone
from student.models import Student, Parent
import random
import datetime
from student.models import Club

FIRST_NAMES = ["John", "Jane", "Michael", "Emily", "Chris", "Sarah", "Daniel", "Laura", "David", "Emma"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]
CLASSES = ["1A", "1B", "2A", "2B", "3A", "3B"]
GENDERS = ["Male", "Female", "Others"]
SECTIONS = ["A", "B", "C"]
CLUBS = ["Chess", "Basketball", "Music", "Drama", "Robotics", "Debate"]


class Command(BaseCommand):
    help = "Seed the database with sample students and parents"

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=30, help="Number of students to create (default 30)")

    def handle(self, *args, **options):
        count = options["count"]
        created = 0
        # ensure clubs exist
        club_objs = []
        for cname in CLUBS:
            club_objs.append(Club.objects.get_or_create(name=cname)[0])

        for i in range(count):
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            student_id = f"S{random.randint(1000,9999)}"
            gender = random.choice(GENDERS)
            dob = datetime.date(2010, 1, 1) + datetime.timedelta(days=random.randint(0, 365 * 8))
            student_class = random.choice(CLASSES)
            religion = random.choice(["Christianity", "Islam", "Hinduism", "Buddhism"])
            joining_date = timezone.now().date() - datetime.timedelta(days=random.randint(0, 365))
            mobile = f"080{random.randint(10000000, 99999999)}"
            admission_number = f"ADM{random.randint(100,999)}"
            section = random.choice(SECTIONS)

            parent = Parent.objects.create(
                father_name=f"Father {last}",
                father_occupation="Engineer",
                father_mobile=f"081{random.randint(10000000, 99999999)}",
                father_email=f"father{student_id.lower()}@mail.com",
                mother_name=f"Mother {last}",
                mother_occupation="Teacher",
                mother_mobile=f"070{random.randint(10000000, 99999999)}",
                mother_email=f"mother{student_id.lower()}@mail.com",
                present_address="123 Demo Street",
                permanent_address="123 Demo Street",
            )

            student = Student.objects.create(
                first_name=first,
                last_name=last,
                student_id=student_id,
                gender=gender,
                date_of_birth=dob,
                student_class=student_class,
                religion=religion,
                joining_date=joining_date,
                mobile_number=mobile,
                admission_number=admission_number,
                section=section,
                parent=parent,
            )
            # assign 0-3 random clubs
            student.clubs.set(random.sample(club_objs, k=random.randint(0,3)))
            created += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully created {created} students.")) 
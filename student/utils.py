import typing

from student.models import Student

CSV_HEADER = "first_name,last_name,student_id,gender,student_class,section\n"


def iter_students_csv(queryset: typing.Iterable[Student]):
    """Yield CSV rows for the given queryset using a generator for memory-efficient streaming."""
    yield CSV_HEADER
    for s in queryset.iterator():
        yield f"{s.first_name},{s.last_name},{s.student_id},{s.gender},{s.student_class},{s.section}\n" 
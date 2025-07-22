import graphene
from graphene_django import DjangoObjectType
from .models import Student

class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "student_id", "student_class")

class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)

    def resolve_all_students(root, info):
        return Student.objects.all()

schema = graphene.Schema(query=Query) 
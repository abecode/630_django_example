from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    courses = models.ManyToManyField(
        'Course',
        through = 'Enrollment',
        through_fields = ('student', 'course')
    )



#class Professor(Person):
class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ADJUNCT = 'ADJ'
    CLINICAL = 'CLI'
    ASSISTANT = 'AST'
    ASSOCIATE = 'ASO'
    FULL = 'FUL'
    VISITING = 'VIS'
    PROF_LEVEL_CHOICES = [
        (ADJUNCT, 'Adjunct'),
        (CLINICAL, 'Clinical'),
        (ASSISTANT, 'Assistant'),
        (ASSOCIATE, 'Associate'),
        (FULL, 'Full'),
        (VISITING, 'Visiting')
    ]
    prof_level = models.CharField(
        max_length=3,
        choices=PROF_LEVEL_CHOICES,
        default=ADJUNCT,
    )

class Course(models.Model):
    JTERM = '10'
    SPRING = '20'
    SUMMER = '30'
    FALL = '40'

    term = models.CharField(
        max_length=2,
        choices=[(JTERM, 'jterm'),
                 (SPRING, 'spring'),
                 (SUMMER, 'summer'),
                 (FALL, 'fall')]
    )
    dept_code = models.CharField(
        max_length = 4,
        default="SEIS"
    )
    course_number = models.IntegerField(
        validators=[
            MinValueValidator(100),
            MaxValueValidator(1000)
        ]
    )
    course_year = models.IntegerField(
        validators=[
            MinValueValidator(1880)
        ]
    )
    section_number = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    professor = models.ForeignKey(Professor, on_delete=models.DO_NOTHING)
        
    students = models.ManyToManyField(
        'Student',
        through = 'Enrollment',
        through_fields = ('course', 'student')
    )
class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.DO_NOTHING)
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING)
    grade = models.CharField(max_length=2)

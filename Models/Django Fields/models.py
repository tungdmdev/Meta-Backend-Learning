from django.db import models  
class Person(models.Model): 
    first_name = models.CharField(max_length=20) 
    last_name = models.CharField(max_length=20) 

class Person(models.Model): 
    name = models.CharField(max_length=50) 
    address = models.CharField(max_length=80, default='Mumbai') 
    tax_code = models.CharField( 
                    max_length = 20,   
                    unique = True 
                    ) 
    
SEMESTER_CHOICES = ( 
    ("1", "Civil"), 
    ("2", "Electrical"), 
    ("3", "Mechanical"), 
    ("4", "CompSci"), 
) 
 
# declaring a Student Model 

class Student(models.Model): 
      semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = '1' 
        )
      
class Student(Model): 
    grade = models.DecimalField( 
                         max_digits = 5, 
                         decimal_places = 2)
    
class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 

class Artist(models.Model): 
    name = models.CharField(max_length=10) 

class Album(models.Model): 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) 

class Song(models.Model): 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) 
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)


class college(Model): 
    CollegeID = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    strength = models.IntegerField() 
    website=models.URLField() 

class Principal(models.Model): 
    CollegeID = models.OneToOneField( 
                College, 
                on_delete=models.CASCADE 
                ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50)

class Teacher(models.Model): 
    TeacherID = models.ItegerField(primary_key=True) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 

class Subject(models.Model): 
    Subjectcode = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=30) 
    credits = model.IntegerField() 
    teacher = model.ManyToManyField(Teacher) 
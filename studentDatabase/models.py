from django.db import models

#most rows in tables are made with least amount of restriction
#and mostly using charfield
#have one to many (foreignkey relation) to both father and mother (parent)
class Student (models.Model):

    student_name = models.CharField(max_length=100)
    student_school_number = models.CharField(max_length=8, primary_key=True)
    student_identification_certificate_number = models.CharField(max_length=50)
    student_class = models.CharField(max_length=3)
    student_homeroom = models.CharField(max_length=50)
    student_phone_number = models.CharField(max_length=50)
    student_sibling_number = models.IntegerField()
    student_sibling_total = models.IntegerField()
    #
    MALAY = "MALAY"
    CHINESE = "CHINESE"
    INDIAN = "INDIAN"
    OTHERS = "OTHERS"
    STUDENT_NATIONALITY_CHOICES = (
        (MALAY, 'MALAY'),
        (CHINESE, 'CHINESE'),
        (INDIAN, 'INDIAN'),
        (OTHERS, 'OTHERS'),
    )
    student_nationality = models.CharField(
        max_length=50,
        choices=STUDENT_NATIONALITY_CHOICES,
        default=MALAY,
    )
    #
    student_date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    #
    MALE = "MALE"
    FEMALE = "FEMALE"
    STUDENT_GENDER_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
    )
    student_gender = models.CharField(max_length=6, choices=STUDENT_GENDER_CHOICES)
    #
    MUSLIM = "MUSLIM"
    BUDDHIST = "BUDDHIST"
    CHRISTIAN = "CHRISTIAN"
    ATHEIST = "ATHEIST"
    STUDENT_RELIGION_CHOICES = (
        (MUSLIM, 'MUSLIM'),
        (BUDDHIST, 'BUDDHIST'),
        (CHRISTIAN, 'CHRISTIAN'),
        (ATHEIST, 'ATHEIST'),
    )
    student_religion = models.CharField(max_length=50, choices=STUDENT_RELIGION_CHOICES)
    #
    student_mother = models.ForeignKey("StudentMother", on_delete=models.CASCADE)
    student_father = models.ForeignKey("StudentFather", on_delete=models.CASCADE)
    #
    #image upload still WIP
    def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.student_school_number, filename)
    student_photo = models.ImageField(upload_to=user_directory_path, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.student_name


class StudentMother(models.Model):

    mother_name = models.CharField(max_length=50)
    mother_income = models.IntegerField()
    mother_phone_number = models.CharField(max_length=50)
    #
    MARRIED = "MARRIED"
    DIVORCED = "DIVORCED"
    MOTHER_MARITAL_STATUS_CHOICES = (
        (MARRIED, 'MARRIED'),
        (DIVORCED, 'DIVORCED'),
    )
    mother_marital_status = models.CharField(max_length=50, choices=MOTHER_MARITAL_STATUS_CHOICES, default=MARRIED)


    def __str__(self):
        return self.mother_name


class StudentFather(models.Model):

    father_name = models.CharField(max_length=50)
    father_income = models.IntegerField()
    father_phone_number = models.CharField(max_length=50)
    #
    MARRIED = "MARRIED"
    DIVORCED = "DIVORCED"
    FATHER_MARITAL_STATUS_CHOICES = (
        (MARRIED, 'MARRIED'),
        (DIVORCED, 'DIVORCED'),
    )
    father_marital_status = models.CharField(max_length=50, choices=FATHER_MARITAL_STATUS_CHOICES, default=MARRIED)


    def __str__(self):
        return self.father_name

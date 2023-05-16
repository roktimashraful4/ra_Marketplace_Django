# //////////// Devoloped by Roktim  ashrafull \\\\\\\\
from datetime import date
from sqlite3 import Date
import uuid
from django.db import models
from django.forms import NumberInput
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from .slugfun import *

# Create your models here.

class courses(models.Model):
    curseName = models.CharField(("Course Name"), max_length=50)
    courseCradit = models.CharField(("Cradit"), max_length=1)
    courseFees = models.CharField(("Fess"), max_length=5)
    dy = models.CharField(("description"), max_length=150, default='')
    regularFees= models.CharField(("regular Fess"), max_length=5, default='100')
    class Meta:
        verbose_name = ("courses")
        verbose_name_plural = ("courses")

    def __str__(self):
        return self.curseName

    def get_absolute_url(self):
        return reverse("courses_detail", kwargs={"pk": self.pk})


class Student(models.Model):
    courseId= models.ForeignKey(courses, verbose_name=("Course"), on_delete=models.CASCADE)
    FastName= models.CharField(("Fast Name"), max_length=50)
    lestName= models.CharField(("Lest Name"), max_length=50)
    FatherName= models.CharField(("Father Name"), max_length=50)
    MotherName= models.CharField(("Mother Name"), max_length=50)
    Phonenumber= models.CharField(("phone number"), max_length=50)
    email=models.EmailField(("Email"), max_length=254)
    dob = models.DateField(("Date of Birth"), auto_now=False, auto_now_add=False)
    img = models.ImageField(("uploadImage"), upload_to='studentProfile', )
    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.FastName 

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})




class Payments(models.Model):
    studentid = models.ForeignKey(Student, verbose_name=("studentID"), on_delete=models.CASCADE)
    fastpay = models.CharField(("Fast Payment"),default=0, max_length=5)
    sectpay = models.CharField(("Secount Payment"),default=0, max_length=5, )
    thirdtpay = models.CharField(("third Payment"),default=0, max_length=5,)
    fastpaydate = models.DateTimeField(("fastdate"), auto_now=False, null=True)
    secoundpaydate = models.DateTimeField(("secounddate"), auto_now=False, null=True )
    thirdpaydate = models.DateTimeField(("thirddate"), auto_now=False, null=True)

    class Meta:
        verbose_name = ("Payments")
        verbose_name_plural = ("Payments")



    def __str__(self):
        return "pay"

    def get_absolute_url(self):
        return reverse("Payments_detail", kwargs={"pk": self.pk})


class CirtificateId(models.Model):
    x =uuid.uuid4()

    studentid = models.ForeignKey(Student, verbose_name=("studentID"), on_delete=models.CASCADE)
    catificateId = models.CharField(("key"), max_length=10 , unique=True, default='')
    
    class Meta:
        verbose_name = ("CirtificateId")
        verbose_name_plural = ("CirtificateIds")

    def __str__(self):
        return self.studentid.FastName

    def get_absolute_url(self):
        return reverse("CirtificateId_detail", kwargs={"pk": self.pk})


# custom user profile 

class Profile(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    fastname = models.CharField(("First name"), max_length=50)
    lestname = models.CharField(("lest name"), max_length=50)
    phone = models.CharField(("phone number"), max_length=16)
    location = models.CharField(("address"), max_length=150)
    website = models.CharField(("website"), max_length=150)
    language = models.CharField(("language"), max_length=150)
    bio = models.TextField(("Bio "))
    img = models.FileField(("img"), upload_to="studentProfile/users", max_length=255, default=True, null=True)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return self.fastname

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})



class Myskill(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    skillname = models.CharField(("Name"), max_length=50)
    progrss = models.CharField(("Progress(%)"), max_length=3)


    

    class Meta:
        verbose_name = ("Myskill")
        verbose_name_plural = ("Myskills")

    def __str__(self):
        return self.skillname

    def get_absolute_url(self):
        return reverse("Myskill_detail", kwargs={"pk": self.pk})


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Start task menagemets \\\\\\\\\\\\\\\\\\\\\
class TaskCetagory(models.Model):
    title = models.CharField(("Catragory Name: "), max_length=50)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    shortdis = models.TextField(("Short Discriptions"))
    img = models.ImageField(("Image"), upload_to="studentProfile/cetagery", max_length=None)
   

    class Meta:
        verbose_name = ("TaskCetagory")
        verbose_name_plural = ("TaskCetagorys")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("TaskCetagory_detail", kwargs={"pk": self.pk})

@receiver(pre_save, sender=TaskCetagory)
def pre_save_receiver(sender, instance, *args, **kwargs):
      if not instance.slug:
            instance.slug = unique_slug_generator(instance)



class AddTask(models.Model):
    cetid = models.ForeignKey(TaskCetagory, verbose_name=("Task Cetagory"), on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=50)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    shortdis = models.TextField(("Short Discriptions"))
    detiles = RichTextField(blank=True,null=True)
    budget = models.CharField(("Budget Price"), max_length=50)
    expdate = models.DateField(("Expire Date "), auto_now=False, auto_now_add=False)
    uploaddata = models.DateField(("Curent date"), auto_now=True, auto_now_add=False)
    uploadtime = models.TimeField(("Curent Time"), auto_now=True, auto_now_add=False)
    image = models.ImageField(("Image"), upload_to='studentProfile/project',  max_length=None)
    @property
    def is_expir(self):
        delta = self.expdate - date.today()
        
        if delta.days + 1 <= 0: 
            return True
        else: 
            return False
    class Meta:
        verbose_name = ("AddTask")
        verbose_name_plural = ("AddTasks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("AddTask_detail", kwargs={"pk": self.pk})

@receiver(pre_save, sender=AddTask)
def pre_save_receiver(sender, instance, *args, **kwargs):
      if not instance.slug:
            instance.slug = unique_slug_generator(instance)


class BitTask(models.Model):
    tastId = models.CharField(("Unice Id"), unique=True, max_length=8)
    bitUser = models.ForeignKey(User, verbose_name=("Users "), on_delete=models.CASCADE)
    task = models.ForeignKey(AddTask, verbose_name=(""), on_delete=models.CASCADE)
    status = models.CharField(("Status"), max_length=10)


    class Meta:
        verbose_name = ("BitTask")
        verbose_name_plural = ("BitTasks")

    def __str__(self):
        return self.tastId

    def get_absolute_url(self):
        return reverse("BitTask_detail", kwargs={"pk": self.pk})

class Bituploadproject(models.Model):
    bitId= models.ForeignKey(BitTask, verbose_name=("Bit Id"), on_delete=models.CASCADE)
    message = models.TextField(("Message"))
    uploaddate = models.DateTimeField(("curentdate"), auto_now=True, auto_now_add=False)
    file = models.FileField(("File"), upload_to="projectfils/")

    

    class Meta:
        verbose_name = ("Bituploadproject")
        verbose_name_plural = ("Bituploadprojects")

    def __str__(self):
        return self.bitId.tastId

    def get_absolute_url(self):
        return reverse("Bituploadproject_detail", kwargs={"pk": self.pk})

class Reviewprojectnote(models.Model):
    bittaskid = models.ForeignKey(BitTask, verbose_name=("Bit Task"), on_delete=models.CASCADE)
    mess = models.TextField(("Message"))
    

    class Meta:
        verbose_name = ("Reviewprojectnote")
        verbose_name_plural = ("Reviewprojectnotes")

    def __str__(self):
        return self.bittaskid

    def get_absolute_url(self):
        return reverse("Reviewprojectnote_detail", kwargs={"pk": self.pk})




class BitpaymentAmount(models.Model):
    uid = models.ForeignKey(User, verbose_name=("User Id"), on_delete=models.CASCADE)
    amount = models.CharField(("Amount"), max_length=50)

    class Meta:
        verbose_name = ("BitpaymentAmount")
        verbose_name_plural = ("BitpaymentAmounts")

    def __str__(self):
        return self.uid.username

    def get_absolute_url(self):
        return reverse("BitpaymentAmount_detail", kwargs={"pk": self.pk})


class PamentOptions(models.Model):
    uid = models.ForeignKey(User, verbose_name=("User Id"), on_delete=models.CASCADE)
    bankname = models.CharField(("Bank Name "), max_length=50)
    number = models.CharField(("number "), max_length=50)
    

    class Meta:
        verbose_name = ("PamentOptions")
        verbose_name_plural = ("PamentOptionss")

    def __str__(self):
        return self.uid.username

    def get_absolute_url(self):
        return reverse("PamentOptions_detail", kwargs={"pk": self.pk})

class paymentrequest(models.Model):
    requid = models.CharField(("requid"), max_length=5)
    uid = models.ForeignKey(User, verbose_name=("User id"), on_delete=models.CASCADE)
    amount = models.CharField(("Amount"), max_length=50)
    curenttime = models.DateTimeField(("time"), auto_now=False, auto_now_add=False)
    status = models.CharField(("status"), max_length=50)

    

    class Meta:
        verbose_name = ("paymentrequest")
        verbose_name_plural = ("paymentrequests")

    def __str__(self):
        return self.requid

    def get_absolute_url(self):
        return reverse("paymentrequest_detail", kwargs={"pk": self.pk})

#\\\\\\\\\\\\\\\\\\\\\\\\\\ End task menagemets \\\\\\\\\\\\\\\\\\\\\



# //////////// Devoloped by Roktim  ashrafull \\\\\\\\


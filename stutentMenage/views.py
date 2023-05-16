# //////////// Devoloped by Roktim  ashrafull \\\\\\\\

import datetime
from datetime import date
from distutils.command import upload
from multiprocessing.dummy import Process
from re import A
from time import time
import uuid
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login , logout, authenticate
from . models import AddTask, BitTask, BitpaymentAmount, Bituploadproject, Myskill, PamentOptions, Reviewprojectnote, TaskCetagory, courses, Student,Payments, CirtificateId, Profile, paymentrequest
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, Count 
from .models import User
from . forms import AddTaskForm, TaskCetagoryForm


def hello(request):
  fc = TaskCetagory.objects.all()
  fd = AddTask.objects.all()
  print(fd[1].is_expir)
  datalist={
    "allcat":fc,
  }
  return render(request,'index.html',datalist)
def about(request):
  return render(request,'about.html')
def contact(request):
  return render(request,'contact.html')
def getcirtificate(request):
  return render(request,'getcirtificate.html')
  
def coursepage(request):
  loadCourse = courses.objects.order_by("?").all()
  loaddata = {
    'allcourse': loadCourse,
    'img' : ["studentProfile/png/9.png",
            "studentProfile/png/45.png",
            "studentProfile/png/2.png",
            "studentProfile/png/3.png",
            "studentProfile/png/5.png",
            ]
  }
  return render(request,'courses.html',loaddata)
def findcartificate(request):
  return render(request,'panel/makeCartificate.html')
def userlogin(request):
    
    if request.method == 'POST':
      loginuser= request.POST['loginuser']
      loginpass= request.POST['loginpass']
      user = authenticate(username=loginuser,password=loginpass)
      if user is not None:
        login(request,user)
        return redirect('/useradminpanel')
      else:
        messages.error(request,'incurrect username or password')
    if request.user.is_superuser:
      return redirect('/useradminpanel')
    elif request.user.is_staff and not request.user.is_superuser:
      return redirect('/profile')
    else:
      return render(request, 'login.html')
def hendellogout(request):
  if request.user.is_authenticated:
    logout (request)
    return redirect('/login')
  else:
    return redirect('/')
def deshboard(request):
  if request.user.is_superuser:
    allcourses = courses.objects.all()
    allstudent = Student.objects.all()
    fastpay = Payments.objects.aggregate(Sum('fastpay'))
    secoundpay = Payments.objects.aggregate(Sum('sectpay'))
    thirdpay = Payments.objects.aggregate(Sum('thirdtpay'))
    totalStudent = Student.objects.aggregate(Count('id'))
    totalCourse = courses.objects.aggregate(Count('id'))
    total_amount = fastpay['fastpay__sum']+secoundpay['sectpay__sum']+thirdpay['thirdtpay__sum']
    print(totalStudent)
    loaddata = {
      'courses': allcourses,
      'students': allstudent,
      'totalPay': total_amount,
      'total_student': totalStudent['id__count'],
      'total_course': totalCourse['id__count'],
    }
    return render(request, 'panel/index.html', loaddata)
  else:
    return redirect('/login')
  

def addstudentpage(request):
  if request.user.is_superuser:
    allcourses = courses.objects.all()
    loaddata = {
      'courses': allcourses,
    }
    return render(request, 'panel/addstudent.html',loaddata)
  else:
    return redirect('/login')

def addnewcoursepage(request):
  if request.user.is_superuser:
    if request.method == "POST":
      cname = request.POST['coursename']
      c_creadit= request.POST['coursecreadit']
      coursedescription= request.POST['coursedescription']
      regularFee= request.POST['regularFees']
      c_fees = request.POST['courseFees']
      newcourse= courses(curseName=cname,dy=coursedescription,regularFees=regularFee,courseCradit=c_creadit,courseFees=c_fees)
      newcourse.save()
      
      messages.success(request,'data save success ! ' )
    return render(request, 'panel/newcourses.html')
  else:
    return redirect('/login')

def courselistpage(request):
  if request.user.is_superuser:
    allcourses = courses.objects.all()
    loaddata = {
      'courses': allcourses,
    }
    return render(request, 'panel/courseList.html',loaddata)
  else:
    return redirect('/login')

def hendel_course_update(request):
  if request.user.is_superuser:
    if request.method == "POST":
      e_c_id = request.POST['e_c_id']
      e_cname = request.POST['e_coursename']
      e_cCreadit = request.POST['e_coursecreadit']
      e_dy = request.POST['e_dy']
      e_Reguler = request.POST['e_Reguler']
      e_cFees = request.POST['e_courseFees']
      find_data = courses.objects.get(id=e_c_id)
      find_data.courseFees = e_cFees
      find_data.curseName = e_cname
      find_data.courseCradit = e_cCreadit
      find_data.dy = e_dy
      find_data.regularFees = e_Reguler
      find_data.save()
      messages.success(request, 'Update data success')
      return redirect('/courselist')
  else:
    return redirect('/login')

def hendel_course_delete(request):
  if request.user.is_superuser:
    if request.method == "POST":
      eCid = request.POST['e_c_idi']
      cfind = courses.objects.get(id=eCid).delete()
      messages.error(request, 'Delete data success')
      return redirect('/courselist')
  else:
    return redirect('/login')
def hendel_save_student(request):
  if request.method == "POST":
    imgfile = request.FILES['images']
    fss = FileSystemStorage()
    file = fss.save('studentProfile/'+imgfile.name, imgfile)
    file_url = fss.url(file)
    fname = request.POST['fname']
    lname = request.POST['lname']
    fathername = request.POST['fatherName']
    motherName = request.POST['motherName']
    email = request.POST['email']
    phone = request.POST['phone']
    dob = request.POST['dob']
    courseid = int(request.POST['courseid'])
    curid = courses.objects.get(id=courseid)
   
    s1 = Student(courseId=curid,FastName=fname,lestName=lname,FatherName=fathername,MotherName=motherName,Phonenumber=phone,
              email=email, dob=dob, img=file)
    s1.save()
    print(courseid)
    messages.success(request, "Add new student successfull !! ")
    return redirect('/addstudent')

def studentlistPage(request):
  if request.user.is_superuser:
    allstudent = Student.objects.all()
    datalist ={
      'students': allstudent,
    }
    return render(request, 'panel/studentlist.html' , datalist)
  else: 
    return redirect('/login')
def hendel_student_update(request):
  if request.user.is_superuser:
    if request.method=="POST":
      dobS = request.POST['e_dob']
      if not dobS =='':
        dob_new = request.POST['e_dob']
        e_s_id  = request.POST['e_s_id']
        dataS= Student.objects.get(id=e_s_id)
        dataS.dob = dob_new
        dataS.save()
        messages.success(request,"Data update successfull !! ")
        return redirect('/studentlist')
        
      else:
        e_s_id  = request.POST['e_s_id']
        f_name = request.POST['e_fastname']
        lname = request.POST['e_lestname']
        fathername = request.POST['e_fathername']
        mothername = request.POST['e_mothername']
        email = request.POST['e_email']
        phone = request.POST['e_phone']

        findStudent= Student.objects.get(id=e_s_id)
        findStudent.FastName = f_name
        findStudent.lestName = lname
        findStudent.FatherName = fathername
        findStudent.MotherName = mothername
        findStudent.email = email
        findStudent.Phonenumber = phone
        findStudent.save()
        messages.success(request,"Data update successfull !! ")
        return redirect('/studentlist') 
def hendel_s_delete(request):
  if request.user.is_superuser:
    if request.method == "POST":
      seid = request.POST['e_s_idi']
      Student.objects.get(id=seid).delete()
      messages.error(request, 'Delete data success')
      return redirect('/studentlist')
  else:
    return redirect('/login')

def studentprofilepage(request,sid):
  if request.user.is_superuser:
    sf = Student.objects.get(id=sid)
    try:
      cirfi = CirtificateId.objects.get(studentid=sf)
      catificatekey =cirfi.catificateId
    except:
      catificatekey= 'nodata'
    try:
      payf = Payments.objects.get(studentid=sf)
      due=int(sf.courseId.courseFees) - (int(payf.fastpay)+int(payf.sectpay)+int(payf.thirdtpay))
      
    except:
      payf ="nodata"
      due=sf.courseId.courseFees
    print(payf)
    loaddata = {
      'studentdata':sf,
      'payment':payf,
      'due' :due,
      'catificatekey':catificatekey,
    }
    return render(request,'panel/studentprofile.html', loaddata)
  else:
    return redirect('/login')

def firstpayment(request):
  if request.method=="POST":
    sid = request.POST['sid']
    sf = Student.objects.get(id=sid)
    fps = request.POST['firstpayment']
    pf = Payments(studentid=sf,fastpay=fps,fastpaydate=datetime.datetime.now())
    pf.save()
    x = uuid.uuid4()
    cr = CirtificateId(studentid=sf, catificateId=str(x)[-11:])
    cr.save()
    return redirect('/studentprofile/'+sid)

def secoundpayment(request):
  if request.method=="POST":
    sid = request.POST['sid']
    sf = Student.objects.get(id=sid)
    fps = request.POST['secoundpayment']
    pf = Payments.objects.get(studentid=sf)
    pf.sectpay = fps 
    pf.secoundpaydate = datetime.datetime.now()
    pf.save()
    return redirect('/studentprofile/'+sid)

def thirdpayment(request):
  if request.method=="POST":
    sid = request.POST['sid']
    sf = Student.objects.get(id=sid)
    fps = request.POST['thirdpayment']
    pf = Payments.objects.get(studentid=sf)
    pf.thirdtpay = fps 
    pf.thirdpaydate = datetime.datetime.now()
    pf.save()
    return redirect('/studentprofile/'+sid)
def editeprofile(request,sid):
  if request.user.is_superuser:
    allstudent = Student.objects.get(id=sid)
    datalist ={
      'students': allstudent,
    }
    return render(request,'panel/editeprofile.html', datalist)
  else:
    return redirect("/login")
    
def billinglist(request):
  if request.user.is_superuser:
    srf = Student.objects.all()
    payments = Payments.objects.all()
    
    datalist = {
      'students':srf,
      'payments':payments

    }
    return render(request,'panel/billing_list.html', datalist)
  else:
    return redirect("/login")




# costomer user functionalty start 
def signup(request):
  if request.method == "POST":
    username = request.POST['signupusername']
    email = request.POST['signupemail']
    password = request.POST['signuppass']
    user = User.objects.create_user(username,email,password)
    user.is_staff=True
    user.save()
    messages.success(request,"Now you can login ")
    return redirect('/login')
  return render(request, 'signup.html')

def  profile(request):
  if request.user.is_staff and not request.user.is_superuser:
    username = request.user.username
    try: 
      fprofile = Profile.objects.get(uid=request.user.id)
    except:
      fprofile = 'nodata'
      uf = User.objects.get(id= request.user.id)
      
      if request.method == "POST":
        imgfile = request.FILES['img']
        fss = FileSystemStorage()
        file = fss.save('studentProfile/'+imgfile.name, imgfile)
        file_url = fss.url(file)
        fastname = request.POST['firstname']
        lestname = request.POST['lestname']
        phones = request.POST['phone']
        language = request.POST['language']
        locations = request.POST['location']
        websites = request.POST['website']
        bios = request.POST['bio']
        
        profile = Profile(uid=uf,fastname=fastname, lestname=lestname,
            phone=phones,location=locations, website=websites,language=language, bio=bios, img= file
        )
        profile.save()
        return redirect('/profile')
      return render(request, 'editprofile.html')
      
    try:
      myskill = Myskill.objects.filter(uid=request.user.id)
    except:
      myskill= 'nodata'
    datalist = {
      'username':username,
      'email': request.user.email,
      'profile': fprofile,
      'myskill': myskill
    }
    return render(request, 'myprofile.html',datalist)

  else:
    return redirect("/login")
def  profileuser(request,usid):
    users = User.objects.get(username=usid)
    findprofie = Profile.objects.get(uid=users.id)
    try:
      myskill = Myskill.objects.filter(uid=users.id)
    except:
      myskill= 'nodata'
    datalist = {
      'username':users.username,
      'email': users.email,
      'profile': findprofie,
      'myskill': myskill
    }
    return render(request, 'myprofile.html',datalist)
def updateprofile(request):
  if request.user.is_staff and not request.user.is_superuser:
    if request.method == "POST":
        fastname = request.POST['fastname']
        lestname = request.POST['lastname']
        phones = request.POST['phone']
        locations = request.POST['location']
        websites = request.POST['website']
        bios = request.POST['bio']
        pf = Profile.objects.get(uid = request.user.id)
        pf.fastname = fastname
        pf.phone = phones
        pf.location = locations
        pf.website = websites
        pf.bio = bios
        pf.save()
        messages.success(request,"Update info Successfull ")
        return redirect("/profile")
  else: 
    return redirect("/login")

def savemyskill(request):
  if request.user.is_staff and not request.user.is_superuser: 
    if request.method == "POST":
      skillname = request.POST['skillname']
      progress = request.POST['progress']
      uf = User.objects.get(id=request.user.id)
      myskill = Myskill(uid=uf,skillname=skillname,progrss= progress)
      myskill.save()
      messages.success(request,"Add new skill \" "+skillname+" \"")
      return redirect("/profile")
      

    else:
      return redirect('/profile')
  else: 
    return redirect('/login')

def skillupdate(request):
  if request.user.is_staff and not request.user.is_superuser:
    if request.method == "POST":
      uid = request.POST['uid']
      skillname = request.POST['skillname']
      progress = request.POST['progress']
      fskill = Myskill.objects.get(id=uid)
      fskill.skillname = skillname
      fskill.progrss = progress
      fskill.save()
      messages.success(request,"Update skill successfull !! ")
      return redirect('/profile')
  else:
    return redirect('/login')
def deleteskill(request):
  if request.user.is_staff and not request.user.is_superuser:
    if request.method == "POST":
      uid = request.POST['uid']
      Myskill.objects.get(id=uid).delete()
      messages.success(request,"Delete Skill ")
      return redirect('/profile')
  else:
    return redirect('/login')


def taskcetagery(request):
  if request.user.is_superuser:
    formadd = TaskCetagoryForm (request.POST, request.FILES)
    if request.method == 'POST':
      if formadd.is_valid():
        formadd.save()
        messages.success(request,"Success ")
        return redirect('/taskcetagery')
      
    allCetagory = TaskCetagory.objects.all()
    datalist = {
      'addform': formadd,
      "cetagoryes": allCetagory
    }
    return render(request,'panel/taskcetagary.html',datalist)
  else:
    return redirect("/login")

def edittaskcetagery(request):
  if request.user.is_superuser:
    if request.method == "POST":
      id = request.POST['e_id']
      title = request.POST['e_title']
      slug = request.POST['e_slug']
      sortdis = request.POST['e_shortdis']
      ftc = TaskCetagory.objects.get(id = id)
      ftc.title = title
      ftc.slug = slug
      ftc.shortdis = sortdis
      ftc.save()
      messages.success(request, "Update successfulll ")
      return redirect("/taskcetagery")


  else:
    return redirect("/login")
def deletetaskcetagerys(request):
  if request.user.is_superuser:
    if request.method == "POST":
      id = request.POST['e_idi']
      TaskCetagory.objects.get(id=id).delete()
      messages.success(request,"Delete successfull")
      return redirect("/taskcetagery")
  else:
    return redirect("/login")

def addnewtask(request):
  if request.user.is_superuser:
    addtaskfrom = AddTaskForm(request.POST, request.FILES)
    if  request.method== "POST":
      if addtaskfrom.is_valid():
        addtaskfrom.save()
        messages.success(request, "add Task successful ")
        return redirect("/newtask")
  

    datalist = {
      'form': addtaskfrom,
    }

    return render(request,'panel/newtask.html',datalist)
  else:
    return redirect("/login")

def tasklist(request):
  if request.user.is_superuser:
    ftask = AddTask.objects.all()
    datalist = {
       "tasks": ftask
    }
    return render(request, "panel/tasklist.html", datalist)
  else:
    return redirect("/login")


def categories(request):
  fc = TaskCetagory.objects.all()
  datenow = datetime.date.today()
  timenow = datetime.datetime.now().time()
  datalist ={
      "allcat":fc,
      'now': datenow,
      'time':timenow,
  }
  return render(request,'categories.html', datalist)

def project(request):
  pass
def categoriproject(request,slug):
  fc  = TaskCetagory.objects.get(slug=slug)
  allcat = TaskCetagory.objects.all() 
  datalist = {
    'tasks': fc,
    "allcat" : allcat,
  }
  return render(request, 'cetagorybyproject.html', datalist)

def getproject(request,slug):
  ftask = AddTask.objects.get(slug=slug)
  timea = ftask.expdate
  se = datetime.date.today()
  ext =  timea - se
  allcat = TaskCetagory.objects.all() 
  isBit = False

  if request.user.is_staff and not request.user.is_superuser:
    try:
      usertask = BitTask.objects.filter(bitUser=request.user.id ,task=AddTask.objects.get(slug=slug).id) 
      if len(usertask) > 0:
        isBit = True
    except:
      isBit = False

  datalist = {
    'project': ftask,
    "allcat" : allcat,
    "exptime": ext.days+1,
    "isBit" : isBit
  }
  return render(request,'projectdetiles.html', datalist)

def addtobittask(request):
  if request.user.is_staff and not request.user.is_superuser:
    if request.method == "POST":
      Uid = request.POST['Uid']
      taskslug = request.POST['task']
      fuser = User.objects.get(id=Uid)
      ftask = AddTask.objects.get(slug= taskslug)
      if len(BitTask.objects.filter(bitUser=fuser.id ,task=ftask.id)) > 0: 
        messages.error(request,"Already added this task")
      else:
        taskid = str(uuid.uuid4())
        addbit = BitTask(tastId=taskid[:8], bitUser=fuser, task=ftask,status="working")
        addbit.save()
        messages.success(request," you are bited this project Bit ID is: #"+str(taskid[:8]))
        
      return redirect("project/"+taskslug)

  else:
    return redirect("/login")

def mybitedtask(request, usid):
  if request.user.is_staff and not request.user.is_superuser:
    users = User.objects.get(username=usid)
    findprofie = Profile.objects.get(uid=users.id)
    findBit = BitTask.objects.filter(bitUser=users.id)
    cancelBit = BitTask.objects.filter(bitUser=users.id,status='cancel')
    completedBit = BitTask.objects.filter(bitUser=users.id,status="completed")
    workingtedBit = BitTask.objects.filter(bitUser=users.id)
    for i in range(len(workingtedBit)):
      timea = workingtedBit[i].task.expdate
      se = datetime.date.today()
      ext =  timea - se
     
      if ext.days <= 0:
        if not  workingtedBit[i].status == "completed":
          cid = workingtedBit[i].id 
          cd = BitTask.objects.get(id=cid)
          cd.status = "expired"
          cd.save()
    
    workingBit = BitTask.objects.filter(bitUser=users.id,status="working")
    expired = BitTask.objects.filter(bitUser=users.id,status="expired")
    processingbit = BitTask.objects.filter(bitUser=users.id,status="processing")
    inreviewbit = BitTask.objects.filter(bitUser=users.id,status="in-review")

    datalist = {
      'username':users.username,
      'email': users.email,
      'profile': findprofie,
      'bittasks': findBit,
      "cancelBit": cancelBit,
      "completedBit":completedBit,
      "expired":expired,
      "processingbit":processingbit,
      "inreviewbit":inreviewbit,
      "workingtedBit":workingBit
     
    }
    return render(request,'mybitedtask.html', datalist)
  else:
    return redirect("/login")

def cancelbit(request):
  if request.user.is_staff and not request.user.is_superuser:
    if request.method == "POST":
      id = request.POST['id']
      fbit = BitTask.objects.get(id=id)
      fbit.status = 'cancel'
      fbit.save()
      messages.success(request,"Cancel bit successful ")
      return redirect(request.user.username+'/mybitedtask')
  else:
    return redirect("/login")
def bitsubmit(request):
  if request.user.is_staff and not request.user.is_superuser:
    if request.method== "POST":
      imgfile = request.FILES['projectfile']
      fss = FileSystemStorage()
      file = fss.save('projectfils/'+imgfile.name, imgfile) 
      id = request.POST['id']
      mess = request.POST['messages']
      fBit = BitTask.objects.get(id=id)
      eft = Bituploadproject(bitId=fBit,message=mess,file=file)
      eft.save()
      fBit.status = "processing"
      fBit.save()
      messages.success(request,'Your project submited')
      return redirect(request.user.username+'/mybitedtask')


  else:
    return redirect("/login")

def bitlist(request):
  if request.user.is_superuser:
    fbitupload = Bituploadproject.objects.all()
    datalist = {
      "finduploads":fbitupload,
      }
    return render(request,"panel/bitlist.html", datalist)
  else: 
    return redirect("/login")

def bitdetils(request,bitid ):
  if request.user.is_superuser:
    fbitupload = Bituploadproject.objects.get(id=bitid)
    datalist = {
      "finduploads":fbitupload,
      }
    return render(request,"panel/bitdetials.html", datalist)
  else: 
    return redirect("/login")


def makecompliteproject(request):
  if request.user.is_superuser:
    if request.method== "POST":
      id = request.POST['id']
      fbt = BitTask.objects.get(id=id)
      fbt.status = 'completed'
      fbt.save()
      bituser  = User.objects.get(id =fbt.bitUser.id) 
      try:
        rf = BitpaymentAmount.objects.get(uid=bituser.id)

        rfamount =rf.amount 
        newamount = int(rfamount) + int(fbt.task.budget)
        rf.amount = newamount
        rf.save()
        print("yes")
      except:
        rf = BitpaymentAmount(uid=bituser,amount=fbt.task.budget)
        rf.save()
        print("no")
      messages.success(request,"updated ")
      return redirect('/bitlist')
  else: 
    return redirect("/login")
def cancelproject(request):
  if request.user.is_superuser:
    if request.method== "POST":
      id = request.POST['id']
      fbt = BitTask.objects.get(id=id)
      fbt.status = 'cancel'
      fbt.save()
      messages.success(request,"updated ")
      return redirect('/bitlist')
  else: 
    return redirect("/login")
def reviewprojects(request):
  if request.user.is_superuser:
    if request.method== "POST":
      id = request.POST['id']
      mess = request.POST['note']
      fbt = BitTask.objects.get(id=id)
      fbt.status = 'in-review'
      fbt.save()
      re = Reviewprojectnote(bittaskid=fbt,mess=mess)
      re.save()
      messages.success(request,"updated ")
      return redirect('/bitlist')
  else: 
    return redirect("/login")


def mypayments(request, usid):
  if request.user.is_staff and not request.user.is_superuser:
    users = User.objects.get(username=usid)
    findprofie = Profile.objects.get(uid=users.id)
    try:
      paymentinfo = PamentOptions.objects.get(uid=users.id)
    except:
      paymentinfo = "no data"
    try:
      bl=  BitpaymentAmount.objects.get(uid=users.id)
      blance = bl.amount
    except:
      blance = "00"
    
    rs = paymentrequest.objects.order_by("-id").filter(uid=users.id)

    datalist = {
      'username':users.username,
      'email': users.email,
      'profile': findprofie,
      'paymentinfo':paymentinfo,
      'blance': blance,
      'rs':rs
     
    }
    return render(request, "mypayments.html", datalist)
  else: 
    return redirect("/login")

def paymentinfo(request):
  if request.user.is_staff and not request.user.is_superuser:
    if request.method == "POST":
      id = request.POST['id']
      agent = request.POST['agent']
      number = request.POST['number']
      fr= User.objects.get(id=id)
      
      try:
        paymentinfo = PamentOptions.objects.get(uid=id)
        paymentinfo.bankname = agent
        paymentinfo.number = number
        paymentinfo.save()
        messages.success(request, "payment method updated. ")

      except:
        re = PamentOptions(uid=fr,bankname=agent,number=number)
        re.save()
        messages.success(request,"save payment method.")
      return redirect(fr.username+'/payment')
  else: 
    return redirect("/login")

def requestpayments(request):
  if request.user.is_staff and not request.user.is_superuser:
    if request.method == "POST":
      id = request.POST['id']
      fu = User.objects.get(id=id)
      amount = request.POST['amount']
      reid =str(uuid.uuid4())
      r = paymentrequest(requid=reid[:5],uid=fu,amount=amount,curenttime=datetime.datetime.now(),status='requested')
      r.save()
      messages.success(request,'your request submited ')
      return redirect(request.user.username+'/payment')
  else: 
    return redirect("/login")

def bitpaymentrequest(request):
  if request.user.is_superuser:
    allrequest =  paymentrequest.objects.order_by("-id").all()
    datalist = {
      'allrequest': allrequest
    }
    return render(request,'panel/bitpaymentrequest.html',datalist)
  else: 
    return redirect("/login")




# //////////// Devoloped by Roktim  ashrafull \\\\\\\\

import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from workerapp.models import *


def loginadd(request):
    return render(request,'index.html')

def login_post(request):
    uname = request.POST['uname']
    pswd = request.POST['psw']

    d = login.objects.filter(username=uname,password=pswd)

    if d.exists():
        logindata = d[0]
        request.session['lid'] = logindata.id
        request.session['lin']="lg"

        if logindata.usertype == 'admin':
            return redirect('/adminhome')
        elif logindata.usertype == 'user':
            return redirect('/userhome')
        elif logindata.usertype == 'worker':
            return redirect('/workerhome')
    else:
        return HttpResponse("<script>alert('Login Failed');window.location='/'</script>")

def logout(request):
    request.session['lin']=""
    return HttpResponse("<script>alert('Logouted');window.location='/'</script>")


def changepasswdadmin(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'Admin/changepasswd.html')

def changepsw_posta(request):
    cpsw = request.POST['cpsw']
    npsw = request.POST['npsw']
    copsw = request.POST['copsw']
    usertype = 'admin'
    psw = login.objects.filter(password=cpsw,id=request.session['lid'])
    if psw.exists():
        if npsw == copsw:
            login.objects.filter(id=request.session['lid']).update(password=npsw)
            return HttpResponse("<script>alert('Password Changed');window.location='/'</script>")
        return HttpResponse("<script>alert('Password Mismatched');window.location='/'</script>")
    return HttpResponse("<script>alert('Wrong current password');window.location='/'</script>")

def changepasswdworker(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'Worker/changepasswd.html')

def changepsw_postw(request):
    cpsw = request.POST['cpsw']
    npsw = request.POST['npsw']
    copsw = request.POST['copsw']
    usertype = 'worker'
    psw = login.objects.filter(password=cpsw,id=request.session['lid'])
    if psw.exists():
        if npsw == copsw:
            login.objects.filter(id=request.session['lid']).update(password=npsw)
            return HttpResponse("<script>alert('Password Changed');window.location='/'</script>")
        return HttpResponse("<script>alert('Password Mismatched');window.location='/'</script>")
    return HttpResponse("<script>alert('Wrong current password');window.location='/'</script>")

def changepasswduser(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'User/changepasswd.html')

def changepsw_postu(request):
    cpsw = request.POST['cpsw']
    npsw = request.POST['npsw']
    copsw = request.POST['copsw']
    usertype = 'user'
    psw = login.objects.filter(password=cpsw,id=request.session['lid'])
    if psw.exists():
        if npsw == copsw:
            login.objects.filter(id=request.session['lid']).update(password=npsw)
            return HttpResponse("<script>alert('Password Changed');window.location='/'</script>")
        return HttpResponse("<script>alert('Password Mismatched');window.location='/'</script>")
    return HttpResponse("<script>alert('Wrong current password');window.location='/'</script>")


def adminhome(request):
    return render(request, 'Admin/index.html')

def userhome(request):
    return render(request, 'User/index.html')

def workerhome(request):
    return render(request, 'Worker/index.html')

#userfunctions
def registeruser(request):
    return render(request, 'User/Registeruser.html')

def user_post(request):
    Name = request.POST['name']
    Email = request.POST['email']
    DOB = request.POST['dob']
    Address = request.POST['addr']
    contact = request.POST['phn']
    Image = request.FILES['img']
    Uname = request.POST['uname']
    Pswd = request.POST['psw']

    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    fs.save(r"D:\Django\workermngt\workerapp\static\image\\" + d + '.jpg', Image)
    path = "/static/image/" + d + '.jpg'

    ob = login()
    ob.username = Uname
    ob.password = Pswd
    ob.usertype = 'user'
    ob.save()

    obj = user()
    obj.UName = Name
    obj.Email = Email
    obj.DOB = DOB
    obj.Address = Address
    obj.Contact = contact
    obj.Image = path
    obj.LOGIN = ob
    obj.save()
    ob.save()
    return HttpResponse("<script>alert('ADDED');window.location = '/'</script>")


#user  view
def viewuser(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = user.objects.filter(LOGIN=request.session['lid'])
    return render(request, 'User/viewuser.html', {'view':data})

#admin view
def vuser(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = user.objects.all()
    return render(request, 'Admin/viewu_user.html', {'view': data})

def edituser(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = user.objects.get(id=id)
    return render(request, 'User/edituser.html', {'view':data})

def edit_upost(request,id):
    try:
        Name = request.POST['name']
        Email = request.POST['email']
        DOB = request.POST['dob']
        Address = request.POST['addr']
        contact = request.POST['phn']
        Image = request.FILES['img']

        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fs.save(r"D:\Django\workermngt\workerapp\static\image\\" + d + '.jpg', Image)
        path = "/static/image/" + d + '.jpg'

        user.objects.filter(id=id).update(UName=Name,Email=Email,DOB=DOB,Address=Address,Contact=contact,Image=path)
        return HttpResponse("<script>alert('Edited');window.location = '/viewuser'</script>")


    except Exception as e:
        Name = request.POST['name']
        Email = request.POST['email']
        DOB = request.POST['dob']
        Address = request.POST['addr']
        contact = request.POST['phn']
    user.objects.filter(id=id).update(UName=Name, Email=Email, DOB=DOB, Address=Address, Contact=contact)
    return HttpResponse("<script>alert('Edited');window.location = '/viewuser'</script>")

def delete_user(request,id):
    user.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location = '/viewu_user'</script>")



#worker functions
def registerworker(request):
    return render(request, 'Worker/registerworker.html')

def worker_post(request):
    wname = request.POST['name']
    email = request.POST['email']
    dob = request.POST['dob']
    contact = request.POST['phn']
    Image = request.FILES['img']
    Uname = request.POST['uname']
    Pswd = request.POST['psw']

    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    fs.save(r"D:\Django\workermngt\workerapp\static\image\\" + d + '.jpg', Image)
    path = "/static/image/" + d + '.jpg'


    ob = login()
    ob.username = Uname
    ob.password = Pswd
    ob.usertype = "pending"
    ob.save()

    obj = worker()
    obj.WName = wname
    obj.Email = email
    obj.DOB = dob
    obj.Contact = contact
    obj.Image = path
    obj.LOGIN=ob
    obj.save()
    return HttpResponse("<script>alert('ADDED');window.location = '/'</script>")


#worker view
def viewworker(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = worker.objects.filter(LOGIN=request.session['lid'])
    return render(request, 'Worker/viewworker.html', {'view': data})

#admin view
def vworker(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = worker.objects.filter(LOGIN__usertype='pending')
    return render(request, 'Admin/vieww_worker.html', {'view': data})

def worker_approve(request, id):
    l=login.objects.filter(id=id).update(usertype='worker')
    lm = login.objects.filter(id=id)
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("abhinavmohan778@gmail.com", "jtap wmdt lvcp amer")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "abhinavmohan778@gmail.com"
    msg['To'] =lm[0].username
    msg['Subject'] = "Approoved your Request"
    body = "Your Password is:- - " + str(lm[0].password)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Approved');window.location = '/verified_worker'</script>")

def worker_reject(request, id):
    login.objects.filter(id=id).update(usertype='reject')
    l = login.objects.filter(id=id).update(usertype='worker')
    lm = login.objects.filter(id=id)
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("abhinavmohan778@gmail.com", "jtap wmdt lvcp amer")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "abhinavmohan778@gmail.com"
    msg['To'] = lm[0].username
    msg['Subject'] = "Rejected your Request"
    body = "Your application Rejected "
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Rejected');window.location = '/vworker'</script>")

def verified_worker(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = worker.objects.filter(LOGIN__usertype='worker')
    return render(request, 'Admin/verifiedworkers.html', {'view': data})

def verified_workeruser(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = worker.objects.filter(LOGIN__usertype='worker')
    return render(request, 'User/verifiedworkers.html', {'view': data})


def editworker(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = worker.objects.get(id=id)
    return render(request, 'Worker/editworker.html', {'view':data})

def edit_wpost(request,id):
    try:
        wname = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        contact = request.POST['phn']
        Image = request.FILES['img']

        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        fs.save(r"D:\Django\workermngt\workerapp\static\image\\" + d + '.jpg', Image)
        path = "/static/image/" + d + '.jpg'

        worker.objects.filter(id=id).update(WName=wname,Email=email,DOB=dob,Contact=contact,Image=path)
        return HttpResponse("<script>alert('Edited');window.location = '/viewworker'</script>")

    except Exception as e:
        wname = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        contact = request.POST['phn']

        worker.objects.filter(id=id).update(WName=wname,Email=email,DOB=dob,Contact=contact)
        return HttpResponse("<script>alert('Edited');window.location = '/viewworker'</script>")

def delete_worker(request,id):
    worker.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location = '/viewworker'</script>")


def sndfeedbackuser(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'User/sndfeedbackuser.html')

def fd_postuser(request):
        date = request.POST.get('date')
        fdback = request.POST.get('fback')

        obj = feedback()
        obj.date = date
        obj.feedback = fdback
        obj.save()

        return HttpResponse("<script>alert('Sent Successfully');window.location = 'User/index.html'</script>")


def sndfeedbackworker(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'Worker/sndfeedbackworker.html')

def fd_postworker(request):
        date = request.POST.get('date')
        fdback = request.POST.get('fback')

        obj = feedback()
        obj.date = date
        obj.feedback = fdback
        obj.save()

        return HttpResponse("<script>alert('Sent Successfully');window.location = 'Worker/index.html'</script>")


def viewfdbackuser(request):
    data = feedback.objects.all()
    ar=[]
    for i in data:
        if i.LOGIN.usertype == "user":
            re=user.objects.filter(LOGIN=i.LOGIN_id)
            if re.exists():
                ar.append({
                    "id":i.id,
                    "name":re[0].UName,
                    "date":i.date,
                    "feedback":i.feedback
                })
        else:
            ob=worker.objects.filter(LOGIN=i.LOGIN_id)
            if ob.exists():
                ar.append({
                    "id": i.id,
                    "name": ob[0].WName,
                    "date": i.date,
                    "feedback": i.feedback
                })
    return render(request, 'Admin/viewfdbackuser.html', {'view': ar})

def sndfbackworker(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'Worker/sndfeedbackworker.html')

def fd_postworker(request):

        Name = request.POST.get('name')
        date = request.POST.get('date')
        fdback = request.POST.get('fback')

        obj = feedback()
        obj.Name = Name
        obj.date = date
        obj.feedback = fdback
        obj.save()

        return HttpResponse("<script>alert('Sent Successfully');window.location = '/viewfdworker'</script>")

def viewfdworker(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = feedback.objects.all()
    return render(request, 'Worker/viewfdbackworker.html', {'view':data})



def sndcomplaints(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'User/sndcomplaints.html')

def sndcom_post(request):
    name = request.POST['name']
    date = request.POST['date']
    complaints_u = request.POST['com']

    obj = complaints()

    obj.Name = name
    obj.date = date
    obj.complaints = complaints_u

    obj.save()
    return HttpResponse("<script>alert('Sended Successfully');window.location='/sndcomplaints'</script>")



def vcomplaints(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = complaints.objects.all()
    return render(request, 'Admin/viewcomplaints.html', {'view':data})

def sndreplay(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'Admin/sendreplay.html',{"id":id})

def sndreplay_post(request,id):
    Sreplay = request.POST['sreplay']
    rdate = request.POST['date']

    complaints.objects.filter(id=id).update(replay=Sreplay,replay_date=rdate)
    return HttpResponse("<script>alert('Sended Successfully');window.location='/vcomplaints'</script>")

def viewreplay(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = complaints.objects.all()
    return render(request, 'User/viewreplay.html', {'view':data})

def service_mngt(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'Worker/serviceadd.html')

def smngt_post(request):
    Sname = request.POST['sname']
    Amount = request.POST['amn']


    obj = service()

    obj.SName = Sname
    obj.amount = Amount

    obj.save()

    return HttpResponse("<script>alert('Added Successfully');window.location='/service_mngt'</script>")

def editservice(request,id):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = service.objects.get(id=id)
    return render(request, 'Worker/editservice.html', {'view':data})

def editservice_post(request,id):
    Sname = request.POST['sname']
    Amount = request.POST['amn']
    service.objects.filter(id=id).update(SName=Sname,amount=Amount)
    return HttpResponse("<script>alert('Edited Successfully');window.location='/viewservice'</script>")

def delete_service(request,id):
    service.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/viewservice'</script>")



def viewservice(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    ser = service.objects.all()
    return render(request, 'Worker/viewservice.html', {'view': ser})

def viewserviceuser(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    ser = service.objects.all()
    return render(request, 'User/viewserviceuser.html', {'view': ser})

def sndrequest(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'User/sndrequest.html')

def req_post(request):
    name = request.POST['name']
    date = request.POST['date']
    address = request.POST['addr']
    sname = request.POST['ser']


    ob = user()
    ob.UName = name
    ob.Address = address
    ob.save()

    obj = service()
    obj.SName = sname
    obj.save()

    ab = servicerequest()
    ab.date = date
    ab.status = "pending"
    ab.USER = ob
    ab.SERVICE = obj
    ab.save()



    return HttpResponse("<script>alert('Added Successfully');window.location='/sndrequest'</script>")


def viewservicereq(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    ser = servicerequest.objects.filter(status='pending')
    return render(request,'Worker/viewrequest.html',{'view': ser})

def approvereq(request,id):

     servicerequest.objects.filter(id=id).update(status='approved')
     return HttpResponse("<script>alert('Approved');window.location = '/viewverifiedreq'</script>")

def rejectrq(request,id):
    servicerequest.objects.filter(id=id).update(status='reject')
    return HttpResponse("<script>alert('Rejected');window.location = '/viewservicereq'</script>")

def viewverifiedreq(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    ser=servicerequest.objects.filter(status='approved')
    return render(request,'worker/verifiedreq.html',{'view':ser})





def sndratings(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    return render(request, 'User/sndratings.html')

def rating_post(request):
    Date = request.POST['date']
    rating = request.POST['rate']


    obj = ratings()
    obj.date = Date
    obj.Ratings = rating
    obj.save()


    return HttpResponse("<script>alert('Sended Successfully');window.location='/sndratings'</script>")


def viewratings(request):
    if request.session['lin']!="lg":
        return HttpResponse("<script>alert('Pleaselogin');window.location='/'</script>")
    data = ratings.objects.filter(WORKER__LOGIN=request.session['lid'])
    return render(request, 'Worker/viewratings.html', {'view': data})

def forgetpassword(request):
    return render(request,'forgot password.html')

def forgotpassword_post(request):
    Email = request.POST['email']
    d=login.objects.filter(username=Email)
    if d.exists():
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("abhinavmohan778@gmail.com", "jtap wmdt lvcp amer")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "abhinavmohan778@gmail.com"
        msg['To'] = d[0].username
        msg['Subject'] = "Your Password for Smart Donation Website"
        body = "Your Password is:- - " + str(d[0].password)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("<script>alert('password send successfully');window.location='/'</script>")

    else:
        return HttpResponse("<script>alert('password not sended');window.location='/'</script>")















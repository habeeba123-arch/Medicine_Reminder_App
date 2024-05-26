from flask import Flask, render_template, request, redirect, session, jsonify
from DBConnection import Db

app = Flask(__name__)
app.secret_key="bjvgvhb"




@app.route('/rn')
def rn():
    return render_template("admin/index.html")


@app.route('/doc_chat')
def doc_chat():
    return render_template('doctor/chat.html')

@app.route("/chatview",methods=['post'])
def chatview():
    db=Db()
    qry = "select * from care_taker"
    res = db.select(qry)
    return jsonify(data=res)



@app.route('/addhealthtips')
def addhealthtips():
    return render_template("admin/adminaddhealthtips.html")

@app.route('/viewhealthtips')
def viewhealthtips():
    db=Db()
    qry="SELECT *  FROM `heralthtips`"
    db=Db()
    res=db.select(qry)

    return render_template("admin/admin_view_healthtips.html",data=res)





@app.route('/andviewhealthtips')
def andviewhealthtips():
    db=Db()
    qry="SELECT *  FROM `heralthtips`"
    db=Db()
    res=db.select(qry)

    return jsonify(status='ok',data=res)





@app.route('/healthtipdelete/<id>')
def healthtipdelete(id):
    db=Db()
    qry="DELETE FROM `heralthtips` WHERE `tipid`='"+id+"'"
    db=Db()
    db.delete(qry)
    return "<script>alert('Health tip deleted successfully');window.location='/viewhealthtips'</script>"


@app.route('/addhealthtippost', methods=['POST'])
def addhealthtippost():
    title= request.form["title"]
    details= request.form["details"]

    db=Db()
    qry="INSERT INTO `heralthtips` (`tipname`,`tipdetails`) VALUES ('"+title+"','"+details+"')"
    db.insert(qry)

    return "<script>alert('Health tip added successfully');window.location='/addhealthtips'</script>"

@app.route("/doc_msg/<id>")        # refresh messages chatlist
def doc_msg(id):
    db = Db()
    qry = "select from_id,message as msg,date,chat_id from chat where (from_id='"+str(session['lid'])+"' and to_id='" +str(id) + "') or ((from_id='" + str(id) + "' and to_id='"+str(session['lid'])+"')) order by chat_id desc"
    res = db.select(qry)

    qry1 = "select * from care_taker where lid='" + str(id) + "'"
    res1 = db.selectOne(qry1)
    print(qry1)
    print(res1)
    return jsonify(data=res,name=res1["caretaker_name"],photo='',user_lid=res1["lid"])

@app.route("/doc_insert_chat/<msg>/<id>")
def doc_insert_chat(msg,id):
    db=Db()
    qry="insert into chat (date,from_id,to_id,message) values (curdate(),'"+str(session['lid'])+"','"+str(id)+"','"+msg+"')"
    db.insert(qry)
    return jsonify(status="ok")

@app.route('/')
@app.route('/login')
def login():
    return render_template("index.html")

@app.route('/logout')
def logout():
    session['lid']=''
    return redirect('/')

@app.route('/login_post', methods=['POST'])
def login_post():
    username=request.form['email']
    password=request.form['password']
    db=Db()
    qry="SELECT * FROM login WHERE username='"+username+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        session['lid']=res['lid']
        if res['type']=="admin":
            return redirect('/a_home')
        elif res['type']=="doctor":
            return '''<script>alert('logined successfully..');window.location='/doc_home'</script>'''
        elif res['type']=='hospital':
            return redirect('/hoshome')
        else:
            return "<script>alert('invalid password or user name');window.location='/'</script>"
    else:
        return "<script>alert('invalid user name or password');window.location='/'</script>"





@app.route('/view_user')
def view_user():
    db=Db()
    qry="SELECT * FROM `user`"
    res=db.select(qry)
    return render_template("admin/admin view user.html",data=res)

@app.route('/view_user_post', methods=['POST'])
def view_user_post():
    search=request.form["textfield"]
    db = Db()
    qry = "SELECT * FROM `user` WHERE user_name LIKE '%"+search+"%'"
    res = db.select(qry)
    return render_template("admin/admin view user.html", data=res)


@app.route('/view_doctor')
def view_doctor():
    db=Db()
    qry="select * from`doctor`join `schedule`on schedule.`doc_lid`=`doctor`.`lid`"
    res=db.select(qry)
    return render_template("admin/admin view doctor.html",data=res)

@app.route('/view_doctor_post', methods=['POST'])
def view_doctor_post():
    search=request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `doctor` WHERE doc_name='%"+search+"%'"
    res = db.select(qry)
    return render_template("admin/admin view doctor.html", data=res)





@app.route('/view_complaints')
def view_complaints():
    db=Db()
    qry="SELECT * FROM complaint JOIN care_taker ON complaint.lid=care_taker.lid"
    res=db.select(qry)
    return render_template("admin/admin view complaints.html",data=res)



@app.route('/send_replay/<id>')
def send_replay(id):
   return render_template("admin/admin send replay.html",id=id)


@app.route('/send_reply_post', methods=['POST'])
def send_reply_post():
    id=request.form['id']
    reply=request.form['textarea']
    db=Db()
    qry="UPDATE complaint SET `replay`='"+reply+"' WHERE complaint_id='"+id+"'"
    res=db.update(qry)
    return "<script>alert('Successfull');window.location='/view_complaints'</script>"


@app.route('/change_password')
def change_password():
    return render_template("admin/change password.html")

@app.route('/change_password_post', methods=['POST'])
def change_password_post():
    current_password=request.form['textfield']
    new_password=request.form['textfield2']
    confirm_password=request.form['textfield3']
    db=Db()
    qry="SELECT * FROM `login` WHERE `password`='"+current_password+"' AND lid='"+str(session['lid'])+"'"
    res=db.selectOne(qry)
    if res is not None:
        if new_password==confirm_password:
            qry2="UPDATE login SET PASSWORD='"+new_password+"' WHERE lid='"+str(session['lid'])+"'"
            res=db.update(qry)
            return "<script>('successfull');window.location='/'</script>"
        else:
            return "<script>alert('Password doesn't match');window.location='/change_password'</script>"
    else:
        return "<script>alert('your current password doesn't match');window.location='/change_password'</script>"


@app.route('/a_home')
def a_home():
    return render_template('admin/adminindex.html')


#====================Doctor======================


@app.route('/registration')
def registration():
    return render_template("doctor/doctor registration.html")

@app.route('/registration_post', methods=['POST'])
def registration_post():
    name=request.form['textfield']
    from datetime import datetime
    photo=request.files['file']
    date=datetime.now().strftime("%Y%m%d%H%M%S")
    photo.save(r"C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\doctor_img\\"+date+".jpg")
    path="/static/doctor_img/"+date+".jpg"

    email=request.form['textfield3']
    phno=request.form['textfield4']
    password=request.form['textfield5']
    gender=request.form['radio']
    department=request.form['textfield6']
    place=request.form['textfield7']
    pin=request.form['textfield8']
    dob=request.form['textfield9']
    experience=request.form['textfield10']
    qualification=request.form['textfield11']
    db=Db()
    qry="INSERT INTO `login`(`username`,`password`,`type`)VALUES('"+email+"','"+password+"','doctor')"
    res=db.insert(qry)
    qry1="INSERT INTO `doctor`(`lid`,`doc_name`,`photo`,`department`,`experience`,`qualification`,`gender`,`DOB`,`place`,`pin`,`phno`,`email`)VALUES('"+str(res)+"','"+name+"','"+path+"','"+department+"','"+experience+"','"+qualification+"','"+gender+"','"+dob+"','"+place+"','"+pin+"','"+phno+"','"+email+"')"
    # qry1="INSERT INTO `doctor`(`lid`,`doc_name`,`photo`,`department`,`experience`,`qualification`,`gender`,`DOB`,`place`,`pin`,`phno`,`email`)VALUES('"+str(res)+"','"+name+"','"+path+"','"+department+"','"+experience+"','"+qualification+"','"+gender+"','"+dob+"','"+place+"',''"+pin+"','"+phno+"','"+email+"')"
    res1=db.insert(qry1)
    return "<script>alert('registerd successfully..');window.location='/'</script>"








@app.route('/view_patient')
def view_patient():

    qry="SELECT * FROM `patient`"
    db=Db()
    data= db.select(qry)
    return render_template("doctor/doctor view patient.html",data=data)





@app.route('/view_patientpost',methods=['post'])
def view_patientpost():
    name= request.form["name"]

    qry="SELECT * FROM `patient` where patient_name like '%"+name+"%'"
    db=Db()
    data= db.select(qry)
    return render_template("doctor/doctor view patient.html",data=data)



@app.route('/schedule_management')
def schedule_management():
    return render_template("doctor/doctor schedule management.html")

@app.route('/schedule_management_post', methods=['post'])
def schedule_management_post():
    date=request.form['textfield']
    from_time=request.form['textfield2']
    to_time=request.form['textfield3']
    db=Db()
    qry="INSERT INTO `schedule`(`doc_lid`,`time_from`,`time_to`,`date`)VALUES('"+str(session['lid'])+"','"+from_time+"','"+to_time+"','"+date+"')"
    res=db.insert(qry)
    return "<script>alert('Added');window.location='/schedule_management'</script>"




@app.route('/view_doctor_schedule')
def view_doctor_schedule():
    db=Db()
    qry="SELECT * FROM `schedule` WHERE`doc_lid`='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template("doctor/doctor view schedule .html", data=res)

@app.route('/delete_doctor_schedule/<id>')
def delete_doctor_schedule(id):
    db=Db()
    qry="DELETE FROM `schedule` WHERE `schedule_id`='"+id+"'"
    res=db.delete(qry)
    return "<script>alert('delete');window.location='/view_doctor_schedule'</script>"


@app.route('/edit_doctor_schedule/<id>')
def edit_schedule_management(id):
    db=Db()
    qry="SELECT * FROM `schedule`WHERE`schedule_id`='"+id+"'"
    res=db.selectOne(qry)
    print(res)
    return render_template("doctor/edit schedule management.html" ,data=res)


@app.route('/edit_schedule_management_post',methods=['POST'])
def edit_schedule_management_post():
    db=Db()
    id=request.form['id']
    date=request.form['textfield']
    time_from=request.form['textfield2']
    time_to=request.form['textfield3']
    qry="UPDATE `schedule` SET  `time_from`='"+time_from+"',`time_to`='"+time_to+"',`date`='"+date+"' WHERE `schedule_id`='"+id+"'"
    res=db.update(qry)
    return "<script>alert('edit');window.location='/view_doctor_schedule'</script>"



@app.route('/view_booking/<id>')
def view_booking(id):
    db=Db()
    qry="SELECT * FROM `booking` INNER JOIN `care_taker` ON `care_taker`.`lid`=`booking`.`patient_id` WHERE `schedule_id`='"+id+"'"
    res=db.select(qry)
    return render_template("doctor/view_booking.html",data=res)

@app.route('/send_complaints')
def send_complaints():
    return render_template("doctor/doctor_send_complaints.html")

@app.route('/send_complaints_post',methods=['POST'])
def send_complaints_post():
    db=Db()
    complaint=request.form['textfield']
    qry="INSERT INTO`complaint`(`lid`,`user_id`,`complaint`,`status`,`date`,`replay`) VALUES('"+str(session['lid'])+"','','"+complaint+"','pending',curdate(),'pending')"
    res=db.insert(qry)
    return "<script>alert('');window.location='/send_complaints'</script>"


@app.route('/doctor_view_replay')
def doctor_view_replay():
    db=Db()
    qry="SELECT * FROM `complaint`WHERE lid='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template("doctor/doctor_view_replay.html",data=res)








@app.route('/doctor_change_password')
def doctor_change_password():
    return render_template("doctor/doctor change password.html")


@app.route('/doctor_change_password_post', methods=['POST'])
def doctor_change_password_post():
    current_password=request.form['textfield']
    new_password=request.form['textfield2']
    confirm_password=request.form['textfield3']
    db = Db()
    qry = "SELECT * FROM `login` WHERE `password`='" + current_password + "' AND lid='" + str(session['lid']) + "'"
    res = db.selectOne(qry)
    if res is not None:
        if new_password == confirm_password:
            qry2 = "UPDATE login SET PASSWORD='" + new_password + "' WHERE lid='" + str(session['lid']) + "'"
            res = db.update(qry2)
            return "<script>('successfull');window.location='/'</script>"
        else:
            return "<script>alert('Password doesn't match');window.location='/doctor_change_password'</script>"
    else:
        return "<script>alert('your current password doesn't match');window.location='/doctor_change_password'</script>"










@app.route('/view_doctor_profile')
def view_doctor_profile():
    db=Db()
    qry="SELECT * FROM `doctor` WHERE `lid`='"+str(session['lid'])+"'"
    res=db.selectOne(qry)
    return render_template("doctor/doctor_view_profile.html",data=res)

@app.route('/edit_profile')
def edit_profile():
    db=Db()
    qry="SELECT * FROM `doctor` WHERE `lid`='"+str(session['lid'])+"'"
    res=db.selectOne(qry)
    return render_template("doctor/edit_profile.html",data=res)


@app.route('/edit_profile_post',methods=['post'])
def edit_profile_post():
    db=Db()
    name = request.form['textfield']
    email = request.form['textfield3']
    phno = request.form['textfield4']
    gender = request.form['radio']
    department = request.form['textfield6']
    place = request.form['textfield7']
    pin = request.form['textfield8']
    dob = request.form['textfield9']
    experience = request.form['textfield10']
    qualification = request.form['textfield11']
    if 'file' in request.files:
        photo = request.files['file']
        if photo.filename !="":
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d%H%M%S")
            photo.save(r"C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\doctor_img\\" + date + ".jpg")
            path = "/static/doctor_img/" + date + ".jpg"
            qry="UPDATE `doctor` SET `doc_name`='"+name+"',`photo`='"+path+"',`department`='"+department+"',`experience`='"+experience+"',`qualification`='"+qualification+"',`gender`='"+gender+"',`DOB`='"+dob+"',`place`='"+place+"',`pin`='"+pin+"',`phno`='"+phno+"',`email`='"+email+"' WHERE `lid`='"+str(session['lid'])+"'"
            res=db.update(qry)
            return "<script>alert('updated');window.location='/view_doctor_profile'</script>"
        else:
            qry = "UPDATE `doctor` SET `doc_name`='" + name + "',`department`='" + department + "',`experience`='" + experience + "',`qualification`='" + qualification + "',`gender`='" + gender + "',`DOB`='" + dob + "',`place`='" + place + "',`pin`='" + pin + "',`phno`='" + phno + "',`email`='" + email + "' WHERE `lid`='" + str(
                session['lid']) + "'"
            res = db.update(qry)
            return "<script>alert('updated');window.location='/view_doctor_profile'</script>"
    else:
        qry = "UPDATE `doctor` SET `doc_name`='" + name + "',`department`='" + department + "',`experience`='" + experience + "',`qualification`='" + qualification + "',`gender`='" + gender + "',`DOB`='" + dob + "',`place`='" + place + "',`pin`='" + pin + "',`phno`='" + phno + "',`email`='" + email + "' WHERE `lid`='" + str(
            session['lid']) + "'"
        res = db.update(qry)
        return "<script>alert('updated');window.location='/view_doctor_profile'</script>"



@app.route('/adminviewhospital')
def adminviewhospital():
    qry="SELECT * FROM `hospital`"
    db=Db()
    res= db.select(qry)

    return render_template("admin/admin view hospital.html",data=res)



# @app.route('/dochome')
# def dochome():
#     return render_template('doctor/dochome.html')


@app.route('/doc_home')
def doc_home():
    return render_template("doctor/index.html")

@app.route('/hospital_registration')
def hospital_registration():
    return render_template("hospital/hospital registration.html")

@app.route('/hospital_registration_post', methods=['POST'])
def hospital_registration_post():
    hospital_name=request.form['textfield']
    photo=request.files['imageField']
    from datetime import datetime
    date = datetime.now().strftime("%d%m%y-%H%M%S")
    photo.save("C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\hospital_image\\" + date + ".jpg")
    path = "/static/hospital_image/"+date+".jpg"
    place=request.form['textfield2']
    phno=request.form['textfield3']
    email=request.form['textfield5']
    password=request.form['textfield6']
    confirm_password=request.form['textfield7']
    db = Db()
    qry =" INSERT INTO `login`(`username`,`password`,`type`)VALUES('"+email+"','"+password+"','hospital')"
    res = db.insert(qry)

    qry1 = "INSERT INTO hospital (`lid`,`hospital_name`,`photo`,`place`,`email`,`phone_no`)VALUES('"+str(res)+"','"+hospital_name+"','"+path+"','"+place+"','"+email+"','"+phno+"')"
    res1 = db.insert(qry1)

    return "<script>alert('registerd successfully..');window.location='/'</script>"





@app.route('/hospital_add_doctor')
def hospital_add_doctor():
    return render_template("hospital/hospital add doctor.html")
@app.route('/hospital_add_doctor_post', methods=['POST'])
def hospital_add_doctor_post():
    name = request.form['textfield']
    from datetime import datetime
    photo = request.files['file']
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    photo.save(r"C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\doctor_img\\" + date + ".jpg")
    path = "/static/doctor_img/" + date + ".jpg"

    email = request.form['textfield3']
    phno = request.form['textfield4']
    import random
    password = random.randint(0000,9999)
    gender = request.form['radio']
    department = request.form['textfield6']
    place = request.form['textfield7']
    pin = request.form['textfield8']
    dob = request.form['textfield9']
    experience = request.form['textfield10']
    qualification = request.form['textfield11']
    db = Db()
    qry = "INSERT INTO `login`(`username`,`password`,`type`)VALUES('" + email + "','" + str(password) + "','doctor')"
    res = db.insert(qry)
    qry1 = "INSERT INTO `doctor`(`lid`,`doc_name`,`photo`,`department`,`experience`,`qualification`,`gender`,`DOB`,`place`,`pin`,`phno`,`email`,hlid)VALUES('" + str(
        res) + "','" + name + "','" + path + "','" + department + "','" + experience + "','" + qualification + "','" + gender + "','" + dob + "','" + place + "','" + pin + "','" + phno + "','" + email + "','"+str(session['lid'])+"')"
    # qry1="INSERT INTO `doctor`(`lid`,`doc_name`,`photo`,`department`,`experience`,`qualification`,`gender`,`DOB`,`place`,`pin`,`phno`,`email`)VALUES('"+str(res)+"','"+name+"','"+path+"','"+department+"','"+experience+"','"+qualification+"','"+gender+"','"+dob+"','"+place+"',''"+pin+"','"+phno+"','"+email+"')"
    res1 = db.insert(qry1)
    return "<script>alert('registerd successfully..');window.location='/hoshome'</script>"


@app.route('/hospital_view_doctors')
def hospital_view_doctors():
    db=Db()
    qry="SELECT * FROM `doctor`WHERE`hlid`='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template("hospital/hospital view doctors.html",data=res)

@app.route('/edit_doctor/<id>')
def edit_doctor(id):
    db=Db()
    qry="SELECT * FROM `doctor` WHERE `lid`='"+id+"'"
    res=db.selectOne(qry)
    return render_template("hospital/hospital edit doctor.html",data=res)

@app.route('/edit_doctor_post',methods=['post'])
def edit_doctor_post():
    db=Db()
    name = request.form['textfield']
    email = request.form['textfield3']
    phno = request.form['textfield4']
    gender = request.form['radio']
    department = request.form['textfield6']
    place = request.form['textfield7']
    pin = request.form['textfield8']
    dob = request.form['textfield9']
    experience = request.form['textfield10']
    qualification = request.form['textfield11']
    if 'file' in request.files:
        photo = request.files['file']
        if photo.filename !="":
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d%H%M%S")
            photo.save(r"C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\doctor_img\\" + date + ".jpg")
            path = "/static/doctor_img/" + date + ".jpg"
            qry="UPDATE `doctor` SET `doc_name`='"+name+"',`photo`='"+path+"',`department`='"+department+"',`experience`='"+experience+"',`qualification`='"+qualification+"',`gender`='"+gender+"',`DOB`='"+dob+"',`place`='"+place+"',`pin`='"+pin+"',`phno`='"+phno+"',`email`='"+email+"' WHERE `lid`='"+str(session['lid'])+"'"
            res=db.update(qry)
            return "<script>alert('updated');window.location='/hospital_view_doctors'</script>"
        else:
            qry = "UPDATE `doctor` SET `doc_name`='" + name + "',`department`='" + department + "',`experience`='" + experience + "',`qualification`='" + qualification + "',`gender`='" + gender + "',`DOB`='" + dob + "',`place`='" + place + "',`pin`='" + pin + "',`phno`='" + phno + "',`email`='" + email + "' WHERE `lid`='" + str(
                session['lid']) + "'"
            res = db.update(qry)
            return "<script>alert('updated');window.location='/hospital_view_doctors'</script>"
    else:
        qry = "UPDATE `doctor` SET `doc_name`='" + name + "',`department`='" + department + "',`experience`='" + experience + "',`qualification`='" + qualification + "',`gender`='" + gender + "',`DOB`='" + dob + "',`place`='" + place + "',`pin`='" + pin + "',`phno`='" + phno + "',`email`='" + email + "' WHERE `lid`='" + str(
            session['lid']) + "'"
        res = db.update(qry)
        return "<script>alert('updated');window.location='/hospital_view_doctors'</script>"





# @app.route('/edit_profile_post',methods=['post'])
# def edit_profile_post():
#     db=Db()
#     name = request.form['textfield']
#     email = request.form['textfield3']
#     phno = request.form['textfield4']
#     gender = request.form['radio']
#     department = request.form['textfield6']
#     place = request.form['textfield7']
#     pin = request.form['textfield8']
#     dob = request.form['textfield9']
#     experience = request.form['textfield10']
#     qualification = request.form['textfield11']
#     if 'file' in request.files:
#         photo = request.files['file']
#         if photo.filename !="":
#             from datetime import datetime
#             date = datetime.now().strftime("%Y%m%d%H%M%S")
#             photo.save(r"C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\doctor_img\\" + date + ".jpg")
#             path = "/static/doctor_img/" + date + ".jpg"
#             qry="UPDATE `doctor` SET `doc_name`='"+name+"',`photo`='"+path+"',`department`='"+department+"',`experience`='"+experience+"',`qualification`='"+qualification+"',`gender`='"+gender+"',`DOB`='"+dob+"',`place`='"+place+"',`pin`='"+pin+"',`phno`='"+phno+"',`email`='"+email+"' WHERE `lid`='"+str(session['lid'])+"'"
#             res=db.update(qry)
#             return "<script>alert('updated');window.location='/view_doctor_profile'</script>"
#         else:
#             qry = "UPDATE `doctor` SET `doc_name`='" + name + "',`department`='" + department + "',`experience`='" + experience + "',`qualification`='" + qualification + "',`gender`='" + gender + "',`DOB`='" + dob + "',`place`='" + place + "',`pin`='" + pin + "',`phno`='" + phno + "',`email`='" + email + "' WHERE `lid`='" + str(
#                 session['lid']) + "'"
#             res = db.update(qry)
#             return "<script>alert('updated');window.location='/view_doctor_profile'</script>"
#     else:
#         qry = "UPDATE `doctor` SET `doc_name`='" + name + "',`department`='" + department + "',`experience`='" + experience + "',`qualification`='" + qualification + "',`gender`='" + gender + "',`DOB`='" + dob + "',`place`='" + place + "',`pin`='" + pin + "',`phno`='" + phno + "',`email`='" + email + "' WHERE `lid`='" + str(
#             session['lid']) + "'"
#         res = db.update(qry)
#         return "<script>alert('updated');window.location='/view_doctor_profile'</script>"
#










@app.route('/delete_doctor/<id>')
def delete_doctor(id):
    db=Db()
    qry="DELETE FROM `doctor`WHERE `lid`='"+id+"'"
    res=db.delete(qry)
    return "<script>alert('delete');window.location='/view_doctor_schedule'</script>"










@app.route('/hospital_view_patient')
def hospital_view_patient():

    db=Db()
    qry="SELECT * FROM `patient`"
    res=db.select(qry)

    return render_template("hospital/hospital view patient.html",data=res)

@app.route('/hospital_view_patient_post', methods=['POST'])
def hospital_view_patient_post():
    search=request.form['textfield']
    db = Db()
    qry = "SELECT * FROM `patient` WHERE patient_name='%"+search+"%'"
    res = db.select(qry)
    return render_template("hospital/hospital view patient.html", data=res)



@app.route('/hospital_view_complaints')
def hospital_view_complaints():
    db = Db()
    qry = "SELECT * FROM complaint JOIN doctor ON complaint.lid=doctor.lid"
    res = db.select(qry)
    return render_template("hospital/hospital view complaints.html",data=res)


@app.route('/hospital_send_replay/<id>')
def hospital_send_replay(id):
    return render_template("hospital/hospital send replay.html",id=id)

@app.route('/hospital_send_reply_post', methods=['POST'])
def hospital_send_reply_post():
    id=request.form['id']
    reply=request.form['textarea']
    db=Db()
    qry="UPDATE complaint SET `replay`='"+reply+"', status='replayed' WHERE cid='"+id+"'"
    res=db.update(qry)
    return "<script>alert('Successfull');window.location='/hospital_view_complaints'</script>"


@app.route('/hospital_change_password')
def hospital_change_password():
    return render_template("hospital/hospital change password.html")

@app.route('/hospital_change_password_post', methods=['POST'])
def hospital_change_password_post():
    current_password=request.form['textfield']
    new_password=request.form['textfield2']
    confirm_password=request.form['textfield3']
    db = Db()
    qry = "SELECT * FROM `login` WHERE `password`='" + current_password + "' AND lid='" + str(session['lid']) + "'"
    res = db.selectOne(qry)
    print(res)
    if res is not None:
        if new_password == confirm_password:
            qry2 = "UPDATE login SET PASSWORD='" + new_password + "' WHERE lid='" + str(session['lid']) + "'"
            res = db.update(qry2)
            return "<script>('successfull');window.location='/'</script>"
        else:
            return "<script>alert('Password doesn't match');window.location='/hospital_change_password'</script>"
    else:
        return "<script>alert('your current password doesn't match');window.location='/hospital_change_password'</script>"



@app.route('/hoshome')
def hoshome():
    return render_template("hospital/index.html")







######################3


#patient

@app.route('/and_login_post', methods=['POST'])
def and_login_post():
    username=request.form['email']
    password=request.form['password']
    db=Db()
    qry="SELECT * FROM login WHERE username='"+username+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        return jsonify(status="ok",lid=res['lid'])
    else:
        return jsonify(status="no")

@app.route('/and_view_hospital_post')
def and_view_hospital_post():
    db=Db()
    qry="SELECT * FROM`hospital`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_view_doctor_post')
def and_view_doctor_post():
    hlid=request.form['hlid']
    db=Db()
    qry="SELECT * FROM `doctor`WHERE `hlid`='"++"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)




@app.route('/and_view_profile_post')
def and_view_profile_post():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM `patient` WHERE `patient_id`='"++"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_alarms_post')
def and_alarms_post():
    return jsonify(status="ok")

@app.route('/and_tips_review')
def and_tips_review_post():
    return jsonify(status="ok")

@app.route('/and_video_call_post')
def and_video_call_post ():
    return jsonify(status="ok")


@app.route('/and_taken_medicine_history')
def and_taken_medicine_history_post():
    return jsonify(status="ok")



@app.route('/user_login', methods=['POST'])
def user_login():
    username= request.form["username"]
    password= request.form["password"]
    db=Db()
    qry="SELECT * FROM login WHERE username='"+username+"' AND PASSWORD='"+password+"'"
    res= db.selectOne(qry)
    if res is None:
        return jsonify(status='no')
    else:
        return jsonify(status='ok',lid= res['lid'], type= res['type'])

@app.route('/and_caretaker_register', methods=['POST'])
def user_register():
    name= request.form["name"]
    place= request.form["place"]
    email= request.form["email"]
    phone= request.form["phone"]
    img= request.form["img"]
    from  datetime import  datetime
    fname= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    import base64
    with open("C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\caretaker\\"+ fname,"wb") as w:
        w.write(base64.b64decode(img))
    path="/static/caretaker/"+ fname
    password= request.form["password"]
    qry="INSERT INTO `login` (`username`,`password`,`type`) VALUES ('"+email+"','"+password+"','caretaker')"
    db=Db()
    lid= db.insert(qry)
    qry="insert into `care_taker` (`lid`,`caretaker_name`,`place`,`email`,`phone_no`,`photo`) values ('"+str(lid)+"','"+name+"','"+place+"','"+email+"','"+phone+"','"+path+"')"
    db.insert(qry)
    return jsonify(status='ok')

@app.route('/and_add_patient', methods=['POST'])
def and_add_patient():
    name= request.form["name"]
    place= request.form["place"]
    email= request.form["email"]
    phone= request.form["phone"]
    age= request.form["age"]
    img= request.form["img"]
    clid= request.form["clid"]
    from  datetime import  datetime
    fname= datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    import base64
    with open("C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\patient\\"+ fname,"wb") as w:
        w.write(base64.b64decode(img))
    path="/static/patient/"+ fname
    password= request.form["password"]
    qry="INSERT INTO `login` (`username`,`password`,`type`) VALUES ('"+email+"','"+password+"','patient')"
    db=Db()
    lid= db.insert(qry)
    qry="INSERT INTO `patient` (`lid`,`patient_name`,`age`,`place`,`phone_no`,`email`,`cid`,photo) VALUES ('"+str(lid)+"','"+name+"','"+age+"','"+place+"','"+phone+"','"+email+"','"+clid+"','"+path+"')"
    db.insert(qry)
    return jsonify(status='ok')


@app.route('/addmodes', methods=['POST'])
def addmodes():
    plid= request.form["plid"]
    ringmode= request.form["ring"]
    touch= request.form["touch"]
    db = Db()

    qry="select * from `modesettings` where `plid`='"+plid+"'"
    res= db.selectOne(qry)

    if res is None:
        qry="INSERT INTO `modesettings` (`plid`,`touch`,`ringmode`) VALUES ('"+plid+"','"+touch+"','"+ringmode+"')"
        db.insert(qry)
        return jsonify(status='ok')
    else:
        qry="update modesettings set touch='"+touch+"',ringmode='"+ringmode+"' where plid='"+plid+"'"
        print(qry)
        return jsonify(status='ok')

    return jsonify(status='ok')



@app.route('/viewmode', methods=['POST'])
def viewmode():
    plid= request.form["plid"]

    qry="select * from modesettings where plid='"+plid+"'"
    db=Db()
    res= db.selectOne(qry)
    if res is None:
        return jsonify(status='no')
    else:
        return jsonify(status='ok',data=res)



@app.route('/addalaram', methods=['POST'])
def addalaram():
    alramtime= request.form["alramtime"]
    date= request.form["date"]
    alaram= request.form["alaram"]
    plid= request.form["plid"]

    qry="INSERT INTO `alaram` (`plid`,`alramtime`,`date`,`alaram`) VALUES ('"+plid+"','"+alramtime+"','"+date+"','"+alaram+"')"
    db=Db()
    db.insert(qry)

    return jsonify(status='ok')



@app.route('/and_bgservice', methods=['POST'])
def and_bgservice():
    lid= request.form["lid"]
    db=Db()
    qry="SELECT * FROM `modesettings` WHERE `plid`='"+lid+"'"
    res=db.selectOne(qry)
    if res is None:
        return jsonify(status='no')
    else:
        return jsonify(status='ok',data=res)





@app.route('/andtaken', methods=['POST'])
def andtaken():
    id= request.form["id"]
    qry="UPDATE `alaram` SET `status`='Taken' WHERE `alaramid`='"+id+"'"
    db=Db()
    db.update(qry)
    return jsonify(status='ok')


@app.route('/andnotaken', methods=['POST'])
def andnotaken():
    id= request.form["id"]
    qry="UPDATE `alaram` SET `status`='NotTaken' WHERE `alaramid`='"+id+"'"
    db=Db()
    db.update(qry)
    return jsonify(status='ok')







@app.route('/and_alaramservice', methods=['POST'])
def and_alaramservice():
    lid= request.form["lid"]

    from datetime import  datetime

    time= datetime.now().strftime("%H:%M")

    db=Db()
    qry="SELECT * FROM `alaram` WHERE `date`=CURDATE() AND `alramtime`='"+time+"' and plid='"+lid+"' and `status`='pending'"
    print(qry)
    res=db.select(qry)
    if len(res)>0:
        print(res[0])
        return jsonify(status='ok', data= res[0])
    else:
        return jsonify(status='no')



@app.route('/viewalaram', methods=['POST'])
def viewalaram():
    db=Db()
    plid= request.form["plid"]
    qry="Select * from `alaram` WHERE `plid`='"+plid+"'"
    res= db.select(qry)
    return jsonify(status='ok',data=res)

@app.route('/deletealaram', methods=['POST'])
def deletealaram():
    aid= request.form["aid"]
    db=Db()
    db.delete("DELETE FROM `alaram` WHERE `alaramid`='"+aid+"'")
    return jsonify(status='ok')




@app.route('/andviewpatient', methods=['POST'])
def andviewpatient():
    lid=request.form["lid"]
    db=Db()
    qry="select * from `patient` where `cid`='"+lid+"'"
    res=db.select(qry)
    print(res)
    print(qry)
    return jsonify(status='ok',data=res)


# @app.route('/and_view_profile_post',methods=['POST'])
# def and_view_profile_post():
#     db=Db()
#     qry="SELECT * FROM`care_taker`WHERE`caretaker_id`='"++"'"
#     res=db.select(qry)
#     return jsonify(status="ok",data=res)




@app.route('/and_update_profile_post',methods=['POST'])
def and_update_profile_post():
    caretaker_name=request.form['caretaker_name']
    place=request.form['place']
    phn_no=request.form['phn_no']
    email=request.form['email']
    lid=request.form['lid']
    db=Db()
    qry="UPDATE`care_taker`SET `caretaker_name`='"+caretaker_name+"',`place`='"+place+"',`email`='"+email+"',`phone_no`='"+phn_no+"'WHERE`lid`='"+lid+"'"
    return jsonify(status="ok")

@app.route('/and_medicine_alarm_post',methods=['POST'])
def and_medicine_alarm_post():
    return jsonify(status="ok")

# @app.route('/and_view_hospital_post',methods=['post'])
# def and_view_hospital_post():
#     db=Db()
#     qry="SELECT * FROM`hospital`"
#     res=db.select(qry)
#     return jsonify(status="ok",data=res)

# @app.route('/and_view_doctor_post',methods=['POST'])
# def and_view_doctor_post():
#     hlid=request.form['hlid']
#     db=Db()
#     qry="SELECT * FROM `doctor`WHERE `hlid`='"++"'"
#     res=db.select(qry)
#     return jsonify(status="ok",data=res)

@app.route('/and_view_schedule_post',methods=['POST'])
def and_view_schedule_post():
    doc_lid=request.form['doc_lid']
    db=Db()
    qry="SELECT * FROM `schedule`WHERE`doc_lid`='"++"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_add_booking_post',methods=['POST'])
def and_add_booking_post():
    schedule_id=request.form['schedule_id']
    patient_id=request.form['patient_id']
    db=Db()
    qry="INSERT INTO `booking` (`schedule_id`,`patient_id`,`date`,`time`,`status`)VALUES('"+schedule_id+"','"+patient_id+"',cur_date(),cur_time(),pending)"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_caretaker_send_complaint_post',methods=['post'])
def and_caretaker_send_complaint_post():
    lid=request.form['lid']
    complaint=request.form['complaint']
    db=Db()
    qry="INSERT INTO `complaint`(`lid`,`complaint`,`status`,`date`,`replay`)VALUES('"+lid+"','"+complaint+"','pending','cur_date()','pending')"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_view_reply_post',methods=['POST'])
def and_view_reply_post():
    lid=request.form['lid']
    db=Db()
    qry="select * from `complaint`where`lid`='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)



@app.route('/and_send_complaint_and_view_reply_post',methods=['POST'])
def and_send_complaint_and_view_reply_post():
    return jsonify(status="ok")

@app.route('/and_send_review_post',methods=['POST'])
def and_send_review_post():
    lid=request.form['lid']
    hospital_id=request.form['hospital_id']
    review=request.form['review']
    db=Db()
    qry="insert into `review`(`lid`,`hospital_id`,`review`)values('"+lid+"','"+hospital_id+"','"+review+"')"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_add_patient',methods=['POST'])
def and_add_patient_post():
    db=Db()
    patient_name=request.form['patient_name']
    age=request.form['age']
    place=request.form['place']
    phn_no=request.form['phn_no']
    email=request.form['email']
    password=request.form['password']
    cid=request.form['cid']

    qry2="INSERT INTO `login`(`username`,`password`,`type`)VALUES('"+email+"','"+password+"','patient')"
    res2=db.insert(qry2)
    qry="INSERT INTO `patient`(`patient_id`,`patient_name`,`age`,`place`,`phone_no`,`email`,`cid`)VALUES('"+str(res2)+"','"+patient_name+"','"+age+"','"+place+"','"+phn_no+"','"+email+"','"+cid+"')"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_view_patient_post',methods=['POST'])
def and_view_patient_post():
    db=Db()
    cid=request.form['cid']
    qry="select * from `patient`where `cid`='"+cid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_edit_patient_post',methods=['POST'])
def and_edit_patient_post():
    pid=request.form['pid']
    db=Db()
    qry="SELECT * FROM `patient`WHERE `lid`='"+pid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_caretaker_edit_patient_post',methods=['POST'])
def and_caretaker_edit_patient_post():
    patient_name=request.form['patient_name']
    age=request.form['age']
    place=request.form['place']
    phn_no=request.form['phn_no']
    email=request.form['email']
    pid=request.form['pid']
    db=Db()
    qry="UPDATE `patient`SET`patient_name`='"+patient_name+"',`age`='"+age+"',`place`='"+place+"',`phone_no`='"+phn_no+"',`email`='"+email+"'WHERE lid='"+pid+"'"
    res=db.update(qry)
    return jsonify(status="ok")

@app.route('/and_delete_patient_post', methods=['POST'])
def and_delete_patient_post():
    lid=request.form['lid']
    db=Db()
    qry="DELETE FROM `patient`WHERE `lid`='"+lid+"'"
    res=db.delete(qry)
    return jsonify(status="ok")


@app.route('/and_video_call_with_patient_',methods=['POST'])
def and_video_call_with_patient_post():
    return jsonify(status="ok")

@app.route('/and_change_password_post',methods=['POST'])
def and_change_password_post():
    current_password=request.form['textfield']
    new_password=request.form['textfield2']
    confirm_password=request.form['textfield3']
    db = Db()
    qry = "SELECT * FROM `login` WHERE `password`='" + current_password + "' AND lid='" + str(session['lid']) + "'"
    res = db.selectOne(qry)
    print(res)
    if res is not None:
            qry2 = "UPDATE login SET PASSWORD='" + new_password + "' WHERE lid='" + str(session['lid']) + "'"
            res = db.update(qry2)
            return jsonify(status="ok")
    else:
        return jsonify(status="no")




@app.route('/and_viewdoctors', methods=['POST'])
def and_viewdoctors():
    db=Db()
    qry="SELECT * FROM `doctor`"
    res=db.select(qry)
    return jsonify(status='ok',data=res)


@app.route('/view_doctorMore', methods=['POST'])
def view_doctorMore():
    lid=request.form["lid"]
    db=Db()
    qry="SELECT * FROM `doctor` where lid='"+lid+"'"
    res=db.selectOne(qry)

    qry="SELECT * FROM `schedule` WHERE doc_lid='"+lid+"'"
    res1=db.select(qry)


    return jsonify(status='ok',data=res,data1=res1)

@app.route('/user_bookSchedule', methods=['POST'])
def user_bookSchedule():
    ulid= request.form["ulid"]
    sid= request.form["sid"]

    db=Db()
    qry="INSERT INTO `booking` (`schedule_id`,`patient_id`,`date`,`status`) VALUES ('"+sid+"','"+ulid+"',CURDATE(),'pending')"
    db.insert(qry)

    return jsonify(status='ok')

@app.route('/andpredictsymptombased', methods=['POST'])
def andpredictsymptombased():
    s=["itching","skin_rash","nodal_skin_eruptions","continuous_sneezing","shivering","chills","joint_pain","stomach_pain","acidity","ulcers_on_tongue","muscle_wasting","vomiting","burning_micturition","spotting_ urination","fatigue","weight_gain","anxiety","cold_hands_and_feets","mood_swings","weight_loss","restlessness","lethargy","patches_in_throat","irregular_sugar_level","cough","high_fever","sunken_eyes","breathlessness","sweating","dehydration","indigestion","headache","yellowish_skin","dark_urine","nausea","loss_of_appetite","pain_behind_the_eyes","back_pain","constipation","abdominal_pain","diarrhoea","mild_fever","yellow_urine","yellowing_of_eyes","acute_liver_failure","fluid_overload","swelling_of_stomach","swelled_lymph_nodes","malaise","blurred_and_distorted_vision","phlegm","throat_irritation","redness_of_eyes","sinus_pressure","runny_nose","congestion","chest_pain","weakness_in_limbs","fast_heart_rate","pain_during_bowel_movements","pain_in_anal_region","bloody_stool","irritation_in_anus","neck_pain","dizziness","cramps","bruising","obesity","swollen_legs","swollen_blood_vessels","puffy_face_and_eyes","enlarged_thyroid","brittle_nails","swollen_extremeties","excessive_hunger","extra_marital_contacts","drying_and_tingling_lips","slurred_speech","knee_pain","hip_joint_pain","muscle_weakness","stiff_neck","swelling_joints","movement_stiffness","spinning_movements","loss_of_balance","unsteadiness","weakness_of_one_body_side","loss_of_smell","bladder_discomfort","foul_smell_of urine","continuous_feel_of_urine","passage_of_gases","internal_itching,toxic_look_(typhos)","depression","irritability","muscle_pain","altered_sensorium","red_spots_over_body","belly_pain","abnormal_menstruation","dischromic _patches","watering_from_eyes","increased_appetite","polyuria","family_history","mucoid_sputum","rusty_sputum","lack_of_concentration","visual_disturbances","receiving_blood_transfusion","receiving_unsterile_injections","coma","stomach_bleeding","distention_of_abdomen","history_of_alcohol_consumption","fluid_overload","blood_in_sputum","prominent_veins_on_calf","palpitations","painful_walking","pus_filled_pimples","blackheads","scurring","skin_peeling","silver_like_dusting","small_dents_in_nails","inflammatory_nails","blister","red_sore_around_nose","yellow_crust_ooze"]

    content= request.form["content"]
    import json

    print(content,"huraaaa",type(content))

    # return jsonify(status='no')
    #
    sa=json.loads(content)
    ms=[]
    for i in sa:
        ms.append(i['name'])


    test=[]

    for i in s:
        if i in ms:
            test.append(1)
        else:
            test.append(0)






    import pandas
    data= pandas.read_csv("C:\\Users\\bafis\\PycharmProjects\\mdicine reminder\\static\\training_data.csv")

    features= data.values[:,0:len(test)]
    labels= data.values[:,len(test)+1]

    print(features)


    print(labels)



    from sklearn.ensemble import RandomForestClassifier

    r= RandomForestClassifier()
    r.fit(features,labels)

    k=r.predict([test])

    return jsonify(status='ok',  result= k[0])


@app.route('/and_viewbooking', methods=['POST'])
def and_viewbooking():
    lid= request.form["lid"]
    db=Db()
    qry="SELECT *  from booking INNER JOIN `schedule` ON `booking`.`schedule_id`=`schedule`.`schedule_id` INNER JOIN `doctor` ON `doctor`.`lid`=`schedule`.`doc_lid` WHERE `booking`.`patient_id`='"+lid+"'"
    res=db.select(qry)

    print(qry)

    print(res)
    return jsonify(status='ok',data=res)




@app.route('/patientviewprofile', methods=['POST'])
def patientviewprofile():
    lid= request.form["lid"]
    qry="SELECT * FROM `patient` WHERE `lid`='"+lid+"'"
    db=Db()
    res=db.selectOne(qry)
    return jsonify(status='ok', data=res)


@app.route('/useraddhospitalreview', methods=['POST'])
def useraddhospitalreview():
    hlid= request.form["hlid"]
    review= request.form["review"]
    ulid= request.form["ulid"]

    db=Db()
    qry="INSERT INTO `review` (`user_id`,`hospital_id`,`review`) VALUES ('"+ulid+"','"+hlid+"','"+review+"')"
    db.insert(qry)

    return jsonify(status='ok')


@app.route('/andviewhospitals', methods=['POST'])
def andviewhospitals():

    db=Db()
    qry="select * from hospital"
    res= db.select(qry)

    return jsonify(status='ok',data=res)

@app.route('/andviewtips', methods=['POST'])
def andviewtips():

    db=Db()
    qry="select * from heralthtips"
    res= db.select(qry)

    return jsonify(status='ok',data=res)


@app.route('/user_Change_Password', methods=['POST'])
def user_Change_Password():
    lid= request.form["lid"]
    password= request.form["password"]

    qry="UPDATE `login` SET PASSWORD='"+password+"' WHERE `lid`='"+lid+"'"
    db=Db()
    db.update(qry)

    return jsonify(status='ok')


@app.route('/in_message', methods=['POST'])
def in_message():
    db=Db()
    fid=request.form["fid"]
    toid=request.form["toid"]
    msg=request.form["msg"]
    qry="INSERT INTO `chat` (`from_id`,`to_id`,`message`,`date`) VALUES ('"+fid+"','"+toid+"','"+msg+"',CURDATE())"
    db.insert(qry)
    return jsonify(status='ok')


@app.route('/view_message2', methods=['POST'])
def view_message2():
    db = Db()
    fid = request.form["fid"]
    toid = request.form["toid"]
    lastmsgid= request.form["lastmsgid"]

    qry="SELECT * FROM `chat` WHERE ((`from_id`='"+fid+"' AND `to_id`='"+toid+"') OR (`from_id`='"+toid+"' AND `to_id`='"+fid+"')) AND `chat_id`>"+ lastmsgid
    res=db.select(qry)

    return jsonify(status='ok')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')

import mysql.connector

constr = mysql.connector.connect(host="localhost", user="root", passwd="1312")
mycursor = constr.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS ALUMINI")
mycursor.execute("USE ALUMINI")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS ALUREG (ALU_ID VARCHAR(20) PRIMARY KEY,FIRST_NAME VARCHAR(20),LAST_NAME VARCHAR(20),DOB DATE,GENDER VARCHAR(10),ADD_CORR VARCHAR(20),ADD_OFFC VARCHAR(20),EMAIL_ADD VARCHAR(30),MOB_NO VARCHAR(10),CURR_CITY VARCHAR(20),URR_COMPANY VARCHAR(20),DESG VARCHAR(20),SESSION_FROM VARCHAR(4),SESSION_TO VARCHAR(4),BRANCH VARCHAR(20),APSWD VARCHAR(30))")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS EVENTS(EID VARCHAR(20) PRIMARY KEY,ENAME VARCHAR(30),EDATE DATE,EVENUE VARCHAR(20),STATUS VARCHAR(30))")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS SELECTED_EVENTS(ALU_ID VARCHAR(20),ALU_NAME VARCHAR(30),EID VARCHAR(20),ENAME VARCHAR(30),EDATE DATE,EVENUE VARCHAR(30),STATUS VARCHAR(30) DEFAULT 'WILL NOT ATTEND')")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS ADMIN(A_ID CHAR(10) PRIMARY KEY, A_NAME VARCHAR(20),A_GENDER CHAR(1), A_AGE INT(3),A_PHONE CHAR(10),A_PSWD VARCHAR(20))")


def add_admin():  # to register admin details
    a_id = input("Enter the Admin id : ")
    a_name = input("Enter the Admin Name: ")
    a_g = input("Enter Admin Genderr : ")
    a_age = int(input("Enter Admin age"))
    a_phone = input("Enter Admin phone number")
    a_pwd = input("Enter the password : ")
    ad = (a_id, a_name, a_g, a_age, a_phone, a_pwd)
    sql = "insert into admin  values (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, ad)
    constr.commit()


def admin_login():  # login module for registered admin
    print("\t\t========================================")
    print("\t\tWELCOME TO LOGIN MODULE OF ADMIN")
    print("\t\t=======================================")
    a_id = input("\t\tEnter Your Registered Admin Id:-")
    a_pwd = input("\t\tEnter Your Password:-")
    mycursor.execute("select a_id,a_pswd from admin where a_id=%s and a_pswd=%s", (a_id, a_pwd,))
    res = mycursor.fetchall()
    if len(res) == 0:  # not entered a valid alumini id or password
        print("\t\tPLEASE ENTER VALID ADMIN ID OR PASSWORD")
    else:
        while True:
            print("\t\t=====================================")
            print("\t\tYOU LOGGED IN SUCCEESSFULLY")
            print("\t\tWELCOME TO THE ADMIN MENU")
            print("\t|t===================================")
            print("\t\t1. TO ADD AN EVENT")
            print("\t\t2. TO VIEW EVENTS")
            print("\t\t3. TO DELETE AN EVENT")
            print("\t\t4. TO MODIFY EVENT DETAILS")
            print("\t\t5. TO VIEW ALUMINI DETAILS")
            print("\t\t6. TO VIEW ALUMINI DETAILS WHO WILL ATTEND THE PARTICULAR EVENT")
            print("\t\t7. EXIT")
            ch = int(input("\n\t\tKINDLY ENTER YOUR CHOICE:-"))
            if ch == 1:
                add_event()
            elif ch == 2:
                view_all_events()
            elif ch == 3:
                delete_event()
            elif ch == 4:
                update_event()
            elif ch == 5:
                view_all_aluminies()
            elif ch == 6:
                view_confirmed_aluminies()
            elif ch == 7:
                break
            else:
                print("\n\t\t PLEASE ENTER A VALID CHOICE")


def view_confirmed_aluminies():  # to view the list of confirmed alumini who attended a particular event
    eid = input("Enter the event id whose alumini you want to see:-")
    mycursor.execute("select * from selected_events where eid=%s and status='confirmed'", (eid,))
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\n\t\tNO ALUMINI RECORD EXISTS OR ENTER A VALID EVENT ID")
    else:
        for i in res:
            print("\t=============================================================================")
            print("\t\tYOUR SELECTED ALUMINI DETAILS FOR AN EVENT ARE:")
            print("\t============================================================================")
            print("\t\t ALUMINI ID:-", i[0])
            print("\t\t ALUMINI NAME:-", i[1])
            print("\t\tEVENT ID:-", i[2])
            print("\t\tEVENT NAME:-", i[3])
            print("\t\tEVENT DATE:-", i[4])
            print("\t\tEVENT VENUE:-", i[5])
            print("\t\tWILL ATTEND:-", i[6])
            print("\t================================================================================")


def view_all_aluminies():  # to view the details of all registerd aluminies
    mycursor.execute("select * from alureg")
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\n\t\tNO ALUMINI RECORD EXISTS")
    else:
        for i in res:
            print("\t\===============================================")
            print("\t\tALUMINI DETAILS ARE")
            print("\t====================================================")
            print("\t\tALUMINI ID:-", i[0])
            print("\t\tALUMINI NAME:-", i[1] + i[2])
            print("\t\tALUMINI DATE OF BIRTH:-", i[3])
            print("\t\tALUMINI GENDER:-", i[4])
            print("\t\tCORRESPONDANCE ADDRESS:-", i[5])
            print("\t\tOFFICIAL ADDRESS:-", i[6])
            print("\t\tEMAIL ADDRESS:-", i[7])
            print("\t\tCONTACT NUMBER:-", i[8])
            print("\t\tCURRENT CITY:-", i[9])
            print("\t\tCURRENT COMPANY:-", i[10])
            print("\t\tDESIGNATION:-", i[11])
            print("\t\tSESSION:-", i[12], "-", i[13])
            print("\t\tBRANCH NAME:-", i[14])
            print("\t=====================================================")


def update_event():  # to modify the details of an event
    print("\t========================================================")
    print("\t\tENTER  EVENT DETAILS")
    print("\t========================================================")
    eid = input("\t\tEnter a Registerd Event id:-")
    mycursor.execute("select * from events where eid=%s", (eid,))
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\n\t\t PLEASE ENTER A VALID EVENT ID")
    else:
        while True:
            print("\t=============================================================")
            print("\t\tSELECT THE FIELD THAT YOU WANT TO CHANGE")
            print("\t==============================================================")
            print("\t\t1.EVENT NAME")
            print("\t\t2.EVENT VENUE")
            print("\t\t3.EVENT DATE")
            print("\t\t4:EVENT STATUS(Will be held/Already held/Cancelled)")
            print("\t\t5:EXIT")
            ch = int(input("\n\t\tENTER YOUR CHOICE:-"))
            if ch == 1:
                new_ename = input("\n\t\tEnter new event name:-")
                mycursor.execute("update events set ename=%s where eid=%s", (new_ename, eid,))
                constr.commit()
            elif ch == 2:
                new_evenue = input("\n\t\tEnter new event venue:-")
                mycursor.execute("update events set evenue=%s where eid=%s", (new_evenue, eid,))
                constr.commit()
            elif ch == 3:
                new_edate = input("\n\t\tEnter new event date(YYYY-MM-DD):-")
                mycursor.execute("update events set edate=%s where eid=%s", (new_edate, eid,))
                constr.commit()
            elif ch == 4:
                new_status = input("\n\t\tEnter new event Status:-")
                mycursor.execute("update events set status=%s where eid=%s", (new_status, eid,))
                constr.commit()
            elif ch == 5:
                break
            else:
                print("\n\t\tENTER A VALID CHOICE")
        print("\t======================================================")
        print("\t\tUPDATED EVENT DETAILS ARE:-")
        mycursor.execute("select * from events where eid=%s", (eid,))
        res = mycursor.fetchall()
        for i in res:
            print("\t========================================================")
            print("\t\tEVENT ID:-", i[0])
            print("\t\tEVENT NAME:-", i[1])
            print("\t\tEVENT DATE:-", i[2])
            print("\t\tEVENT VENUE:-", i[3])
            print("\t\tEVENT STATUS:-", i[4])
            print("\t\t===========================")


def add_event():  # to add a new event
    print("\t========================================================")
    print("\t\tENTER NEW EVENT DETAILS")
    print("\t========================================================")
    eid = input("\t\tEnter an event id:-")
    ename = input("\t\tEnter an event name:-")
    edate = input("\t\tEnter an event Date:-")
    evenue = input("\t\tEnter an event Venue:-")
    estatus = input("\t\tEnter the Event Status(Will be held/Already held/Cancelled)")
    mycursor.execute("insert into events values(%s,%s,%s,%s,%s)", (eid, ename, edate, evenue, estatus,))
    constr.commit()
    print("\t========================================================")
    print("\t\tEVENT IS ADDED SUCCESSFULLY!!!!!!")
    print("\t========================================================")


def delete_event():  # to delete an existing event
    print("\t========================================================")
    print("\t\tENTER  EVENT DETAILS")
    print("\t========================================================")
    eid = input("\t\tEnter a Registerd Event id:-")
    mycursor.execute("select * from events where eid=%s", (eid,))
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\n\t\t PLEASE ENTER A VALID EVENT ID")
    else:
        mycursor.execute("delete from events where eid=%s", (eid,))
        constr.commit()
        print("\t========================================================")
        print("\t\tEVENT IS DELETED SUCCESSFULLY!!!!!!")
        print("\t========================================================")


def register_alumni():  # to register a new alumini
    L = []
    fname = input("Enter Your First Name : ")
    L.append(fname)
    lname = input("Enter Your Last Name :")
    L.append(lname)
    dob = input("Enter Dob in YYYY-MM-DD Format : ")
    L.append(dob)
    gender = input("Enter Your Gender : ")
    L.append(gender)
    add_c = input("Enter your correspondence address : ")
    L.append(add_c)
    add_of = input("Enter your official address : ")
    L.append(add_of)
    email = input("Enter your email address Ex: aa@gmail.com: ")
    L.append(email)
    mob = input("Enter Your Mobile No: ")
    L.append(mob)
    cur_c = input("Enter City Name You Stay : ")
    L.append(cur_c)
    com = input("Enter Company/Organization You are Working : ")
    L.append(com)
    desg = input("Enter Your Desgination in Company/Organization : ")
    L.append(desg)
    start_y = input("Enter Your Session Start Year in College: ")
    L.append(start_y)
    start_e = input("Enter Your Session End Year in College : ")
    L.append(start_e)
    branch = input("Enter Your Branch in College : ")
    L.append(branch)
    apswd = input("Enter your Password:")
    L.append(apswd)
    alid = "al" + fname[0:2] + lname[0:2] + mob[0:4]
    L.insert(0, alid)
    alumni = (L)
    sql = "insert into alureg values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, alumni)
    constr.commit()
    print("\t\t============================================")
    print("\t\tYou Have Been Succesfully Registered: ")
    print("\t\tThis is You Alumni ID ,Use This For Further Correspondence")
    print("\t\t ALUMINI ID:-", alid)


def alu_login():  # login module for registered alumini
    print("\t\t========================================")
    print("\t\tWELCOME TO LOGIN MODULE OF ALUMINI")
    print("\t\t=======================================")
    aid = input("\t\tEnter Your Registered Alumini Id:-")
    apswd = input("\t\tEnter Your Password:-")
    mycursor.execute("select alu_id,apswd from alureg where alu_id=%s and apswd=%s", (aid, apswd,))
    res = mycursor.fetchall()
    if len(res) == 0:  # not entered a valid alumini id or password
        print("\t\tPLEASE ENTER VALID ALUMINI ID OR PASSWORD")
    else:
        while True:
            print("\t\t=====================================")
            print("\t\tYOU LOGGED IN SUCCEESSFULLY")
            print("\t\tWELCOME TO THE ALUMINI MENU")
            print("\t|t===================================")
            print("\t\t1. VIEW PERSONAL DETAILS")
            print("\t\t2. UPDATE PERSONAL DETAILS")
            print("\t\t3. DELETE PERSONAL DETAILS")
            print("\t\t4. VIEW ALL EVENT DETAILS")
            print("\t\t5. SELECT EVENT")
            print("\t\t6. VIEW SELECTED EVENT DETAILS")
            print("\t\t7. EXIT")
            ch = int(input("\n\t\tKINDLY ENTER YOUR CHOICE:-"))
            if ch == 1:
                view_personal_details()
            elif ch == 2:
                update_personal_details()
            elif ch == 3:
                delete_personal_details()
            elif ch == 4:
                view_all_events()
            elif ch == 5:
                select_event()
            elif ch == 6:
                view_selected_events()
            elif ch == 7:
                break
            else:
                print("\n\t\t PLEASE ENTER A VALID CHOICE")


def view_all_events():  # to view details of all events
    mycursor.execute("select * from events")
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\n\t\t NO EVENTS ARE PRSENT")
    else:
        for i in res:
            print("\t\t=============================")
            print("\t\tEVENT DETAILS ARE")
            print("==============================")
            print("\t\tEVENT ID:-", i[0])
            print("\t\tEVENT NAME:-", i[1])
            print("\t\tEVENT DATE:-", i[2])
            print("\t\tEVENT VENUE:-", i[3])
            print("\t\tEVENT STATUS:-", i[4])
            print("\t\t===========================")


def select_event():
    aid = input("\n\t\tEnter a Registerd alumini id:-")
    mycursor.execute("select alu_id,first_name,last_name from alureg where alu_id=%s", (aid,))
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\n\t\tEnter a valid Alumini Id")
    else:
        for i in res:
            aname = i[1] + i[2]

        mycursor.execute("select * from events where status='will be held'")
        res = mycursor.fetchall()
        if len(res) == 0:
            print("\n\t\t NO EVENTS ARE PRSENT")
        else:
            for i in res:
                print("\t=============================")
                print("\t\tFUTURE EVENT DETAILS ARE")
                print("\t==============================")
                print("\t\tEVENT ID:-", i[0])
                print("\t\tEVENT NAME:-", i[1])
                print("\t\tEVENT DATE:-", i[2])
                print("\t\tEVENT VENUE:-", i[3])
                print("\t\tEVENT STATUS:-", i[4])
                print("\t\t===========================")
            eid = input("\n\t\tENter the Event id That you want to attend:-")
            mycursor.execute("select * from events where eid=%s", (eid,))
            res = mycursor.fetchall()
            if len(res) == 0:
                print("\n\t\t Enter a Valid Event ID")
            else:
                for i in res:
                    ename = i[1]
                    edate = i[2]
                    evenue = i[3]
                    status = "CONFIRMED"
                mycursor.execute("insert into selected_events values(%s,%s,%s,%s,%s,%s,%s)",
                                 (aid, aname, eid, ename, edate, evenue, status,))
                constr.commit()
                print("\t===================================")
                print("\t\tCongratulations! Your Entry has been Confirmed.")
                print("\t===================================")


def view_selected_events():  # to view the selected
    aid = input("\n\t\tEnter a Registerd alumini id:-")
    mycursor.execute("select * from selected_events where alu_id=%s", (aid,))
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\n\t\tEnter a valid Alumini Id")
    else:
        for i in res:
            print("\t===================================")
            print("\t\tYOUR SELECTED EVENTS ARE:")
            print("\t==================================")
            print("\t\t ALUMINI ID:-", i[0])
            print("\t\t ALUMINI NAME:-", i[1])
            print("\t\tEVENT ID:-", i[2])
            print("\t\tEVENT NAME:-", i[3])
            print("\t\tEVENT DATE:-", i[4])
            print("\t\tEVENT VENUE:-", i[5])
            print("\t\tWILL ATTEND:-", i[6])
            print("\t====================================")


def view_personal_details():  # to view alumini personal details
    aid = input("\t\tEnter a Registered Alumini Id:-")
    mycursor.execute("select * from alureg where alu_id=%s", (aid,))
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\t\tPLEASE ENTER A VALID ALUMINI ID:-")
    else:
        for i in res:
            print("\t\t================================")
            print("\t\tYOUR PERSONAL DETAILS ARE")
            print("\t\t================================")
            print("\t\tALUMINI ID:-", i[0])
            print("\t\tALUMINI NAME:-", i[1] + i[2])
            print("\t\tALUMINI DATE OF BIRTH:-", i[3])
            print("\t\tALUMINI GENDER:-", i[4])
            print("\t\tCORRESPONDANCE ADDRESS:-", i[5])
            print("\t\tOFFICIAL ADDRESS:-", i[6])
            print("\t\tEMAIL ADDRESS:-", i[7])
            print("\t\tCONTACT NUMBER:-", i[8])
            print("\t\tCURRENT CITY:-", i[9])
            print("\t\tCURRENT COMPANY:-", i[10])
            print("\t\tDESIGNATION:-", i[11])
            print("\t\tSESSION:-", i[12], "-", i[13])
            print("\t\tBRANCH NAME:-", i[14])
            print("\t\t===============================")


def delete_personal_details():  # to delete the alumini account
    aid = input("\t\tEnter a Registered Alumini Id:-")
    mycursor.execute("select * from alureg where alu_id=%s", (aid,))
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\t\tPLEASE ENTER A VALID ALUMINI ID:-")
    else:
        mycursor.execute("delete from alureg where alu_id=%s", (aid,))
        constr.commit()
        print("\n\t\tTHE RECORD HAS BEEN DELETED SUCCESSFULLY")


def update_personal_details():  # to modify the details of alumini
    aid = input("\n\t\tEnter Alumni ID to be edited : ")
    sql = "select * from alureg where alu_id=%s"
    ed = (aid,)
    mycursor.execute(sql, ed)
    res = mycursor.fetchall()
    if len(res) == 0:
        print("\n\tENTER A VALID ALUMINI ID")
    else:
        for x in res:
            fld = input("Enter the field which you want to edit : ")
            val = input("Enter the value you want to set : ")
            sql = "Update alureg set " + fld + "='" + val + "' where alu_id='" + aid + "'"
            sq = sql
            mycursor.execute(sql)
            constr.commit()
            print("\n\t\tRECORD HAS BEEN UPDATED SUCCESSFULLY  ")

            sql = "select * from alureg where alu_id=%s"
            ed = (aid,)
            mycursor.execute(sql, ed)
            res = mycursor.fetchall()
            for i in res:
                print("\t\t================================")
                print("\t\tYOUR UPDATED DETAILS ARE")
                print("\t\t================================")
                print("\t\tALUMINI ID:-", i[0])
                print("\t\tALUMINI NAME:-", i[1] + i[2])
                print("\t\tALUMINI DATE OF BIRTH:-", i[3])
                print("\t\tALUMINI GENDER:-", i[4])
                print("\t\tCORRESPONDANCE ADDRESS:-", i[5])
                print("\t\tOFFICIAL ADDRESS:-", i[6])
                print("\t\tEMAIL ADDRESS:-", i[7])
                print("\t\tCONTACT NUMBER:-", i[8])
                print("\t\tCURRENT CITY:-", i[9])
                print("\t\tCURRENT COMPANY:-", i[10])
                print("\t\tDESIGNATION:-", i[11])
                print("\t\tSESSION:-", i[12], "-", i[13])
                print("\t\tBRANCH NAME:-", i[14])
                print("\t\t===============================")


# ------------------------------------------------------------------------------Main module--------------------------------
while True:
    print("\t====================================================")
    print("\t\tMAIN MENU")
    print("\t==================================================")
    print("\t\t1. ADMIN")
    print("\t\t2. ALUMINI")
    print("\t\t3. EXIT")
    ch = int(input("\n\t\t Enter Your choice"))
    if ch == 1:  # ADMIN MODULE
        while True:
            print("\t======================================================")
            print("\t\tADMIN MENU")
            print("\t======================================================")
            print("\t\t1. REGISTER")
            print("\t\t2. LOGIN")
            print("\t\t3. EXIT")
            cho = int(input("\n\t\t Enter Your choice"))
            if cho == 1:
                add_admin()
            elif cho == 2:
                admin_login()
            elif cho == 3:
                break
    if ch == 2:
        while True:
            print("\t=====================================================")
            print("\t\tALUMINI MENU")
            print("\t====================================================")
            print("\t\t1. REGISTER")
            print("\t\t2. LOGIN")
            print("\t\t3. EXIT")
            cho = int(input("\n\t\t Enter Your choice"))
            if cho == 1:
                register_alumni()
            elif cho == 2:
                alu_login()
            elif cho == 3:
                break
    if ch == 3:
        break
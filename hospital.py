from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital managment system")
        self.root.geometry("1540x800+0+0")

        self.Nameoftables=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NoofTablet=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInfo=StringVar()
        self.BloodPressure=StringVar()
        self.Storage=StringVar()
        self.Medicine=StringVar()
        self.PatientId=StringVar()
        self.NhsNumber=StringVar()
        self.PatientName=StringVar()
        self.pnname=StringVar()
        self.DOB=StringVar()
        self.Address=StringVar()

        lbltitle = Label(self.root,bd=5,relief=RIDGE,text="HOSPITAL MANGMENT SYSTEM",fg='#4682B4',bg='white',font=('times new roman',40,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #**************Datafram*******************************************
        dataFrame=Frame(self.root,bd=5,relief=RIDGE,bg='#4682B4')
        dataFrame.place(x=0,y=100,width=1530,height=400)

        dataFrameleft = LabelFrame(dataFrame,bd=5,relief=RIDGE,padx=10,fg='#4682B4',
                                   font=("arial",15,"bold"),text="Patient Information")
        dataFrameleft.place(x=0,y=5,width=886,height=350)

        dataFrameRight = LabelFrame(dataFrame,bd=5,relief=RIDGE,padx=10,fg='#4682B4',
                                   font=("arial",15,"bold"),text="Prescription")
        dataFrameRight.place(x=890,y=5,width=460,height=350)

        #**************Buttons*******************************************
        ButtonFrame=Frame(self.root,bd=5,relief=RIDGE,bg='#4682B4')
        ButtonFrame.place(x=0,y=510,width=1530,height=50)

        #**************Details Fram*******************************************
        DetailsFrame=Frame(self.root,bd=5,relief=RIDGE,bg='#4682B4')
        DetailsFrame.place(x=0,y=570,width=1530,height=150)

        #**************Details Framleft*******************************************
        lblNameTablet = Label(dataFrameleft,text="Name of Tablet:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        contNametablet=ttk.Combobox(dataFrameleft,textvariable=self.Nameoftables,state="readonly",
                                                        font=("arial",12,"bold"),width=29)
        contNametablet["values"]=("Insuline","paracetamol","aspirin","ibuprofen","Atiavan")
        contNametablet.current(0)
        contNametablet.grid(row=0,column=1)

        lblref=Label(dataFrameleft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.ref,width=31)
        txtref.grid(row=1,column=1)

        lblDose=Label(dataFrameleft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.Dose,width=31)
        txtDose.grid(row=2,column=1)

        lblNoOfTablet=Label(dataFrameleft,font=("arial",12,"bold"),text="No of Tablet:",padx=2,pady=6)
        lblNoOfTablet.grid(row=3,column=0,sticky=W)
        txtNoOfTablet=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.NoofTablet,width=31)
        txtNoOfTablet.grid(row=3,column=1)

        lblLot=Label(dataFrameleft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.Lot,width=31)
        txtLot.grid(row=4,column=1)

        lblIssueDate=Label(dataFrameleft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.IssueDate,width=31)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(dataFrameleft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.ExpDate,width=31)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(dataFrameleft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.DailyDose,width=31)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(dataFrameleft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.SideEffect,width=31)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(dataFrameleft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.FurtherInfo,width=31)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(dataFrameleft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.BloodPressure,width=31)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(dataFrameleft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.Storage,width=31)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(dataFrameleft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.Medicine,width=31)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(dataFrameleft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.PatientId,width=31)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(dataFrameleft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.NhsNumber,width=31)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(dataFrameleft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.PatientName,width=31)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(dataFrameleft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.DOB,width=31)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(dataFrameleft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(dataFrameleft,font=("arial",12,"bold"),textvariable=self.Address,width=31)
        txtPatientAddress.grid(row=8,column=3)

        #******************DataFrameRight********************************

        self.txtPrescription=Text(dataFrameRight,font=("arial",12,"bold"),width=45,height=15,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        #*****************************Buttons*******************************

        btnPrescription=Button(ButtonFrame,command=self.iPrectioption,text="Prescription",bg="#4169E1",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(ButtonFrame,text="Prescription Data",bg="#4169E1",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6, command=self.PrescriptionData)
        btnPrescriptionData.grid(row=0,column=1)

        btnupdate=Button(ButtonFrame,command=self.update,text="Update",bg="#4169E1",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnupdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,command=self.delete,text="Delete",bg="#4169E1",fg="white",font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,command=self.clear,text="Clear",bg="#4169E1",fg="white",font=("arial",12,"bold"),width=22,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,command=self.exit,text="Exit",bg="#4169E1",fg="white",font=("arial",12,"bold"),width=22,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #****************Table************************************************

        #*********************ScrollBar***************************************

        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailsFrame,column=("nameoftable","ref","dose","nooftablets","lot","issuedate",
                                                        "expdate","dailydose","SideEffect","furtherinfor","bloodpressure","storage","medication","patientid","nhsnumber","pnname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Table")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("SideEffect", text="Side Effect")
        self.hospital_table.heading("furtherinfor",text="Further Information")
        self.hospital_table.heading("bloodpressure",text="Blood Pressure")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("medication",text="Medication")
        self.hospital_table.heading("patientid",text="Patient Id")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pnname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
    
        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=10)
        self.hospital_table.column("ref",width=10)
        self.hospital_table.column("dose",width=10)
        self.hospital_table.column("nooftablets",width=10)
        self.hospital_table.column("lot",width=10)
        self.hospital_table.column("issuedate",width=10)
        self.hospital_table.column("expdate",width=10)
        self.hospital_table.column("dailydose",width=10)
        self.hospital_table.column("SideEffect",width=10)
        self.hospital_table.column("furtherinfor",width=10)
        self.hospital_table.column("bloodpressure",width=10)
        self.hospital_table.column("storage",width=10)
        self.hospital_table.column("medication",width=10)
        self.hospital_table.column("patientid",width=10)
        self.hospital_table.column("nhsnumber",width=10)
        self.hospital_table.column("pnname",width=10)
        self.hospital_table.column("dob",width=10)
        self.hospital_table.column("address",width=10)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

        #*********************Functionally Description**************************

    def PrescriptionData(self):
        if self.Nameoftables.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="mydata"
        )
        my_cursor = conn.cursor()
        my_cursor.execute(
            "INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
            self.Nameoftables.get(),
            self.ref.get(),
            self.Dose.get(),
            self.NoofTablet.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.SideEffect.get(),
            self.FurtherInfo.get(),
            self.BloodPressure.get(),
            self.Storage.get(),
            self.Medicine.get(),
            self.PatientId.get(),
            self.NhsNumber.get(),
            self.PatientName.get(),
            self.DOB.get(),
            self.Address.get(),
            )
        )
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been inserted.")

    def update(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mydata"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set nameoftable=%s,dose=%s,nooftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,SideEffect=%s,furtherinfor=%s,bloodpressure=%s,storage=%s,medication=%s,patientid=%s,nhsnumber=%s,pnname=%s,dob=%s,address=%s where ref=%s",(
            self.Nameoftables.get(),
            self.ref.get(),
            self.Dose.get(),
            self.NoofTablet.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.SideEffect.get(),
            self.FurtherInfo.get(),
            self.BloodPressure.get(),
            self.Storage.get(),
            self.Medicine.get(),
            self.PatientId.get(),
            self.NhsNumber.get(),
            self.PatientName.get(),
            self.DOB.get(),
            self.Address.get(),
            )
        )
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record has been updated.")

    def iPrectioption(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftables.get()+"\n")
        self.txtPrescription.insert(END,"ref:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"no of Tablets:\t\t\t"+self.NoofTablet.get()+"\n")
        self.txtPrescription.insert(END,"lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"issue date:\t\t\t"+self.IssueDate.get()+"\n")
        self.txtPrescription.insert(END,"exp date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"daily dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"side effect:\t\t\t"+self.SideEffect.get()+"\n")
        self.txtPrescription.insert(END,"further information:\t\t\t"+self.FurtherInfo.get()+"\n")
        self.txtPrescription.insert(END,"blood pressure:\t\t\t"+self.BloodPressure.get()+"\n")
        self.txtPrescription.insert(END,"storage:\t\t\t"+self.Storage.get()+"\n")
        self.txtPrescription.insert(END,"medicine:\t\t\t"+self.Medicine.get()+"\n")
        self.txtPrescription.insert(END,"patient id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"nhs number:\t\t\t"+self.NhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"patient name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"dob:\t\t\t"+self.DOB.get()+"\n")
        self.txtPrescription.insert(END,"address:\t\t\t"+self.Address.get()+"\n")

    def delete(self):
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="mydata"
            )
        my_cursor = conn.cursor()
        query="delete from hospital where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)


        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Deleted","Patient has been deleted successfully.")

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="mydata"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from hospital")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())  # Clear existing data
                for i, row in enumerate(rows):
                    self.hospital_table.insert("", i, values=row)
                conn.close()
        except Exception as e:
            print(f"Error: {e}")

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftables.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NoofTablet.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.SideEffect.set(row[8])
        self.FurtherInfo.set(row[9])
        self.BloodPressure.set(row[10])
        self.Storage.set(row[11])
        self.Medicine.set(row[12])
        self.PatientId.set(row[13])
        self.NhsNumber.set(row[14])
        self.PatientName.set(row[15])
        self.DOB.set(row[16])
        self.Address.set(row[17])

    def clear(self):
        self.Nameoftables.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NoofTablet.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInfo.set("")
        self.BloodPressure.set("")
        self.Storage.set("")
        self.Medicine.set("")
        self.PatientId.set("")
        self.NhsNumber.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.Address.set("")

        self.txtPrescription.delete('1.0', END)

    def exit(self):
        exit_confirm = messagebox.showinfo("Hospital managment system","Conform you want to exit.")
        if exit_confirm:
            root.destroy()

        
root=Tk()
ob=Hospital(root)
root.mainloop()
import time
import tkinter.messagebox
from tkinter import *

class EMP:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title("Employee Payment System")
        self.root.maxsize(width=1700, height=800)
        self.root.minsize(width=1000, height=520)
        self.root.configure(background="dark gray")

        self.Tops = Frame(root, width=800, height=50, bd=8, bg="dark blue")
        self.Tops.pack(side=TOP)

        self.f1 = Frame(root, width=400, height=600, bd=8, bg="dark gray")
        self.f1.place(x=50, y=180)
        self.f2 = Frame(root, width=300, height=400, bd=8, bg="dark blue")
        self.f2.place(x=1000, y=130)

        self.fla = Frame(self.f1, width=600, height=200, bd=8, bg="dark blue")
        self.fla.pack(side=TOP)
        self.flb = Frame(self.f1, width=300, height=600, bd=8, bg="dark blue")
        self.flb.pack(side=TOP)

        self.lbl_information = Label(self.Tops, font=('arial', 45, 'bold'), text="Employee Payment Management System ",
                                relief=GROOVE, bd=10, bg="Dark Gray", fg="Black")
        self.lbl_information.pack(side=TOP)

        # Variables
        self.FullName = StringVar()
        self.Address = StringVar()
        self.Hrs_Wage = StringVar()
        self.Wrk_Hrs = StringVar()
        self.Payable = StringVar()
        self.Taxable = StringVar()
        self.NetPayable = StringVar()
        self.GrossPayable = StringVar()
        self.OverTimeBonus = StringVar()
        self.CompanyAgency = StringVar()
        self.PhoneNumber = StringVar()
        self.TimeOfOrder = StringVar()
        self.DateOfOrder = StringVar()
        self.DateOfOrder.set(time.strftime("%d/%m/%Y"))

        # Label Widget

        self.labelFirstName = Label(self.fla, text="Full Name", font=('arial', 14, 'bold'), bd=20, fg="white",
                               bg="dark blue").grid(row=0, column=0)

        self.labelAddress = Label(self.fla, text="Home Address", font=('arial', 14, 'bold'), bd=20, fg="white",
                             bg="dark blue").grid(row=0, column=2)

        self.labelCompanyAgency = Label(self.fla, text="Company/Agency", font=('arial', 14, 'bold'), bd=20, fg="white",
                                   bg="dark blue").grid(row=1, column=0)

        self.labelPhoneNumber = Label(self.fla, text="Phone Number", font=('arial', 14, 'bold'), bd=20, fg="white",
                                 bg="dark blue").grid(row=1, column=2)

        self.labelHoursWorked = Label(self.fla, text="Hours Worked", font=('arial', 14, 'bold'), bd=20, fg="white",
                                 bg="dark blue").grid(row=2, column=0)

        self.labelHourlyRate = Label(self.fla, text="Hourly Rate", font=('arial', 14, 'bold'), bd=20, fg="white",
                                bg="dark blue").grid(row=2, column=2)

        self.labelTax = Label(self.fla, text="Tax", font=('arial', 14, 'bold'), bd=20, anchor='w', fg="white",
                         bg="dark blue").grid(row=3, column=0)

        self.labelOverTime = Label(self.fla, text="OverTime", font=('arial', 14, 'bold'), bd=20, fg="white", bg="dark blue").grid(
            row=3, column=2)

        self.labelGrossPay = Label(self.fla, text="GrossPay", font=('arial', 14, 'bold'), bd=20, fg="white", bg="dark blue").grid(
            row=4, column=0)

        self.labelNetPay = Label(self.fla, text="Net Pay", font=('arial', 14, 'bold'), bd=20, fg="white", bg="dark blue").grid(
            row=4, column=2)

        # Entry Widget

        self.txtFullname = Entry(self.fla, textvariable=self.FullName, font=('arial', 16, 'bold'), bd=10, width=15, justify='left')
        self.txtFullname.grid(row=0, column=1)

        self.txtAddress = Entry(self.fla, textvariable=self.Address, font=('arial', 16, 'bold'), bd=10, width=15, justify='left')
        self.txtAddress.grid(row=0, column=3)

        self.txtCompanyAgency = Entry(self.fla, textvariable=self.CompanyAgency, font=('arial', 16, 'bold'), bd=10, width=15,
                                 justify='left')
        self.txtCompanyAgency.grid(row=1, column=1)

        self.txtWrk_hrs = Entry(self.fla, textvariable=self.Wrk_Hrs, font=('arial', 16, 'bold'), bd=10, width=15, justify='left')
        self.txtWrk_hrs.grid(row=2, column=1)

        self.txtHrs_Wages = Entry(self.fla, textvariable=self.Hrs_Wage, font=('arial', 16, 'bold'), bd=16, width=15, justify='left')
        self.txtHrs_Wages.grid(row=2, column=3)

        self.txtPhoneNumber = Entry(self.fla, textvariable=self.PhoneNumber, font=('arial', 16, 'bold'), bd=16, width=15,
                               justify='left')
        self.txtPhoneNumber.grid(row=1, column=3)

        self.txtGrossPayment = Entry(self.fla, textvariable=self.Payable, font=('arial', 16, 'bold'), bd=16, width=15, justify='left')
        self.txtGrossPayment.grid(row=4, column=1)

        self.txtNetPayable = Entry(self.fla, textvariable=self.NetPayable, font=('arial', 16, 'bold'), bd=16, width=15, justify='left')
        self.txtNetPayable.grid(row=4, column=3)

        self.txtTaxable = Entry(self.fla, textvariable=self.Taxable, font=('arial', 16, 'bold'), bd=16, width=15, justify='left')
        self.txtTaxable.grid(row=3, column=1)

        self.txtOverTimeBonus = Entry(self.fla, textvariable=self.OverTimeBonus, font=('arial', 16, 'bold'), bd=16, width=15,
                                 justify='left')
        self.txtOverTimeBonus.grid(row=3, column=3)

        # Text Widget

        self.payslip = Label(self.f2, textvariable=self.DateOfOrder, font=('arial', 21, 'bold'), fg="white", bg="dark blue").grid(
            row=0,
            column=0)
        self.txtPaymentSlip = Text(self.f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="black", bg="white")
        self.txtPaymentSlip.grid(row=1, column=0)

        # buttons

        self.ButtonSalary = Button(self.flb, text='Weekly Salary', padx=16, pady=16, bd=15, font=('arial', 14, 'bold'),
                              relief="groove", width=14, fg="black",
                              bg="dark gray", command=self.WagesForWeekly).grid(row=0, column=0)

        self.ButtonReset = Button(self.flb, text='Reset', padx=16, pady=16, bd=15, font=('arial', 14, 'bold'), relief="groove",
                             width=14, command=self.Reset,
                             fg="black", bg="dark gray").grid(row=0, column=1)

        self.ButtonPaySlip = Button(self.flb, text='View Payslip', padx=16, pady=16, bd=15, font=('arial', 14, 'bold'),
                               relief="groove", width=14,
                               command=self.InformationEntry, fg="black", bg="dark gray").grid(row=0, column=2)

        self.ButtonExit = Button(self.flb, text='Exit System', padx=16, pady=16, bd=15, font=('arial', 14, 'bold'),
                            relief="groove", width=14, command=self.Exit,
                            fg="black", bg="dark gray").grid(row=0, column=3)

        self.ButtonPrintSlip = Button(self.flb, text='Print', padx=12, pady=12, bd=11, font=('arial', 11, 'bold'),
                                 relief="groove", width=10, command=self.Print,
                                 fg="black", bg="dark gray").grid(row=1, column=2)
    def Print(self):
        template = f'''
                Pay Slip
                
        Full Name :      {str(self.FullName.get()).encode('utf-8').decode('utf-8')}  
  		
        Home Address :   {str(self.Address.get()).encode('utf-8').decode('utf-8')}	
            
        Company/Agency : {str(self.CompanyAgency.get()).encode('utf-8').decode('utf-8')}
        
        Phone Number :   {str(self.PhoneNumber.get()).encode('utf-8').decode('utf-8')}		
        
        Hours Worked :   {str(self.Wrk_Hrs.get()).encode('utf-8').decode('utf-8')}		
        
        Wages per hour : {str(self.Hrs_Wage.get()).encode('utf-8').decode('utf-8')}	
        
        Payable :        {str(self.Payable.get()).encode('utf-8').decode('utf-8').split(' ')[-1]} 	
            
        Tax Paid :       {str(self.Taxable.get()).encode('utf-8').decode('utf-8').split(' ')[-1]}	
            
        Net Payable :    {str(self.NetPayable.get()).encode('utf-8').decode('utf-8').split(' ')[-1]}
        '''
        from fpdf import FPDF
        # print(template)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Courier', 'B', 16)
        pdf.multi_cell(200, 5, template, 0, 1)
        pdf.output(f"slips/{str(self.FullName.get())}-slip.pdf", 'F')
        tkinter.messagebox.showinfo("File Saved",f"Slip saved to slips/{str(self.FullName.get())}-slip.pdf")

    def Exit(self):
        wayOut = tkinter.messagebox.askyesno("Employee Payment System", "Do you want to exit the system")
        if wayOut > 0:
            self.root.destroy()
            return

    def Reset(self):
        self.FullName.set("")
        self.Address.set("")
        self.Wrk_Hrs.set("")
        self.Hrs_Wage.set("")
        self.Payable.set("")
        self.Taxable.set("")
        self.NetPayable.set("")
        self.GrossPayable.set("")
        self.OverTimeBonus.set("")
        self.CompanyAgency.set("")
        self.PhoneNumber.set("")
        self.txtPaymentSlip.delete("1.0", END)

    def InformationEntry(self):
        self.txtPaymentSlip.delete("1.0", END)
        self.txtPaymentSlip.insert(END, "\t\tPay Slip\n\n")
        self.txtPaymentSlip.insert(END, "   Full Name :      \t\t" + self.FullName.get() + "\n\n")
        self.txtPaymentSlip.insert(END, "   Home Address :   \t\t" + self.Address.get() + "\n\n")
        self.txtPaymentSlip.insert(END, "   Company/Agency : \t\t" + self.CompanyAgency.get() + "\n\n")
        self.txtPaymentSlip.insert(END, "   Phone Number :   \t\t" + self.PhoneNumber.get() + "\n\n")
        self.txtPaymentSlip.insert(END, "   Hours Worked :   \t\t" + self.Wrk_Hrs.get() + "\n\n")
        self.txtPaymentSlip.insert(END, "   Wages per hour : \t\t" + self.Hrs_Wage.get() + "\n\n")
        self.txtPaymentSlip.insert(END, "   Payable :        \t\t" + self.Payable.get() + "\n\n")
        self.txtPaymentSlip.insert(END, "   Tax Paid :       \t\t" + self.Taxable.get() + "\n\n")
        self.txtPaymentSlip.insert(END, "   Net Payable :   \t\t" + self.NetPayable.get() + "\n\n")


    def WagesForWeekly(self):
        self.txtPaymentSlip.delete("1.0", END)
        print(self.Wrk_Hrs.get())
        hrs_wrk_per_wek = float(self.Wrk_Hrs.get())
        hrs_per_wgs = float(self.Hrs_Wage.get())

        DuePayment = hrs_per_wgs * hrs_wrk_per_wek
        PaymentDue = "₹ " + str('%.2f' % DuePayment)
        self.Payable.set(PaymentDue)

        tax = DuePayment * 0.12
        taxable = "₹ " + str('%.2f' % tax)
        self.Taxable.set(taxable)

        if hrs_wrk_per_wek > 40:
            HoursTimeOver = (hrs_wrk_per_wek - 40) * hrs_per_wgs * 1.5

            OverTime = "₹ " + str('%.2f' % HoursTimeOver)
            self.OverTimeBonus.set(OverTime)
            PaymentNet = DuePayment - tax + HoursTimeOver
            NetPayments = "₹ " + str('%.2f' % PaymentNet)
            self.NetPayable.set(NetPayments)
        else:
            HoursTimeOver = 0
            PaymentNet = DuePayment - tax
            NetPayments = "₹ " + str('%.2f' % PaymentNet)
            self.NetPayable.set(NetPayments)

if __name__ == "__main__":
    root = Tk()
    EMP(root)
    root.mainloop()
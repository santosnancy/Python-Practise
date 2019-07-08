
#importing the library
from tkinter import *
# creating variables or objects that control the main variable
lop = Tk()
# Main Title on the windows
lop.title('Welcome To Our First App')
#closing the mainloop
#-----------------------LEFTFrame-------------------------------
LMF = Frame(lop, width=650, height=500, border=3, relief="raise")
LMF.pack(side=LEFT)
#---------------------------------------------------------------

#-------------------RIGHTfRAME----------------------------------
RMf = Frame(lop, width=400, height=500, border=3, relief="raise")
RMf.pack(side=RIGHT)
#---------------------------------------------------------------

# -------------------------Frames Inside LMF---------------------
car = Frame(LMF, width=650, height=150, border=2, relief="raise")
car.pack(side=TOP)
san = Frame(LMF, width=650, height=150, border=2, relief="raise")
san.pack(side=TOP)
zulu = Frame(LMF, width=650, height=100, border=2, relief="raise")
zulu.pack(side=TOP)
lopes = Frame(LMF, width=650, height=100, border=2, relief="raise")
lopes.pack(side=TOP)
#-----------------------------------------------------------------------

#------------------------TextBox FieldHere-----------------------------------------
txtbox = Text(RMf, height=10, width=28, border=2, font=('arial', 12, 'bold')).grid(row=0, column=0)
#-----------------------------------------------------------------------------------

#----------Fild For the  lopes frames Buttons -------------------------------------
botao = Button(lopes, text='Total', padx=4, border=2, fg='yellow', bg='black', font=('arial', 12, 'bold'), width=8, height=1).grid(row=0, column=0)
botao1 = Button(lopes, text='Add', padx=4, border=2, fg='yellow', bg='black',font=('arial',12, 'bold'),width=8, height=1).grid(row=0, column=1)
botao2 = Button(lopes, text='Clean', padx=4, border=2, fg='yellow', bg='black',font=('arial',12, 'bold'),width=8, height=1).grid(row=0, column=2)
botao3 = Button(lopes, text='Exit', padx=4, border=2, fg='yellow', bg='black',font=('arial',12, 'bold'),width=8, height=1).grid(row=0, column=3)
#-------------------------------------------------------------------------------------
#-------------------------Here Label of the Client------------------------------------
Client = Label(zulu, font=('arial', 10, 'bold'), text='Client ID', border=8)
Client.grid(row=0, column=0, sticky=W)
#-------------------------------------------------------------------------------------
#--------------------------TextBox----------------------------------------------------
txtClient = Entry(zulu, font=('arial', 10, 'bold'), border=1, width=31, justify='left')
txtClient.grid(row=0, column=1)
#-------------------------------------------------------------------------------------
#-------------------------Here Label of the Client------------------------------------
Client = Label(zulu, font=('arial', 10, 'bold'), text='Client ID', border=8)
Client.grid(row=0, column=2, sticky=W)
#-------------------------------------------------------------------------------------
#--------------------------TextBox----------------------------------------------------
txtClient = Entry(zulu, font=('arial', 10, 'bold'), border=1, width=31, justify='left')
txtClient.grid(row=0, column=3)
#-------------------------Here Label of the Client------------------------------------
Client = Label(zulu, font=('arial', 10, 'bold'), text='Client ID', border=8)
Client.grid(row=0, column=4, sticky=W)
#-------------------------------------------------------------------------------------
#--------------------------TextBox----------------------------------------------------
txtClient = Entry(zulu, font=('arial', 10, 'bold'), border=1, width=31, justify='left')
txtClient.grid(row=0, column=5)
#-------------------------Here Label of the Client------------------------------------
Client = Label(zulu, font=('arial', 10, 'bold'), text='Client ID', border=8)
Client.grid(row=1, column=0, sticky=W)
#-------------------------------------------------------------------------------------
#--------------------------TextBox----------------------------------------------------
txtClient = Entry(zulu, font=('arial', 10, 'bold'), border=1, width=31, justify='left')
txtClient.grid(row=1, column=1)
lop.mainloop()
#-------------------------Here Label of the Client------------------------------------
Client = Label(zulu, font=('arial', 10, 'bold'), text='Client ID', border=8)
Client.grid(row=1, column=0, sticky=W)
#-------------------------------------------------------------------------------------
#--------------------------TextBox----------------------------------------------------
txtClient = Entry(zulu, font=('arial', 10, 'bold'), border=1, width=31, justify='left')
txtClient.grid(row=1, column=1)
#-------------------------Here Label of the Client------------------------------------
Client = Label(zulu, font=('arial', 10, 'bold'), text='Client ID', border=8)
Client.grid(row=1, column=0, sticky=W)
#-------------------------------------------------------------------------------------
#--------------------------TextBox----------------------------------------------------
txtClient = Entry(zulu, font=('arial', 10, 'bold'), border=1, width=31, justify='left')
txtClient.grid(row=1, column=1)
lop.mainloop()
lop.mainloop()

print('Closing the Application')
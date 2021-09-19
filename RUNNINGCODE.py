import base64
from datetime import datetime
#GUI CREATION
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('Password Manager') #giving the name to the window
window.geometry("550x400+10+20") #giving the dimensions of the window
window.config(padx=50, pady=50, bg="midnight blue") #giving the color of the window


# insert widgets here
label = Label(window, text = "Welcome to Password Manager", bg = "light cyan", bd = 4, fg = "midnight blue", font=('Helvetica',15,'bold'))
label.grid(row=0,column=1)
label = Label(window,bg = "midnight blue")
label.grid(row=1,column=1)
label = Label(window, bg = "midnight blue")
label.grid(row=1,column=1)
label = Label(window, bg = "midnight blue")
label.grid(row=1,column=1)

# declaring string variable
# for storing name and password
username_var=StringVar()
passw_var=StringVar()

# defining a function that will get the name and password and print them in a file
#function gets called when the submit button is pressed
def submit():

    username_info = str(username_var.get())
    password_info = str(passw_var.get())
   
    
    print(username_info,password_info)
 
    with open(str(username_info)+".txt",'w+') as file:
      info=username_info+"\n"+password_info
      encodedstring=info.encode("ascii")
      base64message=base64.b85encode(base64.b64encode(encodedstring))    #returns encoded version of the given string
      #base64message.decode("ascii")
      file.write(base64message.decode("ascii"))
      print(encodedstring)
      print(base64message)
      file.close()
    
    file = open("user1.txt","a")
    file.write("Your User Name " + username_info)
    file.write("\n")
    file.write("Your Password " + password_info)
    
    file.write("\n")
    file.write("\n")
	
    username_var.set("")
    passw_var.set("")


def decrypt():
    user=str(input("Enter the username whose code you want to decrypt  "))
    with open(str(user)+".txt",'r') as file:
      message = file.read()     

      decrypted_encrypted = base64.b64decode(base64.b85decode(message))        
      message=decrypted_encrypted.decode("ascii")     #returns decoded version of the given string
      
      print(message)
      file.close()

def reminder():

  date = str(datetime.today())                   #take current date and time
  with open("date.txt",'a+') as file:
    file.write(date[:10])              #write only date in file
    file.write("\n")
    file.seek(0)
    startdate = file.readline()
    dayspassed = int(startdate[5:7]) + 3  #add 3 months 
    file.close()
  
  today = date[:10]

  if(dayspassed not in [10,11,12]):
    remind_date = startdate[:5]+'0'+str(dayspassed)+startdate[7:-1]
  else:
    remind_date = startdate[:5]+str(dayspassed)+startdate[7:-1]

  if(today == remind_date):  #if reminder occurs in current year only
    messagebox.showinfo("Reminder",  "It's time to change passwords!")

    #clear all dates in file and keep current date
    with open("date.txt", 'r+') as fp:
    
        lines = fp.readlines()
    
        fp.seek(0)
   
        fp.truncate()

        fp.writelines(lines[-1:])
        fp.close()
    
  elif(today[:4] != remind_date[:4]):    #if reminder occurs next year

    yearchange = int(remind_date[:4]) + 1

    if(remind_date[5:7] == '13'):    #remind in january
        remind_date = str(yearchange) + '-01' + remind_date[7:]

        if(today == remind_date):
            messagebox.showinfo("Reminder:",  "It's time to change passwords!")
            
    elif(remind_date[5:7] == '14'):  #remind in february
        remind_date = str(yearchange) + '-02' + remind_date[7:]

        if(today == remind_date):
            messagebox.showinfo("Reminder:",  "It's time to change passwords!")
            
    elif(remind_date[5:7] == "15"):  #remind in march
        remind_date = str(yearchange) + "-03" + remind_date[7:]
        
        if(today == remind_date):
            messagebox.showinfo("Reminder:",  "It's time to change passwords!")
        
    with open("date.txt", 'r+') as fp:
    
        lines = fp.readlines()
    
        fp.seek(0)
   
        fp.truncate()

        fp.writelines(lines[-1:])
        fp.close() 


L1=Label(window, text="User Name", bg = "light cyan", bd = 4, fg = "midnight blue", font=('calibre',10, 'bold')).grid(row=6)

label = Label(window,bg = "midnight blue")
label.grid(column=7)

L2=Label(window, text="Password", bg = "light cyan", bd = 4, fg = "midnight blue", font=('calibre',10, 'bold')).grid(row=8)

e1 = Entry(window,textvariable = username_var,bg = "light steel blue" , font=('calibre',10,'normal'))
#creating entry for password
e2 =Entry(window, textvariable = passw_var,bg = "light steel blue", font = ('calibre',10,'normal'), show = '*') 

e1.grid(row=6, column=1)

label = Label(window,bg = "midnight blue")
label.grid(column=7)

e2.grid(row=8, column=1)

# creating a button using the widget
# Button that will call the submit function
sub_btn=Button(window,text = 'Submit', command = submit, bg = "light cyan", bd = 4, fg = "midnight blue",font=('calibre',10,'bold'))     
sub_btn.grid(row=10,column=1)

label = Label(window,bg = "midnight blue")
label.grid(column=7)

# creating a button using the widget
# Button that will call the decrypt function
decrypt_btn=Button(window,text = 'Click Here To Decrypt', command = decrypt, bg = "light cyan", bd = 4, fg = "midnight blue",font=('calibre',10,'bold'))     
decrypt_btn.grid(row=14,column=1)
label = Label(window,bg = "midnight blue")
label.grid(column=15)

#reminder to change passwords
L3 = Label(window,text = "You will receive a reminder to change passwords\nevery 3 months.You can choose to ignore this\nwhen you receive the reminder.", bg = "light cyan", bd = 4, fg = "midnight blue", font=('calibre',10, 'bold')).grid(row=18,column=1)
reminder()

window.mainloop()


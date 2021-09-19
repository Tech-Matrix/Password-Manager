
import base64
from datetime import datetime
import pyperclip
#be sure to install pyperclip before-- pip install pyperclip
import random
import array
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
      print(encodedstring,type(encodedstring))
      print(base64message,type(base64message))
      file.close()
    
    file = open("user1.txt","a")
    file.write("Your User Name " + username_info)
    file.write("\n")
    file.write("Your Password " + password_info)
    
    file.write("\n")
    file.write("\n")

    username_var.set("")
    passw_var.set("")

    w=Text(window,height=1,width=29,font=('calibre',10,'bold'), bg = "light cyan", fg = "midnight blue")
    w.insert(INSERT,"Encryption copied to clipboard!")
    w.grid(row=11,column=1)

    
    pyperclip.copy(base64message.decode("ascii"))
    spam = pyperclip.paste()
    

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
    #clear all dates and keep last date  
    with open("date.txt", 'r+') as fp:
    
        lines = fp.readlines()    
        fp.seek(0)   
        fp.truncate()
        fp.writelines(lines[-1:])
        fp.close() 

def rand_pass():

  # maximum length of password needed
  # this can be changed to suit your password length
  MAX_LEN = 8

  # declare arrays of the character that we need in out password
  # Represented as chars to enable easy string concatenation
  DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

  UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z']

  SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '/','!','&',
      '*']

  # combines all the character arrays above to form one array
  COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

  # randomly select at least one character from each character set above
  rand_digit = random.choice(DIGITS)
  rand_upper = random.choice(UPCASE_CHARACTERS)
  rand_lower = random.choice(LOCASE_CHARACTERS)
  rand_symbol = random.choice(SYMBOLS)

  # combine the character randomly selected above
  # at this stage, the password contains only 4 characters but
  # we want a 8-character password
  temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


  # now that we are sure we have at least one character from each
  # set of characters, we fill the rest of
  # the password length by selecting randomly from the combined
  # list of character above.
  for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)

    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

  # traverse the temporary password array and append the chars
  # to form the password
  password = ""
  for x in temp_pass_list:
      password = password + x

  passw_var=password
  # print out password
  print(password)
  L3 = Label(window, text="Your Random Password is:  ",font=('calibre',10, 'bold'),bg = "midnight blue", fg="white").grid(row=14)
  label = Label(window,bg = "midnight blue")
  label.grid(column=1)
  
  L4 = Label(window, text=passw_var,font=('calibre',10, 'bold'),padx=20, pady=20, bg = "midnight blue", fg="white").grid(row=14,column=1)
  e2.config(textvariable=passw_var)


L1=Label(window, text="User Name", bg = "light cyan", bd = 4, fg = "midnight blue", font=('calibre',10, 'bold')).grid(row=6)

label = Label(window,bg = "midnight blue")
label.grid(column=10)

L2=Label(window, text="Password", bg = "light cyan", bd = 4, fg = "midnight blue", font=('calibre',10, 'bold')).grid(row=8)

e1 = Entry(window,textvariable = username_var,bg = "light steel blue" , font=('calibre',10,'normal'))
#creating entry for password
e2 =Entry(window, textvariable = passw_var,bg = "light steel blue", font = ('calibre',10,'normal'), show = '*') 

e1.grid(row=6, column=1)

label = Label(window,bg = "midnight blue")
label.grid(column=7)

e2.grid(row=8, column=1)

rand_pass_btn=Button(window,text = 'Generate Random Password', command = rand_pass, bg = "light cyan", bd = 4, fg = "midnight blue",font=('calibre',10,'bold'))
rand_pass_btn.grid(row=10,column=1)

# creating a button using the widget
# Button that will call the submit function
sub_btn=Button(window,text = 'Submit', command = submit, bg = "light cyan", bd = 4, fg = "midnight blue",font=('calibre',10,'bold'))     
sub_btn.grid(row=19,column=1)

label = Label(window,bg = "midnight blue")
label.grid(column=7)


# creating a button using the widget
# Button that will call the decrypt function
decrypt_btn=Button(window,text = 'Click Here To Decrypt', command = decrypt, bg = "light cyan", bd = 4, fg = "midnight blue",font=('calibre',10,'bold'))     
decrypt_btn.grid(row=24,column=1)

#reminder to change passwords
L5 = Label(window,text = "You will receive a reminder to change passwords\nevery 3 months.You can choose to ignore this\nwhen you receive the reminder.", bg = "light cyan", bd = 4, fg = "midnight blue", font=('calibre',10, 'bold')).grid(row=26,column=1)
reminder()

window.mainloop()


	






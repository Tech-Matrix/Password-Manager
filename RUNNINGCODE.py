import base64

#GUI CREATION
from tkinter import *

window=Tk()
window.title('Password Manager') #giving the name to the window
window.geometry("550x300+10+20") #giving the dimensions of the window
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

window.mainloop()


	



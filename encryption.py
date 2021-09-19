from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#creating a public and private key
privateKey = rsa.generate_private_key(public_exponent=65537,key_size=2048)
publicKey = privateKey.public_key()


username_var=input("Enter Username\n")
passw_var=input("Enter password\n")
# defining a function that will get the name and password and print them in a file
#function gets called when the submit button is pressed
def encryptinon():

  username_info = str(username_var)
  password_info = str(passw_var)
  
  passLetter='*'
  print(f"User Name: {username_info}"),
  print(f"Password: {passLetter*len(password_info)}")
  with open(str(username_info)+".txt",'wb+') as file:
    info=username_info+"\n"+password_info
    encodedstring=info.encode()
    #encrypting using a public key and padding it
    encrymsg = publicKey.encrypt(
    encodedstring,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
      )
    )
    file.write(encrymsg)
    print(encodedstring)
    print(encrymsg)
    file.close()
    
    file = open("user1.txt","a")
    file.write("Your User Name " + username_info)
    file.write("\n")
    file.write("Your Password " + password_info)
    
    file.write("\n")
    file.write("\n")


encryptinon()
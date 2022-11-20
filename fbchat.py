import fbcaht
from getpass import getpass
username=str(raw_input("Username : "))
client=fbcaht.Client(username,getpass())
no_of_friends=int(raw_input("Number of Friends : "))
for i in range(no_of_friends):
  name=str(raw_input("Name :"))
  friends=client.searchForUsers(anme)
  friend=friends[0]
  msg=str(raw_input("Message : "))
  sent=client.sendMessage(msg,thread_id=friend.uid)
if sent:
  print("Message sent successfully !")

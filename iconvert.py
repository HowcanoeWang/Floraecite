import base64
open_icon = open("icon.png","rb")
b64str = base64.b64encode(open_icon.read())
print(b64str)
open_icon.close()
write_data = "img = " + str(b64str)
f = open("icon.py","w+")
f.write(write_data)
f.close()
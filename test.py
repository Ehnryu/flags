from flags import Flags
import sys
x = Flags(sys.argv)
print("flag: " + x.flag )
print("arg: " + x.arg)
print("other args: " + str(x.args))
if x.flag == "help":
  print("welcome to help")
  if x.arg == "":
    print("please specify an argument")
    exit()
  print(f"looking up {x.arg}")
  if x.args != []:
    print("using " + str(x.args))
exit()
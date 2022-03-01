# Flags
A dead simple python library to parse bash flags

### Installation:
`pip install bashflags.py`

### Usage:
```python
from flags import Flags
import sys
x = Flags(sys.argv)
print("flag: " + x.flag )
print("arg: " + x.arg)
print("other args" + str(x.args))
if x.flag == "help":
  print("welcome to help")
  if x.arg == "":
    print("please specify an argument")
    exit()
  print(f"looking up {x.arg}")
  if x.args != []:
    print("using " + str(x.args))
exit()
```
The above example when ran with `<file> help arg somefilter` will generate:
```
flag: help
arg: arg
other args: ['somefilter']
welcome to help
looking up arg
using ['somefilter']
```


### Development:
Install buildproj:

`pip install buildproj`

`build`

In case of the binary not working:

`python buildbinary.py`

All processes are automated except for the sign in for pip, please be sure to also change the version and name in `setup.py

### Tests:
Install buildproj:

`pip install buildproj`

`build test`

In case of the binary not working:

`python buildbinary.py test`
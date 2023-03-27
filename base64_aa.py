from base64 import b64encode
  
s = b'pakistan lost in cricket against siri lanka'
# Using base64.b64encode() method
gfg = b64encode(s)


print('\n\n')
print(s)
print('\n\n')
  
print(gfg)

print('\n\n')
import base64
coded_string = '''Q5YACgA...'''
print(base64.b64decode(gfg))

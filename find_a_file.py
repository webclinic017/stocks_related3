##import os, fnmatch
##def find(pattern, path):
##    result = []
##    for root, dirs, files in os.walk(path):
##        for name in files:
##            if fnmatch.fnmatch(name, pattern):
##                result.append(os.path.join(root, name))
##    return result
##
##result=find('*.py', '/home/az2/')
##print(result)
#############################

import os

def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

print(find_files('*.py','/home/az2/'))

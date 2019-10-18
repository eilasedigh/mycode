#!/usr/bin/env python3
  
loginfail=0
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
#keystone_file_lines = keystone_file.readlines()
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail +=1
            print("Login failed for IP "+line.split(" ")[-1])
print("The number of failed log in attempts is", loginfail)

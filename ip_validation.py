# -*- coding: utf-8 -*-
#!/usr/bin/python
# Python program to validate an Ip address
 
# re module provides support
# for regular expressions
import re
 
# Make a regular expression
# for validating an Ip-address
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
      
# Define a function for
# validate an Ip address
def validate_ip_address(Ip): 
 
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, Ip)): 
        print("IP {} is valid.".format(Ip))
        return True
         
    else: 
        print("IP {} is invalid.".format(Ip))
        return False

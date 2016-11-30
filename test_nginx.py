#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"
print "<h1>Lets see if our Python works!</h1>"
print "<br>"
for i in range(6):
    print "<h3>"
    print "Test: " + str(i)
    print "</h3>"
print "</body>"
print "</html>"
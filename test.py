import urllib

url = urllib.urlopen("http://stackoverflow.com/questions/7861775/python-selenium-accessing-html-source") # Open the URL.
content = url.readlines() # Read the source and save it to a variable.
print content
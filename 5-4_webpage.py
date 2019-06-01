import webbrowser

#create a simple webpage with python.
#filepath for temporary files: "c:\\temp\\helloworld.html"

f = open("helloworld.html","w")

message = """ <html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab("helloworld.html")

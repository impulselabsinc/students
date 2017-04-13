import os
try:
    from appJar import gui
except ImportError:
    print "Trying to Install required module: appJar\n"
    import pip
    pip.main(['install', 'appJar'])
    from appJar import gui

def okay(btn):
    app.stop()
    
def press(btn):
    if btn=="Cancel":
        app.stop()
    else:
        user = app.getEntry('user')
        pwd = app.getEntry('pass')
        
        print("User:", user, "Pass:", pwd)
        app.removeAllWidgets()
        app.addLabel("title", "Hello " + user, 0, 0, 2)
        app.addLabel("subtitle", "Your password is '" + pwd + "'", 2, 0, 2)
        app.addButtons(["Submit"], okay, 3, 0, 2)
        
app = gui()

app.addLabel("title", "Welcome to appJar", 0, 0, 2)  # Row 0,Column 0,Span 2
app.addLabel("user", "Username:", 1, 0)              # Row 1,Column 0
app.addEntry("user", 1, 1)                           # Row 1,Column 1
app.addLabel("pass", "Password:", 2, 0)              # Row 2,Column 0
app.addSecretEntry("pass", 2, 1)                     # Row 2,Column 1
app.addButtons(["Submit", "Cancel"], press, 3, 0, 2) # Row 3,Column 0,Span 2

app.setEntryFocus("user")

app.go()

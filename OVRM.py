from appJar import gui
import sqlite3
import csv 
import time 


with open ( "g1.csv", "r" ) as curdat :
            data = curdat.read()
            print()
app = gui("Template Application", "800x400")
def press(btn):
        if btn == "Add": # the button on the entries row
            data = app.getGridEntries("g1")
            app.addTableRow("g1", data)     
            
def press(btn):
    if btn == "Submit":
        nam = app.getEntry("Name")
        sta = app.getCheckBox("Arrived")
        tsl = app.getOptionBox("TimeSlot")
        car = app.getEntry("Car")
        
        
        app.addTableRow("peoplebook",[nam,sta,tsl,car])
        print("Name:",nam)
        print("Stat:",sta)
        print("TimeSlot:",tsl)
        print("In Car:",car)
        with open ( "data.csv", "a" ) as outFile :
            outFile.write(nam)
            outFile.write(",")
            
            outFile.write(tsl)
            outFile.write(",")
            
            outFile.write(tsl)
            outFile.write(",")
            
            outFile.write(car)
            outFile.write(",")
            
            outFile.write("\n")
            
app.startTabbedFrame("MainMenu") 
app.startTab("MainMenu")  
time_label = app.addLabel("time", "")
time_label.config(font=("Arial", 20))
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    app.after(1000, update_time)
update_time() 


app.addToolbar(["File","save","add","settings","Accessibility"], press, findIcon=False)
app.button('Accessibility',app.showAccess, icon='ACCESS')
app.button('help',app.showSplash, icon='HELP')
app.stopTab()

app.startTab("New Driver")
app.addLabel("l1", "Add New Car")
app.addLabelEntry("Name")
app.addCheckBox("Arrived")
app.addLabelOptionBox("TimeSlot",["2:00","2:30","3:00","3:30","4:00","4:30","5:00","5:30","6:00"])

app.addLabelEntry("Car")
app.addButton("Submit",press)
app.stopTab()

app.startTab("Leaderboard")
app.addDbTable("leaderboard","content.db","leaderboard")
app.stopTab()

app.startTab("PeopleBook")
app.addDbTable("peoplebook","content.db","peoplebook")
app.stopTab()

app.startTab("content")
app.addDbTable("content","content.db","content")
app.stopTab()

app.startTab("Control Panel")

app.stopTab()


app.go() 
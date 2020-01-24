from Tkinter import *
import subprocess, sys, os
import xml.etree.ElementTree as ET

tree = ET.parse('batPaths.xml')
root = tree.getroot()

beatstreamPath = root.find('beatstream')
crossbeatsPath = root.find('crossbeats')
nostalgiaPath = root.find('nostalgia')

window = Tk()
window.title("Touchy Beats Launcher")
window.geometry('350x600')
lbl = Label(window, text="Select Game to Launch")
lbl.grid(column=0, row=0)

def beatstreamClicked():
	print("beatstream clicked")
	bstPath = os.path.dirname(os.path.abspath(beatstreamPath.text))
	os.chdir(bstPath) 
	subprocess.Popen(beatstreamPath.text)
	if exitCheckboxState.get():
		sys.exit(0)
beatstreamButton = Button(window, text="BeatStream", command=beatstreamClicked, height = 10, width = 50, bg="pink")
beatstreamButton.grid(column=0, row=2)

def crossBeatsClicked():
	print("CrossBeats clicked")
	cxbPath = os.path.dirname(os.path.abspath(crossbeatsPath.text))
	os.chdir(cxbPath)
	subprocess.Popen(crossbeatsPath.text)
	if exitCheckboxState.get():
		sys.exit(0)
crossBeatsButton = Button(window, text="CrossBeats", command=crossBeatsClicked, height = 10, width = 50, bg="yellow" )
crossBeatsButton.grid(column=0, row=4)

def nostalgiaClicked():
	print("nostalgia clicked")
	nostPath = os.path.dirname(os.path.abspath(nostalgiaPath.text))
	os.chdir(nostPath) 
	subprocess.Popen(nostalgiaPath.text)
	if exitCheckboxState.get():
		sys.exit(0)
nostalgiaButton = Button(window, text="Nostalgia", command=nostalgiaClicked, height = 10, width = 50, bg="light blue" )
nostalgiaButton.grid(column=0, row=6)

exitCheckboxState = BooleanVar()
exitCheckboxState.set(True) #set check state
chk = Checkbutton(window, text='Exit this window on game launch', var=exitCheckboxState)
chk.grid(column=0, row=8)


window.mainloop()
#To import the tkinter library
from tkinter import *
#To import the ttk styled widgets for stylized buttons
from tkinter import ttk
#To import the regex library
import re
#For creating a scrollable text widget
import tkinter.scrolledtext as scrolledtext

#Function to clear contents of all widgets
def __DataClear__():
    tkTextRegex.delete('1.0', 'end')
    tkTextString.delete('1.0','end')
    tkLabelStatus.config(text='')

#Function to validate the input expression with the input text
def __RegexValidator__(kbEvent):
    sRegex = tkTextRegex.get('1.0','end-1c')  #Get complete string from first text box
    sValidatingString = tkTextString.get('1.0','end-1c') #Get complete text from second text box
    start = '1.0' #Initialize starting index for second text box
    if((sRegex == '') or (sValidatingString == '')): #Check if both text boxes have data or not
        tkLabelStatus.config(text="Please enter both input strings for comparison")
        tkTextString.tag_delete('found them')
        tkTextString.tag_delete('fullmatch')
    else:
        if(re.fullmatch(sRegex,sValidatingString)): #Check if complete string matches the regular expression
            tkLabelStatus.config(text="The entered string matches the regex completely")
            tkTextString.tag_add('fullmatch','1.0','end-1c')
            tkTextString.tag_config('fullmatch',foreground='green')
        elif(re.search(sRegex,sValidatingString)): #Check if only parts of string match with regex
            regex_matches = re.finditer(sRegex,sValidatingString) #Find indices of all matching parts
            for match in regex_matches:
                match_start = tkTextString.index("%s+%dc" % (start, match.start()))
                match_end = tkTextString.index("%s+%dc" % (start, match.end()))
                tkTextString.tag_add('found them',match_start,match_end)
                tkTextString.tag_config('found them', foreground='blue') #Highlight the matching parts individually
            tkLabelStatus.config(text="Part of the string matches the regex, please check the highlighted parts!")
        else: #Nothing matches the regex
            tkLabelStatus.config(text="The string doesn't match the given regex")
            tkTextString.tag_delete('found them')
            tkTextString.tag_delete('fullmatch')

#Intitialize tkinter window and place all the components in it
tkRootWindow = Tk()
tkRootWindow.geometry('500x300')
tkRootWindow.title('Regex Validator')
tkLabelRegex = ttk.Label( tkRootWindow, text = 'Input Regex/Normal String:', padding=15)
tkTextRegex = Text(tkRootWindow, height=2, width=32)
tkTextRegex.bind('<KeyRelease>', __RegexValidator__)
tkLabelString = ttk.Label(tkRootWindow, text='Input String that needs validation:',padding=15)
tkTextString = scrolledtext.ScrolledText(tkRootWindow, height=4, width=30)
tkTextString.bind('<KeyRelease>',__RegexValidator__)
tkLabelStatus = ttk.Label(tkRootWindow)
tkButtonClear = ttk.Button(tkRootWindow, text="CLEAR", command=__DataClear__)
tkButtonClose = ttk.Button(tkRootWindow, text="EXIT", command=tkRootWindow.destroy)
tkLabelRegex.grid(row=0,column=0)
tkTextRegex.grid(row=0,column=1,ipadx=3,ipady=3, pady=15)
tkLabelString.grid(row=1, column=0)
tkTextString.grid(row=1,column=1,ipady=3,ipadx=3)
tkButtonClear.grid(row=2,column=0,columnspan=2,pady=15)
tkButtonClose.grid(row=3,column=0,columnspan=2)
tkLabelStatus.grid(row=4,column=0,columnspan=2, pady=15)
tkRootWindow.mainloop()
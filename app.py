import json 
import pycountry
from tkinter import Tk, Label, Button, Entry
from phone_iso3166.country import phone_country
import os
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        pass

    def handle_starttag(self, tag, attrs):
        pass

    def handle_data(self, data):
        pass

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)    

if __name__ == "__main__":
    main()
totalbytes = 0

# get a list of all the files in the current directory
dirlist = os.listdir()
for entry in dirlist:
    # make sure it's a file!
    if os.path.isfile(entry):
        # add the file size to the total
        filesize = os.path.getsize(entry)
        totalbytes += filesize

# create a subdirectory called "results"
os.mkdir("results")

# create the output file
resultsfile = open("results/results.txt", "w+")
if resultsfile.mode == "w+":
    resultsfile.write("Total bytecount:" + str(totalbytes) + "\n")
    resultsfile.write("Files list:\n")
    resultsfile.write("--------------\n")
    # write the results into the file
    for entry in dirlist:
        if os.path.isfile(entry):
            # write the file name to the results ledger
            resultsfile.write(entry + "\n")

    # close the file when done
    resultsfile.close()


class Location_Tracker:
    def __init__(self, App):
        self.window = App
        self.window.title("Phone number Tracker")
        self.window.geometry("500x400")
        self.window.configure(bg="#3f5efb")
        self.window.resizable(False, False)

        #___________Application menu_____________
        Label(App, text="Enter a phone number",fg="white", font=("Times", 20), bg="#3f5efb").place(x=150,y= 30)
        self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
        self.track_button = Button(App, text="Track Country", bg="#22c1c3", relief="sunken")
        self.country_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")

        #___________Place widgets on the window______
        self.phone_number.place(x=170, y=120)
        self.track_button.place(x=200, y=200)
        self.country_label.place(x=100, y=280)

        #__________Linking button with countries ________
        self.track_button.bind("<Button-1>", self.Track_location)
        #255757294146
    
    def Track_location(self,event):
        phone_number = self.phone_number.get()
        country = "Country is Unknown"
        if phone_number:
            tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
            print(tracked)
            if tracked:
                    if hasattr(tracked, "official_name"):
                        country = tracked.official_name
                    else:
                        country = tracked.name
        self.country_label.configure(text=country)



PhoneTracker = Tk()
MyApp = Location_Tracker(PhoneTracker)
PhoneTracker.mainloop()

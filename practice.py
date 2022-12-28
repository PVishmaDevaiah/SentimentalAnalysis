from tkinter import *
import requests
from bs4 import BeautifulSoup
from tkinter import ttk
# create instance for window
root = Tk()
root.geometry("1200x600")
# set title for window
root.title("The Hindhu")
# cricbuzz url to get score updates
url="https://www.thehindu.com/"
def get_score():
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    team_1 = soup.find_all(class_ = "title")[0].get_text()
    
    team_2 = soup.find_all(class_ = "sub-text")[0].get_text()
    teams.config(text=f"{team_1}\n{team_2}")

title = Label(root,text='INDIAN EXPRESS',font= ("Haveltica ",50), fg="black")
title.grid(row = 1,column=0, pady=5)

teams = Label(root, font=("Haveltica 15 bold"))
teams.grid(row = 5, padx=5)
# call function
get_score()
root.mainloop()
  
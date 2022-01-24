from tkinter import *
from tkcalendar import *
import datetime
import requests
import json
from time import strftime
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("CITY WEATHER APP")
root.geometry("1300x950")
root.config(bg='#1a1830')
date=datetime.datetime.now()
y=date.year
m=date.month
d=date.day
wd=date.strftime("%A")
photo=ImageTk.PhotoImage(Image.open(r"night-3.jpg"))
#time on top
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(960, time)
#time label
lbl = Label(root, font=('courier', 25 ),
            background='black',
            foreground='white')
lbl.pack(anchor="w")

time()#time call
Label(root,image=photo).pack()#background photo

#calendar
calendar= Calendar(root,selectmode="day",date_pattern="dd-mm-yyyy",year=y,day=d,background="#332f63",
                   foreground="white",selectforeground="#2f3969",
                   weekendforeground="#332f63", weekendbackground='#a4aaba', font="courier 23 ",pady=10,padx=100,
                   selectbackground='#ffcd69', headersbackground='#767e92', normalbackground="#fffef9",)
calendar.place(x=10,y=120)
date=datetime.date.today().strftime('%d.%m.%Y')

#month display
display=Label(root, text=wd + "   |   " + date, font="times 21 bold ", borderwidth=3,bg="#332f63",fg='White')
display.place(x=0,y=42,width=320)

#weather api function
def find_weather(city):
    #getting storing api data
    link="http://api.openweathermap.org/data/2.5/weather?appid=b9d582354b051f60f58748f2995c2c51&q="
    data=link+city
    info=requests.get(data).json()
    weather_info1=info['weather']
    weather=weather_info1[0]['description'].capitalize()
    weather_info2=info['main']
    temp=weather_info2['temp']
    temp_c=temp-273.15
    #textbox for storing api data.
    weather_info = "forecast: "+city+"\n\n\n\n\n\n\n\n\n\n\tＷeather=:\t" + weather + "\n\n\tＴemperature:\t" + str(
        "{:.2f}".format(temp_c)) + " °C"
    text = Text(root, height=50, width=45, spacing3=2, bg="black",
                fg="white", bd=4, font="Courier")
    text.place(x=850, y=42)
    text.insert(END, weather_info)
    #if-else ladder for picking weather images based on weather.
    if weather_info1[0]['main']=="Smoke" or weather_info1[0]['main']=="Haze" or weather_info1[0]['main']=="Mist" or weather_info1[0]['main']=="Fog":
        photo2 = ImageTk.PhotoImage(Image.open(r"haze.jpg"))
        lab2=Label(root,image=photo2)
        lab2.image=photo2
        lab2.place(x=960,y=90)
    elif weather_info1[0]['main']=="Clouds":
        if weather=="Broken clouds" or weather=="Scattered clouds" or weather=="Few clouds":
            photo2 = ImageTk.PhotoImage(Image.open(r"cloudy_2.jpg"))
            lab2 = Label(root, image=photo2)
            lab2.image = photo2

            lab2.place(x=960, y=90)
        elif weather=="Overcast clouds":
            photo2 = ImageTk.PhotoImage(Image.open(r"overcast_clouds.jpg"))
            lab2 = Label(root, image=photo2)
            lab2.image = photo2
            lab2.place(x=960, y=90)
    elif weather_info1[0]['main'] == "Clear":
        photo2 = ImageTk.PhotoImage(Image.open(r"sunny (1).jpg"))
        lab2 = Label(root, image=photo2)
        lab2.image = photo2
        lab2.place(x=960, y=90)
    elif weather_info1[0]['main'] == "Rain" or weather_info1[0]['main']=="Drizzle" or weather_info1[0]['main']=="Light rain":
        photo2 = ImageTk.PhotoImage(Image.open(r"rainy.png"))
        lab2 = Label(root, image=photo2)
        lab2.image = photo2
        lab2.place(x=960, y=130)
    elif weather_info1[0]['main'] == "Snow":
        photo2 = ImageTk.PhotoImage(Image.open(r"snowy.jpg"))
        lab2 = Label(root, image=photo2)
        lab2.image = photo2
        lab2.place(x=960, y=90)
    elif weather_info1[0]['main'] == "Thunderstorm":
        photo2 = ImageTk.PhotoImage(Image.open(r"thunder-1.png"))
        lab2 = Label(root, image=photo2)
        lab2.image = photo2
        lab2.place(x=960, y=90)
#hourly weather get
def find_hourly(city):
    link = "http://api.openweathermap.org/data/2.5/forecast?appid=b9d582354b051f60f58748f2995c2c51&q="
    data = link + city
    info = requests.get(data).json()
    x = info['list']
    d = {}
    a=[];b=[];c=[]
    k = 1
    for i in x:
        d[k] = i
        k += 1
    x = 1
    hourly_description = []
    for data in d.values():
        weather_info = data['main']
        Z=data['weather']
        W=Z[0]['description'].capitalize()
        hourly_description.append(W)
        unix = data['dt']
        t=(
            datetime.datetime.fromtimestamp(
                unix
            ).strftime('%H:%M %p')
        )
        a.append(t)
        weather_info1 = data['weather']
        temp_c = weather_info['temp'] - 273.15
        b.append(str("{:.2f}".format(temp_c)) + "°C")
        for i in weather_info1:
            w = i['main'].capitalize()
            c.append(w)

        text = Text(root, height=50, width=45, spacing3=2, bg="black",
                    fg="white", bd=0, font="times 12 bold")
        text.place(x=850, y=425)
        for i in a:
            text.insert(INSERT, i + '\n\n'+" ")
        text.insert(END, '\t')
        text = Text(root, height=50, width=30, spacing3=2, bg="black",
                    fg="white", bd=0, font="times 13 bold")
        text.place(x=924, y=425)
        text.insert(INSERT,'\t'+ "      ")
        for i in b:
            text.insert(INSERT,'  '+i + '\n\n\t'+ "      ")
        m=415
        for i in hourly_description:
            if i == "Smoke" or i == "Haze" or i=='mist' or i=='Fog':
                photo2 = ImageTk.PhotoImage(Image.open(r"sunny_s_cloudy-removebg-preview.jpg"))
                lab2 = Label(root, image=photo2, borderwidth=0)
                lab2.image = photo2
                lab2.place(x=1170, y=m)

            elif i == "Clear" or i == "Clear sky":
                photo2 = ImageTk.PhotoImage(Image.open(r"sunny-removebg-preview.jpg"))
                lab2 = Label(root, image=photo2, borderwidth=0)
                lab2.image = photo2
                lab2.place(x=1170, y=m)

            elif i == "Rain" or i == "Light rain" or i=="Drizzle":
                photo2 = ImageTk.PhotoImage(Image.open(r"RAINNNNNN-removebg-preview .jpg"))
                lab2 = Label(root, image=photo2, borderwidth=0)
                lab2.image = photo2
                lab2.place(x=1170, y=m)
            elif i == "Snow" or i == "Light snow" or i =="Heavy snow":
                photo2 = ImageTk.PhotoImage(Image.open(r"snow.jpg"))
                lab2 = Label(root, image=photo2, borderwidth=0)
                lab2.image = photo2
                lab2.place(x=1170, y=m)
            elif i == "Thunderstorm":
                photo2 = ImageTk.PhotoImage(Image.open(r"thunderstorms-removebg-preview.jpg"))
                lab2 = Label(root, image=photo2, borderwidth=0)
                lab2.image = photo2
                lab2.place(x=1170, y=m)
            elif i == "Overcast clouds" or i == "Broken clouds" or i == "Scattered clouds" or i == "Few clouds":
                photo2 = ImageTk.PhotoImage(Image.open(r"cloudz.png"))
                lab2 = Label(root, image=photo2, borderwidth=0)
                lab2.image = photo2
                lab2.place(x=1170, y=m)

            m += 42
        x += 1
        if (x == 7):
            break
    placing()

def placing():
    entry=Entry(root,bd=3,bg="white",fg="black",border=5,relief="flat",font="times 18 ")
    entry.insert(END,'Change City')
    select=Button(root,text="CHECK WEATHER ",font="Courier 20 ",bg="#373a43",fg="white",width=18,command=lambda:[find_weather(entry.get()),find_hourly(entry.get())])
    select.place(x=915,y=720)
    entry.place(x=980,y=670,width=175,height=40)
find_weather('Bangalore'),find_hourly('Bangalore')

###REMINDER

lbl_draft=Label(root, text='Reminders for '+datetime.datetime.strftime(datetime.date.today(), '%d-%m-%Y'),font=('courier', 16 ),
            background='black',
            foreground='white')
lbl_draft.place(x=14,y=470)
scrollb=Scrollbar(root)
textbox=Text(root, height=9, width=60,yscrollcommand=scrollb.set,font=('courier', 13 ),bg='#fffef9')
textbox.place(x=12,y=500)
scrollb.place(x=600,y=500)

#get events and arrange
data_raw=open('data.json', 'r')
data_rem=json.load(data_raw)
data_raw.close()
count=data_rem['count']
tag='color'
today=''

def event_initialize():
    #deleting older reminders
    calendar.calevent_remove('all')
    for even_date in list(data_rem['events'].keys()):
        date=datetime.datetime.strptime(even_date,'%d-%m-%Y').date()
        if date<datetime.date.today():
            del data_rem['events'][even_date]
    #adding events to calendar and textbox
    textbox.delete('1.0',END)
    for even_date,even_list in data_rem['events'].items():
        date=datetime.datetime.strptime(even_date,'%d-%m-%Y').date()
        is_date_today=date==datetime.date.today()
        for even_data in even_list:
            calendar.calevent_create(date,even_data[0],tags=tag)
            calendar.tag_config(tag,foreground="black",background="#897bc0")
            if is_date_today:
                textbox.insert(END, u'\u2022'+even_data[0]+'\n')
                textbox.insert(END, '\t'+even_data[1]+'\n')
            else:
                textbox.delete('1.0',END)
                textbox.insert(END,'no events for selected date')
                

    lbl_draft.config(text='Reminders for '+datetime.datetime.strftime(datetime.date.today(), '%d-%m-%Y'))
event_initialize()
#add data
def Add_window():
    #function to add data to database
    def func1():
        global data_rem
        if even_name_entry.get():
            even_date1=datetime.datetime.strftime(date_enter.get_date(),'%d-%m-%Y')
            even_data_name=even_name_entry.get()
            even_data_desc=even_desc_entry.get('1.0',END)
            if even_date1 in data_rem['events']:
                data_rem['events'][even_date1].append([even_data_name,even_data_desc])
            else:
                data_rem['events'][even_date1]=[[even_data_name,even_data_desc]]
            data_raw=open('data.json','w')
            json.dump(data_rem,fp=data_raw, indent=2)
            data_raw.close()
            even_name_entry.delete(0,END)
            even_desc_entry.delete('1.0',END)
            event_initialize()
            reminder_change()
        else:
            top_add_prob=Toplevel()
            Label(top_add_prob,text='Enter event name',font=('courier', 14 ),bg='#332f63',fg='red').grid(row=0,column=0)
            Button(top_add_prob,text='Close',font=('courier', 14 ),bg='#332f63',fg='white',command=lambda x=1:top_add_prob.destroy()).grid(row=0,column=1)

    #window gui
    top=Toplevel()
    top.title='Add a reminder'
    top.configure(background='#332f63')
    Label(top, text='Enter the date of reminder', font=('courier', 14 ),bg='#332f63',fg='white').grid(row=1,column=1,columnspan=2)
    date_enter=DateEntry(top,font=('courier', 14 ),pady=10,padx=10)
    date_enter.grid(row=2, column=1,columnspan=2)
    Label(top, text='enter name of event', font=('courier', 14 ),bg='#332f63',fg='white').grid(row=3,column=1,columnspan=2)
    even_name_entry=Entry(top, width=25, font=('courier', 14 ))
    even_name_entry.grid(row=4,column=1,columnspan=2)
    Label(top,text='enter event description',font=('courier', 14 ),bg='#332f63',fg='white').grid(row=7,column=1,columnspan=2)
    even_desc_entry=Text(top, height=5,width=30,font=('courier', 14 ),padx=5,pady=5)
    even_desc_entry.grid(row=8,column=1,columnspan=2)
    b1=Button(top,text='Add Reminder', command=func1, font=('courier', 14 ),background='#373a43',foreground='white')
    b2=Button(top, text='close', command=top.destroy, font=('courier', 14 ),background='#373a43',foreground='white')
    b1.grid(rows=9,column=1,sticky='W')
    b2.grid(row=9,column=2,sticky='E')
b_add=Button(root,text='add reminder',command=Add_window, font=('courier', 14 ),background='#373a43',foreground='white')
b_add.place(x=13,y=687)

#switch reminder date
def reminder_change():
    set_date=calendar.get_date()
    lbl_draft.config(text='Reminders for '+set_date)
    if set_date in data_rem['events']:
        textbox.delete('1.0',END)
        for even_data in data_rem['events'][set_date]:
            textbox.insert(END, u'\u2022'+even_data[0]+'\n')
            textbox.insert(END, '\t'+even_data[1]+'\n')
    else:
        textbox.delete('1.0',END)
        textbox.insert(END,'no events for selected date')
B_reminder_change=Button(root,text='see events of selected date',command=reminder_change,font=('courier', 10 ),background='#373a43',foreground='white')
B_reminder_change.place(x=390,y=470)

#delete reminder
def reminder_delete():
    def delete():
        nonlocal selection
        del_var=selection.get().split(':',2)[0]
        del_var=int(del_var)
        del data_rem['events'][set_date][del_var]
        if not data_rem['events'][set_date]:
            del data_rem['events'][set_date]
        data_raw=open('data.json','w')
        json.dump(data_rem,fp=data_raw, indent=2)
        data_raw.close()
        deltop.destroy()
        event_initialize()
        reminder_change()

    set_date=calendar.get_date()
    Options=[]

    if set_date in data_rem['events']:
        for i in range(len(data_rem['events'][set_date])):
                Options.append(str(i)+': '+data_rem['events'][set_date][i][0])
        deltop=Toplevel()
        deltop.configure(background='#332f63')
        selection=StringVar()
        selection.set('Select reminder to delete')
        dropdown=ttk.Combobox(deltop, textvariable=selection, font=('courier', 12 ),width=30,values=Options)
        dropdown.grid(row=0,column=0)
        Button(deltop,text='Delete',command=delete,font=('courier', 14 ),bg='#332f63',fg='white').grid(row=0,column=1)
        Button(deltop,text='Cancel',command=lambda x=1:deltop.destroy(),font=('courier', 14 ),bg='#332f63',fg='white').grid(row=0,column=2)
    else:
        deltop=Toplevel()
        Label(deltop,text='selected date has no events').grid(row=0,column=0)
Button(root,text='delete events in \n selected date',command=reminder_delete, font=('courier', 10 ),background='#373a43',foreground='white').place(x=470,y=687)
root.mainloop()
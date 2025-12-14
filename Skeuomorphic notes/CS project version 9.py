from tkinter import *
import mysql.connector as msc
import os
from pathlib import Path

base_dir = Path(__file__).parent
assets_dir = base_dir/'assets'

use_mysql = False

if use_mysql:
    try:
        mydb=msc.connect(host='localhost',user='root',passwd='Vedineethu10',database='project')
        mycursor=mydb.cursor()
    except:
        mydb=None
        mycursor=None

def save_filename_to_db(filename):
    inp="insert into proj(Filename) values(%s)"
    data=(filename,)
    mycursor.execute(inp,data)
    mydb.commit()


def get_matching_filenames_from_db(text):
    query="select Filename from proj where Filename like '%"+text+"%'"
    mycursor.execute(query)
    out=[]
    for row in mycursor.fetchall():
        out.append(row[0])
    return out


CHAR_IMAGE_MAP={
"a":"IMG_5342_1_11zon.png",
"b":"IMG_5342 2_2_11zon.png",
"c":"IMG_5342 3_3_11zon.png",
"d":'IMG_5342 4_4_11zon.png',
"e":'IMG_5342 5_5_11zon.png',
"f":'IMG_5342 6_6_11zon.png',
"g":'IMG_5342 7_7_11zon.png',
"h":'IMG_5342 8_8_11zon.png',
"i":'IMG_5342 9_9_11zon.png',
"j":'IMG_5342 10_10_11zon.png',
"k":'IMG_5342 11_11_11zon.png',
"l":'IMG_5342 12_12_11zon.png',
"m":'IMG_5342 13_13_11zon.png',
"n":'IMG_5342 14_14_11zon.png',
"o":'IMG_5342 15_15_11zon.png',
"p":'IMG_5342 41_16_11zon.png',
"q":'IMG_5342 16_16_11zon.png',
"r":'IMG_5342 17_17_11zon.png',
"s":'IMG_5342 18_18_11zon.png',
"t":'IMG_5342 19_19_11zon.png',
"u":'IMG_5342 20_20_11zon.png',
"v":'IMG_5342 21_21_11zon.png',
"w":'IMG_5342 22_22_11zon.png',
"x":'IMG_5342 23_23_11zon.png',
"y":'IMG_5342 24_24_11zon.png',
"z":'IMG_5342 25_25_11zon.png',
"A":'IMG_5342 26_1_11zon.png',
"B":'IMG_5342 27_2_11zon.png',
"C":'IMG_5342 28_3_11zon.png',
"D":'IMG_5342 29_4_11zon.png',
"E":'IMG_5342 30_5_11zon.png',
"F":'IMG_5342 31_6_11zon.png',
"G":'IMG_5342 32_7_11zon.png',
"H":'IMG_5342 33_8_11zon.png',
"I":'IMG_5342 34_9_11zon.png',
"J":'IMG_5342 35_10_11zon.png',
"K":'IMG_5342 36_11_11zon.png',
"L":'IMG_5342 37_12_11zon.png',
"M":'IMG_5342 38_13_11zon.png',
"N":'IMG_5342 39_14_11zon.png',
"O":'IMG_5342 40_15_11zon.png',
"P":'IMG_5342 41_16_11zon.png',
"Q":'IMG_5342 42_17_11zon.png',
"R":'IMG_5342 43_18_11zon.png',
"S":'IMG_5342 44_19_11zon.png',
"T":'IMG_5342 45_20_11zon.png',
"U":'IMG_5342 46_21_11zon.png',
"V":'IMG_5342 47_22_11zon.png',
"W":'IMG_5342 48_23_11zon.png',
"X":'IMG_5342 49_24_11zon.png',
"Y":'IMG_5342 50_25_11zon.png',
"Z":'IMG_5342 51_26_11zon.png',
"!":"IMG_5342 52_1_11zon.png",
".":"IMG_5342 53_2_11zon.png",
"?":"IMG_5342 54_3_11zon.png",
"@":"IMG_5342 55_4_11zon.png",
"#":"IMG_5342 56_5_11zon.png",
"$":"IMG_5342 57_6_11zon.png",
"(":"IMG_5342 58_7_11zon.png",
")":"IMG_5342 59_8_11zon.png",
"+":"IMG_5342 60_9_11zon.png",
"-":"IMG_5342 61_10_11zon.png",
"=":"IMG_5342 62_11_11zon.png",
"_":"IMG_5342 63_12_11zon.png",
":":"IMG_5342 64_13_11zon.png",
";":"IMG_5342 65_14_11zon.png",
"\"":"IMG_5342 66_15_11zon.png",
"'":"IMG_5342 67_16_11zon.png",
"<":"IMG_5342 68_17_11zon.png",
">":"IMG_5342 69_18_11zon.png",
"*":"IMG_5342 70_19_11zon.png",
"&":"IMG_5342 71_20_11zon.png",
"^":"IMG_5342 72_21_11zon.png",
"%":"IMG_5342 73_22_11zon.png",
"/":"IMG_5342 74_23_11zon.png",
",":"IMG_5342 75_24_11zon.png",
"[":"IMG_5342 76_25_11zon.png",
"]":"IMG_5342 77_26_11zon.png",
"{":"IMG_5342 78_27_11zon.png",
"}":"IMG_5342 79_28_11zon.png",
"0":"IMG_5342 80_29_11zon.png",
"\\":"IMG_5342 81_30_11zon.png",
"1":"IMG_5342 82_31_11zon.png",
"2":"IMG_5342 83_32_11zon.png",
"3":"IMG_5342 84_33_11zon.png",
"4":"IMG_5342 85_34_11zon.png",
"5":"IMG_5342 86_35_11zon.png",
"6":"IMG_5342 87_36_11zon.png",
"7":"IMG_5342 88_37_11zon.png",
"8":"IMG_5342 89_38_11zon.png",
"9":"IMG_5342 90_39_11zon.png",
}

def show_suggestions(matches):
    window_suggestions=Toplevel()
    window_suggestions.title("File Suggestions")
    window_suggestions.geometry("300x400")
    suggestions_text=Text(window_suggestions,wrap=WORD,width=40,height=20)
    suggestions_text.pack(padx=10,pady=10)
    if matches:
        suggestions_content="Suggested Filenames:\n"+"\n".join(matches)
    else:
        suggestions_content="No matching files found."
    suggestions_text.insert(END,suggestions_content)
    suggestions_text.config(state=DISABLED)
    scrollbar=Scrollbar(window_suggestions,command=suggestions_text.yview)
    scrollbar.pack(side=RIGHT,fill=Y)
    suggestions_text.config(yscrollcommand=scrollbar.set)

def newnote(event):
    global window1,n1,n2,inp,images,labels,entry,canvas
    images=[]
    labels=[]
    inp=''
    n1=0
    n2=0
    window1=Toplevel()
    window1.bind("<Key>",handle_char_press)
    window1.bind("<BackSpace>",backspace)
    window1.bind("<space>",space)
    window1.bind("<Return>",enter)
    window1.geometry("478x850")
    try:
        icon=PhotoImage(file=os.path.join(assets_dir,'REAL_11zon.png'))
        label1=Label(window1,image=icon)
        label1.image=icon
        label1.place(x=0,y=0,relwidth=1,relheight=1)
    except:pass
    
    canvas = Canvas(window1, width=478, height=850)
    bg_img = PhotoImage(file=assets_dir/'REAL_11zon.png')
    canvas.place(x=0,y=0)
    canvas.create_image(-200, 0, image=bg_img, anchor=NW)
    
    
    window1.title("Skeuomorphic notes")
    end=Button(window1,text='Save and exit')
    end.place(x=50,y=20)
    end.config(command=save)
    filename=entry.get().replace("File name?:","").strip()
    filename+=".txt"
    matches=get_matching_filenames_from_db(filename.replace(".txt",""))
    show_suggestions(matches)
    try:
        with open(filename,'r') as file:
            input1=file.read()
            for char in input1:
                if char in CHAR_IMAGE_MAP:
                    add_char_to_screen(char)
                elif char==" ":
                    space()
                elif char=="\n":
                    enter()
    except FileNotFoundError:pass

def space(event=None):
    global n1,inp
    n1+=1
    inp+=" "

def enter(event=None):
    global n1,inp
    n1=((n1//25)+1)*25
    inp+="\n"

def backspace(event=None):
    global inp,n1,images,labels
    if not inp:return
    char_to_remove=inp[-1]
    inp=inp[:-1]
    if char_to_remove==" ":
        n1-=1
    elif char_to_remove=="\n":
        n1_new=0
        for char in inp:
            if char=='\n':
                n1_new=((n1_new//25)+1)*25
            else:
                n1_new+=1
            n1=n1_new
    elif labels:
        last_label=labels.pop()
        last_label.destroy()
        if images:images.pop()
        n1-=1

def save():
    global entry,inp
    filename=entry.get().replace("File name?:","").strip()
    filename+=".txt"
    with open(filename,'w') as f:
        f.write(inp)
    save_filename_to_db(filename.replace(".txt",""))
    window1.destroy()

def add_char_to_screen(char):
    global labels,inp,n1,images,window1,canvas
    if char in CHAR_IMAGE_MAP:
        try:
            img_path = assets_dir/CHAR_IMAGE_MAP[char]
            img=PhotoImage(file=img_path)
            images.append(img)
            #label=Label(window1,image=img,borderwidth=0)
            #label=Label(window1,text=char,borderwidth=0)
            #label.place(x=20+(16*n1)-((n1//25)*400),y=134+((n1//25)*16))
            
            x=20+(16*n1)-((n1//25)*400)
            y=134+((n1//25)*16)
            canvas.create_text(
                x, y,  # X and Y coordinates (center of the canvas)
                text=char,
                font=("Helvetica", 16, "bold"),
                fill="navy", # Text color
            )
            
            #labels.append(label)
            n1+=1
            inp+=char
        except:pass

def handle_char_press(event):
    char=event.char
    if char in CHAR_IMAGE_MAP:
        add_char_to_screen(char)

def newnoteinput():
    global entry
    window2=Toplevel()
    window2.geometry('300x200')
    try:
        icon=PhotoImage(file=os.path.join(assets_dir,'REAL_11zon.png'))
        window2.iconphoto(False,icon)
        label2=Label(window2,image=icon)
        label2.image=icon
        label2.place(x=0,y=0,relwidth=1,relheight=1)
    except:pass
    entry=Entry(window2)
    entry.insert(0,"File name?:")
    entry.place(x=50,y=60)
    entry.bind("<Return>",newnote)

window=Tk()
window.geometry("300x200")
try:
    icon=PhotoImage(file=os.path.join(assets_dir,'REAL_11zon.png'))
    label=Label(window,image=icon)
    label.image=icon
    label.place(x=0,y=0,relwidth=1,relheight=1)
except:pass
window.title("notes")
button=Button(window,text='Open note or create new note')
button.place(x=45,y=40)
button.config(command=newnoteinput)
window.mainloop()


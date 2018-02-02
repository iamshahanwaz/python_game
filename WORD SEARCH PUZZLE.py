from Tkinter import *
from string import *
import tkMessageBox
import string
import Tkinter as tk


def close_win(root):
    root.destroy()
    
def start(root,frame):
    frame.pack_forget()
    root.unbind("<Button-1>")
    root.unbind("<Button-2>")
    root.unbind("<Button-3>")
    root.unbind("<Double-Button-1>")

    
    def inst1(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        frame1.config(background="#f994f1")
        command=lambda:start(root,frame1)
        button1=Button(frame1,text="  BACK  ",bg="green",font=("Algerian",24),relief="raised",command=command)
        button1.grid(row=13,column=5,pady=20)
        ba=Button(frame1,text="WORD SEARCH PUZZLE",width=40,height=1,bg="deepskyblue1",font=("Algerian",20))
        ba.grid(row=1,pady=3)
        bb=Button(frame1,text="0-WINDOWS TITLE tells you about PUZZLE TYPE e.g Fruit puzzle or other",width=80,height=2,bg="goldenrod2")
        bb.grid(row=2,pady=3)
        bb=Button(frame1,text="1-To move a word RIGHTWARDS hover curser over that word & click LEFT BUTTON",width=80,height=2,bg="goldenrod2")
        bb.grid(row=3,pady=3)
        bb=Button(frame1,text="2-To move a word LEFTWARDS hover curser over that word & click RIGHT BUTTON",width=80,height=2,bg="goldenrod2")
        bb.grid(row=4,pady=3)
        bb=Button(frame1,text="3-To move a word UPWARDS hover curser over that word & click MIDDLE BUTTON",width=80,height=2,bg="goldenrod2")
        bb.grid(row=5,pady=3)
        bb=Button(frame1,text="4-To move a word DOWNWARDS hover curser over word below it & click MIDDLE BUTTON",width=80,height=2,bg="goldenrod2")
        bb.grid(row=6,pady=3)
        bc=Button(frame1,text="5-Word matching works from LEFT-->RIGHT and TOP-->BOTTOM",width=80,height=2,bg="goldenrod2")
        bc.grid(row=7,pady=3)
        bd=Button(frame1,text="6-Get default puzzle by using RESET",width=80,height=2,bg="goldenrod2")
        bd.grid(row=8,pady=3)
        be=Button(frame1,text="7-Click SUBMIT to get result when you are done",width=80,height=2,bg="goldenrod2")
        be.grid(row=9,pady=3)
        bf=Button(frame1,text="8-On submit you get your score",width=80,height=2,bg="goldenrod2")
        bf.grid(row=10,pady=3)
        bi=Button(frame1,text="9-Under score GREEN COLOURED are words you found while RED COLOURED are words you missed",width=80,height=2,bg="goldenrod2")
        bi.grid(row=11,pady=3)
        bj=Button(frame1,text="10-STARS are given to you as achievements as per your score",width=80,height=2,bg="goldenrod2")
        bj.grid(row=12,pady=3)
        frame1.pack()   


    def Easy(root,frame):
        frame.pack_forget()
        frame1=Frame(root)

        p=[0,0,0,0,0,0,0,0,0,0]
        b=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        A=[['D','Z','O','R','B','G'],['T','U','M','C','A','M'],['S','T','O','T','H','L'],['W','L','F','K','L','O'],['E','B','T','E','A','L'],['R','A','H','A','L','E']]
        A1=["D O G","R A T","E E L","B A T","B U L L","H A R E","S L O T H","C A T","W O L F","C O W"]
        '''RTitle=root.title("Windows")
        RWidth=root.winfo_screenwidth()
        RHeight=root.winfo_screenheight()
        root.geometry(("%dx%d")%(RWidth,RHeight))'''
        root.title("ANIMAL WORD PUZZLE")
        frame1.configure(background="#f994f1",pady=120,padx=50)
        J=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        '''Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        #Create & Configure frame 
        frame=Frame(root)
        frame.grid(row=0, column=0, sticky=N+S+E+W)'''

        def check1(root,frame):
            frame.pack_forget()
            frame1=Frame(root)
            frame1.configure(background="#f994f1")
                
            g=0
            z=1
            counter=0
            for i in range(6):
                for j in range(6):
                         J[g]=b[i][j]["text"]
                         g=g+1
                
            for i in range(6):
                for j in range(6):
                         J[g]=b[j][i]["text"]
                         g=g+1
            k=string.join(J)
            for i in range(0,10):
                if A1[i] in k:
                        print A1[i]
                        counter=counter+1
                        
            result1=(counter*100)/10
            print result1
            if(result1==0):
                    z=0
                   
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=0,pady=10)
                    photo=PhotoImage(file="faile.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    
            elif(result1>0 and result1<=20):
                    z=1
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="failed3.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,padx=0,pady=2)
            elif(result1>20 and result1<=40):
                    z=3
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="nhp1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,pady=2)
                    bi1=Button(frame1,image=photo,width="36",height="30")
                    bi1.grid(row=3,column=2,pady=2)
            elif(result1>40 and result1<=60):
                    z=4
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="vgood.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,padx=0)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2,padx=0)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3,padx=0)
            elif(result1>60 and result1<81):
                    z=5
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="awesome1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
            else :
                    z=6
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="congo1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                
            c1=lambda:Easy(root,frame1)
            c2=lambda:close_win(root)
            button3=Button(frame1,text="TRY AGAIN",width=11,height=2,bg="#00bfa5",font=("Algerian"),command=c1)
            button3.grid(row=15,column=6,padx=50)
            button4=Button(frame1,text="EXIT",width=11,height=2,bg="gold",font=("Algerian"),command=c2)
            button4.grid(row=15,column=7)
            for i in range(10):
                if A1[i] in k:
                        p[i]=Button(frame1,text=A1[i],width=10,bg="green2",font=("Arialblack"))
                        p[i].grid(row=6+i,padx=85,pady=5)
                   
            for i in range(10):
                if A1[i] not in k:
                        p[i]=Button(frame1,text=A1[i],width=10,bg="red",font=("Arialblack"))
                        p[i].grid(row=6+i,padx=85,pady=5)
                        
            RTitle=root.title("RESULTS")
            RWidth=1367
            RHeight=768
            root.geometry(("%dx%d")%(RWidth,RHeight))
            root.configure(background="#f994f1")
            frame1.pack()
            root.mainloop()

        for i in range(6):
                for j in range(6):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def reset_1():
            for i in range(6):
                for j in range(6):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def mouse_L(event):
            try:
                grid_info = event.widget.grid_info()
                print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
                if(int(grid_info["column"])>0):
                    b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])-1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])-1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
                else:
                   tkMessageBox.showwarning("Alert","Wrong Move")
            except Exception:
                print
        def mouse_U(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if(int(grid_info["row"])>0):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])-1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])-1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_R(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["column"])<5):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])+1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])+1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_D(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["row"])<5):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])+1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])+1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")

        command=lambda :check1(root,frame1)
        command1=lambda :inst1(root,frame1)
        cc=lambda:start(root,frame1)
        ok=Button(frame1,text="SUBMIT",height=2,width=7,bg="cyan3",command=command)
        ok.grid(row=7,column=2,pady=5)
        re=Button(frame1,text="RESET",height=2,width=7,bg="#ffab00",command=reset_1)
        re.grid(row=7,column=3,pady=5)
        re=Button(frame1,text=" BACK ",height=2,width=12,bg="green2",font=("Algerian"),command=cc)
        re.grid(row=8,column=13,pady=5)
        frame1.pack()   
        root.bind("<Button-1>", mouse_L)
        root.bind("<Button-2>", mouse_U)
        root.bind("<Button-3>", mouse_R)
        root.bind("<Double-Button-1>", mouse_D)

        root.mainloop()

    
    def Medium(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        RTitle=root.title("Windows")
        RWidth=1366
        RHeight=768
        root.geometry(("%dx%d")%(RWidth,RHeight))
        p=[0,0,0,0,0,0,0,0,0,0]
        b=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        A=[['P','C','W','N','L','K','T','A'],['E','A','C','R','X','E','S','D'],['U','S','B','F','U','D','T','N'],['I','E','E','O','H','L','R','C'],['A','I','E','H','X','S','S','W'],['L','E','R','R','Q','O','L','T'],['G','A','O','S','U','N','A','S'],['L','K','Z','P','E','E','R','N']]
        A1=["P L A N C K","T E S L A","G A U S S","N E W T O N","K E P L E R","E D I S O N","B O H R","P A S C A L","C U R I E","E U L E R"]
        '''RTitle=root.title("Windows")
        RWidth=root.winfo_screenwidth()
        RHeight=root.winfo_screenheight()
        root.geometry(("%dx%d")%(RWidth,RHeight))'''
        root.title("SCIENTISTS LAST NAME WORD PUZZLE")
        frame1.configure(background="#f994f1",pady=90,padx=90)
        J=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        '''Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        #Create & Configure frame 
        frame=Frame(root)
        frame.grid(row=0, column=0, sticky=N+S+E+W)'''

        def check2(root,frame):
            frame.pack_forget()
            frame1=Frame(root)
            frame1.configure(background="#f994f1")    
            g=0
            z=1
            counter=0
            for i in range(8):
                for j in range(8):
                         J[g]=b[i][j]["text"]
                         g=g+1
                
            for i in range(8):
                for j in range(8):
                         J[g]=b[j][i]["text"]
                         g=g+1
            k=string.join(J)
            for i in range(0,10):
                if A1[i] in k:
                        print A1[i]
                        counter=counter+1
                        
            result1=(counter*100)/10
            print result1
            if(result1==0):
                    z=0
                   
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=0,pady=10)
                    photo=PhotoImage(file="faile.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    
            elif(result1>0 and result1<=20):
                    z=1
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="failed3.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,padx=0,pady=2)
            elif(result1>20 and result1<=40):
                    z=3
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="nhp1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,pady=2)
                    bi1=Button(frame1,image=photo,width="36",height="30")
                    bi1.grid(row=3,column=2,pady=2)
            elif(result1>40 and result1<=60):
                    z=4
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="vgood.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,padx=0)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2,padx=0)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3,padx=0)
            elif(result1>60 and result1<81):
                    z=5
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="awesome1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
            else :
                    z=6
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="congo1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                
                
            c1=lambda:Medium(root,frame1)
            c2=lambda:close_win(root)
            button3=Button(frame1,text="TRY AGAIN",width=11,height=2,bg="#00bfa5",font=("Algerian"),command=c1)
            button3.grid(row=15,column=6,padx=50)
            button4=Button(frame1,text="EXIT",width=11,height=2,bg="gold",font=("Algerian"),command=c2)
            button4.grid(row=15,column=7)
            for i in range(10):
                if A1[i] in k:
                        p[i]=Button(frame1,text=A1[i],width=10,bg="green2",font=("Arialblack"))
                        p[i].grid(row=6+i,padx=85,pady=5)
                   
            for i in range(10):
                if A1[i] not in k:
                        p[i]=Button(frame1,text=A1[i],width=10,bg="red",font=("Arialblack"))
                        p[i].grid(row=6+i,padx=85,pady=5)
                        
            RTitle=root.title("RESULTS")
            RWidth=1367
            RHeight=768
            root.geometry(("%dx%d")%(RWidth,RHeight))
            #photo1=PhotoImage(file="bg.gif")
            root.configure(background="#f994f1")
            frame1.pack()
            root.mainloop()

        for i in range(8):
                for j in range(8):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def reset_1():
            for i in range(8):
                for j in range(8):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def mouse_L(event):
            try:
                grid_info = event.widget.grid_info()
                print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
                if(int(grid_info["column"])>0):
                    b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])-1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])-1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
                else:
                   tkMessageBox.showwarning("Alert","Wrong Move")
            except Exception:
                print
        def mouse_U(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if(int(grid_info["row"])>0):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])-1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])-1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_R(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["column"])<7):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])+1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])+1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_D(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["row"])<7):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])+1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])+1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")

        command=lambda :check2(root,frame1)
        command1=lambda :inst2(root,frame1)
        cc=lambda:start(root,frame1)
        ok=Button(frame1,text="SUBMIT",height=2,width=7,bg="cyan3",command=command)
        ok.grid(row=10,column=3,pady=5)
        re=Button(frame1,text="RESET",height=2,width=7,bg="#ffab00",command=reset_1)
        re.grid(row=10,column=4,pady=5)
        re=Button(frame1,text=" BACK ",height=2,width=12,bg="green2",font=("Algerian"),command=cc)
        re.grid(row=14,column=15,pady=0)
        frame1.pack()   
        root.bind("<Button-1>", mouse_L)
        root.bind("<Button-2>", mouse_U)
        root.bind("<Button-3>", mouse_R)
        root.bind("<Double-Button-1>", mouse_D)

        root.mainloop()

    def Hard(root,frame):
        frame.pack_forget()
        frame1=Frame(root)
        RTitle=root.title("Windows")
        RWidth=1367
        RHeight=768
        root.geometry(("%dx%d")%(RWidth,RHeight))
        p=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        b=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        A=[['R','R','C','A','A','H','N','V','L','P'],['O','H','D','R','O','L','R','A','T','S'],['S','A','V','K','E','Y','E','W','H','N'],['T','L','W','T','N','A','M','T','N','A'],['M','L','B','C','K','A','O','L','T','B'],['L','O','O','P','D','A','E','D','F','N',],['H','K','L','U','H','N','W','B','M','O'],['N','A','M','R','E','D','I','P','S','R'],['F','F','W','N','V','G','H','D','P','I'],['A','N','F','M','L','S','O','J','C','N']]
        A1=["A N T M A N","D E A D P O O L","B L A C K B O L T","F A L C O N","S P I D E R M A N","I R O N M A N","S T A R L O R D","T H O R","H A W K E Y E","H U L K"]
        '''RTitle=root.title("Windows")
        RWidth=root.winfo_screenwidth()
        RHeight=root.winfo_screenheight()
        root.geometry(("%dx%d")%(RWidth,RHeight))'''
        root.title("MARVEL'S UNIVERSE WORD PUZZLE")
        frame1.configure(background="#f994f1")
        J=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        '''Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        #Create & Configure frame 
        frame=Frame(root)
        frame.grid(row=0, column=0, sticky=N+S+E+W)'''

        def check3(root,frame):
            frame.pack_forget()
            frame1=Frame(root)
            frame1.configure(background="#f994f1")   
            g=0
            z=1
            counter=0
            for i in range(10):
                for j in range(10):
                         J[g]=b[i][j]["text"]
                         g=g+1
                
            for i in range(10):
                for j in range(10):
                         J[g]=b[j][i]["text"]
                         g=g+1
            k=string.join(J)
            for i in range(0,10):
                if A1[i] in k:
                        print A1[i]
                        counter=counter+1
                        
            result1=(counter*100)/10
            print result1
            if(result1==0):
                    z=0
                   
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=0,pady=10)
                    photo=PhotoImage(file="faile.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    
            elif(result1>0 and result1<=20):
                    z=1
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="failed3.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,padx=0,pady=2)
            elif(result1>20 and result1<=40):
                    z=3
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="nhp1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,pady=2)
                    bi1=Button(frame1,image=photo,width="36",height="30")
                    bi1.grid(row=3,column=2,pady=2)
            elif(result1>40 and result1<=60):
                    z=4
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="vgood.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1,padx=0)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2,padx=0)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3,padx=0)
            elif(result1>60 and result1<81):
                    z=5
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="awesome1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
            else :
                    z=6
                    l2=Button(frame1,text="YOUR RESULT IS "+str(result1)+"%",width=35,height=2,bg="deepskyblue1",font=("Algerian"))
                    l2.grid(row=2,padx=10,pady=10)
                    ph=PhotoImage(file="congo1.gif")
                    bi=Button(frame1,image=ph,width="150",height="100",bg="#f994f1")
                    bi.grid(row=3,padx=0,pady=2)
                    photo=PhotoImage(file="r1.gif")
                    #p1=photo.subsample(10,10)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=1)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=2)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=3)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=4)
                    bi=Button(frame1,image=photo,width="36",height="30")
                    bi.grid(row=3,column=5)
                
                
            c1=lambda:Hard(root,frame1)
            c2=lambda:close_win(root)
            button3=Button(frame1,text="TRY AGAIN",width=11,height=2,bg="#00bfa5",font=("Algerian"),command=c1)
            button3.grid(row=15,column=6,padx=50)
            button4=Button(frame1,text="EXIT",width=11,height=2,bg="gold",font=("Algerian"),command=c2)
            button4.grid(row=15,column=7)
            for i in range(10):
                if A1[i] in k:
                        p[i]=Button(frame1,text=A1[i],width=15,bg="green2",font=("Arialblack"))
                        p[i].grid(row=6+i,padx=85,pady=5)
                   
            for i in range(10):
                if A1[i] not in k:
                        p[i]=Button(frame1,text=A1[i],width=15,bg="red",font=("Arialblack"))
                        p[i].grid(row=6+i,padx=85,pady=5)
            RTitle=root.title("RESULTS")
            RWidth=1367
            RHeight=768
            root.geometry(("%dx%d")%(RWidth,RHeight))
            #photo1=PhotoImage(file="bg.gif")
            root.configure(background="#f994f1")
            frame1.pack()
            root.mainloop()
            
        for i in range(10):
                for j in range(10):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def reset_1():
            for i in range(10):
                for j in range(10):
                    b[i][j] = Button(frame1,text=A[i][j],width=7,height=2,bg="black",fg="white") 
                    b[i][j].grid(row=i, column=j,padx=5,pady=5)
                    
        def mouse_L(event):
            try:
                grid_info = event.widget.grid_info()
                print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
                if(int(grid_info["column"])>0):
                    b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])-1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])-1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
                else:
                   tkMessageBox.showwarning("Alert","Wrong Move")
            except Exception:
                print
        def mouse_U(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if(int(grid_info["row"])>0):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])-1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])-1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_R(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["column"])<9):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])+1]["text"]=b[int(grid_info["row"])][int(grid_info["column"])+1]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        def mouse_D(event):
            grid_info = event.widget.grid_info()
            print("row:", int(grid_info["row"]), "column:",int(grid_info["column"]))
            if (int(grid_info["row"])<9):
                b[int(grid_info["row"])][int(grid_info["column"])]["text"],b[int(grid_info["row"])+1][int(grid_info["column"])]["text"]=b[int(grid_info["row"])+1][int(grid_info["column"])]["text"],b[int(grid_info["row"])][int(grid_info["column"])]["text"]
            else:
                tkMessageBox.showwarning("Alert","Wrong Move")
        command=lambda :check3(root,frame1)
        command1=lambda :inst3(root,frame1)
        cc=lambda:start(root,frame1)
        ok=Button(frame1,text="SUBMIT",height=2,width=7,bg="cyan3",command=command)
        ok.grid(row=12,column=4,pady=5)
        re=Button(frame1,text="RESET",height=2,width=7,bg="#ffab00",command=reset_1)
        re.grid(row=12,column=5,pady=5)
        re=Button(frame1,text=" BACK ",height=2,width=12,bg="green2",font=("Algerian"),command=cc)
        re.grid(row=14,column=15,pady=0)
        frame1.pack()   
        root.bind("<Button-1>", mouse_L)
        root.bind("<Button-2>", mouse_U)
        root.bind("<Button-3>", mouse_R)
        root.bind("<Double-Button-1>", mouse_D)
        root.mainloop()


    

    
    frame1=Frame(root)
    frame1.configure(background="#f994f1",pady=100)
    command=lambda :Easy(root,frame1)
    command1=lambda :Medium(root,frame1)
    command2=lambda :Hard(root,frame1)
    command3=lambda :inst1(root,frame1)
    ok=Button(frame1,text=" EASY ",height=2,width=12,bg="turquoise1",font=("Algerian",20),command=command)
    ok1=Button(frame1,text=" MEDIUM ",height=2,width=12,bg="orange",font=("Algerian",20),command=command1)
    ok2=Button(frame1,text=" HARD ",height=2,width=12,bg="red",font=("Algerian",20),command=command2)
    ok3=Button(frame1,text=" INSTRUCTIONS ",height=2,width=12,bg="royal blue",font=("Algerian",20),command=command3)
    ok.grid(pady=20)
    ok1.grid(pady=20)
    ok2.grid(pady=20)
    ok3.grid(pady=20)
    frame1.pack()
    root.mainloop()

root=Tk()
root.title("WORD PUZZLE")
root.resizable(1,1)
RTitle=root.title("WORD PUZZLE")
RWidth=1368
RHeight=768
root.geometry(("%dx%d")%(RWidth,RHeight))
root.configure(background="#f994f1")
ph=PhotoImage(file="puzzle.gif")
w=Label(image=ph)
w.place(x=0, y=0, relwidth=1, relheight=1)
w.ph = ph
frame=Frame(root,width=300)
frame.configure(background="#f994f1",pady=200)
ph=PhotoImage(file="puzzle.gif")
w=Label(frame,image=ph)
w.place(x=0, y=0, relwidth=1, relheight=1)
w.ph = ph
command=lambda :start(root,frame)
command1=lambda :close_win(root)
command2=lambda :credit(root,frame)
ok=Button(frame,text=" START GAME ",height=2,width=20,bg="green",font=("Algerian",24),command=command)
ok2=Button(frame,text=" EXIT ",height=2,width=20,bg="red",font=("Algerian",24),command=command1)
ok.grid(pady=25)
ok2.grid(pady=25)
frame.pack_propagate(0)
w.pack()
frame.pack()
root.mainloop()

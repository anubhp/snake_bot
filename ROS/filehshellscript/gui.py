##-*- coding: utf-8 -*-

from Tkinter import *

import os

import subprocess,sys

import tkMessageBox



mode=0;    ## default random value





## mode=0> Simulation     mode=1> Gait





def isflt(s):

      return ((s.replace('.','',1)).isdigit());









def set1():

      if(mode==1):

		

	     if( (isflt(ax.get())) and (isflt(ay.get())) and (isflt(sx.get())) and (isflt(sy.get()))):



		   if((float(ax.get())>=0) and (float(ax.get())<=150) and (float(ay.get())>=0) and (float(ay.get())<=150)):

		        

			fo = open("new.txt", "w+");

			fo.write( "A_x="+(ax.get())+";A_y="+(ay.get())+";W_x="+(sx.get())+";W_y="+(sy.get())+";");

			fo.close()



			os.system('sh /root/replace.sh');





			fo = open("prev.txt", "w+");

			fo.write( "A_x="+(ax.get())+";A_y="+(ay.get())+";W_x="+(sx.get())+";W_y="+(sy.get())+";");

			fo.close()

		   

		   else:

		        tkMessageBox.showinfo("Warning!", "Amplitude should be\n in 0-150 range!")



	     

	     else:

		   tkMessageBox.showinfo("Warning!", "Invalid Entry..!!")



      else:

         tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")

             







def sim_set():

	if(mode==0):

	     e1=(isflt(a0.get())) and (isflt(a1.get())) and (isflt(a2.get())) and (isflt(a3.get())) and (isflt(a4.get())) and (isflt(a5.get()))

	     e2=(isflt(a6.get())) and (isflt(a7.get())) and (isflt(a8.get())) and (isflt(a9.get())) 

	     e3=(isflt(s0.get())) and (isflt(s1.get())) and (isflt(s2.get())) and (isflt(s3.get())) and (isflt(s4.get())) and (isflt(s5.get()))

	     e4=(isflt(s6.get())) and (isflt(s7.get())) and (isflt(s8.get())) and (isflt(s9.get())) 

	     e5=(isflt(p0.get())) and (isflt(p1.get())) and (isflt(p2.get())) and (isflt(p3.get())) and (isflt(p4.get())) and (isflt(p5.get()))

	     e6=(isflt(p6.get())) and (isflt(p7.get())) and (isflt(p8.get())) and (isflt(p9.get())) 

	     

	     

	     

	     

	     if(e1 and e2 and e3 and e4 and e5 and e6):

		   f1=(float(a0.get())>=0) and (float(a0.get())<=150) and (float(a1.get())>=0) and (float(a2.get())<=150)

		   f2=(float(a2.get())>=0) and (float(a2.get())<=150) and (float(a3.get())>=0) and (float(a3.get())<=150)

		   f3=(float(a4.get())>=0) and (float(a4.get())<=150) and (float(a5.get())>=0) and (float(a5.get())<=150)

		   f4=(float(a6.get())>=0) and (float(a6.get())<=150) and (float(a7.get())>=0) and (float(a7.get())<=150)

		   f5=(float(a8.get())>=0) and (float(a8.get())<=150) and (float(a9.get())>=0) and (float(a9.get())<=150)

		   

		   

		   if(f1 and f2 and f3 and f4 and f5):

		        

		

			fo = open("newsim.txt", "w+");

			fo.write( "A0="+a0.get()+";A1="+a1.get()+";A2="+a2.get()+";A3="+a3.get()+";A4="+a4.get()+";A5="+a5.get()+";");

			fo.write( "A6="+a6.get()+";A7="+a7.get()+";A8="+a8.get()+";A9="+a9.get()+";W0="+s0.get()+";W1="+s1.get()+";");

			fo.write( "W2="+s2.get()+";W3="+s3.get()+";W4="+s4.get()+";W5="+s5.get()+";W6="+s6.get()+";W7="+s7.get()+";");

			fo.write( "W8="+s8.get()+";W9="+s9.get()+";ph0="+p0.get()+";ph1="+p1.get()+";ph2="+p2.get()+";ph3="+p3.get()+";");

			fo.write( "ph4="+p4.get()+";ph5="+p5.get()+";ph6="+p6.get()+";ph7="+p7.get()+";ph8="+p8.get()+";ph9="+p9.get()+";");

			fo.close()



			os.system('sh /root/replacesim.sh');





			fo = open("prevsim.txt", "w+");

			fo.write( "A0="+a0.get()+";A1="+a1.get()+";A2="+a2.get()+";A3="+a3.get()+";A4="+a4.get()+";A5="+a5.get()+";");

			fo.write( "A6="+a6.get()+";A7="+a7.get()+";A8="+a8.get()+";A9="+a9.get()+";W0="+s0.get()+";W1="+s1.get()+";");

			fo.write( "W2="+s2.get()+";W3="+s3.get()+";W4="+s4.get()+";W5="+s5.get()+";W6="+s6.get()+";W7="+s7.get()+";");

			fo.write( "W8="+s8.get()+";W9="+s9.get()+";ph0="+p0.get()+";ph1="+p1.get()+";ph2="+p2.get()+";ph3="+p3.get()+";");

			fo.write( "ph4="+p4.get()+";ph5="+p5.get()+";ph6="+p6.get()+";ph7="+p7.get()+";ph8="+p8.get()+";ph9="+p9.get()+";");

			fo.close()



		   else:

		        tkMessageBox.showinfo("Warning!", "Amplitude should be\n in 0-150 range!")



	     

	     else:

		   tkMessageBox.showinfo("Warning!", "Invalid Entry..!!")



        else:

             tkMessageBox.showinfo("Status:", "Simulation Mode Disabled!!")

               







def save():

  if(mode==0):

    if (len(sv.get())==0):

        tkMessageBox.showinfo("Warning!", "Name field empty!!")

    else:

        fo = open("gait_params_data.txt", "a");

	fo.write( sv.get()+" :");

        fo.write( "\nA0="+a0.get()+"\tW0="+s0.get()+"\tph0="+p0.get()+"\nA1="+a1.get()+"\tW1="+s1.get()+"\tph1="+p1.get());

        fo.write( "\nA2="+a2.get()+"\tW2="+s2.get()+"\tph2="+p2.get()+"\nA3="+a3.get()+"\tW3="+s3.get()+"\tph3="+p3.get());

        fo.write( "\nA4="+a4.get()+"\tW4="+s4.get()+"\tph4="+p4.get()+"\nA5="+a5.get()+"\tW5="+s5.get()+"\tph5="+p5.get());

        fo.write( "\nA6="+a6.get()+"\tW6="+s6.get()+"\tph6="+p6.get()+"\nA7="+a7.get()+"\tW7="+s7.get()+"\tph7="+p7.get());

        fo.write( "\nA8="+a8.get()+"\tW8="+s8.get()+"\tph8="+p8.get()+"\nA9="+a9.get()+"\tW9="+s9.get()+"\tph9="+p9.get()+"\n\n");

        fo.close();

      

  else:

     tkMessageBox.showinfo("Status:", "Simulation Mode Disabled!!")

             





def openfile():

     os.system('gedit gait_params_data.txt')







def callback1():

    #execfile("script.py")

    os.system("sh /root/start.sh")

    lb1.configure(text="Permissions Changed.. :)")



def callback2():

    #execfile("script.py")

    os.system("gnome-terminal -e 'bash -c \"/root/./feedbackmanager.sh; exec bash\"'")





def callback3():

  if(mode==1):  

    lb.configure(text="Status : Running.. :)")

    os.system("gnome-terminal -e 'bash -c \"/root/./sidewinding.sh; exec bash\"'")

    ##lb.configure(text="Status : Not Running..")

  else:

    tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")


def callback4():

  if(mode==1):  

    lb.configure(text="Status : Running.. :)")

    os.system("gnome-terminal -e 'bash -c \"/root/./moveforward.sh; exec bash\"'")

    ##lb.configure(text="Status : Not Running..")

  else:

    tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")

             
def callback5():

  if(mode==1):  

    lb.configure(text="Status : Running.. :)")

    os.system("gnome-terminal -e 'bash -c \"/root/./rotateright.sh; exec bash\"'")

    ##lb.configure(text="Status : Not Running..")

  else:

    tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")


def callback6():

  if(mode==1):  

    lb.configure(text="Status : Running.. :)")

    os.system("gnome-terminal -e 'bash -c \"/root/./rolling.sh; exec bash\"'")

    ##lb.configure(text="Status : Not Running..")

  else:

    tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")


def callback7():

  if(mode==1):  

    lb.configure(text="Status : Running.. :)")

    os.system("gnome-terminal -e 'bash -c \"/root/./mamba.sh; exec bash\"'")

    ##lb.configure(text="Status : Not Running..")

  else:

    tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")
  

def callback8():

  if(mode==1):  

    lb.configure(text="Status : Running.. :)")

    os.system("gnome-terminal -e 'bash -c \"/root/./movebackward.sh; exec bash\"'")

    ##lb.configure(text="Status : Not Running..")

  else:

    tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")

def callback9():

  if(mode==1):  

    lb.configure(text="Status : Running.. :)")

    os.system("gnome-terminal -e 'bash -c \"/root/./rotateleft.sh; exec bash\"'")

    ##lb.configure(text="Status : Not Running..")

  else:

    tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")

def callback10():

  if(mode==1):  

    lb.configure(text="Status : Running.. :)")

    os.system("gnome-terminal -e 'bash -c \"/root/./rolling.sh; exec bash\"'")

    ##lb.configure(text="Status : Not Running..")

  else:

    tkMessageBox.showinfo("Status:", "Gait Mode Disabled!!")


def sim_run():

    if(mode==0):

      #lb.configure(text="Status : Running.. :)")

      lb["text"]="Status : Running.. :)"

      os.system("gnome-terminal -e 'bash -c \"/root/./dynamix.sh; exec bash\"'")

    else:

      tkMessageBox.showinfo("Status:", "Simulation Mode Disabled!!")

             





def callback11():

    #execfile("script.py")

    #os.system("gnome-terminal -e 'bash -c \"pkill terminal; exec bash\"'")

    exit()





def simulation():

    global mode

    mode=0

    gait_lb.configure(text="Gait Mode : Disabled ")

    sim_lb.configure(text="Simulation Mode : Enabled   ")

      

    

def gait():

    global mode

    mode=1

    gait_lb.configure(text="Gait Mode : Enabled   ")

    sim_lb.configure(text="Simulation Mode : Disabled ")







master = Tk()

master.title("Snake Bot")

master.geometry("1000x680")



app=Frame(master)

app.grid()









gait_lb=Label(master, text="Gait Mode : Disabled ")

gait_lb.grid(row=20)

sim_lb=Label(master, text="Simulation Mode : Enabled   ")

sim_lb.grid(row=3)



Label(master, text="     Select Mode: ").grid(row=2,column=1)



Label(master, text="PROCEDURE").grid(row=3,column=5)

Label(master, text="1.Click on 'Start'").grid(row=5,column=5)

Label(master, text="   2.Select Mode [Simulation/Gait]").grid(row=7,column=5)

Label(master, text="3.Enter the Values").grid(row=9,column=5)

Label(master, text="4.Click on 'Set'").grid(row=11,column=5)

Label(master, text="5.Click on 'Run'").grid(row=13,column=5)

Label(master, text="6.Enjoy.. :)").grid(row=15,column=5)





Label(master, text="Amplitude_X").grid(row=21)

Label(master, text="Amplitude_Y").grid(row=22)

Label(master, text="Speed_X").grid(row=23)

Label(master, text="Speed_Y").grid(row=24)

Label(master, text="Run-->").grid(row=20,column=2)



Label(master, text="Amplitude").grid(row=4,column=1)

Label(master, text="  Speed  ").grid(row=4,column=2)

Label(master, text="  Phase  ").grid(row=4,column=3)









Label(master, text="Gait Name : ").grid(row=17)

sv=Entry(master)

sv.grid(row=17,column=1)

bsave=Button(master,text="  Save  ",command=save)

bsave.grid(row=17,column =2,sticky=W,pady=4)



bsave=Button(master,text="  Open  ",command=openfile)

bsave.grid(row=17,column =3,sticky=W,pady=4)



#####  a=Amplitude  s=Speed     p=phase



ax=Entry(master)

ax.grid(row=21,column=1)



ay=Entry(master)

ay.grid(row=22,column=1)



sx=Entry(master)

sx.grid(row=23,column=1)



sy=Entry(master)

sy.grid(row=24,column=1)





lb = Label(master, text="Status : Not Running..")

lb.grid(row=27,column=1)



lb1 = Label(master, text="")

lb1.grid(row=1,column=3)





b1 = Button(master, text="                 Start                 ", command=callback1)

b1.grid(row=1,column=2,sticky =W,pady=4)



bsim = Button(master, text="Simulation", command=simulation)

bsim.grid(row=2,column=2,sticky =W,pady=4)



bgait = Button(master, text="     Gait     ", command=gait)

bgait.grid(row=2,column=3,sticky =W,pady=4)





b2 = Button(master, text=" Feedback ", command=callback2)

b2.grid(row=22,column =2,sticky =W,pady=4)



b3 = Button(master, text="Sidewinding ", command=callback3)

b3.grid(row=21,column =2,sticky =W,pady=4)

b4 = Button(master, text="move forward ", command=callback4)

b4.grid(row=23,column =2,sticky =W,pady=4)

b5 = Button(master, text="rotate right", command=callback5)

b5.grid(row=24,column =2,sticky =W,pady=4)

b6 = Button(master, text="rolling", command=callback6)

b6.grid(row=21,column =3,sticky =W,pady=4)

b6 = Button(master, text="mamba", command=callback7)

b6.grid(row=22,column =3,sticky =W,pady=4)

b7 = Button(master, text="move backward", command=callback8)

b7.grid(row=23,column =3,sticky =W,pady=4)

b9 = Button(master, text="rotate left", command=callback9)

b9.grid(row=24,column =3,sticky =W,pady=4)

b9 = Button(master, text="climbing", command=callback10)

b9.grid(row=21,column =4,sticky =W,pady=4)

b8 = Button(master, text="              Exit              ", command=callback11)

b8.grid(row=17,column=5,sticky =W,pady=4)




bset=Button(master,text="  Set  ",command=sim_set)

bset.grid(row=15,column =1,sticky=W,pady=4)



brun=Button(master,text="  Run  ",command=sim_run)

brun.grid(row=15,column =2,sticky=W,pady=4)





b5=Button(master,text="  Set  ",command=set1)

b5.grid(row=25,column =1,sticky=W,pady=4)













Label(master, text="Motor_ID0").grid(row=5)

a0=Entry(master)

a0.grid(row=5,column=1)

s0=Entry(master)

s0.grid(row=5,column=2)

p0=Entry(master)

p0.grid(row=5,column=3)







Label(master, text="Motor_ID1").grid(row=6)

a1=Entry(master)

a1.grid(row=6,column=1)

s1=Entry(master)

s1.grid(row=6,column=2)

p1=Entry(master)

p1.grid(row=6,column=3)





Label(master, text="Motor_ID2").grid(row=7)

a2=Entry(master)

a2.grid(row=7,column=1)

s2=Entry(master)

s2.grid(row=7,column=2)

p2=Entry(master)

p2.grid(row=7,column=3)





Label(master, text="Motor_ID3").grid(row=8)

a3=Entry(master)

a3.grid(row=8,column=1)

s3=Entry(master)

s3.grid(row=8,column=2)

p3=Entry(master)

p3.grid(row=8,column=3)





Label(master, text="Motor_ID4").grid(row=9)

a4=Entry(master)

a4.grid(row=9,column=1)

s4=Entry(master)

s4.grid(row=9,column=2)

p4=Entry(master)

p4.grid(row=9,column=3)





Label(master, text="Motor_ID5").grid(row=10)

a5=Entry(master)

a5.grid(row=10,column=1)

s5=Entry(master)

s5.grid(row=10,column=2)

p5=Entry(master)

p5.grid(row=10,column=3)





Label(master, text="Motor_ID6").grid(row=11)

a6=Entry(master)

a6.grid(row=11,column=1)

s6=Entry(master)

s6.grid(row=11,column=2)

p6=Entry(master)

p6.grid(row=11,column=3)





Label(master, text="Motor_ID7").grid(row=12)

a7=Entry(master)

a7.grid(row=12,column=1)

s7=Entry(master)

s7.grid(row=12,column=2)

p7=Entry(master)

p7.grid(row=12,column=3)





Label(master, text="Motor_ID8").grid(row=13)

a8=Entry(master)

a8.grid(row=13,column=1)

s8=Entry(master)

s8.grid(row=13,column=2)

p8=Entry(master)

p8.grid(row=13,column=3)





Label(master, text="Motor_ID9").grid(row=14)

a9=Entry(master)

a9.grid(row=14,column=1)

s9=Entry(master)

s9.grid(row=14,column=2)

p9=Entry(master)

p9.grid(row=14,column=3)

























master.mainloop()



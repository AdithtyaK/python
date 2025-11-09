import tkinter as tk
W,H,G,S=400,400,20,40
root=tk.Tk();c=tk.Canvas(root,width=W,height=H,bg="black");c.pack()
x,y,d,run,mouth,score=100,100,"Right",False,1,0
dots,txt=[],None

def draw_p():
    c.delete("p");s={"Right":30,"Left":210,"Up":120,"Down":300}[d]
    c.create_arc(x,y,x+G,y+G,start=s,extent=300 if mouth else 360,fill="yellow",outline="",tags="p")

def move():
    global x,y,mouth,score
    if not run:return
    step=8
    if d=="Right":x+=step
    if d=="Left":x-=step
    if d=="Up":y-=step
    if d=="Down":y+=step
    x%=W;y%=H;mouth^=1;draw_p()
    pb=c.bbox("p")
    for dot in dots[:]:
        db=c.bbox(dot)
        if pb and pb[0]<db[2] and pb[2]>db[0] and pb[1]<db[3] and pb[3]>db[1]:
            c.delete(dot);dots.remove(dot);score+=10;c.itemconfig(txt,text=f"Score:{score}")
    if not dots:over();return
    root.after(S,move)

def key(e):
    global d
    if e.keysym in["Up","Down","Left","Right"]:d=e.keysym
    if e.keysym=="space":start()
    if e.keysym=="Return":home()

def start():
    global run,x,y,score,txt,dots
    c.delete("all");run=True;x=y=100;score=0;dots=[]
    for i in range(2,W//G-2):
        for j in range(2,H//G-2):
            if(i+j)%3==0:dots.append(c.create_oval(i*G+7,j*G+7,i*G+13,j*G+13,fill="white"))
    txt=c.create_text(5,5,text="Score:0",fill="white",anchor="nw",font=("Arial",12))
    draw_p();move()

def over():
    global run;run=False;c.delete("all")
    c.create_text(W/2,H/2-20,text="GAME OVER",fill="red",font=("Arial",20,"bold"))
    c.create_text(W/2,H/2+10,text=f"Final Score:{score}",fill="white")
    c.create_text(W/2,H/2+40,text="Press ENTER",fill="gray")

def home():
    c.delete("all")
    c.create_text(W/2,H/2-30,text="MINI PAC-MAN",fill="yellow",font=("Arial",20,"bold"))
    c.create_text(W/2,H/2+10,text="Press SPACE to start",fill="gray")

root.bind("<Key>",key);home();root.mainloop()

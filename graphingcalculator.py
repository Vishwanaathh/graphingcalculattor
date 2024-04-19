import tkinter as tk
import tkinter.font as f
import matplotlib.pyplot as plt
import numpy as np

            
def go():
    strr=ent.get()
    aa=[]
    n1=np.arange(0,100)
    
    for k in range(0,100):
        s=""
        for j in strr:
            if(j=="x"):
                s+=str(k)
            else:
                s+=str(j)
        
        result=eval(s)
        aa.append(result)
    n2=np.array(aa)
    plt.plot(n1,n2)
    plt.show()
        
        
            
    
        

root=tk.Tk()
root.configure(bg="blue")
root.title("graphbot")
custom_font = f.Font(family="monospace", size=20)

lab=tk.Label(text="Graphing Calculator",width=1000,height=5,bg="black",fg="white",font=custom_font)
lab.pack()
ent=tk.Entry(text="Enter Function here",width=50)
ent.pack()
but=tk.Button(text="plot",command=lambda:go(),width=30,bg="black",fg="white")
but.pack()
text="""
1)use + for addition ,- for subtraction
2)* for multiplication,/ for division
3)** for exponentiation
4)Have fun ;)
"""
text_widget = tk.Text(root, height=10, width=50,bg="blue",fg="white")
text_widget.insert(tk.END,text)
text_widget.config(state=tk.DISABLED)  # Disable editing

text_widget.pack()



root.mainloop()

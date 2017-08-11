import urllib2 as u2
from bs4 import BeautifulSoup as bs
from Tkinter import *
root=Tk()
ss=Scrollbar(root)
tt=Text(root,height=15,width=50)
ss.pack(side=RIGHT,fill=Y)
ss.config(command=tt.yview)
tt.config(yscrollcommand=ss.set)
pr="searching for upcoming contests..\n"
tt.insert(END,pr)
url="https://www.codechef.com/contests\n"
req=u2.urlopen(url)
soup=bs(req,'html.parser')
li=soup.find_all('h3')
s=li[1]
s2=s.next_sibling.next_sibling
li2=s2.find_all('td')
si=len(li2)/4
pr="you have "+str(si)+" upcoming contests...\n"
tt.insert(END,pr)
pr="listing them..\n"
tt.insert(END,pr)
pr1=['-' for ha in range(0,24)]
pr1='-'.join(pr1)
pr1=pr1+"\n"
pr1=pr1+"\n"
tt.insert(END,pr1)
i=0
for it in li2:
    if i%4==0:
        pr=str((i/4)+1)+'\n'
        tt.insert(END,pr)
        pr="code:- "+str(it.get_text())+'\n'
        tt.insert(END,pr)
    elif i%4==1:
        pr="name:- "+str(it.get_text())+'\n'
        tt.insert(END,pr)
    elif i%4==2:
        pr="start date time:- "+str(it.get_text())+'\n'
        tt.insert(END,pr)
    elif i%4==3:
        pr="end date time:- "+str(it.get_text())+'\n'
        tt.insert(END,pr)
        tt.insert(END,pr1)
    i=i+1
s=li[0]
s2=s.next_sibling.next_sibling
li2=s2.find_all('td')
si=len(li2)/4
pr="you have "+str(si)+" current contests...\n"
tt.insert(END,pr)
pr="listing them..\n"
tt.insert(END,pr)
tt.insert(END,pr1)
i=0
for it in li2:
    if i%4==0:
        pr=str((i/4)+1)+'\n'
        tt.insert(END,pr)
        pr="code:- "+str(it.get_text())+'\n'
        tt.insert(END,pr)
    elif i%4==1:
        pr="name:- "+str(it.get_text())+'\n'
        tt.insert(END,pr)
    elif i%4==2:
        pr="start date time:- "+str(it.get_text())+'\n'
        tt.insert(END,pr)
    elif i%4==3:
        pr="end date time:- "+str(it.get_text())+'\n'
        tt.insert(END,pr)
        tt.insert(END,pr1)
    i=i+1
tt.pack(fill=Y)
button=Button(root,text="ok!!I will do it",width="20",command=root.destroy)
button.pack(side="bottom")
root.mainloop()
sys.exit()

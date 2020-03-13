user=input("user ")
passw=input("password ")
from webbot import Browser
web=Browser()
link="https://lz95.instructure.com/login/canvas"
id="pseudonym_session_password"
web.go_to(link)
web.type(user)
web.click(id=id)
web.type(passw)
web.press(web.Key.ENTER)
sauce=web.get_page_source()
print(sauce.count("Course card color region"))
l=sauce.split("Course card color region")
n=sauce.count("Course card color region")
links=[]
for a in range(n):
 links.append(l[a+1].split('href="')[1].split('"')[0])


s="https://lz95.instructure.com/"
print(links)
for link in links:
 site=s+link
 web.go_to(site)


web.quit()
import time
print("finished")
time.sleep(1)
exit()
#導入urllib.request
import urllib.request
#目標url
url  = "https://nfulist.herokuapp.com/"
semester= 1091courseno=0776
#設cp1a為空括弧
cp1a = []
#打開url，並用.rstrip取消/n
for line in urllib.request.urlopen(url):
    cp1a.append(int(line.decode('utf-8').rstrip()))
#列出cp1a內容
print(cp1a)
#列出共幾筆
print("共" + str(len(cp1a)) + "筆")
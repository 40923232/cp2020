import urllib.request
url = "https://nfulist.herokuapp.com/?semester=1091&courseno=0776"
cp1a = []
for line in urllib.request.urlopen(url):
    cp1a.append(int(line.decode('utf-8').rstrip()))
print(cp1a)
print("共" + str(len(cp1a)) + "筆")
def site(num):
    print("https://github.com/" + str(num) + "/cp2020")
for num in cp1a:
    site(num)
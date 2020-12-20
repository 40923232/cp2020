import urllib.request
#導入urllib.request
target_url = "https://nfulist.herokuapp.com/?semester=1091&courseno=0776"
#設target_url = "網址"
cp1b = []
#設cp1b=數列
for line in urllib.request.urlopen(target_url):
#重複打開target_url的迴圈定義line
    cp1b.append(int(line.decode('utf-8').rstrip()))
    #把line重新編碼加進cp1b(數列)   註:rstrip()刪除字尾符號
print(cp1b)
#印出cp1b
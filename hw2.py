#git作業11
#git branch2

#判斷是否為閏年
def leapyear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        leap=1
    else:
        leap=0
    return leap

year=int(input("輸入年份:")) #輸入年份
month=int(input("輸入月份:")) #輸入月份

#計算全部有幾天
sumday=0
for i in range(1900,year,1):
    if leapyear(year)==1: #是閏年就加366
        sumday+=366
    else: #不是閏年就加365
        sumday+=365

for j in range(1,month,1):
    if j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12: #是大月就加31
        sumday+=31
    elif j==2:
        if leapyear(year)==1: #閏年2月加29
            sumday+=29
        else: #不是閏年2月加28
            sumday+=28
    else: #是小月就加30
        sumday+=30

week=(sumday+1)%7+1 #算出當月1號是禮拜幾
#定義每個月有幾天
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12: #大月有31天
    day=31
elif month==2:
    if leapyear(year)==1: #閏年2月有29天
        day=29
    else: #不是閏年2月有28天
        day=28
else: #小月有30天
    day=30

#印出萬年曆
print("日\t一\t二\t三\t四\t五\t六")
count=0 #計算是否需要換行
space=0 #計算需要幾個空格
#印出1號前的空格
while space<=week: 
    space+=1
    count+=1
    print("\t",end="")
    if count%7==0:
        print("\n",end="")

#印出當月的月曆
days=1 #計算印到幾號
while days<=day:
    print(days,"\t",end="")
    days+=1
    count+=1
    if count %7 ==0:
        print("\n")
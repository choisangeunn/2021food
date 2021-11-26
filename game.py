tsand=0
hsand=0
ssand=0
tuna=0
cheese=0
eggmayo=0
abocado=0
fries=0
cstick=0
cnugget=0
count1=0
count2=0
count3=0
count4=0
count5=1
count6=1
count7=1
count8=0
count9=0
count10=0
check=True

while check:
     print("샌드위치 류")
     print("1.터키샌드위치 3500원")
     print("2.햄샌드위치 3000원")
     print("3.새우샌드위치 4000원")
     print("4.참치샌드위치 3000원")
     select=int(input("메뉴를 선택하세요:"))     

     if select == 1:
             count1=int(input("수량을 입력하세요:"))                 
             tsand=tsand+count1 * 3500
     elif select == 2:
             count2=int(input("수량을 입력하세요:"))    
             hsand=hsand+count2 * 3000
     
     elif select == 3:
             count3=int(input("수량을 입력하세요:"))        
             ssand=ssand+count3 * 4000
         
     elif select == 4:
              count4=int(input("수량을 입력하세요:"))    
              tuna=tuna+count4 * 3000
     else:
         print("잘못 입력하셨습니다")
         break
         
     print("추가메뉴 ")
     print("5.치즈 1000원")
     print("6.아보카도 1200원")
     print("7.에그마요 1500원")
     select=int(input("추가메뉴를 선택하세요:"))

     if select == 5:
              count5=1    
              cheese=cheese+count5 * 1000
     elif select == 6:
              count6=1   
              abocado=abocado+count6 * 1200
     elif select == 7:
              count7=1
              eggmayo=eggmayo+count7 * 1500
     else:
         print("잘못 입력하셨습니다")
         break
         
     print("사이드메뉴 류")
     print("8.감자튀김 1500원")
     print("9.치즈스틱 개당 1000원")
     print("10.치킨너겟 5조각 2000원")    
     select=int(input("사이드메뉴를 선택하세요:"))
     
     if select == 8:
              count8=int(input("수량을 입력하세요:"))    
              fries=fries+count8 * 1500
     elif select == 9:
              count9=int(input("수량을 입력하세요:"))    
              cstick=cstick+count9 * 1000
     elif select == 10:
              count10=int(input("수량을 입력하세요:"))    
              cnugget=cnugget+count10 * 2000
     else:
         print("잘못 입력하셨습니다")
         break
         
         
     select = input("추가주문 하시겠습니까? Y/N: ")
     if select == "N":
        check= not check

     elif select == "Y":
        continue
     
print("터키샌드위치:", tsand)
print("햄샌드위치:", hsand)
print("새우샌드위치:", ssand)
print("참치샌드위치:", tuna)
print("치즈:", cheese)
print("아보카도:", abocado)
print("에그마요:", eggmayo)
print("감자튀김:", fries)
print("치즈스틱:", cstick)
print("치킨너겟:", cnugget)
print("총액:", tsand+hsand+ssand+tuna+cheese+abocado+eggmayo+fries+cstick+cnugget)


total = tsand+hsand+ssand+tuna+cheese+abocado+eggmayo+fries+cstick+cnugget

bill=[0,100,500,1000,5000,10000,50000]

for i in range (1,len(bill)):
    print(i,'.',bill[i],'원',end='   ')
print()

pay = 0
while pay < total:
    n = int(input("지불 금액을 입력하세요: "))
    if n>0 and n<len(bill):
        pay = pay + bill[n]
        print('총 지불액:',pay,'원')
    else :
        print('다시 선택하세요.')
        
change = pay - total
print('거스름돈', change,'원')
    

print("구매해주셔서 감사합니다")



def fortune_cookie(num, nolist, todaylist):
    result = "끝내기"

    for i in range(0, len(nolist)):
        if nolist[i] == num:
            result = todaylist[i]

    return result
    

coo_no = [1, 2, 3, 4, 5]
coo_today = ["할 수 있다고 믿으세요. 당신을 할 수 있습니다.",
             "노력은 배신하지 않습니다. 곧 좋은 결과가 있을 거에요.",
             "당신의 오늘을 응원합니다. 오늘 하루도 화이팅!",
             "피할 수 없다면 즐기세요.",
             "선택을 신중히 해야할 때입니다. 한번 더 생각해보세요." ]

while True:
    print("샌드위치를 구매해주신 분들께 포춘쿠키를 선물로 드리는 이벤트를 진행 중입니다.")    
    print(coo_no)
    a=int(input("포춘쿠키 번호를 선택하세요. (0은 끝내기): "))

    if a < 6:
        print("%d -> %s" %(a, fortune_cookie(a, coo_no, coo_today)))
        print("구매해주셔서 감사합니다. 좋은 하루 되세요.")
        break
    elif a == 0:
        print("구매해주셔서 감사합니다. 좋은 하루 되세요.")
        break
    else :
        print("리스트 안에 있는 번호로 골라주세요.")

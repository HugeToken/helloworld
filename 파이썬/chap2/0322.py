#2023-03-22
'''
print("오늘은 파이썬 수업입니다.")
print('hello !!')
print(type("오늘은 파이썬 수업입니다."))
print(2)
print(type(2))
print(5.5)

print("Hello " + " Python")
print("213 호" * 3)

print("Hello ", " hi "," 213")
print("hello","hello",213," ",11111)
#print("Hello " + 33)
print("Hello " , 33)'''
'''
print(1, 2, -5, 3.14, 2.71828)
print('Hi','Python')

print('23000원은','5000원 ?개','1000원 ?개')
print('5000원',23000//5000,'개')
print('1000원',(23000 % 5000) // 1000,'개')

print("3 + 8 =",3+8)


var = '3+8'
print(eval(var))
print(var)'''

'''
▪다음 수식의 결과를 써 봅시다.
▪ 1 + 62 − 3 × 52
▪ 256 × 553 − 152
▪ 162353290930 을 539253 로 나눴을 때의 나머지와 몫의
합을 구해 봅시다.
'''
'''
print(1 + 62 - 3 * 52)
print(255*553-152)
print(162353290930%539253 + 162353290930//539253)
'''
def 거스름돈 (a) :
    오만원권 = a // 50000 
    만원권 = (a - 50000*오만원권) // 10000
    만원나머지 = (a - 50000*오만원권) % 10000
    오천원권 = (a - 50000*오만원권 - 10000*만원권) // 5000
    오천원나머지 = (a - 50000*오만원권 - 10000*만원권) % 5000
    
    print("50000원 지폐는",오만원권,"장")
    print("10000원 지폐는",만원권,"장")
    print("5000원 지폐는",오천원권,"장")
    부족한돈 = a - 50000*오만원권 - 10000*만원권 - 5000*오천원권

    if (부족한돈) :
        print(부족한돈,"원이 부족합니다.")
        print("5000원을 더 내시고", 5000-부족한돈,"만큼 가져가세요.")

거스름돈(78000)
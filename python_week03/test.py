import random
print('โปรแกรมเป่งยิ้งฉุบ')
while True:
    a = random.choice(['ค้อน' , 'กรรไกร' , 'กระดาษ'])
    print(a)
    b = str(input('ระบุคำตอบ'))
    if b == a :
        print('เสมอ')
    elif a =='กรรไกร' and  b =='กระดาษ':
        print('ชนะ')
    elif a =='กรรไกร' and b =='ค้อน':
        print('ชนะ')
    elif a =='ค้อน' and b =='กระดาษ':
        print('ชนะ')
    elif a =='ค้อน' and  b =='กรรไกร':
        print('แพ้')
    elif a =='กระดาษ' and b =='กรรไกร':
        print('แพ้')
    elif a =='กระดาษ' and b =='ค้อน':
        print('แพ้')
    else :
        print('ระบุคำตอบให้ถูกต้อง')
        
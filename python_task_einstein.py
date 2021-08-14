while True:
    print("""
Qaydalar:
1. Dostunuzdan 3 rəqəmli ədəd fikirləşməsini istəyin. Elə qəbul edək ki, onun fikirləşdiyi ədəd 654 olacaq.
2. Daha sonra bu rəqəmi tərsinə (reverse) çevirməyi istəyin (654 -> 456 olacaq)
3. Kiçik olandan böyük olanı çıxın (654 - 456 = 198)
4. Fərqdən alınan yeni rəqəmi də tərsinə çevirməyi istəyin (198 -> 891 olacaq)
5. Daha sonra sonuncu iki rəqəmi toplamasını istəyin, alınan cavab 1089 olacaq (198 + 891 = 1089)
""")
    uc_reqemli_eded = str(input('3 reqemli eded daxil edin: '))
    if len(uc_reqemli_eded) == 3 and uc_reqemli_eded.isdigit():
        
        reverse = str((uc_reqemli_eded[::-1]))
        print(uc_reqemli_eded,reverse)
        reverse = int(reverse)
        uc_reqemli_eded = int(uc_reqemli_eded)
        b = (reverse - uc_reqemli_eded)
        print(b)
        b = str(b)
        c = b[::-1]
        print(c)
        c = int(c)
        b = int(b)
        print(f"sonuncu iki reqemin cemi: {c + b}")
        d = input('yes or no: ')
        if d == 'yes':
            continue
        elif d == 'no':
            break
    else:
        print('yeniden daxil edin: ')
        continue
        
        
        
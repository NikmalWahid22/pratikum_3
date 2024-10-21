A = int(input("Masukkan bilangan A: "))
B = int(input("Masukkan bilangan B: "))
C = int(input("Masukkan bilangan C: "))

if A > B:
    if A > C:
        print(f"Bilangan terbesar adalah A: {A}")
    else:
        print(f"Bilangan terbesar adalah C: {C}")
else:
    if B > C:
        print(f"Bilangan terbesar adalah B: {B}")
    else:
        print(f"Bilangan terbesar adalah C: {C}")

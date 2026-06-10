n=input('Enter Name')
no=input('Enter Roll No')
eng=int(input("enter the English Marks"))
maths=int(input("enter the Maths Makrs"))
hindi=int(input("enter the Hindi Marks"))
cs=int(input("enter the CS Marks"))
science=int(input("enter the Science Marks"))
print('\n\n\n')
Totalmarks=eng+maths+hindi+cs+science
Cgpa= Totalmarks/5
print('\n\n\n')
print(f' Name {n} \t\tRoll no {no}')
print(f'\n Math\t {maths}')
print(f'\n Hindi\t{hindi}')
print(f'\n Computer Science\t{cs}')
print(f'\n Science\t{science}')
print(f'\n english\t{eng}')
print(f'\t\t\t\t\tThe CGPA is {Cgpa}')
print('\t\t\t\t\t\n The University Of Delhi ')
if Cgpa>70:
    print('\n\t\t\t\t\t\n first Divison Passed')
elif Cgpa>60:
    print('\n\t\t\t\t\t\n Second Divison Passed')
else:
    print('\n\t\t\t\t\t\n Third Divison Passed')
print('\t\t\t\t\t\n University Of Delhi ')
print('\t\t\t\t\t\n Head Of Delhi University ')
print('\t\t\t\t\t\nSignture \n\t\t\t\t\t Alihasan')

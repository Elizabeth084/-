n=int(input('Введите количество долек по ширине\n'))
m=int(input('Введите количество долек по длине\n'))
k=int(input('Введите количество долек\n'))
s=n*m
if k<=s:
  if k==m or k==n :
    print('да')
  else:
    print('нет')
else:
    print('нет')
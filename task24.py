n = int(input('Введите количество грядок: '))
if n < 3: print('Грядок должно быть больше двух')
else:
    arr = []
    for i in range(n):
        arr.append(int(input('Введите количество ягод: ')))

    first_num = arr[0] + arr[1] + arr[n-1]
    last_num = arr[0] + arr[n-2] + arr[n-1]
    max_num = 0
    if first_num > last_num:
        max_num = first_num
    else: max_num = last_num
    for i in range(1, n-1):
        if max_num < arr[i] + arr[i-1] + arr[i+1]:
            max_num = arr[i] + arr[i-1] + arr[i+1]
    print(max_num)
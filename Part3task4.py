def min_(x):
    result = x[0]
    for i in x[1:]:
        if i<result:
            result = i
    return result
print(min_([int(input('ввод эл ')) for _ in range(int(input('кол-во эл. ')))]))
#Задание 3

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б',]


def check_gen(tutors: list, klasses: list):
    add_in = 0
    if len(klasses) < len(tutors):
        add_in = len(tutors) - len(klasses)
        for i in range(add_in):
            klasses.append('None')
    check = ((tutors[i], klasses[i],) for i in range(len(tutors)))

    return check


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))

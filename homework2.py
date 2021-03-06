# домашнее задание по Модулю #2

# создаю переменные типа 'словарь' со структурой 'account'

account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

# создаю переменные типа 'словарь' со структурой 'user'

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

# создаю список user_list

user_list = [user1, user2, user3, user4]

# запрос ввода имени ключа

key_name = input('Введите ключ (name или account):')

# преобразование имени ключа в строчные буквы

key_name = key_name.lower()

# проверка имени ключа через словарь 'user1'
# не хотел привязываться жестко к конкретному словарю, но более изящного решения не нашел

try:
    control_key_name = user1[key_name]
except KeyError:
    print('Введенный ключ не найден')
    
# вывод значений ключа для всех юзеров через операцию цикла
# хотя операции циклов мы как бы еще не проходили, но не хотелось тупо принтовать каждую строку

counter_user = 0  # определяю счетчик юзеров

while counter_user < len(user_list):
    counter_user = counter_user + 1
    print(f"значение ключа {key_name} для юзера {counter_user} = {user_list[counter_user-1].get(key_name, 'Такой ключ не существует')}")

# запрос ввода порядкового номера юзера

user_number = input('Введите порядковый номер:')

# создаю список для контроля порядкового номера юзера
# не хотел тупо вбивать [1, 2, 3, 4], ведь количество юзеров может меняться

control_list = []
i = 1  # определяю вспомогательную переменную i
while i <= len(user_list):
    control_list.append(i)
    i = i + 1

# проверка порядкового номера и вывод информации по юзеру

try:
    control_list.index(int(user_number))
    print(f"Данные по юзеру № {user_number}:")
    print(f"имя: {user_list[int(user_number)-1].get('name')}")
    print(f"возраст: {user_list[int(user_number)-1].get('age')}")
    print(f"логин: {(user_list[int(user_number)-1].get('account')).get('login')}")
    print(f"пароль: {(user_list[int(user_number)-1].get('account')).get('password')}")
except:
    print('Пользователь с указанным номером не найден')

# запрос ввода номера юзера, которого нужно перенести в конец списка

user_remove = input('Введите номер пользователя, которого нужно переместить в конец:')

# вывод списка до изменения

print('Список до изменения:')
print(user_list)

# проверка корректности номера перемещаемого юзера и вывод измененного списка

try:
    control_list.index(int(user_remove))    # для проверки использую ранее созданный список 'control_list'
    if int(user_remove) == len(user_list):
        print(f"Не обижайте юзера по имени {user_list[int(user_remove)-1].get('name')}. Этот юзер и так в конце, список не изменился.")
    else:
        element_user = user_list[int(user_remove)-1]    # определяю элемент с перемещаемым юзером
        user_list.remove(element_user)                  # удаляю перемещаемого юзера из списка
        user_list.append(element_user)                  # добавляю перемещаемого пользователя в конец списка
        print(f"Пользователь с именем {element_user.get('name')} перемещен в конец")
        print('Список после изменения:')
        print(user_list)
except:
    print('Пользователь с указанным номером не найден, список не изменился')

sum_age = 0    # определяю переменную суммарного возраста юзеров  
i = 1          # снова использую вспомогательную переменную i
while i <= len(user_list):
    sum_age = sum_age + user_list[i-1].get('age')
    i = i + 1

# определяю и вывожу значение среднего возраста
print(f'Средний возраст юзеров: {sum_age/len(user_list)}')

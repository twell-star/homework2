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

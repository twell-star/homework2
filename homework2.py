# домашнее задание по Модулю №2

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


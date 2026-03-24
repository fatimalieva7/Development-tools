import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8')
def get_user():
    logging.info('Запущена функция запроса возраста')
    age = int(input('Введите ваш возраст: '))
    age=int(age)
    print(f'Ваш возраст: {age}')
    logging.error('ОШИБКА! Возраст введен неверно')
    print('Пожалуйста введите только числа')
if __name__ == '__main__':
    logging.info('Запущена программа')
    get_user()
    logging.info('Программа завершена')
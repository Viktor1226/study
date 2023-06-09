"""Игра угадай число
    Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """    
    count=0
    start=1
    end=100
    predict_number = (start+end)/2
    print(predict_number)
    # while True:
    #     count+=1
        
    #     #predict_number = np.random.randint(1,101) # поменять на мою логику
    #     if predict_number > number:
    #         pass
    #     elif predict_number < number:
    #         pass
    #     else:
    #         break #конец игры. выход из цикла
    # return count

def score_game(random_predict) -> int:
    """За какое среднее количество попыток в 1000 подходов угадывает функция
    Args:
        random_predict (_type_): Функция угадывания
    Returns:
        int: среднее количество попыток
    """    
    count_ls =[]
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1,101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__ == '__main__':
    #RUN
    score_game(random_predict)

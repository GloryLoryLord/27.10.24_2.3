my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index < len(my_list):
    if my_list[index] < 0:
        break
    if my_list[index] == 0:
        index += 1
        continue
    print(my_list[index])
    index += 1

# дополнительно придумал задачу в рамках геймдизайна
# условие задачи - это выявление положительного, нулевого и отрицательного значения очков, которые игрок получил за прохождение каждого из уровней
# можно было подумать побольше, и написать нескольких игроков, сравнив проходимость уровней, аналитически вылавливая проблемные уровни, на основе анализа данных провальных уровней

# player_scores = [10, 15, 0, 5, -5, 20, 55, 2, 0, -1]
#
# levels = 1
# index = 0
#
# positive = 'состояние очков положительное ≽^•⩊ •^≼'
# negative = 'состояние очков отрицательное ₍=୪ Ⱉ ୪=₎'
# zero = 'очки не были получены         (,,>_<,)'
#
# while index < len(player_scores):
#     if player_scores[index] > 0:
#         print('уровень', levels, positive)
# 
#     elif player_scores[index] == 0:
#         print('уровень', levels, zero)
#
#     else:
#         print('уровень',levels, negative)
#     index += 1
#     levels += 1
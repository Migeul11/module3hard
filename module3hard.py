# должно быть подсчитано:
#
#     Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#     Все строки (не важно, являются они ключами или значениям или ещё чем-то)
def calculate_structure_sum(some_value):

    sum = 0
    if isinstance(some_value, int):
        return some_value
    elif isinstance(some_value, str):
        return len(some_value)
    elif isinstance(some_value, tuple) or isinstance(some_value, list) or isinstance(some_value, set):
        for item in some_value:
            sum += calculate_structure_sum(item)
    elif isinstance(some_value, dict):
        for key, value in some_value.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)

    return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

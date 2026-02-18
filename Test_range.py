def test_range(num_1, num_2, num_3):
    if num_2 < num_1 < num_3:
        print()
    else:
        print(f'Число {num_1} не попадает в диапазон между {num_2} и {num_3}')

test_range(3, 8, 10)
import types


def flat_generator(list_of_lists):
    counter = 0
    while counter < len(list_of_lists):
        inside_counter = 0
        while inside_counter < len(list_of_lists[counter]):
            yield list_of_lists[counter][inside_counter]
            inside_counter += 1
        inside_counter = 0
        counter += 1

def inside_list(list):
    max_count = len(list)
    counter = 0
    while counter != max_count:
        yield list[counter]
        counter += 1

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None], print('YES')

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType), print('YES')


if __name__ == '__main__':
    test_2()
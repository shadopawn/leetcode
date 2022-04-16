# leetcode link https://leetcode.com/problems/implement-queue-using-stacks/

example_input = [(1, 42), (2, -1), (1, 14), (3, -1), (1, 28),
                 (3, -1), (1, 60), (1, 70), (2, -1), (2, -1), (3, -1)]

queue = []


def enqueue(value):
    queue.append(value)


def dequeue(_):
    return queue.pop()


def peek(_):
    print(queue[-1])


function_map = {1: enqueue, 2: dequeue, 3: peek}


def process_input(input_list):
    for function_key, value in input_list:
        current_function = function_map[function_key]
        current_function(value)


process_input(example_input)

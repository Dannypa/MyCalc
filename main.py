import logging
import UFraction
from collections import deque


logging.basicConfig(level=logging.ERROR, filename='logs.txt', filemode='a')
signs = {'+', '-', '*', '/', '^'}


def parse(task: str) -> str:
    task = task.replace(' ', '')
    task = list(task)
    cur_index = 0
    parenthesis_count = 0
    last_char = ''
    while cur_index < len(task):
        # check parenthesis
        if task[cur_index] == '(':
            parenthesis_count += 1
        if task[cur_index] == ')':
            if parenthesis_count <= 0:
                raise ArithmeticError("Invalid parenthesis sequence")
            parenthesis_count -= 1

        # check signs
        if task[cur_index] in signs and last_char in signs:
            if task[cur_index] in {'*', '/', '^'}:
                raise ArithmeticError("Invalid signs sequence")
            elif task[cur_index] == '+':
                if last_char in {'-', '+'}:
                    task.pop(cur_index)
                    cur_index -= 1
                else:
                    raise ArithmeticError("Invalid signs sequence")
            elif task[cur_index] == '-':
                if last_char == '-':
                    task[cur_index - 1] = '+'
                    task.pop(cur_index)
                    cur_index -= 1

        if task[cur_index] in signs and last_char == '':
            if task[cur_index] == '+':
                task.pop(cur_index)
            elif task[cur_index] in {'*', '/'}:
                raise ArithmeticError("Invalid signs sequence")
        if cur_index >= len(task):
            raise ArithmeticError("Invalid signs sequence")
        last_char = task[cur_index]
        cur_index += 1
    if last_char in signs:
        raise ArithmeticError("Invalid signs sequence")
    if parenthesis_count > 0:
        raise ArithmeticError("Invalid parenthesis sequence")
    return ''.join(task).lstrip('(').rstrip(')')


def evaluate(task: [str]) -> UFraction:
    # TODO: parse in main
    parenthesis = 0
    tmp = []
    appending = False
    cur_index = 0

    return 0


def main():
    while True:
        task = input()
        print(evaluate(list(parse(task))))


main()

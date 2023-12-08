def count_symbols(line_with_spaces):
    return len(line_with_spaces.replace(' ', '').replace('\n', ''))


with open('text.txt', 'r') as file:
    line_number = 1
    for line in file:
        print(f'line {line_number}: {len(line.split())} words, {count_symbols(line)} symbols')
        line_number += 1

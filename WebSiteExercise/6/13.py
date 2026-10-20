def next_line(line: list[int]) -> list[int]:
    if not line:
        return [1]

    new_line = []
    current_number = line[0]
    number_of_number = 1
    for i in range(1, len(line)):
        if line[i] == current_number:
            number_of_number += 1
        else:
            new_line.append(number_of_number)
            new_line.append(current_number)
            number_of_number = 1
            current_number = line[i]

    new_line.append(number_of_number)
    new_line.append(line[-1])

    return new_line
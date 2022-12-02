class Elf:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
        self.total_calories = sum(calories)

    def pprint(self):
        return("name: {}, calories: {}, total_calories: {}".format(self.name, str(self.calories), self.total_calories))

    def __lt__(self, other):
        return self.total_calories < other.total_calories

    
def codeify_input(input_file_name):
    input = []
    input_file = open(input_file_name, 'r')
    input = input_file.read().splitlines()
    input_file.close()
    return input


def parse_input(codeified_input):
    parsed_input = []
    current_elf = []
    elf_count = 0
    for l in codeified_input:
        if l == '':
            elf = Elf(elf_count, calories=current_elf)
            parsed_input.append(elf)
            current_elf = []
            elf_count+=1
        else:
            current_elf.append(int(l))
    
    print(parsed_input)
    return parsed_input


if __name__ == "__main__":
    input = codeify_input("./aoc_day1_input1.txt")
    elves = parse_input(input)

    print("part_1_answer = {}".format(sorted(elves, reverse=True)[0].pprint()))
    print("part_2_answer = {}".format(sorted(elves, reverse=True)[0].total_calories + sorted(elves, reverse=True)[1].total_calories + sorted(elves, reverse=True)[2].total_calories))
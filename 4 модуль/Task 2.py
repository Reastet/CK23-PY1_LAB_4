# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as inp_file:  # TODO считать содержимое csv файла
        reader = csv.DictReader(inp_file)
        inp_data = []
        for i in reader:
            inp_data.append(i)


    with open(OUTPUT_FILENAME, "w") as out_f: # TODO Сериализовать в файл с отступами равными 4
        json.dump(inp_data, out_f, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

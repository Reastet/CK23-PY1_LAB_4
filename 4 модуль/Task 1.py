# TODO решите задачу
import json


INPUT_FILE = "input.json"
def task() -> float:
    with open(INPUT_FILE, "r") as inp_file:
        list_of_inp_dicts = json.load(inp_file)
        total_sum = sum(i["score"] * i["weight"] for i in list_of_inp_dicts)
    return round(total_sum, 3)


print(task())

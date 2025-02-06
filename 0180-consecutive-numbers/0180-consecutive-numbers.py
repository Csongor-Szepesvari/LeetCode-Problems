import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    consecutive_nums = pd.DataFrame({"ConsecutiveNums":[]})
    already_appears = set()
    appears_thrice = logs["num"]
    prev = None
    counter = 1
    for obj in appears_thrice:
        if obj == prev:
            counter += 1
        else:
            counter = 1
        if counter == 3:
            if not obj in already_appears:
                consecutive_nums.loc[len(consecutive_nums)] = [obj]
                already_appears.add(obj)
        prev = obj


    #print(appears_thrice)

    return consecutive_nums
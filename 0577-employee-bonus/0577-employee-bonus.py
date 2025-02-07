import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # write the name and bonus of each employee, where bonus < 1000
    matching_rows = employee.merge(bonus, on='empId', how='left')
    #print(matching_rows)
    print(matching_rows[["name", "bonus"]])
    
    output = matching_rows[(matching_rows["bonus"].isna()) | (matching_rows["bonus"] < 1000)]
    #print(output)
    return output[["name", "bonus"]]
   
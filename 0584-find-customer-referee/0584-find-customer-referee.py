import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # find the names of the customers that are not referred by the customer with id = 2

    # input table has columns id, name, and referee_id

    # we're going to filter such that id != 2
    return customer[(customer["referee_id"] != 2) | (customer["referee_id"].isna())][["name"]]
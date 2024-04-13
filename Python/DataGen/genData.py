from multiprocessing import Pool
from multiprocessing import cpu_count
import pandas as pd
from dataframe import create_dataframe

if __name__ == "__main__":
    num_cores = cpu_count() - 1
    with Pool() as pool:
        data = pd.concat(pool.map(create_dataframe, range(num_cores)))
    data_dict = data.to_dict('records')

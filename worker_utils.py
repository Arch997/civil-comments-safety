# worker_utils.py
import pandas as pd

def process_batch(batch_data):
    """
    Worker function to convert a list of dicts to a DataFrame.
    This must live in a separate file for Windows multiprocessing to work.
    """
    return pd.DataFrame(batch_data)

def process_batch_csv(file: str, batch_data: int = 50000):
    """
    Worker function to convert a list of dicts to a DataFrame.
    This must live in a separate file for Windows multiprocessing to work.
    """
    return pd.read_csv(file, index=False, chunksize=batch_data)
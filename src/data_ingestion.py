import pandas as pd
import os

def data_ingestion():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, 'data', 'train.csv')
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found at: {file_path}")
        raise
    except Exception as e:
        print(f"Error during data ingestion: {e}")
        raise

if __name__ == "__main__":
    df = data_ingestion()
    print(f"✅ Data loaded successfully. Shape: {df.shape}")

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def read_excel_to_parquet(input_excel_file, output_parquet_file):
    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(input_excel_file)

    # Convert DataFrame to PyArrow Table
    table = pa.Table.from_pandas(df)

    # Write PyArrow Table to Parquet file
    pq.write_table(table, output_parquet_file)

def check_parquet_columns(parquet_file):
    # Read Parquet file into a PyArrow Table
    table = pq.read_table(parquet_file)

    # Extract column names from the PyArrow Table
    parquet_columns = table.column_names

    # Print the column names
    print("Parquet file columns:")
    print(parquet_columns)

    # Perform additional checks or validations as needed

if __name__ == "__main__":
    # Replace 'input_excel_file.xlsx' with the path to your Excel file
    input_excel_file = '/home/neosoft/Downloads/project/main_01.xlsx'
    
    # Replace 'output_parquet_file.parquet' with the desired output Parquet file path
    output_parquet_file = '/home/neosoft/Downloads/project/op.parquet'

    # Read Excel file and write Parquet file
    read_excel_to_parquet(input_excel_file, output_parquet_file)

    # Check Parquet file columns
    check_parquet_columns(output_parquet_file)

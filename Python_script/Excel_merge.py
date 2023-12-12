import pandas as pd
import numpy as np
import glob

df = pd.read_excel('/home/neosoft/Downloads/project/Excel_1.xlsx')
status = pd.read_excel('/home/neosoft/Downloads/project/Excel_2.xlsx')
df2 = pd.read_excel('/home/neosoft/Downloads/project/Excel_3.xlsx')
print(df2.columns)

# Split Name column into fname and lname
df2[['fname', 'lname']] = df2['name'].str.split(' ', expand=True)


print(df2[['fname', 'lname']])
df3 = df2.drop('name', axis=1)


all_data_st = pd.merge(df, status, how='outer')
#all_data_st.to_excel('/home/neosoft/Downloads/project/1&2.xlsx',header=True)
# print(all_data_st)
#output_columns = ['id', 'fname', 'lname', 'date_of_birth', 'email', 'gender', 'address', 'age', 'contact', 'city', 'country']
all_merge = pd.merge(all_data_st, df3, how='outer')
print(all_merge)
all_merge.to_excel('/home/neosoft/Downloads/project/main.xlsx', index=False, header=True)

#### Read the Excel file into a DataFrame
file_path = '/home/neosoft/Downloads/project/main.xlsx'
df0 = pd.read_excel(file_path)

##### Convert the column to string
column_name = 'contact'
df0[column_name] = df0[column_name].astype(str)

# Format the numbers as Indian contact numbers
def format_indian_contact_number(number):
    # Assuming the original numbers are 10 digits
    if len(number) == 12:
        return ('+91' + number)
    else:
        # Handle cases where the number might have a different length
        # You can customize this part based on your specific requirements
        return number

df0[column_name] = df0[column_name].apply(format_indian_contact_number)

# Write the DataFrame back to the Excel file
df0.to_excel('/home/neosoft/Downloads/project/main_01.xlsx', index=False)

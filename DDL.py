import pandas as pd

file_paths = ["data/tidied_population_estimates.csv"]

# Function to generate INSERT statements for the Industry table
def generate_insert_industry_statements(data):
    insert_statements = []
    for row in data:
        insert_statement = f"INSERT INTO Industry (IndustryID, Name, GoodType) VALUES ({row['IndustryID']}, '{row['Name']}', '{row['GoodType']}')"
        insert_statements.append(insert_statement)
    return insert_statements

# Function to generate INSERT statements for the Employees table
def generate_insert_employees_statements(data):
    insert_statements = []
    for row in data:
        insert_statement = f"INSERT INTO Employees (IndustryID, Year, Number) VALUES ({row['IndustryID']}, {row['Year']}, {row['Number']})"
        insert_statements.append(insert_statement)
    return insert_statements

# Function to generate INSERT statements for the Province table
def generate_insert_province_statements(data):
    insert_statements = []
    for index, row in data.iterrows():        
        insert_statement = f"INSERT INTO Province (Name, Year, Population) VALUES ({row[0]},{row[1]}, {row[2]})"
        insert_statements.append(insert_statement)
    return insert_statements

# Function to generate INSERT statements for the FuelEmissions table
def generate_insert_fuel_emissions_statements(data):
    insert_statements = []
    for row in data:
        insert_statement = f"INSERT INTO FuelEmissions (IndustryID, Year, Amount) VALUES ({row['IndustryID']}, {row['Year']}, {row['Amount']})"
        insert_statements.append(insert_statement)
    return insert_statements

# Function to generate INSERT statements for the Household table
def generate_insert_household_statements(data):
    insert_statements = []
    for row in data:
        insert_statement = f"INSERT INTO Household (Province, Emission) VALUES ('{row['Province']}', {row['Emission']})"
        insert_statements.append(insert_statement)
    return insert_statements

# Example usage
if __name__ == "__main__":

    # Loop through each file and generate INSERT statements
    for file_path in file_paths:
        data = pd.read_csv(file_path,header=None,skiprows=1)
        table_name = "province"  # Extract table name from file path
        insert_statements = None
        
        # Generate INSERT statements based on table name
        if table_name == 'industry':
            insert_statements = generate_insert_industry_statements(data)
        elif table_name == 'employees':
            insert_statements = generate_insert_employees_statements(data)
        elif table_name == 'province':
            insert_statements = generate_insert_province_statements(data)
        elif table_name == 'fuel_emissions':
            insert_statements = generate_insert_fuel_emissions_statements(data)
        elif table_name == 'household':
            insert_statements = generate_insert_household_statements(data)
        print(insert_statements)
        # Execute the INSERT statements using your database connection
        # db_connection = your_database_connection_function()
        # execute_insert_statements(insert_statements, db_connection)



    


import pandas as pd

file_paths = ["data/tidied_population_estimates.csv","data/tidied_industry_mapping.csv","data/tidied_employment_estimates.csv","data/tidied_emissions_with_key.csv"]
tables = ['province', 'maping', 'employees', 'fuel_emissions']
# Function to generate INSERT statements for the Industry table


def generate_insert_maping_statements(data):
    insert_statements = []
    for index, row in data.iterrows():
        insert_statement = f"insert into IndustryMapping  values ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', {row[4]});"
        insert_statements.append(insert_statement)
    return insert_statements

# Function to generate INSERT statements for the Employees table
def generate_insert_employees_statements(data):
    insert_statements = []
    #data = pd.melt(data, id_vars=['naics_industry','province'], var_name='Year', value_name='Value')
    for index, row in data.iterrows():
        insert_statement = f"insert into Industry values ('{row[0]}','{row[1]}', {row[2]}, {row[3]});"
        insert_statements.append(insert_statement)
    return insert_statements

# Function to generate INSERT statements for the Province table
def generate_insert_province_statements(data):
    insert_statements = []
    for index, row in data.iterrows():        
        insert_statement = f"insert into Province values ('{row[0]}',{row[1]}, {row[2]});"
        insert_statements.append(insert_statement)
    return insert_statements

# Function to generate INSERT statements for the FuelEmissions table
def generate_insert_fuel_emissions_statements(data):
    insert_statements = []
    for index, row in data.iterrows():
        insert_statement = f"insert into Emissions values ('{row[0]}', '{row[1]}', '{row[2]}', {row[3]}, {row[4]}, '{row[5]}');"
        insert_statements.append(insert_statement)
    return insert_statements

inserts = []
# Example usage
if __name__ == "__main__":

    # Loop through each file and generate INSERT statements
    for i in range(len(file_paths)):
        file_path = file_paths[i]
        table_name = tables[i]
        data = pd.read_csv(file_path,header=None,skiprows=1)
        # Extract table name from file path
        insert_statements = None
        
        # Generate INSERT statements based on table name

        if table_name == 'employees':
            data = pd.read_csv(file_path)
            insert_statements = generate_insert_employees_statements(data)
            inserts.append(insert_statements)
        elif table_name == 'maping':
            insert_statements = generate_insert_maping_statements(data)
            inserts.append(insert_statements)
        elif table_name == 'province':
            insert_statements = generate_insert_province_statements(data)
            inserts.append(insert_statements)
        elif table_name == 'fuel_emissions':
            insert_statements = generate_insert_fuel_emissions_statements(data)
            inserts.append(insert_statements)

       # print(insert_statements)
        # Execute the INSERT statements using your database connection
        # db_connection = your_database_connection_function()
        # execute_insert_statements(insert_statements, db_connection)
    with open('tables.txt', 'r') as file:
        existing_content = file.read()

    
    # Save the updated content as project.sql
    with open('project.sql', 'w') as file:

        file.write(existing_content+ '\n')
        for statement in inserts:
            for line in statement:
                file.write(line+'\n')
        




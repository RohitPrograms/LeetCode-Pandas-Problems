from typing import List
import pandas as pd


# Problem 1: Create a DataFrame from List
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
    first_row = [sub_array[0] for sub_array in student_data]
    second_row = [sub_array[1] for sub_array in student_data]

    return pd.DataFrame({'student_id':first_row, 'age':second_row})


# Problem 2: Get the Size of a DataFrame
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    
    return [len(players.index), len(players.columns)]


# Problem 3: Display the First Three Rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    
    return employees.head(3)


# Problem 4: Select Data
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    
    return students[students['student_id'] == 101][['name', 'age']]


# Problem 5: Create a New Column
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['bonus'] = employees['salary'] * 2
    return employees


# Problem 6: Drop Duplicate Rows
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    
    return customers.drop_duplicates(subset = ['email'])


# Problem 7: Drop Missing Data
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    
    return students.dropna(subset = ['name'])


# Problem 8: Modify Columns
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees['salary'] *= 2
    return employees


# Problem 9: Rename Columns
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    
    return students.rename(columns = {'id':'student_id',
                                    'first':'first_name',
                                    'last':'last_name',
                                    'age':'age_in_years'})


# Problem 10: Change Data Type
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    
    students['grade'] = students['grade'].astype(int)
    return students


# Problem 11: Fill Missing Data
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    
    products['quantity'] = products['quantity'].fillna(0)
    return products


# Problem 12: Reshape Data: Concatenate
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    
    return pd.concat([df1, df2])


# Problem 13: Reshape Data: Pivot
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    
    return weather.pivot(index = 'month', columns = 'city', values = 'temperature')


# Problem 14: Reshape Data: Melt
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    
    return pd.melt(frame = report, 
                id_vars = ['product'], 
                value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], 
                var_name = 'quarter',
                value_name = 'sales')


# Problem 15: Method Chaining
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    
    return animals[animals['weight'] > 100].sort_values(by = 'weight', ascending = False)['name'].to_frame()
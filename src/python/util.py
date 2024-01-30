import json
import pandas
import statistics
import numpy as np
from constants import *
from datetime import date
from datetime import datetime
from collections import Counter


def retrieve_game_data(game: str, url: list, columnList: list):
    json_data = retrieve_game_data_as_json(url, columnList)
    saveCsvToFile(json_data, 'src/assets/'+game.lower()+'.csv')
    json_data = clean_up_data(game, json_data)
    json_data = sort_data_by_date(json_data)
    return json_data

def retrieve_game_data_as_json(urls: list, columns: list):
    dataframes_list = []

    for url in urls:
        print(f'Reading data from => {url}')
        dataframe = pandas.read_csv(url, header=None, on_bad_lines='skip')
        dataframe.columns = columns
        dataframes_list.append(dataframe)

        # Display the total records found for the current URL
        print(f'Total records found for {url}: {len(dataframe)}')

    # Concatenate all DataFrames in the list along the rows (axis=0)
    result_dataframe = pandas.concat(dataframes_list, axis=0)

    # Convert the concatenated DataFrame to JSON
    result_json = dataframeToJson(result_dataframe)

    return result_json


def clean_up_data(game: str, data: list):
    for item in data:
        item['Date'] = f"{item['Year']}-{str(item['Month']).zfill(2)}-{str(item['Day']).zfill(2)}{draw_event_time(item)}"

        numbers = [item[f'Num{i}'] for i in range(1, 7) if f'Num{i}' in item]

        if game == PICK3 or game == DAILY4:
            item['Number'] = ''.join(map(str, numbers))
            # item['SortedDigitsNumber'] = ''.join(sorted(item['Number']))
            item['RepeatedNumbers'] = has_repeated_numbers(numbers)
            item['SumOfDigits'] = sum(numbers)
            item['Quarter'] = find_number_quarter_range(numbers)
        else:
            item['Number'] = '-'.join(map(str, sorted(map(int, numbers))))

        item['SortedNumberArray'] = sorted(map(int, numbers))
        item['OddNumbersCount'] = count_odd_numbers(numbers)
        
        for key in ['Ball1', 'Ball2', 'Year', 'Month', 'Day']:
            item.pop(key, None)

    return data

def draw_event_time(event):
    if str(event['GameName']).endswith('Morning'):
        return 'T09:50:00'
    if str(event['GameName']).endswith('Day'):
        return 'T12:17:00'
    if str(event['GameName']).endswith('Evening'):
        return 'T17:50:00'
    else:
        return 'T22:02:00'

def has_repeated_numbers(numbers):
    return len(numbers) != len(set(numbers))

def find_number_quarter_range(numbers):
    # Your findNumberQuarterRange logic here
    return 0

def sort_data_by_date(data: list, reverse: bool = True):
    # return sorted(data, key=lambda x: datetime.fromisoformat(x["Date"]), reverse=True)
    return sorted(data, key=lambda x: x["Date"], reverse=reverse)

def dataframeToJson(df):
    """Convert a pandas DataFrame to JSON with 'records' orientation."""
    return json.loads(df.to_json(orient='records', indent=4))

def saveCsvToFile(data: any, fileName: str):
    """Saves json data as csv"""
    pandas.DataFrame(data).to_csv(fileName, header=False, index=False)

def save_json_to_file(data: any, file_name: str):
    """    Save data to a JSON file.    """
    pandas.DataFrame(data).to_json(file_name, orient='records', indent=4)
    
def count_odd_numbers(list): 
    count_odd = 0
    for x in list:
        if x % 2:
            count_odd += 1
    return count_odd

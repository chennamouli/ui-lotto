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
            item['NumberInt'] = int(item['Number'])
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

def findCommonValues(array1, array2):
    set1 = set(array1)
    return [elem for elem in array2 if elem in set1]

# Function to calculate the probability of each number in an array
def probabilityOfNumbers(numbers):
    total_elements = len(numbers)
    frequency_dict = {}
    for num in numbers:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1
    return [{'number': num, 'value': freq / total_elements } for num, freq in frequency_dict.items()]


def updatePred2(json_data: list, lastNgames: int):
    nextPredNumbers = []
    for index, data in enumerate(json_data):
        # Given data
        arrayOfLastNGames = [other_item["SortedNumberArray"] for other_item in json_data[index:index+lastNgames]]
        print(f'arrayOfLastNGames: {index} - {arrayOfLastNGames}')
        arrayOfLastNGames = np.concatenate(arrayOfLastNGames) if arrayOfLastNGames else np.array([])
        prob_dict = probabilityOfNumbers(arrayOfLastNGames)
        print(f'prob_dict: {index} - {prob_dict}')
        prob_dict = sorted(prob_dict, key=lambda x: x["value"])
        selectedFiveNumbers = prob_dict[:5]
        predTempList = [item['number'] for item in selectedFiveNumbers]
        print(f'predTempList: {index} - {predTempList}')
        if index == 0:
            nextPredNumbers = predTempList
        else:
            json_data[index-1]['Pred2'] = sorted(predTempList)
            json_data[index-1]['Pred2MatchCount'] = len(findCommonValues(predTempList, json_data[index-1]["SortedNumberArray"]))
    print('updatePred2, nextPredNumbers!!', sorted(nextPredNumbers))
    
def updatePred1(json_data: list):
    for index, data in enumerate(json_data):
        # Given data
        arrayOfLastNGames = [other_item["SortedNumberArray"] for other_item in json_data[index:index+6]]
        mergedNumbersArray = np.concatenate(arrayOfLastNGames) if arrayOfLastNGames else np.array([])

        # Find missing numbers
        missing_numbers = [num for num in range(1, 36) if num not in set(mergedNumbersArray)]

        # Processing for arrayOfLastN2Games
        arrayOfLastN2Games = [other_item["SortedNumberArray"] for other_item in json_data[index:min(index+9, len(json_data))]]
        mergedN2NumbersArray = np.concatenate(arrayOfLastN2Games) if arrayOfLastN2Games else np.array([])

        # Find common numbers between mergedN2NumbersArray and missing_numbers
        mergedCommonNumbersArray = findCommonValues(mergedN2NumbersArray, missing_numbers)
        
        # Calculate probability of numbers in mergedCommonNumbersArray and sort
        probability_of_missed = probabilityOfNumbers(mergedCommonNumbersArray)
        sorted_probability_of_missed = sorted(probability_of_missed, key=lambda x: x["value"])

        # Calculate probability of numbers in mergedN2NumbersArray and sort
        probability_of_repeated_n2 = probabilityOfNumbers(mergedN2NumbersArray)
        sorted_probability_of_repeated_n2 = sorted(probability_of_repeated_n2, key=lambda x: x["value"])

        

        # Retrieve the first 2 elements from sorted_array_common and the last 3 elements from sorted_array_n2
        # result = sorted_probability_of_missed[:2] + sorted_probability_of_repeated_n2[:1] + sorted_probability_of_repeated_n2[-2:] #7, 14 days, 23%
        #7, 14 days, 23%, #7, 10 days, 34%, #7, 9 days, 35%, #9, 11 days, 33%, #7, 8 days 41%
        result = sorted_probability_of_missed[:1] + sorted_probability_of_missed[-1:] + sorted_probability_of_repeated_n2[:1] + sorted_probability_of_repeated_n2[-2:] 
        # result = sorted_probability_of_missed[:2] + sorted_probability_of_repeated_n2[-3:] #11%
        result = [item['number'] for item in result]
        result = sorted(result)
        if index == 0:
            nextPredNumbers = result
        else:
            json_data[index-1]['Pred1'] = result
            json_data[index-1]['Pred1MatchCount'] = len(findCommonValues(result, json_data[index-1]["SortedNumberArray"]))
            
        data['Pred1'] = sorted(result)
        data['Pred1MatchCount'] = len(findCommonValues(result, data["SortedNumberArray"]))
        # print(f'Predict {result}, Actual {data["SortedNumberArray"]}, Matched { len(findCommonValues(result, data["SortedNumberArray"])) }')
        print('updatePred2, nextPredNumbers!!', sorted(nextPredNumbers))
        
        
        
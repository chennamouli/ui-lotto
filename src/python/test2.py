import numpy as np
from util import *

# Function to find common values between two arrays
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

def updatePred1(json_data: list):
    for index, data in enumerate(json_data):
        if index == 0: return
        # Given data
        arrayOfLastNGames = [other_item["SortedNumberArray"] for other_item in json_data[index:index+6]]
        mergedNumbersArray = np.concatenate(arrayOfLastNGames) if arrayOfLastNGames else np.array([])

        # Find missing numbers
        missing_numbers = [num for num in range(1, 36) if num not in set(mergedNumbersArray)]

        # Processing for arrayOfLastN2Games
        arrayOfLastN2Games = [other_item["SortedNumberArray"] for other_item in json_data[index:min(index+7, len(json_data))]]
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
        # data['Pred1'] = sorted(result)
        # data['Pred1MatchCount'] = len(findCommonValues(result, data["SortedNumberArray"]))
        json_data[index-1]['Pred1'] = sorted(result)
        json_data[index-1]['Pred1MatchCount'] = len(findCommonValues(result, data["SortedNumberArray"]))
        print(f'Predict {result}, Actual {data["SortedNumberArray"]}, Matched { len(findCommonValues(result, data["SortedNumberArray"])) }')
    print(json_data)

# Test Data
json_data = [ 
    # {"GameName":"Cash Five"},
    { "GameName":"Cash Five", "Date":"2024-01-30T22:02:00", "SortedNumberArray":[ 6, 9, 16, 27, 31 ] }, 
    { "GameName":"Cash Five", "Date":"2024-01-29T22:02:00", "SortedNumberArray":[ 7, 8, 16, 29, 34 ] }, 
    { "GameName":"Cash Five", "Date":"2024-01-27T22:02:00", "SortedNumberArray":[ 6, 17, 22, 23, 33 ] }, 
    { "GameName":"Cash Five", "Date":"2024-01-26T22:02:00", "SortedNumberArray":[ 12, 16, 17, 18, 34 ] }, 
    { "GameName":"Cash Five", "Date":"2024-01-25T22:02:00", "SortedNumberArray":[ 1, 2, 3, 9, 22 ] }, 
    { "GameName":"Cash Five", "Date":"2024-01-24T22:02:00", "SortedNumberArray":[ 7, 13, 18, 28, 32 ] }, 
    { "GameName":"Cash Five", "Date":"2024-01-23T22:02:00", "SortedNumberArray":[ 3, 9, 11, 15, 35 ] }, 
    { "GameName":"Cash Five", "Date":"2024-01-22T22:02:00", "SortedNumberArray":[ 5, 9, 13, 22, 24 ] }, 
    { "GameName":"Cash Five", "Date":"2024-01-20T22:02:00", "SortedNumberArray":[ 7, 8, 16, 32, 33 ] } 
]

# [
#     # [9, 27, 31, 7, 8]
#     {'GameName': 'Cash Five', 'Date': '2024-01-30T22:02:00', 'SortedNumberArray': [6, 9, 16, 27, 31], 'Pred2': [7, 8, 9, 27, 31], 'Pred2MatchCount': 3}, 
#     {'GameName': 'Cash Five', 'Date': '2024-01-29T22:02:00', 'SortedNumberArray': [7, 8, 16, 29, 34], 'Pred2': [7, 8, 9, 27, 31], 'Pred2MatchCount': 2}, 
#     {'GameName': 'Cash Five', 'Date': '2024-01-27T22:02:00', 'SortedNumberArray': [6, 17, 22, 23, 33], 'Pred2': [7, 8, 9, 27, 31], 'Pred2MatchCount': 0}, 
#     {'GameName': 'Cash Five', 'Date': '2024-01-26T22:02:00', 'SortedNumberArray': [12, 16, 17, 18, 34], 'Pred2': [7, 8, 9, 27, 31], 'Pred2MatchCount': 0}, 
#     {'GameName': 'Cash Five', 'Date': '2024-01-25T22:02:00', 'SortedNumberArray': [1, 2, 3, 9, 22], 'Pred2': [7, 8, 9, 27, 31], 'Pred2MatchCount': 1}, 
#     {'GameName': 'Cash Five', 'Date': '2024-01-24T22:02:00', 'SortedNumberArray': [7, 13, 18, 28, 32], 'Pred2': [7, 8, 9, 27, 31], 'Pred2MatchCount': 1}, 
#     {'GameName': 'Cash Five', 'Date': '2024-01-23T22:02:00', 'SortedNumberArray': [3, 9, 11, 15, 35], 'Pred2': [7, 8, 9, 27, 31], 'Pred2MatchCount': 1}, 
#     {'GameName': 'Cash Five', 'Date': '2024-01-22T22:02:00', 'SortedNumberArray': [5, 9, 13, 22, 24], 'Pred2': [7, 8, 9, 27, 31], 'Pred2MatchCount': 1}, 
#     {'GameName': 'Cash Five', 'Date': '2024-01-20T22:02:00', 'SortedNumberArray': [7, 8, 16, 32, 33]}]


updatePred1(json_data)
updatePred2(json_data, 3)
# print(json_data)

# game = CASH_FIVE
# game_url = CASH_FIVE_URL
# game_columns = CASH_FIVE_COLUMNS
# json_data = retrieve_game_data(game, [LOTTERY_BASE_URL + game_url], game_columns)
# json_data = retrieve_game_data(game, ['src/assets/'+game.lower()+'.csv'], game_columns)

# for index, data in enumerate(json_data[:100]):
#     # Given data
#     arrayOfLastNGames = [other_item["SortedNumberArray"] for other_item in json_data[index:index+7]]
#     mergedNumbersArray = np.concatenate(arrayOfLastNGames) if arrayOfLastNGames else np.array([])

#     # Find missing numbers
#     missing_numbers = [num for num in range(1, 36) if num not in set(mergedNumbersArray)]

#     # Processing for arrayOfLastN2Games
#     arrayOfLastN2Games = [other_item["SortedNumberArray"] for other_item in json_data[index:min(index+14, len(json_data))]]
#     mergedN2NumbersArray = np.concatenate(arrayOfLastN2Games) if arrayOfLastN2Games else np.array([])

#     # Find common numbers between mergedN2NumbersArray and missing_numbers
#     mergedCommonNumbersArray = findCommonValues(mergedN2NumbersArray, missing_numbers)

#     # Calculate probability of numbers in mergedN2NumbersArray and sort
#     probability_dict_n2 = probabilityOfNumbers(mergedN2NumbersArray)
#     sorted_array_n2 = sorted(probability_dict_n2, key=lambda x: x["value"])

#     # Calculate probability of numbers in mergedCommonNumbersArray and sort
#     probability_dict = probabilityOfNumbers(mergedCommonNumbersArray)
#     sorted_array_common = sorted(probability_dict, key=lambda x: x["value"])

#     # Retrieve the first 2 elements from sorted_array_common and the last 3 elements from sorted_array_n2
#     result = sorted_array_common[:2] + sorted_array_n2[-3:]
#     result = [item['number'] for item in result]
#     data['Pred1'] = result
#     data['Pred1MatchCount'] = len(findCommonValues(result, data["SortedNumberArray"]))
#     print(f'Predict {result}, Actual {data["SortedNumberArray"]}, Matched { len(findCommonValues(result, data["SortedNumberArray"])) }')




arrayOfLastNGames: 0 - [[6, 9, 16, 27, 31], [7, 8, 16, 29, 34], [6, 17, 22, 23, 33]]
prob_dict: 0 - [{'number': 6, 'value': 0.13333333333333333}, {'number': 9, 'value': 0.06666666666666667}, {'number': 16, 'value': 0.13333333333333333}, {'number': 27, 'value': 0.06666666666666667}, {'number': 31, 'value': 0.06666666666666667}, {'number': 7, 'value': 0.06666666666666667}, {'number': 8, 'value': 0.06666666666666667}, {'number': 29, 'value': 0.06666666666666667}, {'number': 34, 'value': 0.06666666666666667}, {'number': 17, 'value': 0.06666666666666667}, {'number': 22, 'value': 0.06666666666666667}, {'number': 23, 'value': 0.06666666666666667}, {'number': 33, 'value': 0.06666666666666667}]
predTempList: 0 - [9, 27, 31, 7, 8]
arrayOfLastNGames: 1 - [[7, 8, 16, 29, 34], [6, 17, 22, 23, 33], [12, 16, 17, 18, 34]]
prob_dict: 1 - [{'number': 7, 'value': 0.06666666666666667}, {'number': 8, 'value': 0.06666666666666667}, {'number': 16, 'value': 0.13333333333333333}, {'number': 29, 'value': 0.06666666666666667}, {'number': 34, 'value': 0.13333333333333333}, {'number': 6, 'value': 0.06666666666666667}, {'number': 17, 'value': 0.13333333333333333}, {'number': 22, 'value': 0.06666666666666667}, {'number': 23, 'value': 0.06666666666666667}, {'number': 33, 'value': 0.06666666666666667}, {'number': 12, 'value': 0.06666666666666667}, {'number': 18, 'value': 0.06666666666666667}]
predTempList: 1 - [7, 8, 29, 6, 22]
arrayOfLastNGames: 2 - [[6, 17, 22, 23, 33], [12, 16, 17, 18, 34], [1, 2, 3, 9, 22]]
prob_dict: 2 - [{'number': 6, 'value': 0.06666666666666667}, {'number': 17, 'value': 0.13333333333333333}, {'number': 22, 'value': 0.13333333333333333}, {'number': 23, 'value': 0.06666666666666667}, {'number': 33, 'value': 0.06666666666666667}, {'number': 12, 'value': 0.06666666666666667}, {'number': 16, 'value': 0.06666666666666667}, {'number': 18, 'value': 0.06666666666666667}, {'number': 34, 'value': 0.06666666666666667}, {'number': 1, 'value': 0.06666666666666667}, {'number': 2, 'value': 0.06666666666666667}, {'number': 3, 'value': 0.06666666666666667}, {'number': 9, 'value': 0.06666666666666667}]
predTempList: 2 - [6, 23, 33, 12, 16]
arrayOfLastNGames: 3 - [[12, 16, 17, 18, 34], [1, 2, 3, 9, 22], [7, 13, 18, 28, 32]]
prob_dict: 3 - [{'number': 12, 'value': 0.06666666666666667}, {'number': 16, 'value': 0.06666666666666667}, {'number': 17, 'value': 0.06666666666666667}, {'number': 18, 'value': 0.13333333333333333}, {'number': 34, 'value': 0.06666666666666667}, {'number': 1, 'value': 0.06666666666666667}, {'number': 2, 'value': 0.06666666666666667}, {'number': 3, 'value': 0.06666666666666667}, {'number': 9, 'value': 0.06666666666666667}, {'number': 22, 'value': 0.06666666666666667}, {'number': 7, 'value': 0.06666666666666667}, {'number': 13, 'value': 0.06666666666666667}, {'number': 28, 'value': 0.06666666666666667}, {'number': 32, 'value': 0.06666666666666667}]
predTempList: 3 - [12, 16, 17, 34, 1]
arrayOfLastNGames: 4 - [[1, 2, 3, 9, 22], [7, 13, 18, 28, 32], [3, 9, 11, 15, 35]]
prob_dict: 4 - [{'number': 1, 'value': 0.06666666666666667}, {'number': 2, 'value': 0.06666666666666667}, {'number': 3, 'value': 0.13333333333333333}, {'number': 9, 'value': 0.13333333333333333}, {'number': 22, 'value': 0.06666666666666667}, {'number': 7, 'value': 0.06666666666666667}, {'number': 13, 'value': 0.06666666666666667}, {'number': 18, 'value': 0.06666666666666667}, {'number': 28, 'value': 0.06666666666666667}, {'number': 32, 'value': 0.06666666666666667}, {'number': 11, 'value': 0.06666666666666667}, {'number': 15, 'value': 0.06666666666666667}, {'number': 35, 'value': 0.06666666666666667}]
predTempList: 4 - [1, 2, 22, 7, 13]
arrayOfLastNGames: 5 - [[7, 13, 18, 28, 32], [3, 9, 11, 15, 35], [5, 9, 13, 22, 24]]
prob_dict: 5 - [{'number': 7, 'value': 0.06666666666666667}, {'number': 13, 'value': 0.13333333333333333}, {'number': 18, 'value': 0.06666666666666667}, {'number': 28, 'value': 0.06666666666666667}, {'number': 32, 'value': 0.06666666666666667}, {'number': 3, 'value': 0.06666666666666667}, {'number': 9, 'value': 0.13333333333333333}, {'number': 11, 'value': 0.06666666666666667}, {'number': 15, 'value': 0.06666666666666667}, {'number': 35, 'value': 0.06666666666666667}, {'number': 5, 'value': 0.06666666666666667}, {'number': 22, 'value': 0.06666666666666667}, {'number': 24, 'value': 0.06666666666666667}]
predTempList: 5 - [7, 18, 28, 32, 3]
arrayOfLastNGames: 6 - [[3, 9, 11, 15, 35], [5, 9, 13, 22, 24], [7, 8, 16, 32, 33]]
prob_dict: 6 - [{'number': 3, 'value': 0.06666666666666667}, {'number': 9, 'value': 0.13333333333333333}, {'number': 11, 'value': 0.06666666666666667}, {'number': 15, 'value': 0.06666666666666667}, {'number': 35, 'value': 0.06666666666666667}, {'number': 5, 'value': 0.06666666666666667}, {'number': 13, 'value': 0.06666666666666667}, {'number': 22, 'value': 0.06666666666666667}, {'number': 24, 'value': 0.06666666666666667}, {'number': 7, 'value': 0.06666666666666667}, {'number': 8, 'value': 0.06666666666666667}, {'number': 16, 'value': 0.06666666666666667}, {'number': 32, 'value': 0.06666666666666667}, {'number': 33, 'value': 0.06666666666666667}]
predTempList: 6 - [3, 11, 15, 35, 5]
arrayOfLastNGames: 7 - [[5, 9, 13, 22, 24], [7, 8, 16, 32, 33]]
prob_dict: 7 - [{'number': 5, 'value': 0.1}, {'number': 9, 'value': 0.1}, {'number': 13, 'value': 0.1}, {'number': 22, 'value': 0.1}, {'number': 24, 'value': 0.1}, {'number': 7, 'value': 0.1}, {'number': 8, 'value': 0.1}, {'number': 16, 'value': 0.1}, {'number': 32, 'value': 0.1}, {'number': 33, 'value': 0.1}]
predTempList: 7 - [5, 9, 13, 22, 24]
arrayOfLastNGames: 8 - [[7, 8, 16, 32, 33]]
prob_dict: 8 - [{'number': 7, 'value': 0.2}, {'number': 8, 'value': 0.2}, {'number': 16, 'value': 0.2}, {'number': 32, 'value': 0.2}, {'number': 33, 'value': 0.2}]
predTempList: 8 - [7, 8, 16, 32, 33]
updatePred2, nextPredNumbers!! [9, 27, 31, 7, 8]
[{'GameName': 'Cash Five', 'Date': '2024-01-30T22:02:00', 'SortedNumberArray': [6, 9, 16, 27, 31], 'Pred2': [6, 7, 8, 22, 29], 'Pred2MatchCount': 1}, {'GameName': 'Cash Five', 'Date': '2024-01-29T22:02:00', 'SortedNumberArray': [7, 8, 16, 29, 34], 'Pred2': [6, 12, 16, 23, 33], 'Pred2MatchCount': 1}, {'GameName': 'Cash Five', 'Date': '2024-01-27T22:02:00', 'SortedNumberArray': [6, 17, 22, 23, 33], 'Pred2': [1, 12, 16, 17, 34], 'Pred2MatchCount': 1}, {'GameName': 'Cash Five', 'Date': '2024-01-26T22:02:00', 'SortedNumberArray': [12, 16, 17, 18, 34], 'Pred2': [1, 2, 7, 13, 22], 'Pred2MatchCount': 0}, {'GameName': 'Cash Five', 'Date': '2024-01-25T22:02:00', 'SortedNumberArray': [1, 2, 3, 9, 22], 'Pred2': [3, 7, 18, 28, 32], 'Pred2MatchCount': 1}, {'GameName': 'Cash Five', 'Date': '2024-01-24T22:02:00', 'SortedNumberArray': [7, 13, 18, 28, 32], 'Pred2': [3, 5, 11, 15, 35], 'Pred2MatchCount': 0}, {'GameName': 'Cash Five', 'Date': '2024-01-23T22:02:00', 'SortedNumberArray': [3, 9, 11, 15, 35], 'Pred2': [5, 9, 13, 22, 24], 'Pred2MatchCount': 1}, {'GameName': 'Cash Five', 'Date': '2024-01-22T22:02:00', 'SortedNumberArray': [5, 9, 13, 22, 24], 'Pred2': [7, 8, 16, 32, 33], 'Pred2MatchCount': 0}, {'GameName': 'Cash Five', 'Date': '2024-01-20T22:02:00', 'SortedNumberArray': [7, 8, 16, 32, 33]}]
(.venv) cgajam@ChandraoulisMBP ui-lotto % 

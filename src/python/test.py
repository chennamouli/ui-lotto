import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from util import *
from statistics import mode


def probabilityOfNumbers(numbers: list):
    # Calculate the total number of elements in the list
    total_elements = len(numbers)
    # Create a dictionary to store the frequency of each number
    frequency_dict = {}
    # Count the frequency of each number
    for num in numbers:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    # Calculate the probability of each number
    probability_dict = {}
    for num, frequency in frequency_dict.items():
        probability_dict[num] = frequency / total_elements
    return probability_dict
    
def findLeastProbableNumber(leastIndex, probability_dict):
    """leastIndex=0 means least probable number"""
    if(leastIndex >= len(probability_dict.values())): 
        return -1;
    temp_dict = probability_dict
    for i in range(1,leastIndex+1):
        del temp_dict[min(temp_dict, key=temp_dict.get)]
    return min(temp_dict, key=temp_dict.get)

def findCommonValues(array1: list, array2: list):
    # Create an empty list to store common values
    common_values = []

    # Convert array2 to a set for faster lookup
    set2 = set(array2)

    # Iterate through array1
    for element in array1:
        if element in set2:
            common_values.append(element)

    print("Common values:", common_values)
    return common_values

game = CASH_FIVE
game_url = CASH_FIVE_URL
game_columns = CASH_FIVE_COLUMNS
# json_data = retrieve_game_data(game, [LOTTERY_BASE_URL + game_url], game_columns)
# json_data = retrieve_game_data(game, ['src/assets/'+game.lower()+'.csv'], game_columns)

# Test Data
json_data = [ 
                # { "GameName":"Cash Five", "Date":"2024-01-31T22:02:00", "SortedNumberArray":[ 6, 11, 13, 14, 23 ] }, 
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

arrayOfLastNGames = [other_item["SortedNumberArray"] for other_item in json_data[0 : 7]]
mergedNumbersArray = np.concatenate(arrayOfLastNGames) if arrayOfLastNGames else np.array([])
print(mergedNumbersArray)
print('mergedNumbersArray', mergedNumbersArray)

# Initialize a list to store the missing numbers
missing_numbers = []

# Iterate through the range from 1 to 35 (inclusive)
for num in range(1, 36):
    if num not in set(mergedNumbersArray):
        missing_numbers.append(num)
print('missing_numbers', missing_numbers)

arrayOfLast21Games = [other_item["SortedNumberArray"] for other_item in json_data[0 : min(14, len(json_data))]]
merged21NumbersArray = np.concatenate(arrayOfLastNGames) if arrayOfLastNGames else np.array([])
print('merged21NumbersArray', merged21NumbersArray)
merged21NumbersArray = findCommonValues(merged21NumbersArray, missing_numbers)

probability_dict = probabilityOfNumbers(merged21NumbersArray)
print(probability_dict)
least_probable_number = findLeastProbableNumber(0, probability_dict) 
second_least_probable_number = findLeastProbableNumber(0, probability_dict)

least_probable_number = missing_numbers[0] if least_probable_number < 0 else least_probable_number
second_least_probable_number = missing_numbers[1] if second_least_probable_number < 0 else second_least_probable_number
print(least_probable_number, second_least_probable_number)
# {1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 22, 23, 27, 28, 29, 31, 32, 33, 34, 35}
# [4, 5, 10, 14, 19, 20, 21, 24, 25, 26, 30]
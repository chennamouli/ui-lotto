from util import *
from pystreamapi import Stream

game = PICK3
game_columns = PICK3_COLUMNS
json_data = retrieve_game_data(game, [LOTTERY_BASE_URL + PICK3_MORNING_URL, LOTTERY_BASE_URL + PICK3_DAY_URL, LOTTERY_BASE_URL + PICK3_EVENING_URL, LOTTERY_BASE_URL + PICK3_NIGHT_URL], game_columns)
# json_data = retrieve_game_data(game, ['src/assets/'+game.lower()+'.csv'], game_columns)
save_json_to_file(json_data, 'src/assets/'+game.lower()+'.json')
print('\n')

def has_unique_digits(lst):
    # Convert each integer in the list to a string
    str_lst = [str(num) for num in lst]
    
    # Iterate through each string representation of the integers
    for num_str in str_lst:
        # Count the occurrences of each digit in the string
        for digit in num_str:
            if num_str.count(digit) > 1:
                return False  # If any digit occurs more than once, return False
    
    return True  # If all digits are unique, return True
def count_odd_numbers(lst):
    # Initialize a counter for odd numbers
    odd_count = 0
    
    # Iterate through the list
    for num in lst:
        # Check if the number is odd
        if num % 2 != 0:
            odd_count += 1
    
    return odd_count

count = Stream.of(json_data) \
    .filter(lambda x: len(list(set(x['SortedNumberArray']))) == 3 ) \
    .filter(lambda x: count_odd_numbers(x['SortedNumberArray']) == 2) \
    .count()
print(f'total {len(json_data)}, count {count} prob {count/len(json_data)}' )


print(f"Finished!")



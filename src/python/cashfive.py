from util import *

def check_for_repeated_numbers(data: list, last_n_games: int):
    for index, item in enumerate(data):
        current_sorted_array = item["SortedNumberArray"]
        previous_sorted_arrays = [other_item["SortedNumberArray"] for other_item in data[index+1 : index+1+last_n_games]]
        previous_sorted_merged_arrays = np.concatenate(previous_sorted_arrays) if previous_sorted_arrays else np.array([])

        common_values = np.intersect1d(current_sorted_array, previous_sorted_merged_arrays)

        item[f'RepeatedNumbersFromLast{last_n_games}Games'] = '-'.join(map(str, common_values))
        item[f'RepeatedNumbersFromLast{last_n_games}GamesCount'] = len(common_values)

        # if len(common_values) > 3:
        #     # Uncomment the following line if you want to print details for cases where common values exceed 3
        #     print(f'Date {item["Date"]} -> Current {current_sorted_array} Previous {previous_sorted_merged_arrays}, Common {common_values}')
        #     print(' ')


game = CASH_FIVE
game_url = CASH_FIVE_URL
game_columns = CASH_FIVE_COLUMNS
json_data = retrieve_game_data(game, [LOTTERY_BASE_URL + game_url], game_columns)
# json_data = retrieve_game_data(game, ['src/assets/'+game.lower()+'.csv'], game_columns)
updatePred1(json_data)
updatePred2(json_data, 35)
check_for_repeated_numbers(json_data, 1)
check_for_repeated_numbers(json_data, 2)
check_for_repeated_numbers(json_data, 3)
check_for_repeated_numbers(json_data, 4)
check_for_repeated_numbers(json_data, 5)
check_for_repeated_numbers(json_data, 6)
check_for_repeated_numbers(json_data, 7)
save_json_to_file(json_data, 'src/assets/'+game.lower()+'.json')

print(f"Finished!")



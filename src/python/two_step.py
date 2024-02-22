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


def check_for_repeated_ball(data: list, last_n_games: int):
    for index, item in enumerate(data):
        current_sorted_array = [item["BALL"]]
        previous_sorted_balls = [other_item["BALL"] for other_item in data[index+1 : index+1+last_n_games]]
        print('previous_sorted_balls', previous_sorted_balls)
        common_values = np.intersect1d(current_sorted_array, previous_sorted_balls)
        item[f'RepeatedBallsFromLast{last_n_games}Games'] = len(common_values) > 0


game = TWO_STEP
game_url = TWO_STEP_URL
game_columns = TWO_STEP_COLUMNS
# json_data = retrieve_game_data(game, [LOTTERY_BASE_URL + game_url], game_columns)
json_data = retrieve_game_data(game, ['src/assets/'+game.lower()+'.csv'], game_columns)
updatePred1(json_data)
updatePred2(json_data, 35)
# check_for_repeated_numbers(json_data, 1)
# check_for_repeated_numbers(json_data, 2)
# check_for_repeated_numbers(json_data, 3)
# check_for_repeated_numbers(json_data, 4)
# check_for_repeated_numbers(json_data, 5)
# check_for_repeated_numbers(json_data, 6)
# check_for_repeated_numbers(json_data, 7)
# check_for_repeated_numbers(json_data, 10)
# check_for_repeated_numbers(json_data, 15)

check_for_repeated_ball(json_data, 1)
check_for_repeated_ball(json_data, 3)
check_for_repeated_ball(json_data, 5)
check_for_repeated_ball(json_data, 10)
check_for_repeated_ball(json_data, 15)
check_for_repeated_ball(json_data, 20)
check_for_repeated_ball(json_data, 25)
check_for_repeated_ball(json_data, 35)
save_json_to_file(json_data, 'src/assets/'+game.lower()+'.json')

print(f"Finished!")



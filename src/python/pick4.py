from util import *

game = DAILY4
game_columns = DAILY4_COLUMNS
json_data = retrieve_game_data(game, [LOTTERY_BASE_URL + DAILY4_MORNING_URL, LOTTERY_BASE_URL + DAILY4_DAY_URL, LOTTERY_BASE_URL + DAILY4_EVENING_URL, LOTTERY_BASE_URL + DAILY4_NIGHT_URL], game_columns)
# json_data = retrieve_game_data(game, ['src/assets/'+game.lower()+'.csv'], game_columns)
save_json_to_file(json_data, 'src/assets/'+game.lower()+'.json')

print(f"Finished!")



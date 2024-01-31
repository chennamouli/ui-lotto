from util import *

game = PICK3
game_columns = PICK3_COLUMNS
json_data = retrieve_game_data(game, [LOTTERY_BASE_URL + PICK3_MORNING_URL, LOTTERY_BASE_URL + PICK3_DAY_URL, LOTTERY_BASE_URL + PICK3_EVENING_URL, LOTTERY_BASE_URL + PICK3_NIGHT_URL], game_columns)
# json_data = retrieve_game_data(game, ['src/assets/'+game.lower()+'.csv'], game_columns)
save_json_to_file(json_data, 'src/assets/'+game.lower()+'.json')

print(f"Finished!")



from util import *

game = LOTTO
game_url = LOTTO_URL
game_columns = LOTTO_COLUMNS
json_data = retrieve_game_data(game, [LOTTERY_BASE_URL + game_url], game_columns)
# json_data = retrieve_game_data(game, ['src/assets/'+game.lower()+'.csv'], game_columns)
save_json_to_file(json_data, 'src/assets/'+game.lower()+'.json')

print(f"Finished!")
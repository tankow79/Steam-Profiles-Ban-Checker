import json
import os
import requests

API_KEY = ''  # Замініть це на ваш ключ API від Steam (https://steamcommunity.com/dev/apikey)
output_file = "data.json"  # Збергння данних про кожного користувача
output_file_ban = "data_ban.json"  # Збергння данних про забанених користувачів ([{"filename": "login or steamid.maFile", "SteamID": "steamid"}])
directory_path = "maFile"  # Тека з .maFile
DaysSinceLastBan = 10  # Днів з моменту останнього блокування
URL_profiles = "https://steamcommunity.com/profiles/"


def split_to_batches(data, batch_size):
    return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]


def download_data(steam_ids64, api_key):
    base = {'players': []}

    for i, data in enumerate(steam_ids64):
        url_final = f'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key={api_key}&steamids={",".join(data)}'
        data_from_site = requests.get(url_final)

        data_new = data_from_site.json()
        base['players'].extend(data_new.get('players', []))

    return base


def acc_ban_filter(data, days_since_last_ban):
    return [player for player in data["players"] if 0 < player["DaysSinceLastBan"] < days_since_last_ban]


def get_steam_ids(directory):
    steam_id_list = []

    if not os.path.exists(directory):
        print(f"Директорія '{directory}' не існує")
        return []

    for filename in os.listdir(directory):
        if filename.endswith(".maFile"):
            file_path = os.path.join(directory, filename)

            try:
                with open(file_path, 'r') as file:
                    json_data = json.load(file)
                    steam_id = str(json_data["Session"]["SteamID"])
                    steam_id_list.append({'filename': filename, 'SteamID': steam_id})
            except json.JSONDecodeError:
                print(f"Помилка при розкодуванні JSON у файлі '{filename}'")

    with open("steam_ids64.txt", 'w') as file:
        for item in steam_id_list:
            file.write(str(item) + '\n')

    return steam_id_list


def save_data_accs(output_file, data):
    with open(output_file, "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Отримуємо список Steam ID з вказаної директорії
    steam_id_lists = get_steam_ids(directory_path)
    print(f"Знайдено {len(steam_id_lists)} Steam ID користувачів")

    print("-" * 34)

    # Розмір пакетів для запитів до API
    chunk_size = 50

    # Розділяємо Steam ID на пакети для оптимізації запитів
    steam_id_batches = split_to_batches([entry['SteamID'] for entry in steam_id_lists], chunk_size)

    # Завантажуємо дані з API Steam
    data = download_data(steam_id_batches, API_KEY)

    # Зберігаємо завантажені дані у файл
    save_data_accs(output_file, data)

    # Фільтруємо забанених гравців
    ban_filter = acc_ban_filter(data, DaysSinceLastBan)

    print(f"Знайдено {len(ban_filter)} забанених користувачів")

    # Отримуємо список забанених Steam ID та відповідних імен файлів
    banned_steam_ids = [player.get("SteamId", "") for player in ban_filter]
    filtered_steam_ids = [entry for entry in steam_id_lists if entry.get('SteamID', '') in banned_steam_ids]

    print("-" * 34)

    for SteamID in filtered_steam_ids:
        print(f"{URL_profiles}{SteamID['SteamID']}")

    # Зберігаємо завантажені дані у файл
    save_data_accs(output_file_ban, filtered_steam_ids)

    print(f"Забанені користувачі збережено в файл: {output_file_ban}")

    input("Натисніть ENTER для закриття вікна...")

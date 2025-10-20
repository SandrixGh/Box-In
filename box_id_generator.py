from datetime import datetime

def save_to_txt(data, filename="log.txt"):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(data + '\n')

def get_date_to_token() -> dict[str, int]:
    now = datetime.now()

    date_dict = {
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
        "day": now.day,
        "month": now.month,
        "year": now.year
    }
    return  date_dict

def create_date_part_of_token() -> int:
    date_dict = get_date_to_token()

    result_token = 1

    for item in date_dict:
        smaller_multiplier = date_dict[item] * (date_dict[item] - 1)
        greater_multiplier = (date_dict[item] + 1) * (date_dict[item] + 2)

        step = greater_multiplier - smaller_multiplier

        result_token *= step

    save_to_txt(str(result_token))

    return result_token



create_date_part_of_token()
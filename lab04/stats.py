def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Не ровно три поля")
        
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    
    if not city or not date:
        raise ValueError("Пустой город или дата")
        
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Температура не является числом")
        
    return {'city': city, 'temperature': temp, 'date': date}

def read_valid(lines: list[str]) -> list[dict]:
    pass

def average_by_city(records: list[dict]) -> dict:
    pass

def warmest_city(records: list[dict]) -> str:
    pass

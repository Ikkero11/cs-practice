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
    valid = []
    for line in lines:
        if not line.strip():
            continue
        try:
            valid.append(parse_record(line))
        except ValueError:
            pass
    return valid

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        c = r['city']
        t = r['temperature']
        totals[c] = totals.get(c, 0) + t
        counts[c] = counts.get(c, 0) + 1
    return {c: round(totals[c] / counts[c], 1) for c in totals}

def warmest_city(records: list[dict]) -> str:
    avgs = average_by_city(records)
    if not avgs:
        return ""
    # Сортировка: по температуре (убывание), при равенстве - по имени (возрастание)
    return sorted(avgs.items(), key=lambda x: (-x[1], x[0]))[0][0]

VALID_LEVELS = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}

def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3 or parts[1] not in VALID_LEVELS:
        raise ValueError("Неверный формат или уровень")
    return {'time': parts[0], 'level': parts[1], 'message': parts[2]}

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip(): continue
        try:
            lvl = parse_event(line)['level']
            counts[lvl] = counts.get(lvl, 0) + 1
        except ValueError:
            counts['BROKEN'] = counts.get('BROKEN', 0) + 1
    return counts

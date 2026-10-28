VALID_LEVELS = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}

def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3 or parts[1] not in VALID_LEVELS:
        raise ValueError("Неверный формат или уровень")
    return {'time': parts[0], 'level': parts[1], 'message': parts[2]}

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

def top_errors(lines, n: int) -> list[list]:
    errs = {}
    for line in lines:
        if not line.strip(): continue
        try:
            ev = parse_event(line)
            if ev['level'] == 'ERROR':
                errs[ev['message']] = errs.get(ev['message'], 0) + 1
        except ValueError:
            pass
    
    sorted_errs = sorted(errs.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, count] for msg, count in sorted_errs[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    report = ["Отчёт по журналу"]
    for lvl in sorted(counts.keys()):
        report.append(f"{lvl}: {counts[lvl]}")
    report.append("\nЧастые ошибки:")
    for msg, count in errors:
        report.append(f"- {msg} - {count}")
    return "\n".join(report) + "\n"

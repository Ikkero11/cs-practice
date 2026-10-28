def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3 or parts[1] not in ('DEBUG', 'INFO', 'WARNING', 'ERROR'):
        raise ValueError
    return {'time': parts[0], 'level': parts[1], 'message': parts[2]}

def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip(): continue
        try:
            lvl = parse_event(line)['level']
            counts[lvl] = counts.get(lvl, 0) + 1
        except ValueError:
            counts['BROKEN'] = counts.get('BROKEN', 0) + 1
    return counts

def top_errors(lines, n):
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

def format_report(counts, errors):
    # ИСПРАВЛЕНИЕ: Добавлена пустая строка "" после заголовка
    lines = ["Отчёт по журналу", ""]
    for lvl in sorted(counts.keys()):
        lines.append(f"{lvl}: {counts[lvl]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for msg, count in errors:
        lines.append(f"- {msg} - {count}")
    return "\n".join(lines) + "\n"
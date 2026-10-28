import sys
from logstats import count_levels, top_errors, format_report

def main():
    filename = sys.stdin.readline().strip()

    with open(filename, "r", encoding="utf-8") as f:
        counts = count_levels(f)

    with open(filename, "r", encoding="utf-8") as f:
        errors = top_errors(f, 3)

    total = sum(counts.values())
    
    print(total)
    print(counts.get('ERROR', 0))
    print(counts.get('BROKEN', 0))

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(format_report(counts, errors))

main()
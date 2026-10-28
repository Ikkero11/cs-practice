import sys
from stats import parse_record, read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    
    errors = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            parse_record(line)
        except ValueError:
            errors += 1
            
    print(len(records))
    print(errors)
    
    warmest = warmest_city(records)
    if warmest:
        print(f"{average_by_city(records)[warmest]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()

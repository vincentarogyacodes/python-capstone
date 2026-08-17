def load_purchases(filename):
    records = []
    with open (filename, 'r') as file:
        for line in file:
            parts = line.strip().split(",")
            record = parts[0], parts[1], parts[2]
            records.append(record)
            print(record)
        return record

result = load_purchases("data.txt")
print(result)
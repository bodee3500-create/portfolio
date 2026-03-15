import csv

def file_save(filename):
    rows = []
    with open(filename, "r") as file:
        reader = csv. DictReader(file)
        for row in reader:
            rows.append({
                "Close": float(row["Close"]),
                "Percent Increase": float(row['Percent Increase']),
                "Volume":float(row['Volume']),
            })
    return row

def highest_x(data):
    for i in range(len(data)):
        row = data[i]
        row['Highest Close'] = max(row['Close'])
        row['Lowest Close'] = min(row['Close'])

        row['Biggest Percent Increase'] = max(row['Percent Increase'])
        row['Biggest Percent Decrease'] = min(row['Percent Increase'])
        
        row['Average Daily Volune'] = float(sum(row['Volume'])) / float(sum['Volume'])

        row['Average Daily Range'] = float(max(row['Percent Increase'])) - float(min(row['Percent Increase']))

        if float(row['Percent Increase']) >= 0:
            row['Green Day'] += 1
        elif float(row['Percenet Increase']) < 0:
            row['Red Day'] += 1
    return row
highest_x()
file_save()

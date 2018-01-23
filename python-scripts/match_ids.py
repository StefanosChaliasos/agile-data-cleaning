import csv

d_date = {}  # A  lookup table

with open('dates.csv', 'r') as csvinput:
    """
    Add dates to dictionary d_date which will be used to match
    dates with date_id in data.csv
    """
    reader = csv.reader(csvinput)
    next(reader)

    for row in reader:
        # Keys are year + month. Example: 199303
        key = row[2] + row[1]
        # Values are the ids of rows
        value = row[0]
        d_date[key] = value

with open('data.csv', 'r') as csvinput:
    with open('new_data.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all_rows = []
        # Get first line
        row = next(reader)
        all_rows.append(row)

        for row in reader:
            # Get the date in format of year + month likr 199303
            date = row[1][:4] + str(int(row[1][4:6]))
            # Create a row with all the fields unitl bday,
            # then get the appropriate id from d_date and
            # append the rest fields
            row = row[:1] + [d_date[date]] + row[2:]
            all_rows.append(row)

        writer.writerows(all_rows)

records = []
def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    
    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            line = line.strip("\n") # unsure if there is a better way to do this, but temp. for now
            if i == 0:
                column_names = line.split(",")
            else:
                entry = line.split(",")[0:5]
                records.append({
                    column_names[0]: entry[0],
                    column_names[1]: entry[1],
                    column_names[2]: entry[2],
                    column_names[3]: entry[3],
                    column_names[4]: entry[4],
                })

    print(records)

def save_report(data, filename):
    """This is currently being used for testing purposes"""
    with open(filename, "w") as f:
        f.write(f"Testing\n\n")
        for record in data:
            f.write(f"Date: {record['date']}\n")
            f.write(f"Store ID: {record['store_id']}\n")
            f.write(f"Product: {record['product']}\n")
            f.write(f"Quantity: {record['quantity']}\n")
            f.write(f"Price: {record['price']}\n\n")
            f.write(f"-"*20 + "\n")

read_csv_file("starter_code/sample_sales.csv")
save_report(records, "test_report.txt")
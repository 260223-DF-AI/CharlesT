from exceptions import *

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    TODO: Log errors
    TODO: Check if the raise statements are correct. Unsure if the current formatting is right
    """
    try:
        records = []
        # Opens file in "read" mode
        with open(filepath, "r") as f:
            # Check if the file is a valid UTF-8 or Latin-1 encoded file
            if f.encoding not in ["utf-8", "latin-1"]:
                raise UnicodeDecodeError(f"File '{filepath}' is not a valid UTF-8 or Latin-1 encoded file")

            # Check if file is empty. Raise error early
            if f.read(1) == "":
                raise FileProcessingError(f"File '{filepath}' is empty")
            
            # Iterate through each line of the file
            for i, line in enumerate(f):
                line = line.strip() # unsure if there is a better way to do this, but temp. for now
                # Separate column names into their own list to pull from
                if i == 0:
                    column_names = line.split(",")
                # Append to a list containing each row in their own dict. entry
                else:
                    entry = line.split(",")[0:5]
                    records.append({
                        column_names[0]: entry[0],
                        column_names[1]: entry[1],
                        column_names[2]: entry[2],
                        column_names[3]: entry[3],
                        column_names[4]: entry[4],
                    })
            # print(records) # for testing purposes
        return records
    except UnicodeDecodeError:
        raise FileProcessingError(f"File '{filepath}' is not a valid UTF-8 or Latin-1 encoded file")
    except FileNotFoundError:
        raise FileProcessingError(f"File '{filepath}' not found")
    except Exception as e:
        raise FileProcessingError(f"An error occurred while processing the file: {str(e)}")

# def save_report(data, filename):
#     """This is currently being used for testing purposes"""
#     with open(filename, "w") as f:
#         f.write(f"Testing\n\n")
#         for record in data:
#             f.write(f"Date: {record['date']}\n")
#             f.write(f"Store ID: {record['store_id']}\n")
#             f.write(f"Product: {record['product']}\n")
#             f.write(f"Quantity: {record['quantity']}\n")
#             f.write(f"Price: {record['price']}\n\n")
#             f.write(f"-"*20 + "\n")

# read_csv_file("starter_code/sample_sales_empty.csv")
# # save_report(records, "test_report.txt")
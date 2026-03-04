from exceptions import *

def parse(filepath) -> list[dict]:
    records = []
    # iterate through each line of the file
    for i, line in enumerate(filepath):
        # skip first row
        if i == 0:
            continue
        # append to a list containing each row in their own dict. entry
        entry = line.strip().split(",")
        records.append({
            "date": entry[0],
            "store_id": entry[1],
            "product": entry[2],
            "quantity": entry[3],
            "price": entry[4]
        })
    return records

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
    # try parsing through file with utf-8 encoding first
    try:
        # opens file and uses utf-8 encoding
        with open(filepath, "r", encoding="utf-8") as f:
            # check if file is empty. raise error early
            if f.read(1) == "":
                raise FileProcessingError(f"File '{filepath}' is empty")
            return parse(f)
    except UnicodeDecodeError as e:
        # if utf-8 fails, try latin-1 encoding
        try:
            # opens file and uses latin-1 encoding
            with open(filepath, "r", encoding="latin-1") as f:
                # check if file is empty. raise error early
                if f.read(1) == "":
                    raise FileProcessingError(f"File '{filepath}' is empty")
                return parse(f)
        # if both encoders fail, raise exception
        except UnicodeDecodeError as e:
            raise FileProcessingError(f"File '{filepath}' has an unsupported encoding. Please use UTF-8 or Latin-1")
    # if file is not found, raise exception
    except FileNotFoundError as e:
        raise FileProcessingError(f"File '{filepath}' not found")
    # general exception handler
    except Exception as e:
        raise FileProcessingError(f"An error occurred while processing the file: {str(e)}")
    
read_csv_file("sample_sales.csv")
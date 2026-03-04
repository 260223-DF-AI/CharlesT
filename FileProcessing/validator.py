from exceptions import *

def validate_sales_record(record, line_number):
    """
    Validate a single sales record.
    
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number
    
    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError

    TODO: Check if regex could be used here for cleaner formatting
    TODO: Might be understanding the purpose of record and line_number?
    """
    # Validate whether or not the record contains all required fields
    for field in ["date", "store_id", "product", "quantity", "price"]:
        if field not in record[line_number] or record[line_number][field] == "":
            raise MissingFieldError(field)
        
        # Validate the date to ensure the format is correct
        if field == "date":
            try:
                year, month, day = record[line_number]["date"].split("-")
                if len(year) != 4 or len(month) != 2 or len(day) != 2:
                    raise InvalidDataError(f"Invalid date format: {record[line_number]['date']}")
            except ValueError:
                raise InvalidDataError(f"Invalid date format: {record[line_number]['date']}")
            
        # Validate the quantity to ensure it is a positive integer
        if field == "quantity":
            try:
                quantity = int(record[line_number]["quantity"])
                if quantity <= 0:
                    raise InvalidDataError(f"Quantity must be a positive integer: {record[line_number]['quantity']}")
            except ValueError:
                raise InvalidDataError(f"Quantity must be a positive integer: {record[line_number]['quantity']}")
            
        # Validate the price to ensure it is positive
        if field == "price":
            try:
                price = float(record[line_number]["price"])
                if price <= 0 or not isinstance(price, float): # Checks if price is positive and a float
                    raise InvalidDataError(f"Price must be a positive number: {record[line_number]['price']}")
            except ValueError:
                raise InvalidDataError(f"Price must be a positive number: {record[line_number]['price']}")

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    pass
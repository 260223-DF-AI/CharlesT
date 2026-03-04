from exceptions import *
from datetime import date

def validate_sales_record(record:dict, line_number:int):
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

    DONE: Might be misunderstanding the purpose of record and line_number? 
    Line number is meant to track the sales record. If a sale happened, we assign it a number to indicate
    the order of the sales. So the first sale would be line_number 1, the second sale would be line_number
    2, etc. This could be used for logging?
    """
    

    for field in record:
        # if the field is empty, raise an error
        if record[field] == "":
            raise MissingFieldError(str(field))
        
        # validate the date to ensure the format is correct
        if field == "date":
            try:
                validate: bool = date.strptime(record[field],"%Y-%m-%d")
                if not validate:
                    raise InvalidDataError(f"Invaid date format: {record[field]}")
            except ValueError:
                raise InvalidDataError(f"Invalid date format: {record[field]}")
            
        # validate the quantity to ensure it is a positive integer
        if field == "quantity":
            try:
                quantity = int(record[field])
                if quantity <= 0:
                    raise InvalidDataError(f"Quantity must be a positive integer: {record[field]}")
            except ValueError:
                raise InvalidDataError(f"Quantity must be a positive integer: {record[field]}")
            
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
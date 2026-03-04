from unittest import case

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
            raise MissingFieldError(f"Line {line_number}: Missing required field: {field}")
        
        match field:
            # validate the date to ensure the format is correct
            case "date":
                try:
                    validate: bool = date.strptime(record[field],"%Y-%m-%d")
                    if not validate:
                        raise InvalidDataError(f"Line {line_number}: Invalid date format: {record[field]}")
                except ValueError:
                    raise InvalidDataError(f"Line {line_number}: Invalid date format: {record[field]}")

            # validate the quantity to ensure it is a positive integer
            case "quantity":
                try:
                    record[field] = int(record[field])
                    if record[field] <= 0:
                        raise InvalidDataError(f"Line {line_number}: Quantity must be a positive integer: {record[field]}")
                except ValueError:
                    raise InvalidDataError(f"Line {line_number}: Quantity must be a positive integer: {record[field]}")
                
            # validate the price to ensure it is a positive float
            case "price":
                try:
                    record[field] = float(record[field])
                    if record[field] <= 0:
                        raise InvalidDataError(f"Line {line_number}: Price must be a positive number: {record[field]}")
                except ValueError:
                    raise InvalidDataError(f"Line {line_number}: Price must be a positive number: {record[field]}")
                
    return record

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    valid_records = []
    error_list = []
    for i, record in enumerate(records):
        try:
            valid_record = validate_sales_record(record, i+1)
            valid_records.append(valid_record)
        except FileProcessingError as e:
            error_list.append(str(e))
    return tuple((valid_records, error_list))
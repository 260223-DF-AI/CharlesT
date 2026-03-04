from datetime import datetime


def write_summary_report(filepath, valid_records, errors, aggregations):
    """
    Write a formatted summary report.
    
    Report should include:
    - Processing timestamp
    - Total records processed
    - Number of valid records
    - Number of errors (with details)
    - Sales by store
    - Top 5 products
    """
    saved_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "w") as f:
        f.write(f"""=== Sales Processing Report ===
                Generated: {saved_time}

                Processing Statistics:
                - Total records processed: {len(valid_records) + len(errors)}
                - Valid records: {len(valid_records)}
                - Errors: {len(errors)}

                Sales by Store:""")

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    pass

def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    pass
from exceptions import *

def calculate_totals(records:list[dict]):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """

    for record in records:
        record['total'] = record['quantity'] * record['price']
    return records

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    store_totals = {}
    for record in records:
        store_id = record['store_id']
        total = record['total']
        if store_id in store_totals:
            store_totals[store_id] += total
        else:
            store_totals[store_id] = total
    return store_totals

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    product_totals = {}
    for record in records:
        product = record['product']
        quantity = record['quantity']
        if product in product_totals:
            product_totals[product] += quantity
        else:
            product_totals[product] = quantity
    return product_totals
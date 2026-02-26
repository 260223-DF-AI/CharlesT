# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts, name, phone, email, category):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    # TODO: Create a contact dictionary with all fields
    # TODO: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO: Append to contacts list
    # TODO: Return the new contact
    
    # Register the time that the new contact was made
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Input contact info into a dictionary object
    contact = {
        "name" : name, 
        "phone" : phone, 
        "email" : email, 
        "category" : category,
        "created_at" : timestamp
    }

    # Put the new contact into the contacts list
    return contacts.append(contact)


# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts):
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # TODO: Print header with contact count
    # TODO: Print table headers
    # TODO: Loop through contacts and print each row
    # TODO: Print footer
    
    # Header
    print("=" * 40)
    print(" " * 8 + f"CONTACT BOOK ({len(contacts)} contacts)")
    print("=" * 40)
    print("#  | Name            | Phone         | Category")
    print("---|-----------------|---------------|----------")

    # Iterate through contacts list and display relevant info
    # TODO: generate space in between each column to look like the expected output
    for i, contact in enumerate(contacts):
        print(f"{i}{" " * 3}{contact["name"]}{" " * 18}{contact["phone"]} | {contact["category"]}")


def display_contact_details(contact):
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # TODO: Print formatted contact details
    print("--- Contact Details ---")
    print(f"Name: {contact["name"]}")
    print(f"Phone: {contact["phone"]}")
    print(f"Email: {contact["email"]}")
    print(f"Category: {contact["category"]}")
    print(f"Added: {contact["created_at"]}")
    print("-----------------------")


# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # TODO: Filter contacts where query is in name (case-insensitive)
    # Hint: Use list comprehension and .lower()
    
    # Initialized list for storing multiple contacts if applicable
    matched = []

    # Scan through 
    for contact in contacts:
        curr_name = contact["name"].lower()
        if curr_name.find(query.lower()) >= 0:
            matched.append(contact)

    return matched


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # TODO: Filter contacts by category
    
    matched = []

    # Scan through 
    for contact in contacts:
        curr_category = contact["category"].lower()
        if curr_category == category.lower():
            matched.append(contact)

    return matched


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone
    
    for contact in contacts:
        curr_phone = contact["phone"]
        if curr_phone == phone:
            return contact

    return None


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    # TODO: Find contact by phone
    # TODO: Update the specified field
    # TODO: Return success/failure
    
    # Iterate through contacts for specific phone query
    for contact in contacts:
        curr_phone = contact["phone"]
        if curr_phone == phone:
            # Set the found contacts entered field into the new value provided
            contact[field] = new_value
            return True
        else:
            return False


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    
    for contact in contacts:
        curr_phone = contact["phone"]
        if curr_phone == phone:
            # Remove contact if found
            contacts.remove(contact)
            return True
        else:
            return False


# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    # TODO: Count total contacts
    # TODO: Count contacts by category
    # TODO: Find most recently added contact
    pass


# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    # TODO: Implement menu loop
    # Use while True and break on exit choice
    pass


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    
    # TODO: Add at least 5 sample contacts
    add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Bob Smith", "555-987-6543", "bob@work.com", "work")
    add_contact(contacts, "Carol White", "555-456-7890", "carol@family.net", "family")
    
    # TODO: Test your functions
    display_all_contacts(contacts)
    display_contact_details(contacts[0])

    print("\nfind by phone test")
    results = find_by_phone(contacts, "555-456-7890")
    print(results)

    print("\nfilter by category test")
    results = filter_by_category(contacts, "family")
    print(results)
    # etc.
    
    # STRETCH: Uncomment to run interactive menu
    # main()

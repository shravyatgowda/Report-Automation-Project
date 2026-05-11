from configs.auto_email import send_email
from configs.email_template import get_template
from utils.query import run_query,generate_select_query,generate_insert_query,generate_update_query,generate_delete_query
from utils.data_cleaning import clean_data,clean_whitespace,remove_empty_entries,standardize_case,remove_special_characters,drop_duplicates

def main():
    print("Starting automation process...")
    data = [' Alice ', ' Bob ', '', 'Charlie']
    cleaned = clean_data(data)
    run_query('sample_db', 'SELECT * FROM users')
    template = get_template()
    for name in cleaned:
        if name:
            body = template.format(name=name)
            send_email('poojakr@example.com', 'Automated Report', body)



if __name__ == "__main__":
    raw_data = [" Alice ", "Bob", "", None, "Charlie", "bob", "Alice!"]
    print("Original:", raw_data)

    cleaned = clean_whitespace(raw_data)
    cleaned = remove_empty_entries(cleaned)
    cleaned = standardize_case(cleaned)
    cleaned = remove_special_characters(cleaned)
    cleaned = drop_duplicates(cleaned)

    print("Cleaned:", cleaned)

    db = "example.db"
    select_q = generate_select_query("users", "*", "age > 25")
    print("Generated SELECT query:", select_q)

    insert_q = generate_insert_query("users", {"name": "Pooja", "age": 29})
    print("Generated INSERT query:", insert_q)

    update_q = generate_update_query("users", {"age": 30}, "name = 'Pooja'")
    print("Generated UPDATE query:", update_q)

    delete_q = generate_delete_query("users", "name = 'Pooja'")
    print("Generated DELETE query:", delete_q)
    
    send_email(
        recipient="pooja.kr@example.com",
        subject="Automation Report",
        body="Hi Pooja,\n\nYour automation report is ready.\n\nRegards,\nAutomation Bot"
    )


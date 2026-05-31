import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))
os.makedirs(DATA_DIR, exist_ok=True) # Creates new data directory if it doesn't exist


# default categories
expense_categories = ["food", "rent", "transport", "utilities", "entertainment", "health", "misc"]
income_categories = ["salary", "freelance", "bonus", "other"]

data = {"expense": expense_categories,
        "income": income_categories, }



JSON_TRANSACTIONS = os.path.join(DATA_DIR, "transactions.json")
JSON_CATEGORIES = os.path.join(DATA_DIR, "categories.json")

def load_transactions():
    if not(os.path.isfile(JSON_TRANSACTIONS)):
        return []
    with open(JSON_TRANSACTIONS, "r") as f:
        return json.load(f)

def save_transactions(data):
    with open(JSON_TRANSACTIONS, "w") as f:
        json.dump(data, f, indent=4)


def load_categories():
    if not(os.path.exists(JSON_CATEGORIES)):
        return {}
    with open(JSON_CATEGORIES, "r") as f:
        return json.load(f)

def save_categories(data):

    with open(JSON_CATEGORIES, "w") as f:
        json.dump(data, f, indent=4)


if load_categories() == {}:
    save_categories(data)

categories = load_categories()
transactions = load_transactions()





def validate_category(category):
    if category :
        category = category.strip().lower()
        if category not in categories["expense"] and category not in categories["income"]:
            return True
    return False

def add_expense(amount, category, note=None):
    try :
        amount = int(amount)
    except ValueError:
        return "❌ Invalid amount"

    category = category.strip().lower()
    transaction = {"type": "expense",
                   "amount": int(amount),
                   "category": category,
                   "note": note}

    if category not in expense_categories:
        choice = input(f"'{category}' is not a valid category. Add it? (y/n): ").strip().lower()
        if choice == "y":
            categories["expense"].append(category)
            save_categories(categories)
        elif choice == "n":
            return f"❌ '{category}' is not a valid category."
        else:
            return f"❌ Invalid operation"

    transactions.append(transaction)
    save_transactions(transactions)
    return f"✅ Added {amount} to {category}"

def add_income(amount, category, note=None):
    try :
        amount = int(amount)
    except ValueError:
        return "❌ Invalid amount"

    category = category.strip().lower()

    if category not in income_categories:

        a = input(f"❓ Category '{category}' is not recognized. Do you want to record it under 'other'? (y/n): ").strip().lower()
        if a == "n":
            return f"❌ Transaction canceled. Please enter a valid category."
        elif a == "y":
            category = "other"
        else:
            return "❌ Invalid operation"


    transaction = {"type": "income",
                   "amount": int(amount),
                   "category": category,
                   "note": note}

    transactions.append(transaction)
    save_transactions(transactions)
    return f"✅ Added {amount} to {category}"

def list_transactions(category=None,ttype=None):
    ls = []
    if validate_category(category):
        return f"❌ Invalid category"
    if ttype and ttype.strip().lower() != "income" and ttype.strip().lower() != "expense":
        return f"❌ Invalid type"
    for i in transactions:
        if category and category.strip().lower() != i["category"]:
            continue
        if ttype and ttype.strip().lower() != i["type"]:
            continue
        ls.append(i)
    return ls


def list_transactions_cli(category=None, ttype=None):
    results = list_transactions(category, ttype)


    if isinstance(results, str):
        print(results)
        return

    if not results:
        return "No transactions found."


    for i,t in enumerate(results):
        note = t["note"] if t["note"] else ""
        print(f"{i} | {t['type'].capitalize():6} | {t['amount']:8} | {t['category'].capitalize():12} | {note}")



def show_balance():
    balance = sum([x["amount"] for x in transactions if x["type"]=="income"])-sum([x["amount"] for x in transactions if x["type"]=="expense"])
    return f"💰 Current balance: {balance}"


def total_by_category(ttype):
    dct = {}
    if ttype not in ["income", "expense"]:
        return "❌ Invalid type"
    for i in transactions:
        if i["type"]==ttype:
            dct[i["category"]] = dct.get(i["category"], 0) + i["amount"]
    return dct


def add_category(category,ttype):
    category = category.strip().lower()
    ttype = ttype.strip().lower()
    if ttype not in ["expense" ,"income"]:
        return f"❌ Invalid type"
    if category in categories[ttype]:
        return f"❌ Category already exists"
    categories["expense"].append(category) if ttype == "expense" else categories["income"].append(category)
    save_categories(categories)
    return f"✅ Added new {ttype} category: {category}"

def delete_transaction():
    if list_transactions_cli() == "No transactions found.":
        return "No transactions found."

    a = input("Select a transaction de delete ")
    try:
        a = int(a)
    except ValueError:
        return f"❌ Invalid input. Please enter a number."
    if 0<= a < len(transactions):
        del transactions[a]
        save_transactions(transactions)
        return f"✅ Transaction deleted."
    else :
        return f"❌ Invalid choice"

def show_categories():
    return f"income categories: {categories['income']} \nexpense categories: {categories['expense']}"

def show_types():
    return f"Income / Expense"

def delete_category(category, ttype):
    category = category.strip().lower()
    ttype = ttype.strip().lower()
    if ttype not in ["expense" ,"income"]:
        return f"❌ Invalid type"
    if category not in categories[ttype]:
        return f"❌ Category doesn't exists"
    categories[ttype].remove(category)
    save_categories(categories)
    return f"✅ Category '{category}' deleted from {ttype}"

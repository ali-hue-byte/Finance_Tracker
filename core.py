transactions = []
expense_categories = ["food", "rent", "transport", "utilities", "entertainment", "health", "misc"]
income_categories = ["salary", "freelance", "bonus", "other"]


def validate_category(category):
    if category :
        category = category.strip().lower()
        if category not in expense_categories and category not in income_categories:
            return True
    return False
def add_expense(amount, category, note=None):
    category = category.strip().lower()
    transaction = {"type": "expense",
                   "amount": amount,
                   "category": category,
                   "note": note}

    if category not in expense_categories:
        choice = input(f"'{category}' is not a valid category. Add it? (y/n): ").strip().lower()
        if choice == "y":
            expense_categories.append(category)
        elif choice == "n":
            return f"❌ '{category}' is not a valid category."
        else:
            return f"❌ Invalid operation"

    transactions.append(transaction)
    return f"✅ Added {amount} to {category}"

def add_income(amount, category, note=None):
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
                   "amount": amount,
                   "category": category,
                   "note": note}

    transactions.append(transaction)
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
        print("No transactions found.")
        return


    for i,t in enumerate(results):
        note = t["note"] if t["note"] else ""
        print(f"{i} | {t['type'].capitalize():6} | {t['amount']:8} | {t['category'].capitalize():12} | {note}")



def show_balance():
    balance = sum([x["amount"] for x in transactions if x["type"]=="income"])-sum([x["amount"] for x in transactions if x["type"]=="expense"])
    return f"💰 Current balance: {balance}"


def total_by_category(ttype="expense"):
    dct = {}
    for i in transactions:
        if i["type"]==ttype:
            dct[i["category"]] = dct.get(i["category"], 0) + i["amount"]
    return dct


def add_category(category,ttype):
    category = category.strip().lower()
    ttype = ttype.strip().lower()
    if ttype != "expense" and ttype != "income":
        return f"❌ Invalid type"
    if category in income_categories or category in expense_categories:
        return f"❌ Category already registered"
    expense_categories.append(category) if ttype == "expense" else income_categories.append(category)
    return f"✅ Added new {ttype} category: {category}"

def delete_transaction():
    list_transactions_cli()
    a = input("Select a transaction de delete ")
    try:
        a = int(a)
    except ValueError:
        return f"❌ Invalid input. Please enter a number."
    if 0<= a < len(transactions):
        del transactions[a]
        return f"✅ Transaction deleted."
    else :
        return f"❌ Invalid choice"

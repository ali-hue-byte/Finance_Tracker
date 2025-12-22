from .menu_driven_cli import (add_expense,
                  add_income,
                  list_transactions_cli,
                  show_balance,
                  total_by_category,
                  add_category,
                  delete_transaction,
                  show_categories,
                  show_types,
                  delete_category)

def main():
    print("----Welcome to Finance Tracker----")
    print("default income categories: salary, freelance, bonus, other")
    print("default expense categories: food, rent, transport, utilities, entertainment, health, miscellaneous")
    print()
    while True:
        print("1. Add Expense")
        print("2. Add Income")
        print("3. List Transactions")
        print("4. Show Balance")
        print("5. Show Categories")
        print("6. Show Types")
        print("7. Total by Category")
        print("8. Manage Categories")
        print("9. Delete Transaction")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            amount = input("Amount: ")
            category = input("Category: ")
            note = input("Note (optional): ")
            print(add_expense(amount, category, note))
            print()
        elif choice == "2":
            amount = input("Amount: ")
            category = input("Category: ")
            note = input("Note (optional): ")
            print(add_income(amount, category, note))
            print()
        elif choice == "3":
            category = input("Category (optional): ")
            ttypt = input("Transaction Type (optional): ")
            list_transactions_cli(category, ttypt)
            print()
        elif choice == "4":
            print(show_balance())
            print()
        elif choice == "5":
            print(show_categories())
            print()
        elif choice == "6":
            print(show_types())
            print()
        elif choice == "7":
            ttype = input("Transaction Type : ")
            print(total_by_category(ttype))
            print()
        elif choice == "8":
            print("1. Add Category")
            print("2. Delete Category")
            print("0. Back")
            ndchoice = input("Choose an option: ").strip()
            if ndchoice == "1":
                 category = input("Category : ")
                 ttype = input("income or expense? : ")
                 print(add_category(category, ttype))
                 print()
            elif ndchoice == "2":
                print(show_categories())
                ttype = input("Select a type: ")
                categoryy = input("Category: ")
                print(delete_category(categoryy, ttype))
                print()
            elif ndchoice == "0":
                print()
            else:
                print("❌ Invalid choice")
                print()

        elif choice == "9":
            print(delete_transaction())
            print()
        elif choice == "0":
            return
        else:
            print("❌ Invalid choice")
            print()

if __name__ == "__main__":
    main()




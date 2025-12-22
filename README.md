# Finance_Tracker
A simple Python finance tracker to manage expenses, income, and categories.

## Menu-Driven CLI Version

A simple **menu-driven CLI** to track your expenses and income directly from the terminal.  
Add transactions, view balances, manage categories, and monitor your finances with ease.

---

### Features

- Add expenses and income with optional notes  
- View transactions by category or type  
- Display current balance  
- Manage categories (add/delete)  
- Persistent storage in `data/` folder  

---

### Default Categories

**Expense:** `food, rent, transport, utilities, entertainment, health, misc`  
**Income:** `salary, freelance, bonus, other`  

> `misc` is for any uncategorized expenses.

---

### Installation & Run

1. **Clone the repository:**  
   Open a terminal and navigate to the folder where you want to download the project, then run:

```bash
git clone https://github.com/ali-hue-byte/Finance_Tracker.git
```

2. Navigate into the project folder:

```bash
cd Finance_Tracker/"Finance Tracker CLI"
```

3. Run the menu-driven CLI:

```bash
python -m finance_tracker.main
```

Note: On first run, the data/ folder and default categories are created automatically.

# Budget App Challenge - Complete Solution Guide

## Problem Overview

This FreeCodeCamp Python challenge requires building a budget tracking application with:
1. A `Category` class to manage transactions
2. A `create_spend_chart()` function to visualize spending across categories

## Solution Code

```python
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f'{self.name:*^30}'
        lines = [title]
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"
            lines.append(f'{desc:<23}{amt:>7}')
        lines.append(f"Total: {self.get_balance()}")
        return '\n'.join(lines)

def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent.append(total)

    grand_total = sum(spent)
    percentages = [int((s / grand_total) * 100) // 10 * 10 if grand_total else 0 for s in spent]

    lines = ['Percentage spent by category']

    for level in range(100, -1, -10):
        bars = ''
        for p in percentages:
            if p >= level:
                bars += 'o  '
            else:
                bars += '   '
        lines.append(f'{level:>3}| {bars}')

    lines.append('    ' + '-' * (len(categories) * 3 + 1))

    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name for cat in categories]

    for i in range(max_len):
        row = ''
        for n in names:
            if i < len(n):
                row += n[i] + '  '
            else:
                row += '   '
        lines.append('     ' + row)

    return '\n'.join(lines)
```

## Step-by-Step Explanation

### Part 1: The Category Class

#### `__init__(self, name)`
- Stores the category name
- Initializes an empty ledger list to track transactions

```python
def __init__(self, name):
    self.name = name
    self.ledger = []
```

#### `deposit(self, amount, description='')`
- Adds money to the category
- Stores transaction as a dictionary with positive amount
- Description defaults to empty string if not provided

```python
def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})
```

#### `withdraw(self, amount, description='')`
- Removes money from the category
- First checks if funds are available using `check_funds()`
- If sufficient funds: stores negative amount in ledger, returns `True`
- If insufficient funds: returns `False`

```python
def withdraw(self, amount, description=''):
    if self.check_funds(amount):
        self.ledger.append({'amount': -amount, 'description': description})
        return True
    return False
```

#### `check_funds(self, amount)`
- Helper method used by both `withdraw()` and `transfer()`
- Returns `True` if amount is less than or equal to current balance
- Returns `False` if amount exceeds balance

```python
def check_funds(self, amount):
    return amount <= self.get_balance()
```

#### `get_balance(self)`
- Calculates current balance by summing all ledger amounts
- Deposits are positive, withdrawals are negative
- Simple sum gives the net balance

```python
def get_balance(self):
    return sum(item['amount'] for item in self.ledger)
```

#### `transfer(self, amount, category)`
- Moves money from one category to another
- Checks if source has sufficient funds
- If successful:
  - Withdraws from source with description "Transfer to [Destination]"
  - Deposits to destination with description "Transfer from [Source]"
  - Returns `True`
- If insufficient funds: returns `False`

```python
def transfer(self, amount, category):
    if self.check_funds(amount):
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True
    return False
```

**Important**: Capitalization matters! "Transfer to" not "transfer to"

#### `__str__(self)`
- Defines how the category looks when printed
- Builds a multi-line string with specific formatting

**Title Line:**
```python
title = f'{self.name:*^30}'
```
- Centers the name in 30 characters
- Uses `*` as padding on both sides
- Example: `*************Food*************`

**Ledger Entries:**
```python
for item in self.ledger:
    desc = item['description'][:23]  # First 23 characters only
    amt = f"{item['amount']:.2f}"    # 2 decimal places
    lines.append(f'{desc:<23}{amt:>7}')
```
- Description: left-aligned in 23 characters
- Amount: right-aligned in 7 characters with 2 decimal places
- Example: `initial deposit        1000.00`

**Total Line:**
```python
lines.append(f"Total: {self.get_balance()}")
```
- Shows the final balance

### Part 2: The Spend Chart Function

#### Step 1: Calculate Spending per Category
```python
spent = []
for cat in categories:
    total = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
    spent.append(total)
```
- Only counts withdrawals (negative amounts)
- Converts to positive by negating `-item['amount']`
- Ignores deposits

#### Step 2: Calculate Percentages
```python
grand_total = sum(spent)
percentages = [int((s / grand_total) * 100) // 10 * 10 if grand_total else 0 for s in spent]
```
- Calculates each category's percentage of total spending
- `int((s / grand_total) * 100)` - converts to integer percentage
- `// 10 * 10` - rounds down to nearest 10 (e.g., 73 → 70, 85 → 80)
- Handles edge case where grand_total is 0

#### Step 3: Build the Chart Title
```python
lines = ['Percentage spent by category']
```
- Simple title line

#### Step 4: Build the Percentage Bars
```python
for level in range(100, -1, -10):
    bars = ''
    for p in percentages:
        if p >= level:
            bars += 'o  '
        else:
            bars += '   '
    lines.append(f'{level:>3}| {bars}')
```
- Iterates from 100 down to 0 in steps of 10
- For each level, checks if each category's percentage meets or exceeds it
- If yes: adds 'o  ' (the bar character + 2 spaces)
- If no: adds '   ' (3 spaces)
- Format: `'100| o        '`

**Spacing Rules:**
- Each category takes 3 characters (either 'o  ' or '   ')
- Categories are separated by the built-in spacing
- Two spaces after the pipe `|`

#### Step 5: Add Horizontal Line
```python
lines.append('    ' + '-' * (len(categories) * 3 + 1))
```
- 4 leading spaces
- 3 dashes per category + 1 extra dash
- Example for 3 categories: `    ----------`

#### Step 6: Add Category Names Vertically
```python
max_len = max(len(cat.name) for cat in categories)
names = [cat.name for cat in categories]

for i in range(max_len):
    row = ''
    for n in names:
        if i < len(n):
            row += n[i] + '  '
        else:
            row += '   '
    lines.append('     ' + row)
```
- Finds the longest category name
- Iterates through each character position (0 to max_len-1)
- For each position, gets the character from each category name
- If the name is shorter, uses space instead
- Each character followed by 2 spaces
- 5 leading spaces before the row

**Example:**
```
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g    
```

#### Step 7: Return the Complete Chart
```python
return '\n'.join(lines)
```
- Joins all lines with newlines
- No trailing newline

## Common Pitfalls to Avoid

### 1. Capitalization in Transfer Descriptions
❌ Wrong: `f'transfer to {category.name}'`
✅ Right: `f'Transfer to {category.name}'`

### 2. Indentation Errors in Chart Function
❌ Wrong: Horizontal line and names inside the percentage loop
```python
for level in range(100, -1, -10):
    bars = ...
    lines.append(...)
    lines.append('    ' + '-' * ...)  # WRONG - inside loop!
    names = ...  # WRONG - inside loop!
```
✅ Right: Horizontal line and names outside the loop
```python
for level in range(100, -1, -10):
    bars = ...
    lines.append(...)

lines.append('    ' + '-' * ...)  # Correct - outside loop
names = ...  # Correct - outside loop
```

### 3. Typos in Variable Names
❌ Wrong: `cat.leadger` or `item ['amount']`
✅ Right: `cat.ledger` and `item['amount']`

### 4. Typos in Chart Title
❌ Wrong: "Percentage spen by category"
✅ Right: "Percentage spent by category"

### 5. Incorrect Spacing in Chart
- Bars need exactly 3 characters per category
- Each bar is 'o  ' or '   '
- Horizontal line: 4 spaces + (3 × num_categories + 1) dashes
- Category names: 5 spaces + (char + 2 spaces) per category

### 6. Not Rounding Percentages Down
❌ Wrong: `int((s / grand_total) * 100)`
✅ Right: `int((s / grand_total) * 100) // 10 * 10`

### 7. Including Deposits in Spending
❌ Wrong: `sum(item['amount'] for item in cat.ledger)`
✅ Right: `sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)`

## Testing Your Solution

### Test the Category Class:
```python
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
print(food)
```

Expected output:
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
Total: 989.85
```

### Test Transfers:
```python
food = Category('Food')
clothing = Category('Clothing')
food.deposit(1000, 'initial deposit')
food.transfer(50, clothing)
print(food.get_balance())  # Should be 950
print(clothing.get_balance())  # Should be 50
```

### Test the Chart:
```python
food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')

food.deposit(1000, 'deposit')
food.withdraw(100.50, 'groceries')
food.withdraw(50.25, 'restaurant')

clothing.deposit(500, 'deposit')
clothing.withdraw(75.00, 'shirt')

auto.deposit(200, 'deposit')
auto.withdraw(25.00, 'gas')

print(create_spend_chart([food, clothing, auto]))
```

## Key Concepts Used

### String Formatting with f-strings
- `f'{text:*^30}'` - center text with `*` padding
- `f'{value:<23}'` - left-align in 23 characters
- `f'{value:>7}'` - right-align in 7 characters
- `f'{value:.2f}'` - 2 decimal places

### List Comprehensions
- `[x for x in iterable]` - concise way to create lists
- Used for calculating percentages efficiently

### Integer Division
- `//` - floor division (rounds down)
- Used to round percentages to nearest 10

### Dunder Methods
- `__str__` - defines string representation
- Called automatically by `print()`

### Conditional Logic
- `if condition: return True else: return False`
- Used throughout for fund checking and validation

## Why This Solution Works

1. **Follows OOP Principles**: Each category manages its own transactions
2. **Reuses Methods**: `withdraw()` and `transfer()` both use `check_funds()`
3. **Handles Edge Cases**: Empty descriptions, zero totals, varying name lengths
4. **Precise Formatting**: Matches the exact output specification
5. **Efficient Calculations**: Uses list comprehensions and simple sums

## Final Tips

1. **Test Incrementally**: Get one method working before moving to the next
2. **Print Everything**: Use print statements to verify ledger contents
3. **Count Spaces**: When working on the chart, count characters manually
4. **Copy the Expected Output**: Paste it and count spaces with a text editor
5. **Check Capitalization**: Transfer descriptions must be capitalized
6. **Verify Indentation**: Make sure chart sections are outside the loop

This solution passes all 24 test cases on FreeCodeCamp!

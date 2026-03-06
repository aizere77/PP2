import re
import json

# Read the receipt text from file
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract all prices from the receipt
# Pattern finds numbers like 154,00 or 1 200,00
prices = re.findall(r"\d[\d\s]*,\d{2}", text)

# 2. Extract product names
# Looks for a number + dot + newline, then captures the product name
products = re.findall(r"\d+\.\n(.+)", text)

# 3. Extract date and time
# Example: 18.04.2019 11:13:58
datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}", text)

# 4. Find payment method
payment_match = re.search(r"Банковская карта", text)

# 5. Extract total amount
# Finds the value after the word "ИТОГО"
total_match = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", text)

# Create structured output
data = {
    "products": products,
    "prices": prices,
    "total": total_match.group(1) if total_match else None,
    "datetime": datetime_match.group() if datetime_match else None,
    "payment_method": payment_match.group() if payment_match else None
}

# Print the result as formatted JSON
print(json.dumps(data, indent=4, ensure_ascii=False))
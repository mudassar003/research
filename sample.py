# sample.py - A deliberately problematic Python file
OPENAI_API_KEY = "sk-1234567890abcdef1234567890abcdef"
def calculateTotalPrice(items, tax_rate, discount):
    total = 0
    for i in items:
        total = total + i['price'] * i['quantity']
    if discount > 0:
        total = total - (total * discount)
    total = total + (total * tax_rate)
    return total

def process_user_data(user_input):
    # No input validation - security issue
    result = eval(user_input)  # Dangerous!
    return result
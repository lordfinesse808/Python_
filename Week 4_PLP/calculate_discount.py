def calculate_discount(price, discount_percent):    
    """Calculate the price after applying a discount percentage"""
    if discount_percent >= 20 : 
        discount_amount =(discount_percent/100)* price      
        final_price = price - discount_amount 
        return final_price
    else :
        return price    
    
# Prompt user for input
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage (%): "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount_percent)
print("The final price is: $", round(final_price, 2))
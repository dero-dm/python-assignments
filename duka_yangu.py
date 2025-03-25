def add_product(product_name: str, price: float, quantity: int) -> dict:
    """
    Creates a new product dictionary with the given details.
    
    Args:
        product_name: Name of the product
        price: Price of the product
        quantity: Initial stock quantity
        
    Returns:
        Dictionary representing the product
    """
    if price <= 0:
        raise ValueError("Price must be positive")
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")
        
    return {
        'product_name': product_name,
        'price': float(price),
        'quantity': int(quantity)
    }

def update_price(product: dict, new_price: float) -> dict:
    """
    Updates the price of a product.
    
    Args:
        product: Product dictionary to modify
        new_price: New price for the product
        
    Returns:
        Updated product dictionary
    """
    if new_price <= 0:
        raise ValueError("Price must be positive")
        
    product['price'] = float(new_price)
    return product

def update_quantity(product: dict, quantity_change: int) -> dict:
    """
    Updates the quantity of a product in stock.
    
    Args:
        product: Product dictionary to modify
        quantity_change: Amount to adjust quantity by (positive to add, negative to subtract)
        
    Returns:
        Updated product dictionary
        
    Raises:
        ValueError: If resulting quantity would be negative
    """
    new_quantity = product['quantity'] + quantity_change
    if new_quantity < 0:
        raise ValueError("Quantity cannot be negative")
        
    product['quantity'] = new_quantity
    return product

# Example usage
if __name__ == "__main__":
    # Create a new product
    laptop = add_product("Laptop", 999.99, 10)
    print("New product:", laptop)
    
    # Update the price
    laptop = update_price(laptop, 899.99)
    print("After price update:", laptop)
    
    # Update the quantity (add 5)
    laptop = update_quantity(laptop, 5)
    print("After adding stock:", laptop)
    
    # Update the quantity (sell 3)
    laptop = update_quantity(laptop, -3)
    print("After selling some:", laptop)
    
    try:
        # This will raise an error
        laptop = update_quantity(laptop, -20)
    except ValueError as e:
        print("Error:", e)
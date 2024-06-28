def main():

    original_price = int(200)
    print(original_price)
    
    rate = int(20)

    # regular = 200
    # rate = 20
    
    discount_amount = int(original_price)*(int(rate)/100) # complete this statement to calcualte the discount amount
    print(discount_amount)
    
    final_price = int(original_price)- int(discount_amount)       # complete this statement to calculate the final price
    print(final_price)

    

   ##################################################
   # Do not delete the return statement
   ##################################################
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    main()
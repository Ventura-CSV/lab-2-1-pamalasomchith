def main():

    original_price = int(input())
    rate = int(input())

    # regular = 200
    # rate = 20
      
    discount_amount = original_price * rate/100 
    final_price = original_price - discount_amount
    
    print(original_price)
    print(discount_amount)
    print(final_price)
   


   ##################################################
   # Do not delete the return statement
   ##################################################
    return original_price, discount_amount, final_price

if __name__ == '__main__':
    main()
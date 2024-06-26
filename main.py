def main():

    original_price = int(input('100'))
    rate = int(input('20'))

    # regular = 100
    # rate = 20

    discount_amount = int(original_price) / int(rate)     # complete this statement to calcualte the discount amount
    
    final_price = int(original_price) - int(discount_amount)       # complete this statement to calculate the final price

    print('original_price')
    print('discount_amount')
    print('final_price')

   ##################################################
   # Do not delete the return statement
   ##################################################
    return original_price, discount_amount, final_price


if __name__ == '__main__':
    main()
def main():

    original_price = int(input('100'))
    rate = int(input('20'))

    # regular = 100
    # rate = 20

    discount_amount = int(original_price) / int(rate)     # complete this statement to calcualte the discount amount
    print(discount_amount)
    
    final_price = int(original_price) - int(discount_amount)       # complete this statement to calculate the final price
    print(final_price)

    print(f'100: {original_price}')
    print(f'20: {discount_amount}')
    print(f'80: {final_price}')

   ##################################################
   # Do not delete the return statement
   ##################################################
    return original_price, discount_amount, final_price


if __name__ == '__main__':
    main()
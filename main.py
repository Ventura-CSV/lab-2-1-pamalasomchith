def main():

    original_price = int(input('Enter the regular price: 100'))
    rate = int(input('Enter the discount rate: 20'))

    # regular = 100
    # rate = 20

    discount_amount = 20     # complete this statement to calcualte the discount amount
    final_price = 80         # complete this statement to calculate the final price

    print(f'Regular Price: {original_price}')
    print(f'Discount Amount: {discount_amount}')
    print(f'Final Price: {final_price}')

   ##################################################
   # Do not delete the return statement
   ##################################################
    return original_price, discount_amount, final_price


if __name__ == '__main__':
    main()

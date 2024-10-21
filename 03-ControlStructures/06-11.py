new_price=140
old_price=200
if new_price/old_price<=0.9:
    print(f'Buy the product!')
    print(f'Product price reduced by {(1-new_price/old_price)*100}')
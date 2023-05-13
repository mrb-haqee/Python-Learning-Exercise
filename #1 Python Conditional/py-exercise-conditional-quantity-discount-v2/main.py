def quantityDiscount(quantity: int, price: int) -> int:
    if quantity >= 10:
        result = (quantity*price)-(quantity*price)*0.2
        return result+result*0.11
    elif quantity >= 5:
        result = (quantity*price)-(quantity*price)*0.15
        return result+result*0.11
    else:
        result = quantity*price
        return result+result*0.11
    return  # TODO: replace this


# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(quantityDiscount(1, 100))
    print(quantityDiscount(3, 100))
    print(quantityDiscount(5, 100))
    print(quantityDiscount(10, 100))
    print(quantityDiscount(15, 3))
    print(quantityDiscount(3, 10000))
    print(quantityDiscount(12, 10000))

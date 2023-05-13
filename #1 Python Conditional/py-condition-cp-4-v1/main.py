def GetTicketPrice(VIP: int, regular: int, student: int, day: int) -> float:
    totalTiket = VIP + regular + student
    totalPrice=VIP*30+regular*20+student*10
    if totalPrice>100:
        if day%2==1:
            if totalTiket<5:
                return totalPrice-totalPrice*0.15
            else:
                return totalPrice-totalPrice*0.25
        else:
            if totalTiket<5:
                return totalPrice-totalPrice*0.1
            else:
                return totalPrice-totalPrice*0.2
    else:
        return totalPrice  # TODO: replace this

print(11%3)
# gunakan untuk melakukan debug
if __name__ == "__main__":
    print(GetTicketPrice(1, 1, 1, 20))

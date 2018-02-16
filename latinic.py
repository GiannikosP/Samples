from collections import OrderedDict

def wlat(num):

    lat = OrderedDict()
    lat[1000] = "M"
    lat[900] = "CM"
    lat[500] = "D"
    lat[400] = "CD"
    lat[100] = "C"
    lat[90] = "XC"
    lat[50] = "L"
    lat[40] = "XL"
    lat[10] = "X"
    lat[9] = "IX"
    lat[5] = "V"
    lat[4] = "IV"
    lat[1] = "I"

    def latnum(num):
        for r in lat.keys():
            x, y = divmod(num, r)
            yield lat[r] * x
            num -= (r * x)
            if num > 0:
                latnum(num)
            else:
                break

    return "".join([a for a in latnum(num)])
	
newnum= int(raw_input("insert a number"))
print wlat(newnum)
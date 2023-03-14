def currency_converter(curency, conv_coef):
    return curency*conv_coef

if __name__=="__main__":
    USD_to_Yuan = 6.85
    Yuan_to_USD = 1/6.85
    USD_to_Yuan1 = [1, 1750, 28000]
    Yuan_to_USD1 = [1,1500,25000]

    #Converting USD to Yuan
    print("\nConvert USD to Yuan:")

    for USD in USD_to_Yuan1:
        USD_converter = currency_converter(USD, USD_to_Yuan)
        print(f"{USD} USD -> {USD_converter} Yuan")

    #Converting USD to Yuan
    print("\nConvert Yuan to USD:")

    for Yuan in Yuan_to_USD1:
        Yuan_converter = currency_converter(Yuan, Yuan_to_USD)
        print(f"{Yuan} Yuan -> {Yuan_converter} USD")
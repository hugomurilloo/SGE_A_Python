nomsalari = 55000

if nomsalari < 15000:
    print(f"0% d'IVA = {nomsalari} ")
elif 15000 <= nomsalari < 30000:
    print(f"10% d'IVA = {nomsalari*10/100}")
elif 30000 <= nomsalari < 60000:
    print(f"21% d'IVA = {nomsalari*21/100}")

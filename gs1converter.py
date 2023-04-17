import sys

def convert_ean_to_gs1(ean):
    if len(ean) != 13:
        print("Ungültige EAN: Muss 13-stellig sein.")
        return

    company_prefix = ean[:3]
    item_reference = ean[3:9]
    check_digit = ean[-1]

    ai = "01"
    gs1 = f"({ai}{company_prefix}{ai}{item_reference}{ai}{check_digit})"

    print(f"GS1-128-Barcode: {gs1}")

if __name__ == "__main__":
    ean = input("Geben Sie die EAN-13-Nummer ein: ")
    convert_ean_to_gs1(ean)

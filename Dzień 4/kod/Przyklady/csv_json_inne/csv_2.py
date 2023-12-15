import csv


def get_miasto(adres):
    lst_adres = adres.split(",")
    miasto = lst_adres[1]
    miasto = miasto[7:]

    return miasto


def get_mail(mail):
    adres_mail = mail.split("@")[1]
    return adres_mail


def odczyt_csv(filename):
    dane_csv = []
    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f, delimiter=';')
        dane_csv = [row for row in reader]
    return (dane_csv)


def zapis_csv(filename, dane_csv):
    with open(filename, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(dane_csv)


def modyfi_csv(dane_csv):
    dane_out = []
    for row in dane_csv:
        lst_row = ["", "", "", ""]
        lst_row[0], lst_row[1] = row[0], row[1]
        lst_row[2], lst_row[3] = get_miasto(row[4]), get_mail(row[8])
        dane_out.append(lst_row)
    return dane_out


dane = odczyt_csv('d:\\dane\\dane_test.csv')
dane = modyfi_csv(dane)
zapis_csv('d:\\dane\\dane_out.csv', dane)

def yearToCentury(year): 

    str_year = str(year)  # Yılı stringe çevir

    if len(str_year) < 3:  # İki basamaklı yıllar (1-99)
        return 1
    elif len(str_year) == 3:  # Üç basamaklı yıllar (100-999)
        if str_year[1:3] == "00":  # 100, 200, 300 gibi tam yüzler
            return int(str_year[0])
        else:  # 101, 150, 250 gibi yıllar
            return int(str_year[0]) + 1
    else:  # Dört basamaklı yıllar (1000 ve sonrası)
        if str_year[2:4] == "00":  # 1000, 2000 gibi tam yüzler
            return int(str_year[:2])
        else:  # 1001, 1508 gibi yıllar
            return int(str_year[:2]) + 1


# Test örneği
result = yearToCentury(2024)
print(result)  # Çıktı: 15

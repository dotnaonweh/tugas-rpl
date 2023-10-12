def checkNomor(noHp):
    if noHp[0:2] == '08' or noHp[0:2] == '62':
        if len(str(noHp)) == 11 or len(str(noHp)) == 12:
            return True
    return False

def checkPulsa(punyaPulsa, butuhPulsa):
    if punyaPulsa >= butuhPulsa:
        return True
    else:
        return False

def transferPulsa(userPulsa):
    print("Silahkan masukkan nomor tujuan Transfer Pulsa:\n(contoh: 08xxxx atau 628xxxx)")
    noHp = str(input("> "))

    if not checkNomor(noHp):
        print("Nomor yang kamu masukan invalid silahkan menggunakan format: 08xxxx atau 628xxxx")
        exit()

    print("Silahkan masukkan jumlah pulsa yang akan\nditransfer : (min 5000, max 1jt & tanpa. (titik)\natau, (koma))")
    nominalPulsa = int(input("> "))
    if nominalPulsa < 5000:
        print("Jumlah pulsa yang Anda masukkan kurang dari Rp5000")
        exit()

    print(f"Hati2 penipuan. Anda akan Transfer\nPulsa {nominalPulsa} ke nomor{noHp}?\n(Biaya 1850 & 1 Poin undian TP\niPhone14)\n1. Ya\n0. Kembali ke menu")
    confirm = int(input("> "))
    if confirm == 1:
        if not checkPulsa(userPulsa, nominalPulsa):
            print("Maaf, pulsa Anda tidak mencukupi untuk melakukan transfer pulsa.")
            exit()
        userPulsa = userPulsa - nominalPulsa
        print("Terima kasih permintaan Anda sedang diproses.")
    elif confirm == 0:
        main()
    else:
        print("Maaf, input Anda salah. Silahkan coba lagi.")
        exit()

def mintaPulsa():
    print("Silahkan masukkan nomor tujuan Minta Pulsa:\n(contoh: 08xxxx atau 628xxxx)")
    noHp = str(input("> "))
    if checkNomor(noHp):
        print("Silahkan masukkan jumlah pulsa yang akan\ndiminta : (min 5000, max 1jt & tanpa. (titik) atau , (koma))")
        jumlahPulsa = int(input("> "))
        if 5000 <= jumlahPulsa <= 1000000:
            print(f"Anda akan meminta pulsa: {jumlahPulsa} ke nomor {noHp}? (biaya 100)\n1. Ya\n2. Back\n0. Home")
            validateTransfer = int(input("> "))
            if validateTransfer == 1:
                print("Terima kasih permintaan Anda sedang diproses\nSampaikan pd JIWA YANG BERSEDIH! Lagu viral dr Ghea Indrawari di LangitMusik Midium RP4400/3hr. Mau?\n1. Ya\n2. Tidak")
                validateIklan = int(input("> "))
                if validateIklan == 1:
                    print("Terima kasih permintaan Anda sedang di proses")
                    exit()
                elif validateIklan == 2:
                    print("Terima kasih.")
            elif validateTransfer == 2:
                mintaPulsa()
            else:
                main()
        else:
            print("Maaf nominal yang Anda masukan tidak sesuai.\nmin 5000, max 1jt & tanpa . (titik) atau , (koma)")
            exit()
    else:
        print("Nomor yang anda masukkan tidak valid\n(contoh: 08xxxx atau 628xxxx)")
        exit()

def autoTp(userPulsa,userInputList):
    print("Silahkan masukkan nomor tujuan yang anda Auto Transfer Pulsa:")
    nomorTujuan = input("> ")

    if not checkNomor(nomorTujuan):
        print("nomor yang kamu masukan invalid silahkan menggunakan format: 08xxxx atau 628xxxx")
        exit()

    print("Masukkan jumlah pulsa minimal 5000: ")
    jumlahPulsa = int(input("> "))
    tanggalTransfer = input("Masukkan tanggal transfer: ")

    print(f"Hati2 penipuan. Anda akan Transfer\nPulsa {jumlahPulsa} ke nomor{nomorTujuan}?\n(Biaya 1850 & 1 Poin undian TP\niPhone14)\n1. Ya\n0. Menu")
    validateTransfer = int(input("> "))
    if validateTransfer == 1:
        print("Terima kasih permintaan Anda sedang diproses.")

        if not checkPulsa(userPulsa, jumlahPulsa):
            print("SMS: pulsa anda tidak mencukupi")
        else:
            userInputList[nomorTujuan] = tanggalTransfer

        print("Sampaikan pd JIWA BERSEDIH! Lagu viral dr Ghea Indrawari di LangitMusik Midium Rp4400/3hr. Mau?\n1. Ya\n2. Tidak")
        validateIklan = int(input("> "))
        if validateIklan == 1:
            print("Terima kasih permintaan Anda sedang diproses.")
        else:
            print("Terima kasih.")
    else:
        autoTp()

def deleteAutoTp(listNoAutoTp):
    print("Silahkan masukkan nomor tujuan yg akan\ndihapus dari list Auto Transfer Pulsa:")
    hapusDariList = input("> ")
    listNoAutoTp.remove(hapusDariList)
    print(f"Anda akan menghapus nomor '{hapusDariList}' dari daftar Auto TP anda?\n1. Ya\n0. Home")
    confirm = int(input("> "))
    if confirm == 1:
        print(f"nomor '{hapusDariList}' telah di hapus")
    elif confirm == 0:
        main()
    else:
        exit()

def listAutoTp():
    print("Terima kasih permintaan Anda sedang diproses.\nSampaikan pd JIWA BERSEDIH! Lagu viral\ndr Ghea Indrawari di LangitMusik Midium\nRp4400/3hr. Mau?\n1. Ya\n2. Tidak")
    inputlistAutoTp = int(input("> "))
    if inputlistAutoTp == 1:
        print("Terima kasih permintaan Anda sedang di proses")
    else:
        print("Terima kasih.")

def cekKuponTp():
    print("Jumlah kupon Anda adalah: 0 Kupon")

def main():
    inputLayanan = input("> ")
    if inputLayanan == "*858#":
        print("\nMau Samsung Fold 4 dr Aldi Taher?\nHub di *500*352#\n1. Transfer Pulsa\n2. Minta Pulsa\n3. Auto TP\n4. Delete Auto TP\n5. List Auto TP\n6. Cek Kupon Undian TP\n")
        choose = int(input("> "))
        if choose == 1:
            transferPulsa(userPulsa)
        elif choose == 2:
            mintaPulsa()
        elif choose == 3:
            autoTp(userPulsa,userInputList)
        elif choose == 4:
            deleteAutoTp(listNoAutoTp)
        elif choose == 5:
            listAutoTp()
        elif choose == 6:
            cekKuponTp()
        else:
            print("Angka yang anda masukan salah!")
            main()
    else:
        print("Layanan Tidak Tersedia")

if __name__ == "__main__":
    listNoAutoTp = ['081316555666']
    userInputList = {}
    userPulsa = 50000
    main()

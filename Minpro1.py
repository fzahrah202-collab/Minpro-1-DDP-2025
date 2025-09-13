#sistem manajemen jasa penitipan hewam

print("===Data penitipan Hewan===")

#input data hewan yang dititipkan
nama1 = input("Masukkan nama hewan peliharaan anda   : ")
jenis1 = input("Masukkan jenis hewan peliharaan anda : ")
lama1 = input("Masukkan lama penitipan (hari)        : ")


pilihan = input("Mau masukkan data lagi? (ya/tidak)  : ")

if pilihan == "ya" :

    #input data ke 2
    nama2 = input("Masukkan nama hewan peliharaan anda   : ")
    jenis2 = input("Masukkan jenis hewan peliharaan anda : ")
    lama2 = input("Masukkan lama penitipan (hari)        : ")

    pilihan = input("Mau masukkan data lagi? (ya/tidak)  : ")

    if pilihan == "ya" :

        #input data ke 3
        nama3 = input("Masukkan nama hewan peliharaan anda   : ")
        jenis3 = input("Masukkan jenis hewan peliharaan anda : ")
        lama3 = input("Masukkan lama penitipan (hari)        : ")

        #output data ke 3
        print("\ninput selesai data penuh (maksimal 3 hewan)")
        print("===Daftar hewan yang dititipkan===")
        print("1. Nama : ", nama1, "Jenis : ", jenis1, "lama : ",lama1 )
        print("2. Nama : ", nama2, "Jenis : ", jenis2, "lama : ",lama2 )
        print("3. Nama : ", nama3, "Jenis : ", jenis3, "lama : ",lama3 )
        print("\nTerimakasih! hewan kesayanganmu siap kami rawat dengan penuh cinta🐶🐱🐰")

    else :
        
        #output data ke 2
        print("\ninput selesai, ada 2 hewan!")
        print("===Daftar hewan yang dititipkan===")
        print("1. Nama : ", nama1, "Jenis : ", jenis1, "lama : ",lama1 )
        print("2. Nama : ", nama2, "Jenis : ", jenis2, "lama : ",lama2 )
        print("\nTerimakasih! hewan kesayanganmu siap kami rawat dengan penuh cinta🐶🐱🐰")

else :

    #output data ke 1
    print("\ninput selesai, ada 1 hewan!")
    print("===Daftar hewan yang dititipkan===")
    print("1. Nama : ", nama1, "Jenis : ", jenis1, "lama : ",lama1 )
    print("\nTerimakasih! hewan kesayanganmu siap kami rawat dengan penuh cinta🐶🐱🐰")


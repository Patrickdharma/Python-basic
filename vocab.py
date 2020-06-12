import random
mulai = input("apakah anda ingin menggunakan Program Penghapal Vocab?(y/n)= ")
while mulai =="y":
    vocab = []
    print("          SELAMAT DATANG DI PROGRAM PENGHAPAL VOCAB             ")
    print("===============================================================")
    print("          tulis daftar vocab sebanyak yang anda mau"           )
    print("  tekan '.'(titik) pada input vocab indo untuk mengakhiri list dan mulai menghapal!!" )
    print("===============================================================")
    print("tekan 1 untuk mode set ")
    print("tekan 2 untuk mode manual dengan kunci")
    print("tekan 3 untuk mode manual tanpa kunci")
    milih = int(input("silahkan pilih mode= "))
    listsoal = []
#============PILIHAN 3======================================================================================
    if milih == 3:
        while True:
            soalsoal = input("silahkan masukkan vocab= ")
            listsoal.append(soalsoal)
            if soalsoal == ".":
                listsoal.remove(".")
                random.shuffle(listsoal)
                print("LIST VOCAB")
                for a in listsoal:
                    input(f"{listsoal.index(a)+1}) {a}=  ")
                nanya = input("apakah anda masih ingin menambah list(y/n)= ")
                if nanya ==  "y":
                    continue
                elif nanya == "n":
                    nanya2 = input("apakah anda ingin ke menu utama?(y/n)= ")
                    if nanya2 == "y":
                        break
                    if nanya2 == "n":
                        print("terimakasih!")
                        mulai = "n"
                        break
                        
            
#============PILIHAN 2======================================================================================
    pertanyaan = {}
    kumpulan_salah = {}
    if milih == 2:
        while True:
            indo = input("silahkan masukkan vocab indo= ")
            jepang = input("silahkan masukkan vocab jepang= ")
            pertanyaan[indo]=jepang
            pert = list(pertanyaan.keys())
            benar = 0
            salah = 0
            rev_benar = 0
            rev_salah = 0
            if indo == ".":
                pert.remove(".")
                print("LIST VOCAB")
                random.shuffle(pert)
                for x in pert:
        #pake .index() buat bikin nomor 
                    answir = input(f"{pert.index(x)+1}) {x}    =  ")
                    if answir == pertanyaan[x]:
                        print("="*25)
                        print("CORRECT")
                        print(f"jawabannya adalah {pertanyaan[x]}")
                        benar += 1 
                        print (f"{benar} benar : {salah} salah")
                        print("="*25)
                    else:
                        kumpulan_salah[x]=pertanyaan[x] 
                        print("="*25)
                        print("eeeitsss salaaahhh!")
                        print(f"jawabannya adalah {pertanyaan[x]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")

                kump_salah = list(kumpulan_salah.keys())
                asking = input("apakah anda ingin memperbaiki yang salah?(y/n) ")
                if asking == "y":
                    print("berikut adalah list perbaikan")
                    for kump in kump_salah:
                        answir = input(f"{kump_salah.index(kump)+1}) {kump} = ")
                        if answir == kumpulan_salah[kump]:
                            print("="*25)
                            print("CORRECT!")
                            print(f"jawabannya adalah {kumpulan_salah[kump]}")
                            rev_benar += 1
                            print(f"{rev_benar} benar : {rev_salah} salah")
                            print("="*25)
                        else:
                            print("="*25)
                            print("eeeitsss salaaahhh!")
                            print(f"jawabannya adalah {kumpulan_salah[kump]}")
                            rev_salah += 1
                            print(f"{rev_benar} benar : {rev_salah} salah")
                            print("="*25)
                

                ulang = input("apakah anda ingin menambah list?(y/n)= ")
                if ulang == "y":
                    continue
                elif ulang == "n":
                    nanya2 = input("apakah anda ingin ke menu utama?(y/n)= ")
                    if nanya2 == "y":
                        break
                    elif nanya2 == "n":
                        print("terimakasih!")
                        mulai = "n"
                        break

                        


#============PILIHAN 3======================================================================================

    bab1 = ["saya","kami,kita","anda,saudara,tuan","orang itu","anda sekalian","sdr-","guru/dosen(untuk pekerjaan sendiri)","guru/dosen(untuk kalangan sendiri)","mahasiswa","pegawai perusahaan","pegawai bank","dokter","peneliti","insinyur","universitas","rumah sakit","listrik","lampu","siapa","umur-tahun","siapa nama anda"]

    bab15 = {"berdiri" : "たちます","duduk" : "すわります","memakai":"つかいます","menaruh":"おきます","membuat": "つくります","menjual":"うります","mengetahui":"しります","tinggal":"すみます","meneliti":"けんきゅうします","data/bahan":"しりょう","jadwal":"じこくひょう","pakaian":"ふく","barang jadi,komoditi":"せいひん","jurusan,keahlian":"せんもん","dokter gigi":"はいしゃ","tukang pangkas rambut":"とこや","bujangan":"どくしん","terutama,teristimewa":"とくに","teringat":"おもいだします","keluarga(orang lain)":"ごかぞく","ada(bentuk sopan)":"いらっしゃいます","SMU":"こうこう"}
    bab15_rev = {}
    bab16 = {"naik(kereta api)":"のります","turun(kereta api)":"おります","ganti kendaraan":"のりかえます","memasukkan":"いれます","mengeluarkan,mengajukan":"だします","masuk(universitas)":"はいります","menamatkan(universitas)":"でます","meninggalkan(perusahaan)":"やめます","menekan":"おします","muda":"わかい","panjang":"ながい","pendek":"みじかい","terang":"あかるい","gelap":"くらい","tinggi(badan)":"せがたかい","pintar,pandai":"あたまがいい","badan":"からだ","kepala":"あたま","rambut":"かみ","muka,wajah":"かお","mata":"め","telinga":"みみ","mulut":"くち","gigi":"は","perut":"おなか","kaki":"あし","pelayanan":"サービス","joging":"ジョギング","hijau,tumbuhan hijau":"みどり","kuil,wihara(Buddha)":"おてら","tempat keramat(shinto)":"じんじゃ","mahasiswa asing":"りゅうがくせい","nomor-":"ーばん","dengan cara bagaimana":"どうやって"}
    bab16_rev = {}
    bab17 = {"mengingat,menghapal":"おぼえます","lupa":"わすれます","hilang":"なくします","menyerahkan":"だします","membayar":"はらいます","mengembalikan":"かえします","pergi keluar, berangkat keluar":"でかけます","membuka(pakaian,sepatu)":"ぬぎます","membawa(pergi)(dipakai untuk barang)":"もっていきます","membawa(datang)(dipakai untuk barang)":"もってきます","cemas":"しんぱいします","lembur(kerja)":"ざんぎょうします","dinas keluar kota":"しゅっちょうします","minum [obat]":"のみます","masuk[ofuro]":"はいります","penting,berharga":"たいせつ","tidak apa apa":"だいじょうぶ","berbahaya":"あぶない","pertanyaan,masalah":"もんだい","jawaban":"こたえ","larangan merokok":"きねん","kartu asuransi":"ほけんしょう","masuk angin,pilek":"かぜ","panas badan":"ねつ","penyakit":"びょうき","obat":"くすり","kamar mandi":"おふろ","jaket":"うわぎ","pakaian dalam":"したぎ","dokter":"せんせい","oleh karena itu":"ですから"}
    bab17_rev = {}
    kanji3 = {"hundred":"hyaku","ensiklopedia":"hakkajiten","thousand":"sen","prefektur chiba":"chibaken","10.000":"man","all nation":"bankoku","fountain pen":"mannenhitsu","lingkaran":"maru","strong yen":"endaka","year":"toshi","next year":"rainen","pension":"nenkin","above":"ue","go up":"agaru","water skii":"aijousukii","bawah":"shita","to go down":"sagaru","up&down":"jouge","middle":"naka","all day long":"ichinichijuu","junior high":"chuugaku","center":"chuushin","half":"han","half a year":"hantoshi","half":"hanbun","half a day":"hannichi","to divide":"wakeru","understand":"wakaru","10 minute":"juppun","enough":"juubun"}
    kanji3_rev = {}
    kanji4 = {"japanese" : "nihonjin","girls":"joshi","woman":"josei","anak kecil":"kodomo","kondisi":"choushi","man and woman":"danjo","eldest son":"chounan","man":"dansei","eye":"me","the first day":"ichinichime","obat mata": "megusuri","purpose": "mokuteki","mouth":"kuchi","entrance" : "iriguchi","population" : "jinkou","ear" : "mimi","hand" :  "te","skillfull" : "jouzu","unskillfull" : "heta","letter" : "tegami","legs": "ashi","a pair" : "itsusoku","enough" : "tariru","tamasya" : "ensoku","power" : "chikara","water power" : "suiryoku","physical strenght" :  "tairyoku"}
    kanji4_rev = {}
    kanji5 = {"ayah":"chichi","ibu":"haha","parents":"fubo","mother country":"bokoku","last month":"sengetsu","senior":"senpai","lahir":"umaremasu","hidup":"ikimasu","guru":"sensei","kehidupan":"seikatsu","student":"gakusei","university":"daigaku","science":"kagaku","international student":"ryuugakusei","sekolah":"gakkou","kepsek":"kouchou","sekolah dasar":"syuugakkou","almamater":"bokou","SMA":"koukou","friend":"tomodachi","best friend":"shinyuu","book":"hon","toko buku":"honya","every":"mai","everyday":"mainichi","every month":"maitsuki","what":"nan","what month":"nangatsu"}
    kanji5_rev = {}


    if milih == 1:
        while True:
            print("SELAMAT DATANG DI TES VOCAB PER BAB")
            print("silahkan tekan 1 untuk bab 1 ")
            print("tekan 2 untuk bab 2 ")
            print("tekan K1 untuk vocab kanji bab 1")
            print("dan seterusnya!")

            pilihan = input("silahkan masukkan pilihan anda= ")
            benar = 0
            salah = 0
            benar_rev = 0
            salah_rev = 0

            if pilihan == "1":
                random.shuffle(bab1)
                for a in bab1:
                    input(f"{bab1.index(a)+1}){a}    = ")


            elif pilihan == "15":
                soal = list(bab15.keys())
                random.shuffle(soal)
                for a in soal:
                    jawaban = input(f"{soal.index(a)+1}){a}= ")
                    if jawaban == (bab15[a]):
                        print("="*25)
                        print("CORRECT")
                        print(f"jawabannya adalah {bab15[a]}")
                        benar += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                    else:
                        bab15_rev[a]=bab15[a]
                        print("="*25)
                        print("eeeitsss salaahhhh")
                        print(f"jawabannya adalah {bab15[a]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")
                askwing = input("apakah anda ingin merevisi kesalahan\" anda?(y/n)=")

                if askwing == "y":
                    perbaikan = list(bab15_rev.keys())
                    random.shuffle(perbaikan)
                    for a in perbaikan:
                        answir = input(f"{perbaikan.index(a)+1}){a}= ")
                        if answir == (bab15_rev[a]):
                            print("="*25)
                            print("CORRECT")
                            print(f"jawabannya adalah {bab15_rev[a]}")
                            benar_rev += 1
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                        else:
                            print("="*25)
                            print("eeitsss salahhhhhh")
                            print(f"jawabannya adalah {bab15_rev[a]}")
                            salah_rev += 1 
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                    print(f"nilai remedial kamu adalah {(benar_rev/(benar_rev+salah_rev))*100:.1f}")
                elif askwing == "n":
                    print("okeeee")

            elif pilihan == "16":
                soal = list(bab16.keys())
                random.shuffle(soal)
                for a in soal:
                    jawaban = input(f"{soal.index(a)+1}){a}= ")
                    if jawaban == (bab16[a]):
                        print("="*25)
                        print("CORRECT")
                        print(f"jawabannya adalah {bab16[a]}")
                        benar += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                    else:
                        bab16_rev[a]=bab16[a]
                        print("="*25)
                        print("eeeitsss salaahhhh")
                        print(f"jawabannya adalah {bab16[a]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")
                askwing = input("apakah anda ingin merevisi kesalahan\" anda?(y/n)=")

                if askwing == "y":
                    perbaikan = list(bab16_rev.keys())
                    random.shuffle(perbaikan)
                    for a in perbaikan:
                        answir = input(f"{perbaikan.index(a)+1}){a}= ")
                        if answir == (bab16_rev[a]):
                            print("="*25)
                            print("CORRECT")
                            print(f"jawabannya adalah {bab16_rev[a]}")
                            benar_rev += 1
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                        else:
                            print("="*25)
                            print("eeitsss salahhhhhh")
                            print(f"jawabannya adalah {bab16_rev[a]}")
                            salah_rev += 1 
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                    print(f"nilai remedial kamu adalah {(benar_rev/(benar_rev+salah_rev))*100:.1f}")
                elif askwing == "n":
                    print("okeeee")

            elif pilihan == "k3":
                soal = list(kanji3.keys())
                random.shuffle(soal)
                for a in soal:
                    jawaban = input(f"{soal.index(a)+1}){a}= ")
                    if jawaban == (kanji3[a]):
                        print("="*25)
                        print("CORRECT")
                        print(f"jawabannya adalah {kanji3[a]}")
                        benar += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                    else:
                        kanji3_rev[a]=kanji3[a]
                        print("="*25)
                        print("eeeitsss salaahhhh")
                        print(f"jawabannya adalah {kanji3[a]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")
                askwing = input("apakah anda ingin merevisi kesalahan\" anda?(y/n)=")

                if askwing == "y":
                    perbaikan = list(kanji3_rev.keys())
                    random.shuffle(perbaikan)
                    for a in perbaikan:
                        answir = input(f"{perbaikan.index(a)+1}){a}= ")
                        if answir == (kanji3_rev[a]):
                            print("="*25)
                            print("CORRECT")
                            print(f"jawabannya adalah {kanji3_rev[a]}")
                            benar_rev += 1
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                        else:
                            print("="*25)
                            print("eeitsss salahhhhhh")
                            print(f"jawabannya adalah {kanji3_rev[a]}")
                            salah_rev += 1 
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                    print(f"nilai remedial kamu adalah {(benar_rev/(benar_rev+salah_rev))*100:.1f}")
                elif askwing == "n":
                    print("okeeee")







            elif pilihan == "k4":
                soal = list(kanji4.keys())
                random.shuffle(soal)
                for a in soal:
                    jawaban = input(f"{soal.index(a)+1}){a}= ")
                    if jawaban == (kanji4[a]):
                        print("="*25)
                        print("CORRECT")
                        print(f"jawabannya adalah {kanji4[a]}")
                        benar += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                    else:
                        kanji4_rev[a]=kanji4[a]
                        print("="*25)
                        print("eeeitsss salaahhhh")
                        print(f"jawabannya adalah {kanji4[a]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")
                askwing = input("apakah anda ingin merevisi kesalahan\" anda?(y/n)=")

                if askwing == "y":
                    perbaikan = list(kanji4_rev.keys())
                    random.shuffle(perbaikan)
                    for a in perbaikan:
                        answir = input(f"{perbaikan.index(a)+1}){a}= ")
                        if answir == (kanji4_rev[a]):
                            print("="*25)
                            print("CORRECT")
                            print(f"jawabannya adalah {kanji4_rev[a]}")
                            benar_rev += 1
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                        else:
                            print("="*25)
                            print("eeitsss salahhhhhh")
                            print(f"jawabannya adalah {kanji4_rev[a]}")
                            salah_rev += 1 
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                    print(f"nilai remedial kamu adalah {(benar_rev/(benar_rev+salah_rev))*100:.1f}")
                elif askwing == "n":
                    print("okeeee")




            elif pilihan == "k5":
                soal = list(kanji5.keys())
                random.shuffle(soal)
                for a in soal:
                    jawaban = input(f"{soal.index(a)+1}){a}= ")
                    if jawaban == (kanji5[a]):
                        print("="*25)
                        print("CORRECT")
                        print(f"jawabannya adalah {kanji5[a]}")
                        benar += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                    else:
                        kanji5_rev[a]=kanji5[a]
                        print("="*25)
                        print("eeeitsss salaahhhh")
                        print(f"jawabannya adalah {kanji5[a]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")
                askwing = input("apakah anda ingin merevisi kesalahan\" anda?(y/n)=")

                if askwing == "y":
                    perbaikan = list(kanji5_rev.keys())
                    random.shuffle(perbaikan)
                    for a in perbaikan:
                        answir = input(f"{perbaikan.index(a)+1}){a}= ")
                        if answir == (kanji5_rev[a]):
                            print("="*25)
                            print("CORRECT")
                            print(f"jawabannya adalah {kanji5_rev[a]}")
                            benar_rev += 1
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                        else:
                            print("="*25)
                            print("eeitsss salahhhhhh")
                            print(f"jawabannya adalah {kanji5_rev[a]}")
                            salah_rev += 1 
                            print(f"{benar_rev} benar : {salah_rev} salah")
                            print("="*25)
                    print(f"nilai remedial kamu adalah {(benar_rev/(benar_rev+salah_rev))*100:.1f}")
                elif askwing == "n":
                    print("okeeee")


            bertanya = input("apakah anda masih ingin mengulang?(y/n)= ")
            if bertanya == "y":
                continue
            elif bertanya == "n":
                nanya2 = input("apakah anda ingin ke menu utama?(y/n)= ")
                if nanya2 == "y":
                    break
                if nanya2 == "n":
                    mulai = "n"
                    print("terimakasih!")
                    break


                    

import random
while True:
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
                        False
                        
            

    pertanyaan = {}
    if milih == 2:
        while True:
            indo = input("silahkan masukkan vocab indo= ")
            jepang = input("silahkan masukkan vocab jepang= ")
            pertanyaan[indo]=jepang
            pert = list(pertanyaan.keys())
            benar = 0
            salah = 0
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
                        print("="*25)
                        print("eeeitsss salaaahhh!")
                        print(f"jawabannya adalah {pertanyaan[x]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)


                ulang = input("apakah anda ingin menambah list?(y/n)= ")
                if ulang == "y":
                    continue
                elif nanya == "n":
                    nanya2 = input("apakah anda ingin ke menu utama?(y/n)= ")
                    if nanya2 == "y":
                        break
                    if nanya2 == "n":
                        print("terimakasih!")
                        False

    bab1 = ["saya","kami,kita","anda,saudara,tuan","orang itu","anda sekalian","sdr-","guru/dosen(untuk pekerjaan sendiri)","guru/dosen(untuk kalangan sendiri)","mahasiswa","pegawai perusahaan","pegawai bank","dokter","peneliti","insinyur","universitas","rumah sakit","listrik","lampu","siapa","umur-tahun","siapa nama anda"]
    bab15 = {"berdiri" : "tachimasu","duduk" : "suwarimasu","memakai":"tsukaimasu","menaruh":"okimasu","membuat": "tsukurimasu","menjual":"urimasu","mengetahui":"shirimasu","tinggal":"sumimasu","meneliti":"kenkyuushimasu","data/bahan":"shiryou","jadwal":"jikokuhyou","pakaian":"fuku","barang jadi,komoditi":"seihin","jurusan,keahlian":"senmon","dokter gigi":"haisha","tukang pangkas rambut":"tokoya","bujangan":"dokushin","terutama,teristimewa":"tokuni","teringat":"omoidashimasu","keluarga(orang lain)":"gokazoku","ada(bentuk sopan)":"irasshaimasu","SMU":"koko"}
    kanji3 = {"hundred":"hyaku","ensiklopedia":"hyakkajiten","thousand":"sen","prefektur chiba":"chibaken","10.000":"man","all nation":"bankoku","fountain pen":"mannenhitsu","lingkaran":"maru","strong yen":"endaka","year":"toshi","next year":"rainen","pension":"nenkin","above":"ue","go up":"agaru","water skii":"aijousukii","bawah":"shita","to go down":"sagaru","up&down":"jouge","middle":"naka","all day long":"ichinichijuu","junior high":"chuugaku","center":"chuushin","half":"han","half a year":"hantoshi","half":"hanbun","half a day":"hannichi","to divide":"wakeru","understand":"wakaru","10 minute":"juppun","enough":"juubun"}
    kanji4 = {"japanese" : "nihonjin","girls":"joshi","woman":"josei","anak kecil":"kodomo","kondisi":"choushi","man and woman":"danjo","eldest son":"chounan","man":"dansei","eye":"me","the first day":"ichinichime","obat mata": "megusuri","purpose": "mokuteki","mouth":"kuchi","entrance" : "iriguchi","population" : "jinkou","ear" : "mimi","hand" :  "te","skillfull" : "jouzu","unskillfull" : "heta","letter" : "tegami","legs": "ashi","a pair" : "itsusoku","enough" : "tariru","tamasya" : "ensoku","power" : "chikara","water power" : "suiryoku","physical strenght" :  "tairyoku"}
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
                        print("="*25)
                        print("eeeitsss salaahhhh")
                        print(f"jawabannya adalah {bab15[a]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")

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
                        print("="*25)
                        print("eeeitsss salaahhhh")
                        print(f"jawabannya adalah {kanji3[a]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")

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
                        print("="*25)
                        print("eeeitsss salaahhhh")
                        print(f"jawabannya adalah {kanji4[a]}")
                        salah += 1
                        print(f"{benar} benar : {salah} salah")
                        print("="*25)
                print(f"nilai kamu adalah {(benar/(benar+salah))*100:.1f}")            
                        

            bertanya = input("apakah anda masih ingin mengulang?(y/n)= ")
            if bertanya == "y":
                continue
            elif bertanya == "n":
                nanya2 = input("apakah anda ingin ke menu utama?(y/n)= ")
                if nanya2 == "y":
                    break
                if nanya2 == "n":
                    print("terimakasih!")
                    False

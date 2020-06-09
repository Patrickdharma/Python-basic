
vocab = {}
while True:
    vocab_indo = input("masukkan vocab indo ")
    vocab_jepang = input("masukkan vocab jepang ")
    vocab[vocab_indo] = vocab_jepang
    nanya = input("mau nambah vocab?(y/n) = ")
    if nanya == "y":
        continue
    else:
        soal = list(vocab.values())
        for x in soal:
            print(soal.format(x))
            
        break



    
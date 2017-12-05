#Eliisa Raal
#Kypsisetort

laius = int(input("Palun sisestage, mitu küpsist mahub kandikule laiuses: "))

pikkus = int(input("Palun sisestage, mite küpsist mahub kandikule pikkuses: "))

kihid = int(input("Palun sisestage küpsisetordi kihtide arv: "))

küpsised = int(input("Palun sisestage, mitu küpsist on ühes pakis: "))


küpsisepakk = round((laius * pikkus * kihid) / küpsised)

print("Sellise tordi tegemiseks tuleb osta " , küpsisepakk , "küpsisepakki. Mõnusat maiustamist!")

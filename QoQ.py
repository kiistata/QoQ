from random import shuffle, randint
import sys

def b():
    global tear, ruby, VP, ratta, B
    if input("Kas sa olid kõige kaugemal? (y/n) KAugus: " +str(s)).strip()=="y":
        B()
    if summeeri("m"):
        print("Musti on",summeeri("m"))
        ra=int(input("Kas sa saad? (0,1,2)"))
        if ra>0:
            if input("Kas ratta? (y/n)").strip()=="y":
                ratta()
                ruby+=2
            else:
                tear+=1
        if ra==2:
            ruby+=1
    
    ruby+=sum([1 for i in board[-2:] if i[0]=="r"])

    l=summeeri("l")
    if l==1:
        VP+=1
    if l==2:
        VP+=1
        ruby+=1
    if l>=3:
        VP+=2
        if input("Kas ratta? (y/n)").strip()=="y":
            ratta()
            ruby+=2
        else:
            tear+=1
    
    if laud[s][-1]=="r":
        ruby+=1
    if summeeri("v")>7 and input("Läksi lõhki. Kas punktid (y/n)?").strip()=="y":
        VP+=int(laud[s].split()[1])
        print("Veel peab rubiine kulutama, siis resa.")
        print("Rubiine:",ruby)
    elif summeeri("v")>7:
        print("Veel peab ostma ja ruppi kulutama, siis resa.")
        print("Raha:",laud[s].split()[0],"  Ruppi:",ruby)
    else:
        VP+=int(laud[s].split()[1])
        print("Veel peab ostma ja ruppi kulutama, siis resa.")
        print("Raha:",laud[s].split()[0],"  Ruppi:",ruby)
def t():
    global ruby, tear
    ruby-=2
    tear+=1
rada=0
def ratta():
    global ruby, VP,a, rada
    ruby-=2
    rada+=1
    if rada==1:
        ruby+=1
    if rada==2:
        VP+=1
    if rada==3:
        a("s1")
    if rada==4:
        VP+=2
    if rada==5:
        a("m1")
    if rada==6:
        VP+=2
    if rada==7:
        a("p2")
    if rada==8:
        VP+=3
    if rada==9:
        a("l1")
    if rada==10:
        VP+=3
    if rada==11:
        a("k4")
    if rada==12:
        VP+=4
        print("See oli viimane, rohkem ei tasu.")
def B():
    ra=randint(0,5)
    l=["1VP","1VP","2VP","tear+1","o1","r"]
    print("Said "+l[ra])
    global VP, tear, sack, ruby, a
    if ra<2:
        VP+=1
    elif ra==2:
        VP+=2
    elif ra==3:
        tear+=1
    elif ra==4:
        a("o1")
    else:
        ruby+=1
def vaata():
    print("Kotis:",sorted(sack))
def pikk(x):
    global s
    print("Sisesta see, mida sa tahad v enter\nValik:",sack[:x])
    
    v=input().strip()
    if v!="":
        sack.remove(v)
        board.append(v)
        s+=int(board[-1][1])
        vaata()
        behaviour[board[-1][0]](int(board[-1][1]))

def redb(x):
    global s
    ot=summeeri("o")
    if ot>=3:
        s+=2
    elif ot>0:
        s+=1
def goldb(x):
    if len(board)>1 and board[-2][0]=="v":
        sack.append(board.pop(-2))
behaviour={}
behaviour["p"]=redb
behaviour["k"]=goldb

behaviour["v"]=lambda x: print("\nPLAHVATUS!" if summeeri("v")>7 else "")
behaviour["r"]=lambda x: 1
behaviour["o"]=lambda x: 1
behaviour["l"]=lambda x: 1
behaviour["m"]=lambda x: 1
behaviour["s"]=pikk
def summeeri(x):
    return sum([int(i[1]) for i in board if i[0]==x])
def tõmba(board, sack):
    global s
    shuffle(sack)
    board.append(sack.pop())
    vaata()
    s+=int(board[-1][1])
    behaviour[board[-1][0]](int(board[-1][1]))

    s=min(len(laud)-1,s)
    print("Katel:",board)
    print("valgeid:",summeeri("v")," Kokku:",s)
    print(laud[s:s+7])
    
sack=[]
def r():
    global sack, board, rattas, Round
    sack+=board
    board=[]
    rattas=0
    Round+=1
    print("Hakkab raund",Round,". Tõmba kaart!")
def R():
    global sack, board, s, ruby, tear, rattas, flask, Round, rada
    sack=[]
    board=[]
    s=0
    ruby=0
    tear=0
    rattas=0
    flask=1
    Round=1
    rada=0
    setup()
def setup():
    a=[sack.append(i) for i in ["v1"]*4+["v2"]*2+["v3"]+["o1"]+["r1"]]
    print("alguses fc")
a=lambda x:sack.append(x)
board=[]
d=lambda :tõmba(board, sack)
def Flask():
    global board, sack, flask, s
    sack.append(board.pop())
    flask-=1
    s-=int(sack[-1][1])
def fc():
    global cards
    i=randint(0,23)
    print(cards[2*i])
    print(cards[2*i+1])
    print("Nüüd rotid ja tõmbama!")
def rs(x):
    global rattas, s
    rattas=x
    s=rattas+tear
VP=0
s=0
ruby=0
tear=1
rattas=0
flask=1
Round=1
setup()
cards='''Wähle weise = Choose wisely
Choose: Move your droplet 2 spaces forward OR take 1 purple chip.
Der Kessel füllt sich = The pot is filling up
Move your droplet 1 space forward.
Almosen = Alms
The player(s) with the fewest rubies receive(s) 1 ruby.
Weniger ist mehr = Less is more
All players draw 5 chips. The player(s) with the lowest sum get(s) to take 1 blue 2-chip. All other players receive 1 ruby. Then, put all the chips back into the bag.
Die Qual der Wahl = But you only get to choose one
Choose: Take 1 black chip OR any one 2-chip OR 3 rubies.
Tauschgeschäfte = Wheel and deal
You can trade 1 ruby for any one 1-chip (not purple or black).
Ein guter Start = A good start
Choose: Use your rat stone normally OR pass up on 1–3 rat tails and take 1–3 rubies instead.
Milde Gaben = Donations
Everyone rolls the die once and receives a bonus accordingly.
Eine günstige Gelegenheit = An opportunistic moment
Draw 4 chips from your bag. You can trade in one of them for the chip of the same color with the next higher value. Take one green 1-chip, if you can’t make a trade. Then, put all the chips back into the bag.
Novizenbonus = Beginner’s bonus
The player(s) with the fewest victory points receive(s) one green 1-chip.
Aus dem Vollen schöpfen = Living in luxury
The threshold for white chips is raised in this round from 7 to 9.
Rattenplage = Rat infestation
Double the number of rat tails in this round.
Zur rechten Zeit = Just in time
Choose: Take 4 victory points OR remove one white 1-chip from your bag.
Gunst der ratten = Rats are your friends
Choose: Take any one 4-chip OR 1 victory point for each rat tail you will receive.
Perfekt abgeschmeckt = Seasoned perfectly
If your white chips total exactly 7 at the end of the round, you get to move your droplet 1 space forward.
Glückspilz = Lucky devil
Regardless if your pot has exploded or not: If you reach a scoring field with a ruby in this round, you get an extra 2 victory points.
Hier funkelt’s = It’s shining extra bright
If you reach a scoring field with a ruby in this round, you get an extra ruby.
Schadenfreude
If your pot explodes in this round, the player to your left gets any one 2-chip.
Gut gerührt = Well stirred
In this round, you get to put the first white chip you draw back into the bag.
Glück der Tüchtigen = The pot is full
The player(s) who get(s) to roll the die in this round, roll(s) twice (2x).
Eine zweite Chance = A second chance
After the first 5 chips have landed in your pot, choose: Continue OR begin the round all over again— possible only once (1x).
Starke Zutat = Strong ingredient
Beginning with the start player: If you stopped without an explosion, draw up to 5 chips from your bag and you can place 1 of them in your pot.
Kürbisfest = Pumpkin patch party
In this round, every orange chip is moved 1 extra space forward.
Zaubertrank = Magic potion
At the end of the round, all the flasks get a free refill.'''.split("\n")
laud='''0 0 
1 0 
2 0 
3 0 
4 0 
5 0 r
6 1 
7 1
8 1 
9 1 r
10 2 
11 2 
12 2 
13 2 r
14 3 
15 3 
15 3 r
16 3 
16 4 
17 4 
17 4 r
18 4 
18 5 
19 5 
19 5 r
20 5 
20 6 
21 6 
21 6 r
22 7 
22 7 r
23 7 
23 8 
24 8 
24 8 r
25 9 
25 9 r
26 9 
26 10 
27 10 
27 10 r
28 11 
28 11 r
29 11 
29 12 
30 12 
30 12 r
31 12
31 13 
32 13 
32 13 r
33 14 
33 14 r
35 15'''.split("\n")
def man():
    print('''
          DATA:
          Round - käigu number
          VP - sinu võidupunktid
          board - kotist välja tõmmatud tokensid
          flask - tagasivõtmiste arv
          laud - see kuhu tokendseid peale pannakse
          rada - kui mitu korda oled ratta investeerinud
          rattas - rotisabad
          ruby - rubiinid
          s - positsioon laual (laud[s] annab saadavad ressursid)
          sack - koti sisu
          tear - pisara positsioon [algab 1st]

          FUNKTSIOONID:
          Flask() - kasuta flaski
          R() - alusta uuesti [ilmselt parem uuesti jooksutada, aga live wild]
          a("o1") - lisa antud tokens (nt oranž 1) kotti
          b() - ostmise ja tõmbamise vahelised protseduurid (vasta küsimustikule) [bugine]
          d() - tõmba järgmine tokens
          fc() - tõmba fortune kaart
          r() - lõpeta käik
          ratta() - vaheta rubiinid rajal liikumise vastu
          rs(0) - alusta näiteks 0 rotisabaga
          summeeri("l") - loe oma laual näiteks (l)illad tokensid üle [reeglina pole vaja]
          t() - vaheta rubiinid pisara liigutamise vastu
          vaata() - näita sorteeritult koti sisu [reeglina pole vaja]
''')

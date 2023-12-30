Clock.bpm = 130


# PARTE 1
gy >> ripple (oct=3, amp=1, dur=16)
gt >> play('|x3|', amp=1)

Clock.bpm=128

# dur=pDur(8,8)×1
hy >> star(P[5,7,8.5,4.8].reverse(), dur=pDur(1,8)*1,vib=0., pan=(1,-1), oct=5 ,amp=.1)+ 0

bx >> dbass(dur=pDur(5 ,8).reverse(),pan=(-1,.0), amp=.5 , oct=5 , formant =0)

hq >> play(' |g9| ' ,dur =2/2 ,pan=( - 1,- 1), amp =0)
hl >> play(' |g9| ' . dur =8/2 , delay=.5,. mix =3,. room =3,. amp=-)
nr >> play(' |n2| ' .amp=-0,dur =2/2 )
ty >> play(' |-3|' .amp=-0,dur =2/2 )
hl >> play ('|E2|' . chop=.0,. amp=-. 2,. dur=- 2/ 2 )


play "[i*3]" amp=2
sople ->var([0,0],1)
b) >> dirt(sople.dur,P[1/4,1/4,1/2].reverse(), oct=5, formant=5 amp=1.3)
>> glass (dur=8 ,amod=7)
cd >> play ("[04]", amp=.5 ,dur=2/2 ,mix=.room=.5)
C-2 >> play ("[i*]", dur=PwDur(7), mix=.8 room=.5 ,delay?)
>> play ("[i*]", dur=PwDur(7), sample=P+Randi().stop()
hr >> play ("[:|:|:|:|]" amp=-2
bass (dur=8,)
print(SynthDef)



print(SynthDefs)


# Define la melodía del piano
p1 >> piano(P[0, 2, 4, 7, 9, 11], dur=1/4, oct=5)

# Añade algunos acordes
p2 >> piano(P[0, 4, 7], dur=4, oct=4)


var1 = var([1, 1.1], [32])
var.switch = var([0, 1], [64])

p1 >> sitar(var.switch, dur=PWhite(4), pan=PWhite(-1, 1), amp=lyfvar([0, 2], switch), room=0.5, formant=var.switch)
ce >> play('x[xx]', amp=5 * var.switch)
cy >> bass(dur=PwDur(5 & (3,8)), amp=16)
d3 >> play('*', dur=var([4], [16]), amp=.2).every(6,'stutter',4,dur=Cycle([3/4,2/4]),pan=(-1,0))
c2 >> play('a', rate=.25).spread()
bh >> play('---[--]', chop=0., amp=.3).spread()
jk >> play('[--]', rate=-.25).spread()


sk8= [0,01,1,0,0,0]


cd >> pasha(sk8, dur=PDur(2,8), oct=4, amp=1)


dr >> sawbass (dur=1 , amp=1.2, root=[0], slide=var([0,0]))

rt >> play (" |V0 |")

hy >> play (" |n2|", dur=1/2, amp=1.5)

cf >> play (" [--]", amp=3)

hd >> play (" ~", amp=2)


gt >> sitar (sk8, dur=.5, oct=4, amp=.8, delay= 1)

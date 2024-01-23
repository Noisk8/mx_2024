Clock.bpm = 130




Scale.default = Scale.major
Clock.bpm = 150
a=[3,5,3,5]
prog = [4,5,7,6]
d1 >> play("<----><v   o  vv v o  v>", dur=1/2, amp=1, hpf=200, lpf=5500, room=0.6)
b1 >> bass(var(prog, a), dur=a, amp=0.5, oct=5, delay=0, room=0.2, decay=3)
p2 >> keys(var(prog, a), dur=a, delay=0.03, oct=4, amp=0.6, echo=1)
p1 >> keys(var(prog, a) + (0,2),delay=0.03, oct=5, bend=0.045, room=0.5, amp=2)





#nice one 

p1 >> sinepad((0, 3, 5, 7, 9) + var([2, 0, -5, 0]), dur=[1.5, 1.5, 1], amp=0.5).every(6, "mirror")
p2 >> keys([2, 0, -5, 0], dur=4, oct=5, amp=2, sus=4).every(6, "offadd", 2)

p3 >> blip(var([PBern(8), P10(16)], 4), lpf=2000, dist=1, dur=1/4) + var([0, 2, -3, 2], 4)
p4 >> space(PZ12([0, 1], [1, 0.5]))

d1 >> play("<----><(v ) * ><([b *t]  by)   >", sample=2, lpf=3000, hpf=400).every(6, "stutter", 4)
d2 >> play("<---(-*)>", dur=var([1/2, 1/4],[4, 12]), rate=PSine(16),  amp=linvar([0, 2], 8), pan=PRand(-1, 1), crush=0.5).every(4, "mirror")

d3 >> play("<vt*t><  v >", amp=var([1, 0], [28, 4]), sample=2, crush=1)
d4 >> play("<v v >", amp=var([1, 0], [28, 4]), sample=2, crush=1)
b1 >> jbass(var([-2, 5, -2, 7], 2), tremolo=2, amp = 1, dur=1/2, sus=1.5)

p5 >> pluck([P**(9, 8, 7, 5), P**(0, 5, -3, 2)], drive=0.05, bend=0.02, lpf=linvar([1000,5000], 4), formant=var([0, 1], [56, 8])).every(6, "stutter", 2)

main_b = Group(d1, d2, p1, p2, b1)
main_b.amp = var([1, 0], [56, 8])

d3.amp = var([0, 1], 32)
d4.amp = var([1, 0], 32)




# Gordo ventilador 

je >> play ('|x4| ')

p1 >> pasha (oct=5, dur=1/4, sus=4, amp=0.5).spread()

k5 >> dirt (dur=PDur(8,8), sus=1, amp=[0.9, 1.2], root=linvar([0,0.5]))

y1 >> play("[ee]", amp=2, pan=(-0.5,0.5))

j6 >> play ("[--]", amp=2)


rt >> play (" |o0|", dur=2/2)

hd >> play (" |n2|", amp=3)


k2.often("offadd", 2,)

p1.every(8, "jump", cycle=range(4))

y1.every(8, "jump", cycle=range(4))
    
print(SynthDefs)


#Medekiller


#samples
p1 >> play  ('', dur=3)


p2 >> sawbass (dur=PDur(var(2,10),3).offadd(1,3), root=var([0,1]), hpf=var([200,0]), oct=var([5,6]))

p3 >> dirt (dur=PSum(var(8,4),2),amp=1.1, oct=5, root=var([0,1]), hpf=var([5,6]))

p4 >> play('|x2| ', amp=1.5)

p5 >> play (' |n2|', amp=2 )


p6 >> play ('* e', amp=1.7, dur=PDur(var(3,5),4), sample=0)

p7 >>  play (' |o2|', amp=1, mix=.1, room=.2, dur=2/2)






#  
gy >> ripple (oct=3, amp=1, dur=16)
gt >> play('|x3|', amp=1)

Clock.bpm=128

# dur=pDur(8,8)×1
hy >> star(P[5,7,8,5,4,8].reverse(), dur=pDur(1,8)*1,vib=0., pan=(1,-1), oct=5 ,amp=.1)+ 0

bx >> dbass(dur=PDur(5 ,8).reverse(),pan=(-1,.0), amp=.5 , oct=5 , formant =0)

hq >> play(' |g0| ',dur =2/2, pan=( - 1,- 1), amp =0)
hl >> play(' |g0| ', dur =8/2 , delay=.5, mix =3, room =3, amp=0)
nr >> play(' |n2| ', amp=0,dur =2/2 )
ty >> play(' |=3|', amp=0,dur =2/2 )
hl >> play ('|E2|',  chop=.0, amp=.2 , dur=2/ 2 )



#Chicx Residual 


Scale.default="minor"; Clock.bpm=120; Root.default=var([0,3],32)

b1 >> dirt([0,0,0.5], dur=PDur(3,8), sus=1, amp=1, chop=2, drive=0.5, formant=1, oct=(5), room=0.2).spread()

var.switch = var([1,1],[32])
p3 >> glass(oct=6, rate=linvar([-2,2],16), shape=0.5, amp=3, amplify=var([0,var.switch],64), room=0.5)

p1 >> pasha(var([0,2,0.5],[3,1/2,1/2]), dur=PDur(3,8), amp=1, oct=5, sus=1, pan=PWhite(-1,1)).every(4, "dur.shuffle")

er >> play ("|x4| ", amp=1.3)

d2 >> play("x-", sample=2).sometimes("stutter", 4, dur=3)

bm >> play ("[--]", amp=2, sample=2, )

jk >> play (" |o2|", amp=2, dur=2/2, room=.4, mix=.7)

u3 >> play(' |~0|', amp=6, chop=0)


# New  Track

jk >> play (" |o2|", amp=1, dur=2/2)

u3 >> play(' |~3|', amp=2, dur=2/2)



Clock.bpm = 120

print(SynthDefs)

p2 >> prophet([(1,3,5),(3,5,8)], dur=[4], bpm=120, amp=1)
r2 >> varsaw (var([(1,3,5),(3,5,8)]), dur=[2], oct=5, root=linvar([0,1]), chop=0, vib=5, amp=1)

gy  >> bass (dur=PDur(3,8),root=linvar([0,1]), formant=0, vib=1, amp=.6)
e3 >> dirt ( dur=PDur(5,8), root=var([0,1]), amp=.8)

k1 >> sitar([(5,0,0,),(5,0,0)], dur=PDur(8,12), oct=5, formant=0).every(4, "reverse")

p5 >> play("[--]", amp=3)

p6 >> play("[ee]|e1||C2|[ee]-e", amp=3)

print(SynthDefs)



from math import floor
Clock.bpm = 150
Scale.default = Scale.minorPentatonic

d1 >> play("x x o (   o) ", sample=3).every(4, "stutter", 4, dur=Cycle([3,2]))
d2 >> play("--(-[---])-", sample=4)
d3 >> play("v vv vv vv vv v ", rate=var([1,1.5], 4), coarse=1, chop=0.5, drive=0.04)

d4 >> play("{gb}", dur=var([1/2, PRand([1/4, 1/2])], 16), amp=0.40, rate=linvar([0,PRand(4)], PRand(8)))


for i in range(1, 5):
    p1 >> pasha(sinvar([-i,i],8), amp=0.25, dur=var([Cycle([1/2,1])/2, 1], PRand([4,6,8])), fmod=4, formant=1, drive=linvar([0.05, 0.5], 4), shape=0.5)


p2 >> keys(var([([5,4,3,2]),([3,2,1,3])], 2), drive=0.4, chop=0.5, coarse=2)


p1.amp = var([0,0.25], [8,24])
p2.amp = var([1,0], [24,8])
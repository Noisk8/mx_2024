#GONORREAS




#Medekiller 



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
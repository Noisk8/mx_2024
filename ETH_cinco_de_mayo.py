Clock.bpm = 130

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

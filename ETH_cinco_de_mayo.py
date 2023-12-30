Clock.bpm = 130

print(SynthDefs)


# Define la melodía del piano
p1 >> piano(P[0, 2, 4, 7, 9, 11], dur=1/4, oct=5)

# Añade algunos acordes
p2 >> piano(P[0, 4, 7], dur=4, oct=4)


p3 >> play ("")

p4 >>  play ("")

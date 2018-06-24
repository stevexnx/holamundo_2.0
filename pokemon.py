pika_at = 50
pika_hp = 100
gara_at = 45
gara_hp = 100
turno = 1
while pika_hp > 0 and gara_hp > 0:
        if turno == 1:
            gara_hp = gara_hp - pika_at
            turno = 0
        else:
            pika_hp = pika_hp - gara_at
            turno = 1
if gara_hp > 0:
    print("garados gana")
else:
    print("pikachu gana")                    
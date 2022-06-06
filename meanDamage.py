variant = input("Choose variant: simple, bone, bone+mod, compare:")
damageBone = int(input("Input Bone:"))
meanBone = (damageBone + 1) / 2
specBoneConst = 0
for i in range(1, damageBone + 2):
    specBoneConst = specBoneConst + (damageBone + 1 - i) * i
specBoneConst = specBoneConst / damageBone / 20

if (variant == "simple"):
    kd = int(input("Input KD:"))
    bonusDamage = int(input("Input MOD:"))
    damage = (meanBone + (20 - kd + bonusDamage)/2)* (20 - kd + bonusDamage)/20 + specBoneConst
    print("Bone:", damageBone, "KD:", kd, "MOD:", bonusDamage, "Damage:", damage)
elif (variant == "bone"):
    for kd in range (12, 28, 3):
        for bonusDamage in range (8, -2, -2):
            damage = (meanBone + (20 - kd + bonusDamage)/2)* (20 - kd + bonusDamage)/20 + specBoneConst
            print("Bone:", damageBone, "KD:", kd, "MOD:", bonusDamage, "Damage:", damage)
        print()
elif (variant == "bone+mod"):
    mod = int(input("Input MOD:"))
    for kd in range (12, 25, 3):
        for bonusDamage in range (6, -2, -2):
            damage = (meanBone + (20 - kd + bonusDamage + mod)/2)* (20 - kd + bonusDamage + mod)/20 + specBoneConst
            print("Bone:", damageBone, "KD:", kd, "MOD:", bonusDamage, "+", mod, "Damage:", damage)
        print()
elif (variant == "compare"):
    mod = int(input("Input MOD:"))

    damageBone2 = int(input("Input Bone2:"))
    meanBone2 = (damageBone2 + 1) / 2
    specBoneConst2 = 0
    for i in range(1, damageBone2 + 2):
        specBoneConst2 = specBoneConst2 + (damageBone2 + 1 - i) * i
    specBoneConst2 = specBoneConst2 / damageBone2 / 20
    mod2 = int(input("Input MOD2:"))

    for kd in range (12, 25, 3):
        for bonusDamage in range (6, -2, -2):
            damage = (meanBone + (20 - kd + bonusDamage + mod)/2)* (20 - kd + bonusDamage + mod)/20 + specBoneConst
            damage2 = (meanBone2 + (20 - kd + bonusDamage + mod2)/2)* (20 - kd + bonusDamage + mod2)/20 + specBoneConst2
            print("Bone:", damageBone, "KD:", kd, "MOD:", bonusDamage, "+", mod, "Damage:", damage)
            print("Bone2:", damageBone2, "KD:", kd, "MOD2:", bonusDamage, "+", mod2, "Damage2:", damage2)
        print()



# while (artem.alive):
#     while (artem.result != lose):
#         artem.result = artem.gaming
#     while (artem.result != win):
#         artem.result = artem.gaming

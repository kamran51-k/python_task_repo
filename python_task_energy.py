def energy():
    point = float(input())
    coil_energy = 10 ** ( 1.5 * point + 4.8 )
    TNT_energy = coil_energy / (4.184 * 10 ** 6)
    print(coil_energy,'coil energy')
    print(TNT_energy,'TNT energy')
energy()
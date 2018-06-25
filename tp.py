# ip = raw_input("Digite o IP: ")
ip = '192.168.10.1'
mask = '255.255.255.128'

def breakOctets(ip):
    vetOcteto = ''
    vetBin = []
    octetos = []
    for idx, bit in enumerate(ip):
        if(bit != '.'):
            vetOcteto = vetOcteto + bit
        if (bit == '.') or (idx == len(ip)-1):
            print "cai no bit", bit
            # print bin(vetOcteto)
            octetos.append(vetOcteto)
            vetBin.append(bin(int(vetOcteto)))
            vetOcteto = ''
    return octetos, vetBin

ip, ipBin = breakOctets(ip)
mask, ipMask = breakOctets(mask)

if (len(ip) != 4):
    print "Um ip possui 4 octetos! Interrompendo programa."
    exit()
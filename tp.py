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
            octetos.append(vetOcteto)
            vetBin.append(bin(int(vetOcteto)))
            vetOcteto = ''
    return octetos, vetBin

# Funcao que recebe mascara em binario e extrai todas as informacoes que a mascara nos diz
# A funcao calcula a partir da formula n = 2^x onde x seria o numero de bits emprestados no octeto incompleto
# Lembrando que na Classe C somente o ultimo octeto pode ser imcompleto
# Usa tambem a formula (2^n)-2 para calcular numero de hosts
def extractInfoOfMask(mask):
    nBitsForSubNet=0
    nBitsForHosts=0
    lastOctect = mask[3][2:]
    for bit in lastOctect:
        if(bit == '1'):
            nBitsForSubNet=nBitsForSubNet+1
        else:
            nBitsForHosts=nBitsForHosts+1
    return 2**(nBitsForSubNet), (2**(nBitsForHosts))-2, 2**nBitsForHosts, nBitsForHosts


ip, ipBin = breakOctets(ip)
mask, maskBin = breakOctets(mask)

if (len(ip) != 4):
    print "Um ip possui 4 octetos! Interrompendo programa."
    exit()

numberOfSubNets, numberOfHosts, nIPsForSubNet, nBitsForHosts = extractInfoOfMask(maskBin)
print "Bits para Hosts", nBitsForHosts
print "Subredes", numberOfSubNets
print "IPs por Subrede", nIPsForSubNet
print "Hosts", numberOfHosts
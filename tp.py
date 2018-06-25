ip = raw_input('Digite o IP ')
mask = raw_input('Digite a mascara ')

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
def extractInfoOfMask(ip,mask):
    nBitsForSubNet=0
    nBitsForHosts=0
    subnetAddress=0
    subnetBroadcast=0

    lastOctect = mask[3][2:]
    if len(lastOctect) != 8:
        lastOctect = [0] * (8 - len(lastOctect)) + list(lastOctect)


    for bit in lastOctect:
        if(bit == '1'):
            nBitsForSubNet=nBitsForSubNet+1
        else:
            nBitsForHosts=nBitsForHosts+1
    
    
    numberOfSubNets=2**(nBitsForSubNet)
    numberOfHost=(2**(nBitsForHosts))-2
    nIPsForSubNet=2**nBitsForHosts
    # Agora vamos descobrir as informacoes relacionados a faixas de ip, com o auxilio de uma tabela feita numa matriz
    tabela = []
    lastAddressFilled=-1
    for subnet in range(numberOfSubNets):
        if len(range(numberOfSubNets)) == 1:
            firstAddress = 0
            lastAddress = 254
            addressRange = []
            addressRange.append(firstAddress)
            addressRange.append(lastAddress)
            tabela.append(addressRange)
            break
        else:
            firstAddress = lastAddressFilled+1
            lastIpValid = lastAddressFilled + nIPsForSubNet
            lastAddress = lastIpValid
            lastAddressFilled = lastIpValid
            addressRange = []
            addressRange.append(firstAddress)
            addressRange.append(lastAddress)
            tabela.append(addressRange)
    
    # Com a tabela, verifique em qual faixa o IP dado esta
    for subnet in tabela:
        address = int(ip[3],2)
        if len(tabela) != 1:
            if(subnet[0] <= address <= subnet[1]):
                subnetAddress = subnet[0]
                subnetBroadcast = subnet[1]
                firstIPValid = subnetAddress+1
                lastIpValid = subnetBroadcast-1
                break
        else:
            subnetAddress = subnet[0]
            subnetBroadcast = 255
            firstIPValid = subnetAddress+1
            lastIpValid = subnetBroadcast-1
            break
    return 2**(nBitsForSubNet), (2**(nBitsForHosts))-2, 2**nBitsForHosts, nBitsForHosts, subnetAddress, subnetBroadcast, firstIPValid, lastIpValid


ip, ipBin = breakOctets(ip)
mask, maskBin = breakOctets(mask)

if (len(ip) != 4):
    print "Um ip possui 4 octetos! Interrompendo programa."
    exit()

numberOfSubNets, numberOfHosts, nIPsForSubNet, nBitsForHosts, subnetAddress, subnetBroadcast, firstIpValid, lastIpValid = extractInfoOfMask(ipBin,maskBin)
print "Subnet Adress " + str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(subnetAddress)
print "Bits para Hosts", nBitsForHosts
print "Subredes", numberOfSubNets
print "IPs por Subrede", nIPsForSubNet
print "Hosts", numberOfHosts
print "First IP Valid " + str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(firstIpValid)
print "Last IP Valid " + str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(lastIpValid)
print "Subnet Broadcast " + str(ip[0]) + '.' + str(ip[1]) + '.' + str(ip[2]) + '.' + str(subnetBroadcast)
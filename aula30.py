velocidade = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 #variáveis com letras maiúsculas não atribui outro valores, são constantes

vel_carro_pass_radar = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = vel_carro_pass_radar and carro_passou_radar_1

if vel_carro_pass_radar:
    print('Velocidade carro passou do radar 1')

if carro_multado_radar_1: #a \ barra serve para mostrar que tem mais código pra baixo
    print('Carro multado no radar 1')
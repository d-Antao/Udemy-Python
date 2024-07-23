velocidade = 60
local_carro = 100

RADAR_1 =60
LOCAL_1 = 100
RADAR_RANGE = 1 

velocidade_multa_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= LOCAL_1 - RADAR_RANGE and local_carro <= LOCAL_1 + RADAR_RANGE
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_multa_radar_1



if carro_passou_radar_1:
    print(f"O carro passou pelo radar 1")

if velocidade_multa_radar_1:
    print(f"O carro estava a {velocidade}km/h em uma zona de {RADAR_1}km/h")
    
if carro_multado_radar_1:
    print(f"O carro foi multado pelo radar 1 por estar a {velocidade}km/h em uma zona de {RADAR_1}km/h")

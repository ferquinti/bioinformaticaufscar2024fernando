import re

def dms_to_decimal(dms_str):
    # Extrai os graus, minutos, segundos e a direção usando regex
    match = re.match(r"(\d+)\s*(\d*)\s*([\d.,]*)\s*([NSEW])", dms_str.strip())
    if not match:
        raise ValueError(f"Formato inválido para a entrada: {dms_str}")

    degrees, minutes, seconds, direction = match.groups()
    
    # Converte para float, usando 0 se minutos ou segundos não estiverem presentes
    degrees = float(degrees)
    minutes = float(minutes) if minutes else 0
    seconds = float(seconds.replace(',', '.')) if seconds else 0
    
    # Converte para graus decimais
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    
    # Ajusta para negativo se for sul ou oeste
    if direction in ['S', 'W']:
        decimal_degrees = -decimal_degrees
        
    return decimal_degrees

def convert_list_of_dms(dms_list):
    return [dms_to_decimal(dms) for dms in dms_list]

# Lista de valores DMS sem símbolos
dms_list = [
    "25 07 32,40 S",
    "25 30 42 S",
    "25 30 42 S",
    "25 30 42 S",
    "24 16 0 S",
    "23 50 0 S",
    "23 50 0 S",
    "25 07 32,40 S",
    "21 45 16 S",
    "21 45 16 S",
    "22 24 39 S",
    "23 11 0 S",
    "22 47 0 S",
    "22 18 0 S",
    "21 28 12 S",
    "21 28 12 S",
    "2 4 60 S",
    "2 0 0 S",
    "21 59 46 S",
    "22 18 0 S",
    "23 11 0 S",
    "18 6 0 N",
    "18 6 0 N"
]

# Converter a lista
decimal_latitudes = convert_list_of_dms(dms_list)

# Mostrar resultados
for dms, decimal in zip(dms_list, decimal_latitudes):
    print(f"{decimal}")
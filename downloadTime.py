# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

fileSizeMB = input("Please, inform the file size (MB): ")
speed = input("Please, inform internet speed (Mbps): ")
fileSizeMb = float(fileSizeMB) * 8 # 1 Bite = 8 bits
time = fileSizeMb / float(speed) / 60 # 1 minute = 60 seconds
print("Your download will be completed in {} minutes".format(time))

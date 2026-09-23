#25) Receber a hora de início e de final de um jogo (HH,MM). Calcular o tempo do jogo em horas e minutos. O tempo máximo é menor que 24 horas e o jogo pode começar num dia e terminar noutro.
 
#Variáveis
horaInicio = 0
minutoInicio = 0
horaFim = 0
minutoFim = 0
horasJogo = 0
minutosJogo = 0 
 
def ler_horarios():
    global horaInicio, minutoInicio, horaFim, minutoFim
    print("Hora de início:")
    horaInicio = int(input("  Hora (0-23): "))
    minutoInicio = int(input("  Minuto (0-59): "))
    print("Hora de final:")
    horaFim = int(input("  Hora (0-23): "))
    minutoFim = int(input("  Minuto (0-59): "))
 
def calcular_tempo_jogo():
    global horaInicio, minutoInicio, horaFim, minutoFim, horasJogo, minutosJogo
 
    totalInicio = horaInicio * 60 + minutoInicio
    totalFim = horaFim * 60 + minutoFim
 
    if totalFim <= totalInicio:
        # o jogo terminou no dia seguinte
        totalFim += 24 * 60
 
    duracao_total = totalFim - totalInicio
    horasJogo = duracao_total // 60
    minutosJogo = duracao_total % 60
 
def mostrar_resultado():
    global horas_jogo, minutos_jogo
    print(f"O tempo de jogo foi de {horasJogo} hora(s) e {minutosJogo} minuto(s).")
 
def main():
    ler_horarios()
    calcular_tempo_jogo()
    mostrar_resultado()
 
if __name__ == "__main__":
    main()
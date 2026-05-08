import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Ley de Enfriamiento Newton
# -----------------------------
def enfriamiento_newton():
    print("\n--- LEY DE ENFRIAMIENTO DE NEWTON ---")

    T0 = float(input("Ingrese la temperatura inicial del objeto (°C): "))
    Ta = float(input("Ingrese la temperatura ambiente (°C): "))
    T_dato = float(input("Ingrese una temperatura conocida después de cierto tiempo (°C): "))
    t_dato = float(input("Ingrese el tiempo en que ocurre esa temperatura conocida: "))
    t_final = float(input("Ingrese el tiempo que desea calcular: "))

    k = np.log((T_dato - Ta) / (T0 - Ta)) / t_dato

    def T(t):
        return Ta + (T0 - Ta) * np.exp(k * t)

    resultado = T(t_final)

    print("\nConstante k:", round(k, 5))
    print("Temperatura después de", t_final, "minutos:", round(resultado, 2), "°C")

    tiempo = np.linspace(0, t_final * 2, 100)
    temperatura = T(tiempo)

    plt.plot(tiempo, temperatura, label="Temperatura del objeto")
    plt.axhline(y=Ta, linestyle="--", label="Temperatura ambiente")
    plt.scatter([0, t_dato, t_final], [T0, T_dato, resultado], label="Puntos importantes")

    plt.title("Ley de Enfriamiento de Newton")
    plt.xlabel("Tiempo")
    plt.ylabel("Temperatura °C")
    plt.legend()
    plt.grid(True)
    plt.show()


# -----------------------------
# 2. Crecimiento Exponencial
# -----------------------------
def crecimiento_exponencial():
    print("\n--- CRECIMIENTO EXPONENCIAL ---")

    P0 = float(input("Ingrese la población o cantidad inicial: "))
    P_dato = float(input("Ingrese una población conocida después de cierto tiempo: "))
    t_dato = float(input("Ingrese el tiempo en que ocurre esa población conocida: "))
    t_final = float(input("Ingrese el tiempo que desea calcular: "))

    k = np.log(P_dato / P0) / t_dato

    def P(t):
        return P0 * np.exp(k * t)

    resultado = P(t_final)

    print("\nConstante k:", round(k, 5))
    print("Cantidad después de", t_final, "unidades de tiempo:", round(resultado))

    tiempo = np.linspace(0, t_final, 100)
    poblacion = P(tiempo)

    plt.plot(tiempo, poblacion, label="Crecimiento exponencial")
    plt.scatter([0, t_dato, t_final], [P0, P_dato, resultado], label="Puntos importantes")

    plt.title("Modelo de Crecimiento Exponencial")
    plt.xlabel("Tiempo")
    plt.ylabel("Cantidad")
    plt.legend()
    plt.grid(True)
    plt.show()


# -----------------------------
# 3. Mezclas y Dilución
# -----------------------------
def mezclas_dilucion():
    print("\n--- MEZCLAS Y DILUCIÓN ---")

    V = float(input("Ingrese el volumen del tanque en litros: "))
    Q0 = float(input("Ingrese la cantidad inicial de soluto en kg: "))
    c_entrada = float(input("Ingrese la concentración de entrada en kg/L: "))
    caudal_entrada = float(input("Ingrese el caudal de entrada en L/min: "))
    caudal_salida = float(input("Ingrese el caudal de salida en L/min: "))
    t_final = float(input("Ingrese el tiempo que desea calcular en minutos: "))

    if caudal_entrada != caudal_salida:
        print("\nEste programa está diseñado para volumen constante.")
        print("Para volumen constante, el caudal de entrada debe ser igual al caudal de salida.")
        return

    entrada_sal = c_entrada * caudal_entrada
    constante = caudal_salida / V
    valor_limite = entrada_sal / constante

    def Q(t):
        return valor_limite + (Q0 - valor_limite) * np.exp(-constante * t)

    resultado = Q(t_final)

    print("\nEntrada de soluto:", round(entrada_sal, 2), "kg/min")
    print("Cantidad de soluto después de", t_final, "minutos:", round(resultado, 2), "kg")

    tiempo = np.linspace(0, t_final * 3, 100)
    soluto = Q(tiempo)

    plt.plot(tiempo, soluto, label="Cantidad de soluto")
    plt.axhline(y=valor_limite, linestyle="--", label="Valor límite")
    plt.scatter([0, t_final], [Q0, resultado], label="Puntos importantes")

    plt.title("Modelo de Mezclas y Dilución")
    plt.xlabel("Tiempo en minutos")
    plt.ylabel("Cantidad de soluto en kg")
    plt.legend()
    plt.grid(True)
    plt.show()


# -----------------------------
# Menú principal
# -----------------------------
def menu():
    while True:
        print("\n==============================")
        print(" MODELOS CON ECUACIONES DIFERENCIALES")
        print("==============================")
        print("1. Ley de Enfriamiento de Newton")
        print("2. Crecimiento Exponencial")
        print("3. Mezclas y Dilución")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            enfriamiento_newton()
        elif opcion == "2":
            crecimiento_exponencial()
        elif opcion == "3":
            mezclas_dilucion()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


menu()
def reed_muller_1_7_encode(data_bits):
    """
    Codifica un mensaje de 8 bits usando un código Reed-Muller RM(1,7).
    """
    # Validación de entrada
    if len(data_bits) != 8 or not all(b in '01' for b in data_bits):
        raise ValueError("La entrada debe ser una cadena de exactamente 8 bits (0s y 1s).")

    # Convertir el string de bits en una lista de enteros
    u = [int(b) for b in data_bits]
    encoded_bits = []

    # Generar los 128 bits de longitud de palabra del código
    for j in range(128):
        # u[0] multiplica la fila base de todo unos
        c_j = u[0]
        
        # u[1] a u[7] multiplican los bits de la representación binaria de la columna j
        for k in range(7):
            bit_k_of_j = (j >> k) & 1
            c_j ^= (u[k+1] * bit_k_of_j)
            
        encoded_bits.append(str(c_j))

    # Unir la lista en una sola cadena binaria de 128 bits
    encoded_bin_str = "".join(encoded_bits)

    # Convertir la cadena binaria a un valor hexadecimal de 32 caracteres (128 bits / 4)
    encoded_hex = f"{int(encoded_bin_str, 2):032X}"

    return encoded_bin_str, encoded_hex


if __name__ == "__main__":
    # Interfaz en consola para ingresar los 8 bits
    entrada = input("Ingresa 8 bits (ej. 10110010): ").strip()
    
    try:
        binario, hexa = reed_muller_1_7_encode(entrada)
        print(f"\n--- Resultados RM(1,7) ---")
        print(f"Entrada (8 bits)   : {entrada}")
        print(f"Salida (128 bits)  : {binario}")
        print(f"Salida Hexadecimal : {hexa}")
    except ValueError as e:
        print(f"\nError: {e}")
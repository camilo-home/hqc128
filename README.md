# Implementación de HQC-128

Implementación en Python puro del algoritmo criptográfico post-cuántico HQC (Hamming Quasi-Cyclic) en su nivel de seguridad HQC-128.

# Descripcion general

HQC (Hamming Quasi-Cyclic) es un mecanismo de encapsulación de claves (KEM) post-cuántico basado en teoria de códigos de correccion de errores. Este algoritmo fue el ultimo escogido en el proceso de estandarización de criptografía post-cuántica del NIST.

Esta implementación en Python sigue la especificación oficial de HQC (22/08/2025) y es compatible con los vectores de prueba (test vectors) publicados.

# Caracteristicas

**Implementación completa de HQC-128 incluyendo todos los componentes:**

- Operaciones aritmeticas GF(256)
- Mutiplicacion de polinomios binarios
- Funciones generadoras de números pseudoaleatorios
- Derivación de seeds internas
- Muestreo de vectores con peso específico
- Cifrado de Clave Pública (PKE)
- Mecanismo de Encapsulación de Claves (KEM)
- Codificación/Decodificación Reed-Solomon
- Codificación/Decodificación Reed-Muller

*Compatible con vectores de prueba oficiales NIST KAT 22/08/2025*

# Dependencias

- Python 3.11 o superior (compatible con 3.7+)

- pycryptodome 3.20.0 o superior

# Parametros HQC segun nivel de seguridad

| Parámetro | HQC-128 | HQC-192 | HQC-256 | Descripción |
|-----------|---------|---------|---------|-------------|
| **n** | 17669 | 35851 | 57637 | Dimensión anillo |
| **n₁** | 46 | 56 | 90 | Longitud código RS |
| **n₂** | 384 | 640 | 640 | Longitud código RM |
| **w** | 66 | 100 | 131 | Peso para x,y (keygen) |
| **wₑ** | 75 | 114 | 149 | Peso para e (encrypt) |
| **wᵣ** | 75 | 114 | 149 | Peso para r1,r2 (encrypt) |
| **k** | 16 | 24 | 32 | Tamaño mensaje (bytes) |
| **Δ** | 15 | 16 | 29 | Distancia código RS |
| **pk_sz** | 2241 | 4481 | 7205 | Tamaño clave pública |
| **sk_sz** | 2321 | 4545 | 7285 | Tamaño clave privada |
| **ct_sz** | 4433 | 8929 | 14418 | Tamaño texto cifrado |
| **ss_sz** | 32 | 32 | 32 | Tamaño secreto compartido |

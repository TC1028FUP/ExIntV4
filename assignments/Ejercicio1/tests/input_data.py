# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    [2, 3, 5, 18, 0, 21, -1, 3],
    ["Ingresa números positivos, para terminar de capturar ingresa un negativo",">>> ", ">>> ", ">>> ", 
    ">>> ", ">>> ", ">>> ", ">>> ", "[2, 3, 5, 18, 0, 21]", "Múltiplos de: ",
    "[3, 18, 0, 21]", "[2, 5]"],
    ["La salida no cumple con el caso de prueba."]
    ),
    # Test case 2
    (
    ["-1", "-1"],
    ["Ingresa números positivos, para terminar de capturar ingresa un negativo",">>> ","[]","Múltiplos de: ","Error"],
    ["Qué pasa si de entrada recibes un -1 y el múltiplo no es un número positivo"]
    )
    ]

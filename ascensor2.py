def getAllRequestInCertainDirection(requests, direction, floor):
    requestInDirection = [] # Lista de solicitudes en la dirección actual
    if direction == 1: # Si la dirección es subiendo
        for x in requests:
            if x > floor:
                requestInDirection.append(x)
        return sorted(requestInDirection) # Se ordenan las solicitudes de menor a mayor(Para poder subir)
    elif direction == 0: # Si la dirección es bajando
        for x in requests:
            if x < floor:
                requestInDirection.append(x)
        return sorted(requestInDirection, reverse=True) # Se ordenan las solicitudes de mayor a menor(Para poder bajar)

def simulateElevator(floorRequests, startFloor):
    direction = 1 if floorRequests[0] > startFloor else 0  # 1: subiendo. 0: bajando. Definir la dirección inicial
    actualFloorIterative = startFloor # Piso actual en la simulación
    while floorRequests: # Mientras haya solicitudes pendientes
        print('Elevador en el piso:', actualFloorIterative)  # Se imprime en donde está el elevador
        userInput = input('Piso:')     
        if userInput != '' and userInput.isnumeric():
            floorRequests.append(int(userInput))
            print("Piso ingresado:", userInput) # Se imprime el piso ingresado
        
        if actualFloorIterative == floorRequests[0]: # Si el elevador está en un piso solicitado, entonces se realiza el proceso
            actualFloor = floorRequests.pop(0) # Se trae la solicitud del piso actual
            print('Elevador se detiene en piso:', actualFloor) # El elevador se detuvo en ese piso
            uppers = getAllRequestInCertainDirection(floorRequests, 1, actualFloor) # Se obtienen las solicitudes uppers
            lowers = getAllRequestInCertainDirection(floorRequests, 0, actualFloor) # Se obtienen las solicitudes lowers
            if direction == 1: # Si la dirección es subiendo
                if len(uppers) == 0: # Si no hay solicitudes uppers, se actualiza la dirección(Misma logica)
                    direction = 0
                floorRequests = uppers + lowers # Se actualiza la lista de solicitudes
            else: # Si la dirección es bajando
                if len(lowers) == 0: # Si no hay solicitudes lowers, se actualiza la dirección(Misma logica)
                    direction = 1
                floorRequests = lowers + uppers # Se actualiza la lista de solicitudes
        print('Direccion:', "Subiendo" if direction == 1 else "Bajando") # Se imprime la dirección
        print('Pisos pendientes:', floorRequests) # Se imprime la lista de solicitudes pendientes
        actualFloorIterative += 1 if direction == 1 else -1 # Se actualiza el piso actual
        print()
simulateElevator([5, 29, 13, 10], 4)

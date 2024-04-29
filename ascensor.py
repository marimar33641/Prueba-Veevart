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

def simulateElevator(floorRequests, startFloor, inputFloorMap):
    direction = 1 if floorRequests[0] > startFloor else 0  # 1: subiendo. 0: bajando. Definir la dirección inicial
    actualFloorIterative = startFloor # Piso actual en la simulación
    while floorRequests: # Mientras haya solicitudes pendientes
        if actualFloorIterative == floorRequests[0]: # Si el elevador está en un piso solicitado, entonces se realiza el proceso
            actualFloor = floorRequests.pop(0) # Se trae la solicitud del piso actual
            print('Elevador se detiene en piso:', actualFloor) # El elevador se detuvo en ese piso
            if actualFloor in inputFloorMap.keys(): # Si hay una solicitud de ascensor en el piso actual
                floorRequests.append(inputFloorMap[actualFloor]) # Se agrega la solicitud del piso ingresado
                print("Piso ingresado:", inputFloorMap[actualFloor]) # Se imprime el piso ingresado
                del inputFloorMap[actualFloor] # Se elimina la solicitud del piso actual
            
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
        print('Elevador en el piso:', actualFloorIterative) # Se imprime en donde está el elevador
        print('Direccion:', "Subiendo" if direction == 1 else "Bajando") # Se imprime la dirección
        actualFloorIterative += 1 if direction == 1 else -1 # Se actualiza el piso actual
        print()
simulateElevator([5, 29, 13, 10], 4, {5: 2, 29: 10, 13: 1, 10: 1})
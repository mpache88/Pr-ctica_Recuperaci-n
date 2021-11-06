firstdevice = input("Enter device name: Cisco 1941 Router")
lastdevice = input("Enter device name: Cisco 2950 Catalyst Switch")
enddevice = input("Enter device name: Salir")
print = input("TODO LISTO!")
file = open("devices.txt", "a")
while True:
    newItem = input("Enter device name: ")
    if newItem == "exit":
        print("TODO LISTO!")
        break
    file.write(newItem + "\n")
file.close()


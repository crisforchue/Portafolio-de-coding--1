import os 

shutdown = input("Deseas apagar la laptop? (si/no)")

if shutdown.lower() == "si":
    os.system('shutdown /s /t 1')
else:
    exit()

    
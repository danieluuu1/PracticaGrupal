import socket
import threading
import time

# ═══════════════════════════════════════
#   LAPTOP 1 - Arranca como Super-nodo
# ═══════════════════════════════════════
# Solo cambia esta IP por la tuya:
MI_IP  = "192.168.1.10"   # <-- pon tu IP aqui (ipconfig en windows)
PUERTO = 9000

es_supernodo = True
print("="*45)
print("   LAPTOP 1 - RED P2P JERARQUICA")
print("="*45)
print(f"⭐ Soy el SUPER-NODO principal")
print(f"📍 Mi IP: {MI_IP}:{PUERTO}")
print(f"⏳ Esperando que las otras laptops se conecten...\n")

# ── Servidor: responde a los demas nodos ──
def servidor():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', PUERTO))
    s.listen(10)

    while True:
        try:
            conn, addr = s.accept()
            msg = conn.recv(1024).decode().strip()

            if msg == "HAY_SUPERNODO":
                conn.send("SI".encode())
                print(f"✅ Nodo {addr[0]} se conecto a mi como nodo normal")

            elif msg.startswith("MENSAJE:"):
                contenido = msg.replace("MENSAJE:", "")
                print(f"\n📩 Mensaje recibido de {addr[0]}: {contenido}")
                conn.send("OK".encode())

            elif msg == "QUIEN_SOY":
                conn.send(f"SUPERNODO:{MI_IP}".encode())

            conn.close()
        except:
            pass

# ── Hilo del servidor ──
t = threading.Thread(target=servidor, daemon=True)
t.start()

# ── Menu ──
while True:
    print("\n" + "-"*35)
    print("1. Enviar mensaje a otro nodo")
    print("2. Ver mi estado")
    print("3. Salir (simula que el Super-nodo se apaga)")
    print("-"*35)
    op = input("Opcion: ").strip()

    if op == "1":
        ip   = input("IP destino: ").strip()
        texto = input("Mensaje: ").strip()
        try:
            c = socket.socket()
            c.settimeout(3)
            c.connect((ip, PUERTO))
            c.send(f"MENSAJE:{texto}".encode())
            c.recv(1024)
            c.close()
            print(f"✅ Mensaje enviado a {ip}")
        except:
            print(f"❌ No se pudo conectar con {ip}")

    elif op == "2":
        print(f"\n📍 Mi IP: {MI_IP}")
        print("⭐ Soy: SUPER-NODO")

    elif op == "3":
        print("\n💀 Cerrando Super-nodo... las otras laptops elegiran uno nuevo!")
        break

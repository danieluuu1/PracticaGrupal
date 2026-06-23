import socket
import threading
import time

# ═══════════════════════════════════════
#   LAPTOP 2 - Nodo normal
# ═══════════════════════════════════════
# Solo cambia estas IPs:
MI_IP        = "192.168.1.11"   # <-- pon tu IP aqui (ipconfig en windows)
IP_LAPTOP1   = "192.168.1.10"   # <-- IP de Laptop 1
IP_LAPTOP3   = "192.168.1.12"   # <-- IP de Laptop 3
PUERTO       = 9000

es_supernodo = False
supernodo_ip = None

print("="*45)
print("   LAPTOP 2 - RED P2P JERARQUICA")
print("="*45)
print(f"📍 Mi IP: {MI_IP}:{PUERTO}")
print(f"🔍 Buscando Super-nodo en la red...\n")

# ── Buscar supernodo ──
def buscar_supernodo():
    global supernodo_ip
    for ip in [IP_LAPTOP1, IP_LAPTOP3]:
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, PUERTO))
            s.send("HAY_SUPERNODO".encode())
            r = s.recv(1024).decode()
            s.close()
            if r == "SI":
                supernodo_ip = ip
                return True
        except:
            continue
    return False

# ── Convertirse en supernodo ──
def ser_supernodo():
    global es_supernodo, supernodo_ip
    es_supernodo = True
    supernodo_ip = MI_IP
    print("\n" + "="*45)
    print("⭐  SOY EL NUEVO SUPER-NODO!")
    print(f"⭐  IP: {MI_IP}")
    print("="*45 + "\n")

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
                if es_supernodo:
                    conn.send("SI".encode())
                    print(f"✅ Nodo {addr[0]} se conecto a mi como nodo normal")
                else:
                    conn.send("NO".encode())

            elif msg.startswith("MENSAJE:"):
                contenido = msg.replace("MENSAJE:", "")
                print(f"\n📩 Mensaje recibido de {addr[0]}: {contenido}")
                conn.send("OK".encode())

            conn.close()
        except:
            pass

# ── Monitor: detecta si el supernodo cayo ──
def monitor():
    while True:
        time.sleep(5)
        if es_supernodo:
            continue
        print("🔍 Verificando si el Super-nodo sigue activo...")
        if not buscar_supernodo():
            print("⚠️  Super-nodo caido! Esperando para ver si otro toma el rol...")
            time.sleep(2)
            if not buscar_supernodo():
                ser_supernodo()

# ── Inicio ──
t_srv = threading.Thread(target=servidor, daemon=True)
t_srv.start()

time.sleep(1)

if buscar_supernodo():
    print(f"💻 Me uno como nodo normal")
    print(f"🔗 Conectado al Super-nodo: {supernodo_ip}")
else:
    print("🚀 No hay Super-nodo, yo me convierto en Super-nodo!")
    ser_supernodo()

t_mon = threading.Thread(target=monitor, daemon=True)
t_mon.start()

# ── Menu ──
while True:
    print("\n" + "-"*35)
    print("1. Enviar mensaje a otro nodo")
    print("2. Ver mi estado")
    print("3. Salir")
    print("-"*35)
    op = input("Opcion: ").strip()

    if op == "1":
        ip    = input("IP destino: ").strip()
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
        if es_supernodo:
            print("⭐ Soy: SUPER-NODO")
        else:
            print("💻 Soy: Nodo normal")
            print(f"🔗 Super-nodo actual: {supernodo_ip or 'buscando...'}")

    elif op == "3":
        print("👋 Cerrando nodo...")
        break

# PracticaGrupal
# P2P Jerárquico - Demostración de Red Distribuida

## 🎯 ¿Qué es este ejercicio?

Este proyecto demuestra cómo funciona una **red P2P (Peer-to-Peer) Jerárquica**, donde 3 laptops se comunican entre sí por WiFi ejecutando el mismo programa. Lo especial es que **el sistema elige automáticamente quién controla la red**, sin intervención manual.

---

## 📋 ¿Cómo funciona? Paso a paso

### El flujo completo de la demostración:

1. **Las 3 laptops inician el programa**
   - Cada una ejecuta su archivo Python correspondiente
   - Se conectan automáticamente entre sí por la red WiFi

2. **La primera laptop que se conecta se vuelve Super-nodo**
   - El Super-nodo es como el "coordinador" de la red
   - Es quien gestiona la comunicación entre todos

3. **Las otras dos laptops se conectan como nodos normales**
   - Se registran con el Super-nodo
   - Reciben órdenes de él

4. **Apagamos la laptop que es Super-nodo** (simulamos una caída)
   - Cerramos el programa de la laptop 1
   - La red pierde su coordinador

5. **Las laptops restantes detectan que el Super-nodo desapareció**
   - En pocos segundos, se dan cuenta de que no hay respuesta

6. **Una de las laptops se elige a sí misma como nuevo Super-nodo**
   - ¡SIN QUE NADIE LE DIGA QUE LO HAGA!
   - El sistema lo decide automáticamente

7. **La red sigue funcionando perfectamente** ✅
   - Como si nada hubiera pasado
   - La comunicación continúa

### ¿Por qué esto es importante? 🤔

Este ejercicio demuestra que:
- **No hay un punto único de fallo**: Si el líder cae, otro toma su lugar
- **El sistema es autónomo**: Nadie tiene que decidir manualmente quién manda
- **La red es resiliente**: Continúa funcionando incluso con cambios
- **El P2P Jerárquico es inteligente**: El orden importa, pero el sistema se auto-organiza

---

## 📁 Los 3 archivos del proyecto

| Archivo | Laptop | Rol | Descripción |
|---------|--------|-----|-------------|
| `laptop1.py` | Compañero 1 | ⭐ Super-nodo | Arranca primero y toma el control |
| `laptop2.py` | Compañero 2 | 💻 Nodo normal | Se conecta al Super-nodo |
| `laptop3.py` | Tú | 💻 Nodo normal | Se conecta al Super-nodo |

---

## ⚙️ Configuración inicial: Cambiar las IPs

Antes de ejecutar cualquier programa, **cada persona debe actualizar las direcciones IP** en su archivo Python.

### Paso 1: Encuentra tu IP

En **Windows**, abre la terminal y escribe:
```bash
ipconfig
```

Busca la línea que dice `IPv4 Address` (algo como `192.168.X.X`)

### Paso 2: Edita tu archivo Python

Abre tu archivo (laptop1.py, laptop2.py o laptop3.py) y busca estas líneas al inicio:

```python
MI_IP      = "192.168.1.X"   # ← Cambia esto a TU IP
IP_LAPTOP1 = "192.168.1.X"   # ← IP del compañero 1
IP_LAPTOP2 = "192.168.1.X"   # ← IP del compañero 2
```

**Ejemplo real:**
```python
MI_IP      = "192.168.1.45"   # Mi laptop
IP_LAPTOP1 = "192.168.1.52"   # IP de Juan
IP_LAPTOP2 = "192.168.1.78"   # IP de María
```

---

## 🚀 Orden de ejecución (¡ESTO ES IMPORTANTE!)

**Todos deben estar en la misma red WiFi antes de empezar**

1. **Primero**: Compañero 1 ejecuta:
```bash
   python laptop1.py
```
   ➜ Verá: `"🌟 SOY EL SUPER-NODO"`

2. **Después de 2 segundos**: Compañero 2 ejecuta:
```bash
   python laptop2.py
```
   ➜ Verá: `"✅ Conectado al Super-nodo"`

3. **Luego de otros 2 segundos**: Tú ejecutas:
```bash
   python laptop3.py
```
   ➜ Verá: `"✅ Conectado al Super-nodo"`

**⚠️ Nota**: Si ejecutas todo al mismo tiempo, puede que haya confusión sobre quién es el Super-nodo. ¡Espera unos segundos entre cada ejecución!

---

## 🎥 Cómo hacer la demostración (lo que el profesor verá)

Sigue estos pasos para demostrar que el sistema funciona:

### ✅ Paso 1: Inicialización
- Los 3 compañeros ejecutan su código en orden (con 2 segundos de diferencia)
- Deberías ver 3 ventanas de terminal mostrando conexiones

### ✅ Paso 2: Confirmación del Super-nodo
- En la terminal de Laptop 1 debe aparecer: `"🌟 SOY EL SUPER-NODO"`
- En las terminales de Laptop 2 y 3 debe aparecer: `"✅ Conectado al Super-nodo"`

### ✅ Paso 3: Simular una caída
- En la terminal de Laptop 1, elige la opción `3` (o cierra directamente)
- Esto simula que el Super-nodo se "apaga"

### ✅ Paso 4: El cambio automático
- **En 5-10 segundos**, una de las otras laptops detectará la caída
- Verás el mensaje: `"🌟 SOY EL NUEVO SUPER-NODO"`
- ¡Y eso es! El sistema se auto-reparó

### ✅ Paso 5: Verificación final
- Las laptops restantes mostrarán: `"✅ Conectado al nuevo Super-nodo"`
- La red sigue funcionando sin intervención manual

---

## 🎓 Lo que demuestra este proyecto

| Concepto | Lo que ves |
|----------|-----------|
| **Resiliencia** | La red no muere si cae un nodo |
| **Auto-elección** | El sistema elige un líder sin intervención |
| **P2P Jerárquico** | Hay orden, pero es flexible |
| **Detección de fallos** | El sistema nota rápidamente cuando algo falla |
| **Red distribuida** | Ninguna laptop es indispensable |

---

## ⚡ Consejos prácticos

- 🔗 **Conexión WiFi estable**: Asegúrate de que todas las laptops estén en la MISMA red
- ⏱️ **Sincronización**: Respeta los 2 segundos entre ejecuciones
- 📱 **Sin VPN**: Desactiva cualquier VPN mientras haces la prueba
- 🖥️ **Firewall**: Permite que Python use la red en tu firewall
- 🔄 **Para reintentar**: Cierra todo con `Ctrl+C` y comienza de nuevo

---

## ❓ ¿Qué pasa si algo sale mal?

| Problema | Solución |
|----------|----------|
| "Connection refused" | Verifica que las IPs sean correctas y estén actualizadas |
| Las laptops no se ven | Comprueba que todas estén en la misma red WiFi |
| El Super-nodo no se elige | Espera 10 segundos, a veces tarda un poco |
| El programa no avanza | Cierra con `Ctrl+C` y reinicia desde cero |

---

¡**Listo para demostrar cómo funciona una red P2P resiliente! 🚀**

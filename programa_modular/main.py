import monitor

def main():
    hosts = ["192.168.1.1", "192.168.1.2", "10.0.0.1"]
    resultados = monitor.verificar_disponibilidad(hosts)
    for host, disponibilidad in resultados.items():
        print(f"Host: {host}, Disponibilidad: {disponibilidad}")

if __name__ == "__main__":
    main()

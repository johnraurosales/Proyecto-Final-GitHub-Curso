#!/usr/bin/env python3
"""
Sistema de Gestión de Pacientes para Clínica Médica
Archivo principal de la aplicación
"""

import sys
from datetime import datetime

def main():
    """
    Función principal del sistema
    """
    print("="*60)
    print("Sistema de Gestión de Pacientes - Clínica Médica")
    print("="*60)
    print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("\nBienvenido al sistema de gestión de pacientes")
    print("\nOpciones disponibles:")
    print("1. Registrar nuevo paciente")
    print("2. Buscar paciente")
    print("3. Agendar cita")
    print("4. Ver historial clínico")
    print("5. Generar reporte")
    print("6. Salir")
    print("\n" + "="*60)

if __name__ == "__main__":
    main()

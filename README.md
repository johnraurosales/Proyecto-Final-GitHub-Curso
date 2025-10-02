# Sistema de Gestión de Pacientes para Clínica Médica

## Descripción
Sistema completo de gestión de pacientes desarrollado en Python para clínicas médicas. Este proyecto permite administrar la información de pacientes, citas médicas, historiales clínicos y generar reportes.

## Objetivos del Proyecto
- Proporcionar una interfaz intuitiva para la gestión de pacientes
- Mantener registros organizados de historiales médicos
- Facilitar la programación y seguimiento de citas
- Generar reportes y estadísticas clínicas
- Asegurar la privacidad y seguridad de los datos médicos

## Características Principales
- Registro y gestión de pacientes
- Historial clínico completo
- Sistema de citas médicas
- Generación de reportes
- Base de datos segura
- Interfaz de usuario amigable

## Requisitos del Sistema
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Base de datos SQLite (incluida con Python)

## Instalación
### Clonar el repositorio
```bash
git clone https://github.com/johnraurosales/Proyecto-Final-GitHub-Curso.git
cd Proyecto-Final-GitHub-Curso
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Configurar la base de datos
```bash
python src/database/setup.py
```

## Uso

### Iniciar la aplicación
```bash
python src/main.py
```

### Comandos principales
- Registrar nuevo paciente: `python src/pacientes.py --nuevo`
- Agendar cita: `python src/citas.py --agendar`
- Generar reporte: `python src/reportes.py --generar`

## Estructura del Proyecto
```
Proyecto-Final-GitHub-Curso/
├── src/              # Código fuente
├── docs/             # Documentación
├── tests/            # Pruebas unitarias
├── requirements.txt  # Dependencias
└── README.md         # Este archivo
```

## Tecnologías Utilizadas
- Python 3.x
- SQLite
- Flask (para interfaz web)
- SQLAlchemy (ORM)

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios propuestos.

## Licencia
Este proyecto está bajo la Licencia MIT. Ver archivo LICENSE para más detalles.

## Autor
John Rauro Sales

## Contacto
Para preguntas o sugerencias, por favor abre un issue en el repositorio.

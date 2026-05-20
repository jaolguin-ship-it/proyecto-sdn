# Solución Profesional: Extractor Automatizado de Indicadores Económicos

**Asignatura:** Programación y Redes Virtualizadas (DRY7122)  
**Entorno de Despliegue:** Laboratorio Presencial / Infraestructura Virtualizada

## 1. Definición del Contexto (Narrativa)
* **Stakeholder:** Administrador de Redes y Conectividad / Ingeniero de Soporte TI.
* **Propuesta de Valor (Problema/Solución):** En entornos de infraestructura tecnológica corporativa, los costos de hardware, licencias internacionales e insumos se cotizan frecuentemente en monedas extranjeras (Dólar/Euro) o unidades indexadas (UF). El cálculo manual de estos valores retrasa la generación de presupuestos y puede inducir a errores críticos de facturación. Esta herramienta automatiza la consulta instantánea de los indicadores económicos clave directamente desde una API confiable, procesando los datos en tiempo real y desplegándolos por consola de manera limpia para facilitar la toma de decisiones técnicas y presupuestarias rápidas en el laboratorio.

## 2. Guía de Configuración
* **Tecnologías Utilizadas:** Python 3.9, Docker, Git.
* **Seguridad y Variables de Entorno:** Para cumplir con las políticas de seguridad técnica y evitar el "hardcoding", la aplicación recupera la dirección base del endpoint mediante la variable de entorno `API_URL_PROYECTO`, asegurando que no se expongan enlaces ni credenciales fijas en el código fuente.

## 3. Instrucciones de Ejecución (Comandos Docker)
Para construir la imagen y desplegar el contenedor de forma automatizada en el laboratorio, ejecute los siguientes comandos:

1. **Dar permisos de ejecución al script (opcional en entornos Linux):**
   ```bash
   chmod +x build.sh

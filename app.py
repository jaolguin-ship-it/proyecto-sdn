import os
import requests

def consultar_api():
    # 1. SEGURIDAD: Recuperamos la URL o parámetros desde variables de entorno [cite: 33, 61]
    # Aunque la API sea pública, esto demuestra el uso obligatorio de la librería 'os'[cite: 33, 54].
    api_url = os.getenv('API_URL_PROYECTO', 'https://mindicador.cl/api')
    
    print("Consultando indicadores económicos...")
    
    try:
        # Realizamos la petición con un timeout de 10 segundos para prevenir bloqueos [cite: 31]
        respuesta = requests.get(api_url, timeout=10)
        
        # ERROR 1: Lanza una excepción si el status_code no es 200 (ej. 404, 500) [cite: 31]
        respuesta.raise_for_status()
        
        # Si la respuesta es exitosa, transformamos a JSON
        datos = respuesta.json()
        
        # PROCESAMIENTO: Extraemos al menos 3 campos de datos requeridos [cite: 31, 54]
        uf_valor = datos['uf']['valor']
        dolar_valor = datos['dolar']['valor']
        euro_valor = datos['euro']['valor']
        
        # RESULTADO POR CONSOLA (Requisito de la consigna) 
        print("\n--- RESULTADOS DEL STAKEHOLDER ---")
        print(f"Valor de la UF: ${uf_valor}")
        print(f"Valor del Dólar: ${dolar_valor}")
        print(f"Valor del Euro: ${euro_valor}")
        print("----------------------------------")
        
    # MANEJO DE ERRORES: ≥4 tipos de errores configurados de forma robusta [cite: 31, 54]
    except requests.exceptions.HTTPError as error_http:
        print(f"[Error 1 - HTTP] La API respondió con un error (ej. 404/500): {error_http}")
    except requests.exceptions.Timeout:
        print("[Error 2 - Timeout] El tiempo de espera para conectar con la API ha expirado.")
    except requests.exceptions.ConnectionError:
        print("[Error 3 - Conexión] No se pudo establecer conexión de red con el servidor de la API.")
    except KeyError as error_llave:
        print(f"[Error 4 - Estructura] El campo {error_llave} no fue encontrado en la respuesta JSON.")
    except Exception as e:
        print(f"[Error Genérico] Ocurrió un fallo inesperado: {e}")

if __name__ == "__main__":
    consultar_api()
# check_your_password

_Herramienta para verificar si una contraseña existe en un "wordlist" público y descargar los diccionarios encontrados.
Eventualmente, se añade la funcionalidad de mostrar contraseñas similares, pero con distintos patrones._

## Pre config 📋

Para instalar las librerías necesarias, ejecute el siguiente comando.

```
pip install -r requirements.txt
```

## Deploy 🚀

Ejecución para consulta simple

```
python3 encuentra_tu_pass.py -p tu_password
```

Para consultar y descargar los diccionarios
```
python3 encuentra_tu_pass.py -p tu_password -d
```

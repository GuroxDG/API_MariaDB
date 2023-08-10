# __FASTAPI MariaDB__

proyecto realizado con el fin de reforzar el uso de FastAPI, obteniendo información de Alphaventage

## __Requerimientos__
1. Instalar las librerías descritas en el archivo requirements.txt
2. El proyecto fue implementado con python 3.11 debido a que también se deseaba usar la librería de pandas 2.0
3. Es necesario crear un archivo __"credenciales.ini"__ en la raíz del proyecto en donde se definan las credenciales de la conección a la base de datos de mariadb de la sigueinte forma
```{.ini}
[CREATE]
user=
password=
host=
port=
database=

[GET]
API_KEY=
```
4. Continuara...
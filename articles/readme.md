[PRUEBA CECOTEC]

En este pequeño documento se describen los pasos necesarios y los recursos que existen para la comprobación del funcionamiento del ejercicio de prueba.

REQUISITOS :wrench:

La aplicación ha sido desarrollada en Python 3.6, por lo tanto la instalación del mismo es indispensable. Asimismo, deberemos contar con Ruby :gem: instalado en nuestro ordenador
para poder instalar el cliente de correo para depuración Mailcatcher :email: . La instalación de este cliente es recomendable para poder comprobar que los correos se envían correctamente. No existen más modulos del sistema necesarios para hacer funcionar la aplicación.
A nivel de módulos y librerías utilizados para el desarrollo existen varios que son indispensables para el correcto funcionamiento. Todos se encuentran recopilados en el directorio /requirements/requirements.txt. Con lo que una simple instalación :cd: de todos ellos debería bastar para hacer funcionar la API.

PROBAR LA API :test_tube:

Para probar la api existe un superusuario creado con las siguientes credenciales:

:bust_in_silhouette: Usuario cecotec
:no_entry: Contraseña 12341234

Una vez que accedamos podremos crear más usuarios con las contraseñas que deseemos dentro del panel de administración de django. Para ello basta con dirigirnos al apartado AUTHENTICATION AND AUTHORIZATION :white_check_mark: e introducir las credenciales que deseemos. También se ha implementado OAuth2, por lo que se recomienda, si se desea probar los endpoints del módulo Article, crear una OAuth2 Application con las credenciales que deseemos para tal usuario. Pueden usarse para probar los endpoints las asignadas al superusuario cecotec, las cuales se describen a continuación:

Client ID 1234asdf
Client secret asdf1234

Si decidimos crear token para un nuevo usuario deberemos asegurarnos de que sean 'Client-type': Confidential y 'Authorization grant type': Client credentials. Una vez que hayamos creado la appication o bien decidamos utilizar la que existe para el superusuario cecotec deberemos obtener el token de autenticación en la url http://localhost:8000/o/token/.
Siempre y cuando ya tengamos el token podremos probar los endpoints de Articles. Hay dos endpoints creados funcionales: un GET que trae todos los artículos almacenados y un POST para crear artículos nuevos. No se han implementado el resto de los endpoints. Se adjuntan exportados los endpoints en la carpeta /requests del proyecto para poder importarlos al cliente POSTMAN :rocket:.

Tanto como si decidimos crear artículos nuevos desde el panel de administración como si deseamos hacerlo desde los endpoints, estos podrán ser asociados, a través del panel de administración, a la entidad Bill, que simula un carrito de la compra. Para realizar esta acción deberemos haber creado previamente un User :sunglasses: . No obstante este usuario deberíamos crearlo desde el apartado 'Users' del panel de administración y no desde el de 'Authentication and Authorization'. Cuando hayamos completado su creación, podremos volver a generar un "carrito de la compra" :shopping_cart: dirigiéndonos a la entidad 'Bill' del apartado 'Billing'. Añadiremos una factura nueva, la vincularemos al usuario que deseemos y añadiremos tantos artículos como creamos conveniente. Una vez que guardemos la factura :book:, podremos visitar nuestra página donde se ejecuta el cliente de correo Mailcatcher, http://localhost:1080, y comprobar que se envía el correo con el archivo csv adjunto. 

DOCUMENTACIÓN CON SWAGGER DOCS :memo:

Existe documentación de los endpoints de 'Article' esto es, /article GET y POST. Para visualizarlo, simplemente deberemos levantar la API y acceder a http://localhost:8000/docs.
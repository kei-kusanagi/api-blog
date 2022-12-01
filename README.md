# Enlace para registro de usuarios

El enlace http://127.0.0.1:8000/account/register/ nos ayudara a crear usuarios, los cuales tendrán sólo el rango de usuario normal (no de Staff o Administrador), los datos que debemos pasar en el JSON por medio de una petición 'POST' son:

```Json
{

    "username": "NEW_USERNAME",

    "email": "USER_EMAIL",

    "password": "USER_PASSWORD",

    "password2": "USER_PASSWORD"

}
```

Esto como respuesta nos dará el siguiente JSON:

```Json
{

    "response": "Registration Successful!",

    "username": "USER_PASSWORD",

    "email": "USER_EMAIL",

    "token": "688779351aac04259ee2af6976e79ead9da0df80"

}
```

Este Token se quedara guardado en la base de datos hasta hacer #Logout

## Errores en registro

En caso de usar un usuario ya existente, en la base de datos, nos regresara el siguiente mensaje de error:

```Json
{

    "username": [

        "A user with that username already exists."

    ]

}
```

Si el Email introducido ya esta registrado con otro usuario, en la base de datos nos regresara el siguiente error:

```Json
{

    "error": "Email already exists!"

}
```


Si nuestra contraseña y su confirmación no coinciden, nos regresara el siguiente mensaje de error:

Entrada
```Json
{

    "username": "NEW_USERNAME",
    "email": "USER_EMAIL",
    "password": "USER_PASSWORD",
    "password2": "USER_PASS"

}
```

Salida
```Json
{

    "error": "P1 and P2 should be same!"

}

```


# Enlace para hacer Login

Con el enlace http://127.0.0.1:8000/account/login/ podemos hacer Log in de nuestros usuarios que ya creamos con el anterior método, solo debemos pasarle una petición 'POST' y como body el Json con el usuario y contraseña registradas, esto creara (si no lo tiene ya) el token de este usuario en la base de datos.

Entrada
```Json
{

    "username": "USERNAME",

    "password": "USER_PASSWORD"

}
```

Salida
```Json
{

    "token": "1c86186cb1ea5c5ffcb7311b8f77d9e618531cd2"

}
```


## Errores en Login


En caso de mandar mal el username o el password nos regresara el mismo error:

```Json
{

    "non_field_errors": [

        "Unable to log in with provided credentials."

    ]

}
```


# Logout

Al mandar la petición de logout se destruirá el token asignado al usuario del token que estamos pasando. La petición será al link http://127.0.0.1:8000/account/logout/ 

Tendrá que ser un 'POST' y dentro del body pasar como headers la KEY Authorization y como VALUE Token ``"el token del usuario que hará logout"``

![image](/IMG/Pasted%20image%2020221130195948.png)

## Errores al hacer Logout

Si mandamos mal la petición por que el token esta incompleto nos regresara el siguiente response

```JSON
{

    "detail": "Invalid token."

}
```


## Lista de Blog's existentes

Para obtener la lista de Blogs existentes en la base de datos de TODOS los usuarios, necesitamos mandar una petición GET al link http://127.0.0.1:8000/api/blog/ , en esta no importa si en los headers lleva algún token de autenticación ya que los permisos están configurados para que cualquier usuario, ya sea anónimo, normal, staff o admin, pueda hacer las peticiones GET que necesite sin ningún limite.

Este nos regresara un response con un JSON englobando todas las entradas existentes en orden en el que fueron creadas, mostrando primeramente el numero de "id" de la entrada, el nombre del usuario que escribió la entrada como "review_user", seguido del texto de la entrada mostrándolo como "entrada" y la fecha en que fue creado como "fecha"


```Json
[

    {

        "id": 7,

        "review_user": "keikusanagi",

        "titulo": "Primera entrada - edit",

        "entrada": "ljkahflkaklfafa - edit",

        "fecha": "2022-11-29T22:16:16.202267Z"

    },

    {

        "id": 8,

        "review_user": "test",

        "titulo": "hola 2",

        "entrada": "hola otra ves - actualizado por administrador",

        "fecha": "2022-11-29T19:52:06.271416Z"

    },

    {

        "id": 9,

        "review_user": "keikusanagi",

        "titulo": "Token",

        "entrada": "Intento de crear uina entrada con un token",

        "fecha": "2022-11-29T23:42:31.068123Z"

    }

]
```

## Entrada de Blog

Para crear una entrada de Blog mandaremos una petición POST al link 
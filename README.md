# Enlace para registro de usuarios

El enlase http://127.0.0.1:8000/account/register/ nos ayudara a crear usuarios, lso cuales tendran solo el rango de usuario normal (node Staff o Administrador), los datos que devemos pasar en el JSON por medio de una peticion 'POST' son:

```Json
{

    "username": "NEW_USERNAME",

    "email": "USER_EMAIL",

    "password": "USER_PASSWORD",

    "password2": "USER_PASSWORD"

}
```

Esto como respuesta nos dara el siguiente JSON

```Json
{

    "response": "Registration Successful!",

    "username": "USER_PASSWORD",

    "email": "USER_EMAIL",

    "token": "688779351aac04259ee2af6976e79ead9da0df80"

}
```

Este Token se quedara guardado en la base de datos hasta hacer #Logout

## Erores en registro

En caso de usar un usuario ya existente en la base de datos nos regresara el siguiente mensaje de error:

```Json
{

    "username": [

        "A user with that username already exists."

    ]

}
```

Si el Email introducido ya esta registrado con otro usuario en la base de datos, nos regresara el siguiente eror:

```Json
{

    "error": "Email already exists!"

}
```


Si nuestra contraseña y su confirmacion no coinciden nos regresara el siguiente mensaje de error:

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

Con el enlase http://127.0.0.1:8000/account/login/ podemos hacer Log in de nuestros usuarios que ya creeamos con el anterior metodo, solo devemos pasarle una peticion 'POST' y como body el Json con el usuario y contraseña registradas, esto crera (si no lo tiene ya) el token de este usuario en la base de datos.

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

Al mandar la peticion de logout se destruira el token asignado al usuario del token que estamos pasando, la peticion sera al link http://127.0.0.1:8000/account/logout/ tendra que ser un 'POST' y dentro del body pasar como headers la KEY Authorization y como VALUE Token 'el token del usuario que hara logout'

![[Pasted image 20221130195948.png]]

## Errores al hacer Logout

Si mandamos mal la peticion por que el token esta incompleto nos regresara el sigueinte response

```JSON
{

    "detail": "Invalid token."

}
```
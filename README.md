# Proyecto Final: Blog
## Coderhouse, comisión 31075
### Marzo - Junio 2022

---
### Autores
* César Aracena: Encargado de la creación del sistema de sesión, búsqueda y APIs
* José Orozco: Encargado de la creación del sistema de blog y creación de nuevos artículos
* Esteban Orozco: Encargado de la creación del sistema de contacto y acerca de nosotros

---
### Descripción

Este es el repositorio del proyecto final grupal del curso de Python de Coderhouse, comisión 31075, donde creamos un blog utilizando Django 4.0.4 y Python 3.10. El mismo cuenta con un listado de artículos en forma de blog que pueden ser vistos por cualquier visitante. Cuenta con un sistema de manejo de sesión propio de Django con el cual los visitantes pueden registrarse. Una vez iniciada su sesión, los visitantes pueden dejar comentarios en los artículos e inclusive escribir nuevos artículos.

Además cuenta con un formulario de contacto, una página que muestra información de nosotros (los autores del proyecto) y un sistema de búsqueda que devuelve los artículos según las coincidencias en los títulos y contenido de los artículos. También hay un sistema de APIs que provee acceso al listado de artículos, detalles sobre un artículo en particular, listado de comentarios de un artíuclo en particular, lista de plataformas de los juegos y las etiquetas que se utilizan en cada artículo.

Elegimos extender el sistema de usuarios para que el ingreso sea utilizando una dirección de email como nombre de usuario.

---
### Hospedaje
* Sitio: Heroku https://gamerblog.herokuapp.com/
* Archivos estáticos y media: AWS S3 Buckets
* Base de datos: AWS PostgreSQL RDS
* Link a video en YouTube: https://youtu.be/VI_3vVYM08w

---
#### Acceso restringido a administradores:
- Admin

#### Acceso restringido a cualquier usuario registrado:
- Ver/Editar Mi Perfil
- Realizar comentarios en los articulos del blog
- Crear nuevo artículo (se dió permiso a todos los usuarios para poder probar el sistema)

#### Acceso irrestricto:
- Inicio / Blog
- Artículo
- Búsqueda
- Perfil de usuarios
- Acerca de nosotros
- Contáctenos
- APIs

---
### APIs

El sistema de API se puede acceder en https://gamerblog.herokuapp.com/api/ y tiene los siguientes endpoints:
- Listado de artículos: https://gamerblog.herokuapp.com/api/blog-list/
- Un artículo específico: https://gamerblog.herokuapp.com/api/blog-detail/<id del articulo>
- Comentarios de un artículo: https://gamerblog.herokuapp.com/api/comments/<id del articulo>
- Listado de etiquetas: https://gamerblog.herokuapp.com/api/tag-list/
- Listado de plataformas: https://gamerblog.herokuapp.com/api/platform-list/

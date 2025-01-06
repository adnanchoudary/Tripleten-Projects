#!/usr/bin/env python
# coding: utf-8

# 
# 
# Como parte del equipo de análisis, lo primero que debes hacer es evaluar la calidad de una muestra de datos recopilados y prepararla para analizarla posteriormente. Después, en la segunda parte de este proyecto en el segundo sprint, desarrollarás más tus habilidades y harás tu primer análisis completo, respondiendo a las necesidades del cliente.

# Estos son los datos que el cliente nos proporcionó. Tienen el formato de una lista de Python, con las siguientes columnas de datos:
# 
# - **user_id:** Identificador único para cada usuario.
# - **user_name:** El nombre del usuario.
# - **user_age:** La edad del usuario.
# - **fav_categories:** Categorías favoritas de los artículos que compró el usuario, como 'ELECTRONICS', 'SPORT' y 'BOOKS' (ELECTRÓNICOS, DEPORTES y LIBROS), etc.
# - **total_spendings:** Una lista de números enteros que indican la cantidad total gastada en cada una de las categorías favoritas.
# 

# In[ ]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]


# # Paso 1
# 
# Store 1 tiene como objetivo garantizar la coherencia en la recopilación de datos. Como parte de esta iniciativa, se debe evaluar la calidad de los datos recopilados sobre los usuarios y las usuarias. Te han pedido que revises los datos recopilados y propongas cambios. A continuación verás datos sobre un usuario o una usuaria en particular; revisa los datos e identifica cualquier posible problema.
# 

# In[ ]:


user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']


# **Opciones:**
# 
# 1. Se debe cambiar el tipo de dato de `user_id` de cadena a entero.
#     
# 2. La variable `user_name` contiene una cadena que tiene espacios innecesarios y un guion bajo entre el nombre y el apellido.
#     
# 3. El tipo de dato de `user_age` es correcto y no hay necesidad de convertirlo.
#     
# 4. La lista `fav_categories` contiene cadenas en mayúsculas. En lugar de ello, debemos convertir los valores de la lista en minúsculas.
# 

# Para cada una de las opciones, escribe en la siguiente celda markdown si la identificaste como un problema real en los datos o no. Justifica tu razonamiento. Por ejemplo, si crees que la primera opción es correcta, escríbelo y explica por qué piensas que es correcta.

# **Escribe tu respuesta y explica tu argumentación:**
# 1. Se debe cambiar el tipo de dato de user_id de cadena a entero.
# Identificado como problema real: No.
# El user_id es un identificador único que no tiene por qué ser necesariamente un número entero. Mantenerlo como una cadena permite una mayor flexibilidad, especialmente si decidimos incluir letras o caracteres especiales en los identificadores en el futuro.
# 
# 2. La variable user_name contiene una cadena que tiene espacios innecesarios y un guion bajo entre el nombre y el apellido.
# Identificado como problema real: Sí.
# Los espacios y guiones bajos innecesarios pueden causar problemas en el procesamiento y análisis de datos. Se recomienda limpiar los datos eliminando los espacios adicionales y reemplazando el guión bajo por un espacio para mantener la coherencia en el formato de los nombres.
# 
# 3. El tipo de dato de user_age es correcto y no hay necesidad de convertirlo.
# Identificado como problema real: No.
# El tipo de datos float para user_age es adecuado, ya que permite representar las edades con decimales si es necesario. No es necesario convertirlo a otro tipo de datos.
# 
# 4. La lista fav_categories contiene cadenas en mayúsculas. En lugar de ello, debemos convertir los valores de la lista en minúsculas.
# Identificado como problema real: Sí.
# La conversión de categorías favoritas a minúsculas mejora la coherencia y facilita el análisis de datos al evitar problemas de distinción entre mayúsculas y minúsculas durante consultas y comparaciones.

# # Paso 2
# 
# Vamos a implementar los cambios que identificamos. Primero, necesitamos corregir los problemas de la variable `user_name` Como vimos, tiene espacios innecesarios y un guion bajo como separador entre el nombre y el apellido; tu objetivo es eliminar los espacios y luego reemplazar el guion bajo con el espacio.
# 

# In[5]:


user_name = ' mike_reed '
user_name = user_name.strip()  # Elimina los espacios al principio y al final  # escribe tu código aquí
user_name = user_name.replace('_', ' ')  # Reemplaza el guion bajo con un espacio  # escribe tu código aquí

print(user_name)


# ********Hint********
# 
# Existe un método, `strip()`, que puede eliminar espacios al principio y al final de una cadena. Además, el método `replace()` se puede usar para reemplazar una parte de una cadena. En este caso, queremos reemplazar los guiones bajos (`_`) con espacios.
# 

# # Paso 3
# 
# Luego, debemos dividir el `user_name` (nombre de usuario o usuaria) actualizado en dos subcadenas para obtener una lista que contenga dos valores: la cadena para el nombre y la cadena para el apellido.

# In[4]:


user_name = 'mike reed'
name_split = user_name.split() # escribe tu código aquí

print(name_split)


# ********Hint********
# 
# El método `split()` se utiliza para dividir una cadena. Por defecto, utiliza un espacio como separador.
# 

# # Paso 4
# 
# ¡Genial! Ahora debemos trabajar con la variable `user_age`. Como ya mencionamos, esta tiene un tipo de datos incorrecto. Arreglemos este problema transformando el tipo de datos y mostrando el resultado final.
# 

# In[3]:


user_age = 32.0
user_age = int(user_age) # escribe tu código aquí

print(user_age)


# ********Hint********
# 
# ¿Qué tipo de datos eliminará la parte de coma flotante?
# 

# # Paso 5
# 
# Como sabemos, los datos no siempre son perfectos. Debemos considerar escenarios en los que el valor de `user_age` no se pueda convertir en un número entero. Para evitar que nuestro sistema se bloquee, debemos tomar medidas con anticipación.
# 
# Escribe un código que intente convertir la variable `user_age` en un número entero y asigna el valor transformado a `user_age_int`. Si el intento falla, mostramos un mensaje pidiendo al usuario o la usuaria que proporcione su edad como un valor numérico con el mensaje: `Please provide your age as a numerical value.` (Proporcione su edad como un valor numérico.)

# In[2]:


user_age = 'treinta y dos'

# escribe tu código aquí

try:
    user_age_int = int(user_age)
except ValueError:
    print("Please provide your age as a numerical value. (Proporcione su edad como un valor numérico.)")


# ********Hint********
# 
# Utiliza un bloque `try-except` para intentar la conversión; si falla, proporciona un mensaje claro indicando que la entrada debe ser numérica.

# # Paso 6
# 
# El equipo de dirección de Store 1 te pidió ayudarles a organizar los datos de sus clientes para analizarlos y gestionarlos mejor.
# 
# Tu tarea es ordenar esta lista por ID de usuario de forma ascendente para que sea más fácil acceder a ella y analizarla.
# 

# In[1]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

# escribe tu código aquí

# Ordenar la lista usando el método sort() directamente
users.sort(key=lambda x: x[0])

# Imprimir la lista ordenada
print(users)


# ********Hint********
# 
# Puedes utilizar el método `sort()` en la lista de usuarios para ordenarla de forma ascendente.
# 

# # Paso 7
# 
# Tenemos la información de los hábitos de consumo de nuestros usuarios, incluyendo la cantidad gastada en cada una de sus categorías favoritas. La dirección está interesada en conocer la cantidad total gastada por el usuario.
# 
# 
# Calculemos este valor y despleguémoslo.
# 

# In[6]:


fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category) # escribe tu código aquí

print(total_amount)


# ********Hint********
# 
# ¿Cuáles son los tres métodos que se pueden aplicar a una lista para calcular sus valores mínimo, máximo y total?
# 

# # Paso 8
# 
# La dirección de la empresa nos pidió pensar en una manera de resumir toda la información de un usuario. Tu objetivo es crear una cadena formateada que utilice información de las variables `user_id`, `user_name` y `user_age`.
# 
# Esta es la cadena final que queremos crear: `User 32415 is mike who is 32 years old.` (El usuario 32415 es Mike, quien tiene 32 años).
# 

# In[7]:


user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_info = f"User {user_id} is {user_name[0]} who is {user_age} years old." # escribe tu código aquí
print(user_info)



# ********Hint********
# 
# Para crear una cadena, puedes utilizar el método `format()` o f-string. Para extraer el nombre de la lista `user_name`, puedes utilizar la segmentación.
# 

# # Paso 9
# 
# La dirección también quiere una forma fácil de conocer la cantidad de clientes con cuyos datos contamos. Tu objetivo es crear una cadena formateada que muestre la cantidad de datos de clientes registrados.
# 
# Esta es la cadena final que queremos crear: `Hemos registrado datos de X clientes`.
# 

# In[10]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]


user_info = f"We have registered data on {len(users)} clients." # escribe tu código aquí
print(user_info)


# ********Hint********
# 
# Para crear una cadena, puedes utilizar el método `format()` o f-string. Para extraer la cantidad de clientes en la lista, puedes utilizar la función que devuelve la longitud de la lista.
# 

# # Paso 10
# 
# Apliquemos ahora todos los cambios a la lista de clientes. Para simplificar las cosas, te proporcionaremos una más corta.
# Debes:
# 1. Eliminar todos los espacios iniciales y finales de los nombres, así como cualquier guion bajo.
# 2. Convertir todas las edades en números enteros.
# 3. Separar todos los nombres y apellidos en una sublista.
# 
# Guarda la lista modificada como una nueva lista llamada `users_clean` y muéstrala en la pantalla.
# 

# In[12]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
]

users_clean = []

# Procesa al primer usuario
user_id_1 = users[0][0]
user_name_1 = users[0][1].strip().replace('_', ' ').split()
user_age_1 = int(users[0][2])
fav_categories_1 = users[0][3]
spendings_1 = users[0][4]
users_clean.append([user_id_1, user_name_1, user_age_1, fav_categories_1, spendings_1])

# Procesa al segundo usuario
user_id_2 = users[1][0]
user_name_2 = users[1][1].strip().replace('_', ' ').split()
user_age_2 = int(users[1][2])
fav_categories_2 = users[1][3]
spendings_2 = users[1][4]
users_clean.append([user_id_2, user_name_2, user_age_2, fav_categories_2, spendings_2])

# Procesa al tercer usuario
user_id_3 = users[2][0]
user_name_3 = users[2][1].strip().replace('_', ' ').split()
user_age_3 = int(users[2][2])
fav_categories_3 = users[2][3]
spendings_3 = users[2][4]
users_clean.append([user_id_3, user_name_3, user_age_3, fav_categories_3, spendings_3])

print(users_clean)


# ********Hint********
# 
# Para procesar a cada usuario, comienza por acceder a los elementos requeridos de la lista de usuarios. Utiliza el método `strip()` para eliminar los espacios iniciales y finales y el método `replace('_',' ')` para reemplazar los guiones bajos por espacios en los nombres. Convierte la edad a un número entero utilizando `int()`. Separa el nombre completo en nombre y apellido utilizando el método `split()`. Por último, `append` (agrega) los datos limpios a la lista `users_clean`.
# 

# ----------
# 

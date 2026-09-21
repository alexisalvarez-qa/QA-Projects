# Casos de prueba de API

| ID | Escenario | Método | Resultado esperado |
|---|---|---|---|
| API-001 | Consultar un post existente | GET | 200 y objeto JSON válido |
| API-002 | Consultar un post inexistente | GET | Respuesta 404 |
| API-003 | Crear un post con datos válidos | POST | Respuesta exitosa con los datos enviados |
| API-004 | Crear un post sin título | POST | Comportamiento documentado y respuesta validada |
| API-005 | Actualizar un post existente | PUT | Respuesta exitosa con los datos actualizados |
| API-006 | Eliminar un post existente | DELETE | Respuesta de eliminación exitosa |
| API-007 | Validar tipo de contenido | GET/POST | Se devuelve una respuesta JSON |
| API-008 | Validar estructura de respuesta | GET | Están presentes los campos esperados |

Los resultados de ejecución deben registrarse después de ejecutar la colección en Postman.
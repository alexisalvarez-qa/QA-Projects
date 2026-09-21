# Plan de pruebas — Checkout de e-commerce

## Objetivo
Validar el flujo principal de compra y checkout de una aplicación de demostración de comercio electrónico.

## Dentro del alcance
Autenticación, navegación de productos, gestión del carrito, validación del formulario de checkout y finalización del pedido.

## Fuera del alcance
Integración con proveedores de pago, infraestructura de producción, pruebas de carga y transacciones reales.

## Prioridad
P0: Disponibilidad del inicio de sesión y checkout  
P1: Carrito y selección de productos  
P2: Validaciones secundarias y observaciones de usabilidad

## Riesgos
- El usuario no puede iniciar sesión.
- No se puede agregar o eliminar un producto.
- Los productos del carrito no coinciden con la selección.
- El checkout acepta datos obligatorios inválidos.
- El pedido no puede completarse.
- Los datos inválidos generan mensajes poco claros.

## Evidencia de salida
Casos de prueba ejecutados, reportes de defectos cuando corresponda, capturas de pantalla de hallazgos importantes y un resumen de pruebas.
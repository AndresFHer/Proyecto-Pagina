# Tabla de codigo de productos
import pandas as pd
producto_id = pd.Series([100,101,102,103,104], index= ['Correas', 'Bolsos', 'Zapatos', 'Tenis', 'Carteras'])

# Tabla de productos
precio_producto = pd.Series([40000, 150000, 120000, 220000, 800000], index= ['Correa', 'Bolso', 'Zapato', 'Teni', 'Cartera'])

# Tabla de clientes
cliente = pd.Series([1072528654, 1037640871, 1037659741, 10525785], index= ['Andres Felipe Hernandez', 'Alejandra Peña', 'Erika Rivera', 'Juan Carlos'])

print("Precio y compra por cliente")
for producto, precio, cliente in zip(producto_id.index, precio_producto, cliente.index):
    print(f"Producto: {producto} -  Precio: {precio} -  Cliente: {cliente}")
    


# Dataframe de productos
datos_ventas = pd.DataFrame({
    'Producto': ['Correas', 'Bolsos', 'Zapatos', 'Tenis', 'Carteras'],
    'Tienda': ['El Tesoro', 'CC Santafe', 'Viva Envigado', 'El Tesoro', 'CC Santafe'],
    'Precio': [40000, 150000, 120000, 220000, 800000],
    'Cliente': ['Andres Felipe Hernandez', 'Alejandra Peña', 'Erika Rivera', 'Juan Carlos', 'Andres Felipe Hernandez']
})

filter = datos_ventas[(datos_ventas.Precio > 50000) & (datos_ventas.Tienda == 'El Tesoro')]
print(filter)

total = datos_ventas.groupby('Tienda')['Precio'].sum()
print(total)

venta_por_cliente = datos_ventas.groupby('Cliente')['Precio'].mean('Cliente').sum()
print(venta_por_cliente)

clientes_compras = datos_ventas.groupby('Cliente').size().reset_index(name='Cantidad_de_compras')
print(clientes_compras)


producto_mas_economico = datos_ventas.loc[datos_ventas['Precio'].idxmin()]
print(producto_mas_economico)


productos_vendidos = datos_ventas.groupby('Producto').size().reset_index(name='Cantidad_vendida')
producto_mas_vendido = productos_vendidos.loc[productos_vendidos['Cantidad_vendida'].idxmax()]
print(producto_mas_vendido)

productos_por_tienda = datos_ventas.groupby('Tienda').size().reset_index(name='Cantidad_vendida')
print(productos_por_tienda)


precio_promedio_por_tienda = datos_ventas.groupby('Tienda')['Precio'].mean().reset_index(name='Precio_promedio')
print(precio_promedio_por_tienda)

gasto_por_cliente = datos_ventas.groupby('Cliente')['Precio'].sum().reset_index(name='Gasto_total')
print(gasto_por_cliente)
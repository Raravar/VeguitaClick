--Comentarios
--Ultima modificacion: 18-06-2022

--Comentarios
--Ultima modificacion: 18-06-2022

--Tabla Tienda_Producto
COMMENT ON COLUMN tienda_producto.nombre
    IS 'Nombre del producto';
COMMENT ON COLUMN tienda_producto.precio
    IS 'Precio del producto';
COMMENT ON COLUMN tienda_producto.categoria
    IS 'Categoria del producto';
    
--Tabla TipoUsuario
COMMENT ON COLUMN tipousuario.nomtipousuario
    IS 'Nombre del tipo de usuario';
    
--Tabla Usuario
COMMENT ON COLUMN usuario.correousuario
    IS 'Correo del usuario';
COMMENT ON COLUMN usuario.contrasenausuario
    IS 'Contraseña del usuario';
COMMENT ON COLUMN usuario.nomusuario
    IS 'Nombres del usuario';
COMMENT ON COLUMN usuario.apellidosusuario
    IS 'Apellidos del usuario';
COMMENT ON COLUMN usuario.estadousuario
    IS 'Estado del usuario';
COMMENT ON COLUMN usuario.fecharegistrousuario
    IS 'Fecha en que se registra el usuario';

--Tabla TipoAlimento
COMMENT ON COLUMN tipoalimento.nomtipoalimento
    IS 'Nombre del tipo de alimento';
COMMENT ON COLUMN tipoalimento.codtipoalimento
    IS 'Código del tipo de alimento para sub-clasificar';
    
--Tabla Alimento
COMMENT ON COLUMN alimento.nomalimento 
   IS 'Nombre del alimento';
COMMENT ON COLUMN alimento.codalimento 
   IS 'Codigo del alimento para sub-clasificar';
COMMENT ON COLUMN alimento.pesoalimento 
   IS 'Peso del alimento';
   
--Tabla Compra
COMMENT ON COLUMN compra.fechacompra
   IS 'Fecha de la compra';
COMMENT ON COLUMN compra.fechaestadocompra
   IS 'Fecha en que la compra cambió de estado';
COMMENT ON COLUMN compra.numcompra
   IS 'Número de compra';
COMMENT ON COLUMN compra.totalcompra
   IS 'Total a pagar de la compra';
COMMENT ON COLUMN compra.estadocompra
   IS 'Estado en que se encuentra la compra';
   
--Tabla DetalleCompra
COMMENT ON COLUMN detallecompra.cantidadcompra
   IS 'Cantidad a comprar';
COMMENT ON COLUMN detallecompra.preciocompra
   IS 'Precio del alimento a comprar';
   
--Tabla Venta
COMMENT ON COLUMN venta.fechaventa
    IS 'Fecha en que se realiza la venta';
COMMENT ON COLUMN venta.numventa
    IS 'Número de la venta';
COMMENT ON COLUMN venta.totalventa
    IS 'Total a pagar de la venta';
COMMENT ON COLUMN venta.estadoventa
    IS 'Estado de la venta';

--Tabla DetalleVenta
COMMENT ON COLUMN detalleventa.cantidaddetalleventa
   IS 'Cantidad del detalle de la venta';
COMMENT ON COLUMN detalleventa.precioventa
   IS 'Precio al que se vende';
COMMENT ON COLUMN detalleventa.descuentoventa
   IS 'Descuento de la venta';

--Tabla TipoEmpleado
COMMENT ON COLUMN tipoempleado.nomtipoempleado
    IS 'Nombre del tipo de empleado';
COMMENT ON COLUMN tipoempleado.salariotipoempleado
    IS 'Salario del tipo de empleado';
   
--Tabla Empleado
COMMENT ON COLUMN empleado.nomempleado
   IS 'Nombres del empleado';
COMMENT ON COLUMN empleado.apmaternoemp
   IS 'Apellido materno del empleado';
COMMENT ON COLUMN empleado.appaternoemp
    IS 'Apellido paterno del empleado';
COMMENT ON COLUMN empleado.rutemp
    IS 'Rut del empleado';
COMMENT ON COLUMN empleado.dvrutemp
    IS 'Dígito verificador del rut del empleado';
COMMENT ON COLUMN empleado.direccionemp
    IS 'Dirección del empleado';
COMMENT ON COLUMN empleado.correoemp
    IS 'Correo electrónico del empleado';

--Tabla Inventario
COMMENT ON COLUMN inventario.fechainventario
    IS 'Fecha en que se efectua el inventario';
COMMENT ON COLUMN inventario.nominventario
    IS 'Nombre descriptivo del inventario';
COMMENT ON COLUMN inventario.conteoinventario
    IS 'Conteo del inventario';
COMMENT ON COLUMN inventario.precioconteoinventario
    IS 'Total del dinero de los alimentos inventariados';

--Tabla TipoProveedor
COMMENT ON COLUMN tipoproveedor.nomtipoproveedor
    IS 'Nombre del tipo de proveedor';
    
--Tabla Proveedor
COMMENT ON COLUMN proveedor.nomproveedor
    IS 'Nombre del proveedor';
COMMENT ON COLUMN proveedor.telefproveedor
    IS 'Número de teléfono del proveedor';
COMMENT ON COLUMN proveedor.celuproveedor
    IS 'Número de celular del proveedor';
COMMENT ON COLUMN proveedor.direccionproveedor
    IS 'Dirección del proveedor';
COMMENT ON COLUMN proveedor.rutproveedor
    IS 'Rut del proveedor';
COMMENT ON COLUMN proveedor.dvrutproveedor
    IS 'Dígito verificador del rut';
    
--Tabla Transporte
COMMENT ON COLUMN transporte.nomtransporte
    IS 'Nombre del transporte';

--Tabla Despacho
COMMENT ON COLUMN despacho.nomdespacho
    IS 'Nombre del despacho';
COMMENT ON COLUMN despacho.fechainicdespacho
    IS 'Fecha en que inicia el despacho';
COMMENT ON COLUMN despacho.fechafindespacho
    IS 'Fecha en que finaliza el despacho';
COMMENT ON COLUMN despacho.estadodespacho
    IS 'Estado del despacho';
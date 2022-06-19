------------------------------------------------------
--Script de dropeo y creacion BD ORACLE VeguitaClick
--Ultima modificacion: 18-06-2022
------------------------------------------------------
DROP TABLE TIPOUSUARIO CASCADE CONSTRAINTS;
DROP TABLE USUARIO CASCADE CONSTRAINTS;
DROP TABLE ALMTO_INV CASCADE CONSTRAINTS;
DROP TABLE ALIMENTO CASCADE CONSTRAINTS;
DROP TABLE COMPRA CASCADE CONSTRAINTS;
DROP TABLE DESPACHO CASCADE CONSTRAINTS;
DROP TABLE DETALLECOMPRA CASCADE CONSTRAINTS;
DROP TABLE DETALLEVENTA CASCADE CONSTRAINTS;
DROP TABLE EMP_INV CASCADE CONSTRAINTS;
DROP TABLE EMPLEADO CASCADE CONSTRAINTS;
DROP TABLE INVENTARIO CASCADE CONSTRAINTS;
DROP TABLE PROVE_ALMTO CASCADE CONSTRAINTS;
DROP TABLE PROVEEDOR CASCADE CONSTRAINTS;
DROP TABLE TIPOALIMENTO CASCADE CONSTRAINTS;
DROP TABLE TIPOEMPLEADO CASCADE CONSTRAINTS;
DROP TABLE TIPOPROVEEDOR CASCADE CONSTRAINTS;
DROP TABLE TRANSPORTE CASCADE CONSTRAINTS;
DROP TABLE VENTA CASCADE CONSTRAINTS;
----------------------------------------------
DROP SEQUENCE idtipoempleado;
----------------------------------------------



CREATE TABLE tipousuario (
    idtipousuario 		INTEGER NOT NULL,
    nomtipousuario  	NVARCHAR2(50) NOT NULL
);

ALTER TABLE tipousuario ADD CONSTRAINT tipousuario_pk PRIMARY KEY ( idtipousuario );

CREATE TABLE usuario (
    idusuario                  INTEGER NOT NULL,
	correousuario              NVARCHAR2(200) NOT NULL,
    contrasenausuario          NVARCHAR2(20)  NOT NULL,
    nomusuario                 NVARCHAR2(100) NOT NULL,
    apellidosusuario           NVARCHAR2(500) NOT NULL,
    estadousuario              NVARCHAR2(100),
    fecharegistrousuario       DATE,
    idtipousuario			   INTEGER NOT NULL
);

ALTER TABLE usuario ADD CONSTRAINT usuario_pk PRIMARY KEY ( idusuario );

CREATE TABLE alimento (
    idalimento                   INTEGER NOT NULL,
    nomalimento                  NVARCHAR2(100) NOT NULL,
    codalimento                  NVARCHAR2(100),
    idtipoalimento               INTEGER NOT NULL,
    pesoalimento                 NUMBER(38, 1),
	precioalimento				 NUMBER(38, 1)
);

ALTER TABLE alimento ADD CONSTRAINT alimento_pk PRIMARY KEY ( idalimento );

CREATE TABLE almto_inv (
    idalimento      INTEGER NOT NULL,
    idinventario    INTEGER NOT NULL
);

ALTER TABLE almto_inv ADD CONSTRAINT almto_inv_pk PRIMARY KEY ( idalimento,
                                                                idinventario );

CREATE TABLE compra (
    idcompra           INTEGER NOT NULL,
    fechacompra        DATE,
    fechaestadocompra  DATE NOT NULL,
    numcompra          INTEGER NOT NULL,
    totalcompra        INTEGER NOT NULL,
    estadocompra       NVARCHAR2(150) NOT NULL
);

ALTER TABLE compra ADD CONSTRAINT compra_pk PRIMARY KEY ( idcompra );

CREATE TABLE despacho (
    iddespacho               INTEGER NOT NULL,
    nomdespacho              NVARCHAR2(250),
    fechainicdespacho        DATE,
    fechafindespacho         DATE,
    estadodespacho           NVARCHAR2(250),
	direcciondespacho		 NVARCHAR2(250),
    idtransporte             INTEGER NOT NULL,
    idventa                  INTEGER
);

ALTER TABLE despacho ADD CONSTRAINT despacho_pk PRIMARY KEY ( iddespacho );

CREATE TABLE detallecompra (
    iddetallecompra        INTEGER NOT NULL,
    cantidadcompra         INTEGER NOT NULL,
    preciocompra           INTEGER NOT NULL,
    idcompra               INTEGER NOT NULL,
    idproveedor            INTEGER NOT NULL,
    idalimento             INTEGER NOT NULL
);

CREATE TABLE tienda_producto (
    id  		INTEGER NOT NULL,
    nombre  	NVARCHAR2(64) NOT NULL,
	precio  	NUMBER(38, 1) NOT NULL,
	categoria	NVARCHAR2(64) NOT NULL
);


ALTER TABLE detallecompra ADD CONSTRAINT detallecompra_pk PRIMARY KEY ( iddetallecompra );

CREATE TABLE detalleventa (
    iddetalleventa        INTEGER NOT NULL,
    cantidaddetalleventa  INTEGER NOT NULL,
    precioventa           INTEGER NOT NULL,
    descuentoventa        INTEGER,
    idventa               INTEGER NOT NULL,
    idalimento            INTEGER NOT NULL
);

ALTER TABLE detalleventa ADD CONSTRAINT detalleventa_pk PRIMARY KEY ( iddetalleventa );

CREATE TABLE emp_inv (
    idempleado      INTEGER NOT NULL,
    idinventario    INTEGER NOT NULL
);

ALTER TABLE emp_inv ADD CONSTRAINT emp_inv_pk PRIMARY KEY ( idempleado,
                                                            idinventario );

CREATE TABLE empleado (
    idempleado                    INTEGER NOT NULL,
    nomempleado                   NVARCHAR2(150) NOT NULL,
    apmaternoemp                  NVARCHAR2(150) NOT NULL,
    appaternoemp                  NVARCHAR2(150) NOT NULL,
    rutemp                        INTEGER NOT NULL,
    dvrutemp                      NVARCHAR2(1) NOT NULL,
    direccionemp                  NVARCHAR2(250) NOT NULL,
    correoemp                     NVARCHAR2(80),
    idtipoempleado                INTEGER NOT NULL
);

ALTER TABLE empleado ADD CONSTRAINT empleado_pk PRIMARY KEY ( idempleado );

CREATE TABLE inventario (
    idinventario     INTEGER NOT NULL,
    fechainventario  DATE,
    nominventario    NVARCHAR2(250),
    conteoinventario NUMBER(38),
    precioconteoinventario	NUMBER(38, 2)
);

ALTER TABLE inventario ADD CONSTRAINT inventario_pk PRIMARY KEY ( idinventario );

CREATE TABLE prove_almto (
    idproveedor  INTEGER NOT NULL,
    idalimento   INTEGER NOT NULL
);

ALTER TABLE prove_almto ADD CONSTRAINT prove_almto_pk PRIMARY KEY ( idproveedor,
                                                                    idalimento );

CREATE TABLE proveedor (
    idproveedor                    INTEGER NOT NULL,
    nomproveedor                   NVARCHAR2(150) NOT NULL,
    telefproveedor                 NUMBER(8),
    celuproveedor                  NUMBER(9),
    direccionproveedor             NVARCHAR2(500),
    idtipoproveedor                INTEGER NOT NULL,
    rutproveedor                   INTEGER NOT NULL,
    dvrutproveedor                 INTEGER NOT NULL
);

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( idproveedor );

CREATE TABLE tipoalimento (
    idtipoalimento   INTEGER NOT NULL,
    nomtipoalimento  NVARCHAR2(150) NOT NULL,
    codtipoalimento  NVARCHAR2(150)
);

ALTER TABLE tipoalimento ADD CONSTRAINT tipoalimento_pk PRIMARY KEY ( idtipoalimento );

CREATE TABLE tipoempleado (
    idtipoempleado   INTEGER,
    nomtipoempleado  NVARCHAR2(250) NOT NULL,
    salariotipoempleado	INTEGER
);

ALTER TABLE tipoempleado ADD CONSTRAINT tipoempleado_pk PRIMARY KEY ( idtipoempleado );

CREATE TABLE tipoproveedor (
    idtipoproveedor   INTEGER NOT NULL,
    nomtipoproveedor  NVARCHAR2(300)
);

ALTER TABLE tipoproveedor ADD CONSTRAINT tipoproveedor_pk PRIMARY KEY ( idtipoproveedor );

CREATE TABLE transporte (
    idtransporte         INTEGER NOT NULL,
    nomtransporte        NVARCHAR2(250) NOT NULL,
    idempleado           INTEGER NOT NULL
);

ALTER TABLE transporte ADD CONSTRAINT transporte_pk PRIMARY KEY ( idtransporte );

CREATE TABLE venta (
    idventa              INTEGER NOT NULL,
    fechaventa           DATE NOT NULL,
    numventa             INTEGER NOT NULL,
    totalventa           INTEGER,
    estadoventa          NVARCHAR2(100) NOT NULL,
    idempleado           INTEGER NOT NULL
);

ALTER TABLE usuario
    ADD CONSTRAINT usuario_tipousuario_fk FOREIGN KEY ( idtipousuario )
        REFERENCES tipousuario ( idtipousuario );
		
ALTER TABLE venta ADD CONSTRAINT venta_pk PRIMARY KEY ( idventa );

ALTER TABLE alimento
    ADD CONSTRAINT alimento_tipoalimento_fk FOREIGN KEY ( idtipoalimento )
        REFERENCES tipoalimento ( idtipoalimento );

ALTER TABLE almto_inv
    ADD CONSTRAINT almto_inv_alimento_fk FOREIGN KEY ( idalimento )
        REFERENCES alimento ( idalimento );

ALTER TABLE almto_inv
    ADD CONSTRAINT almto_inv_inventario_fk FOREIGN KEY ( idinventario )
        REFERENCES inventario ( idinventario );

ALTER TABLE despacho
    ADD CONSTRAINT despacho_transporte_fk FOREIGN KEY ( idtransporte )
        REFERENCES transporte ( idtransporte );

ALTER TABLE despacho
    ADD CONSTRAINT despacho_venta_fk FOREIGN KEY ( idventa )
        REFERENCES venta ( idventa );

ALTER TABLE detallecompra
    ADD CONSTRAINT detallecompra_alimento_fk FOREIGN KEY ( idalimento )
        REFERENCES alimento ( idalimento );

ALTER TABLE detallecompra
    ADD CONSTRAINT detallecompra_compra_fk FOREIGN KEY ( idcompra )
        REFERENCES compra ( idcompra );

ALTER TABLE detallecompra
    ADD CONSTRAINT detallecompra_proveedor_fk FOREIGN KEY ( idproveedor )
        REFERENCES proveedor ( idproveedor );

ALTER TABLE detalleventa
    ADD CONSTRAINT detalleventa_alimento_fk FOREIGN KEY ( idalimento )
        REFERENCES alimento ( idalimento );

ALTER TABLE detalleventa
    ADD CONSTRAINT detalleventa_venta_fk FOREIGN KEY ( idventa )
        REFERENCES venta ( idventa );

ALTER TABLE emp_inv
    ADD CONSTRAINT emp_inv_empleado_fk FOREIGN KEY ( idempleado )
        REFERENCES empleado ( idempleado );

ALTER TABLE emp_inv
    ADD CONSTRAINT emp_inv_inventario_fk FOREIGN KEY ( idinventario )
        REFERENCES inventario ( idinventario );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_tipoempleado_fk FOREIGN KEY ( idtipoempleado )
        REFERENCES tipoempleado ( idtipoempleado );

ALTER TABLE prove_almto
    ADD CONSTRAINT prove_almto_alimento_fk FOREIGN KEY ( idalimento )
        REFERENCES alimento ( idalimento );

ALTER TABLE prove_almto
    ADD CONSTRAINT prove_almto_proveedor_fk FOREIGN KEY ( idproveedor )
        REFERENCES proveedor ( idproveedor );

ALTER TABLE proveedor
    ADD CONSTRAINT proveedor_tipoproveedor_fk FOREIGN KEY ( idtipoproveedor )
        REFERENCES tipoproveedor ( idtipoproveedor );

ALTER TABLE transporte
    ADD CONSTRAINT transporte_empleado_fk FOREIGN KEY ( idempleado )
        REFERENCES empleado ( idempleado );

ALTER TABLE venta
    ADD CONSTRAINT venta_empleado_fk FOREIGN KEY ( idempleado )
        REFERENCES empleado ( idempleado );

CREATE SEQUENCE idtipoempleado START WITH 1 NOCACHE ORDER;
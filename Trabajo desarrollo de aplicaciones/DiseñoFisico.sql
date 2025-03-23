create table usuario(
  	id      int AUTO_INCREMENT not null primary key, 
    usuario varchar(255) not null unique,
    clave   varchar(255) not null
);

create table raza(
  	id          int AUTO_INCREMENT not null primary key, 
    nombre      varchar(255),
    descripcion varchar(255)
);

create table equipamientos(
  	id          int AUTO_INCREMENT not null primary key, 
    nombre      varchar(255) not null,
    descripcion varchar(255) not null,
    rareza      varchar(255) not null
);

create table habilidades(
  	id          int AUTO_INCREMENT not null primary key, 
    nombre      varchar(255) not null,
    descripcion varchar(255) not null,
    raza_id     int not null,
    constraint fk_habraz foreign key (raza_id) references raza(id)
);

create table poderes(
  	id          int AUTO_INCREMENT not null primary key, 
    nombre      varchar(255) not null,
    descripcion varchar(255) not null,
    raza_id     int not null,
    constraint fk_podRaz foreign key (raza) references raza(id)
);

CREATE TABLE personaje (
  	id              int AUTO_INCREMENT not null primary key, 
  	nombre          varchar(255) not null,
  	usuario_id      int not null,
  	raza_id         int NOT NULL,
  	nivel           INT NOT NULL,
    habilidad_id    int not null,
    equipamiento_id int not null,
    poderes_id      int not null,
  	estado          VARCHAR(10) not null DEFAULT 'vivo' CHECK (estado IN ('vivo', 'muerto', 'congelado')),
  	constraint fk_perUsu foreign key (usuario_id) references usuario(id),
    constraint fk_perRaz foreign key (raza_id) references raza(id),
    constraint fk_perHab foreign key (habilidad_id) references habilidades(id),
    constraint fk_perEqu foreign key (equipamiento_id) references equipamientos(id),
    constraint fk_perPod foreign key (poderes_id) references poderes(id)
);
-- tabla de jugadores
CREATE TABLE Jugadores (
    ID INT PRIMARY KEY,
    Nombre VARCHAR2(50) NOT NULL,
    Email VARCHAR2(100) UNIQUE NOT NULL,
    Contraseña VARCHAR2(50) NOT NULL
);

-- tabla de personajes
CREATE TABLE Personajes (
    ID INT PRIMARY KEY,
    Nombre VARCHAR2(50) NOT NULL,
    Clase VARCHAR2(50) NOT NULL,
    Nivel INT NOT NULL,
    Jugador_ID INT,
    FOREIGN KEY (Jugador_ID) REFERENCES Jugadores(ID)
);

-- tabla de objetos
CREATE TABLE Objetos (
    ID INT PRIMARY KEY,
    Nombre VARCHAR2(50) NOT NULL,
    Tipo VARCHAR2(50) NOT NULL
);

-- tabla de inventario para los personajes
CREATE TABLE Inventario (
    ID INT PRIMARY KEY,
    Personaje_ID INT,
    Objeto_ID INT,
    Cantidad INT NOT NULL,
    FOREIGN KEY (Personaje_ID) REFERENCES Personajes(ID),
    FOREIGN KEY (Objeto_ID) REFERENCES Objetos(ID)
);

-- tabla de habilidades
CREATE TABLE Habilidades (
    ID INT PRIMARY KEY,
    Nombre VARCHAR2(50) NOT NULL,
    Descripcion TEXT
);

-- tabla de habilidades de los personajes
CREATE TABLE Personaje_Habilidades (
    ID INT PRIMARY KEY,
    Personaje_ID INT,
    Habilidad_ID INT,
    FOREIGN KEY (Personaje_ID) REFERENCES Personajes(ID),
    FOREIGN KEY (Habilidad_ID) REFERENCES Habilidades(ID)
);

-- tabla de razas
CREATE TABLE Razas (
    ID INT PRIMARY KEY,
    Nombre VARCHAR2(50) NOT NULL
);

-- tabla de estados
CREATE TABLE Estados (
    ID INT PRIMARY KEY,
    Nombre VARCHAR2(50) NOT NULL
);

-- Raza a la tabla de Personajes
ALTER TABLE Personajes
ADD Raza_ID INT,
ADD FOREIGN KEY (Raza_ID) REFERENCES Razas(ID);

-- Estado a la tabla de Personajes
ALTER TABLE Personajes
ADD Estado_ID INT,
ADD FOREIGN KEY (Estado_ID) REFERENCES Estados(ID);

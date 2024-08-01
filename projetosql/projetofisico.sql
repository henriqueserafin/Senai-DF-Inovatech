/* projetologico: */

CREATE TABLE Aluno (
    id int PRIMARY KEY,
    ra char(8)
);

CREATE TABLE avaliacao (
    nota4 int,
    nota3 int,
    nota1 int,
    id int PRIMARY KEY,
    nota2 int,
    fk_Aluno_id int
);

CREATE TABLE diariobordo (
    id int PRIMARY KEY,
    datahora datetime,
    texto text
);
 
ALTER TABLE avaliacao ADD CONSTRAINT FK_avaliacao_2
    FOREIGN KEY (fk_Aluno_id)
    REFERENCES Aluno (id)
    ON DELETE CASCADE;
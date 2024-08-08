CREATE DATABASE schooltracker;
USE schooltracker;

CREATE TABLE Aluno (
    id int PRIMARY KEY auto_increment,
    ra char(8) NOT null unique
);
-- ----------------------------
Alter table aluno add constraint unique (ra);
select * from aluno;
delete from aluno where id>0;
truncate table aluno;
describe aluno;
-- Isso cria uma tabela aluno com os atributos id e ra, e diz que id é nossa chave primária auto incrementada, e ra não pode ser nulo
select * from aluno;
INSERT INTO Aluno (ra) VALUES ('0034541');
INSERT INTO Aluno (ra) VALUES ('0034542');
INSERT INTO Aluno (ra) VALUES ('0034543');
INSERT INTO Aluno (ra) VALUES ('0034544');
INSERT INTO Aluno (ra) VALUES ('0034545');
INSERT INTO Aluno (ra) VALUES ('0034546');
INSERT INTO Aluno (ra) VALUES ('0034547');
INSERT INTO Aluno (ra) VALUES ('0034548');
INSERT INTO Aluno (ra) VALUES ('0034549');
INSERT INTO Aluno (ra) VALUES ('0034550');
INSERT INTO Aluno (ra) VALUES ('0034551');
INSERT INTO Aluno (ra) VALUES ('0034552');
INSERT INTO Aluno (ra) VALUES ('0034553');
INSERT INTO Aluno (ra) VALUES ('0034554');
INSERT INTO Aluno (ra) VALUES ('0034555');
INSERT INTO Aluno (ra) VALUES ('0034556');
INSERT INTO Aluno (ra) VALUES ('0034557');
INSERT INTO Aluno (ra) VALUES ('0034558');
INSERT INTO Aluno (ra) VALUES ('0034559');
INSERT INTO Aluno (ra) VALUES ('0034560');
INSERT INTO Aluno (ra) VALUES ('0034561');
INSERT INTO Aluno (ra) VALUES ('0034562');
INSERT INTO Aluno (ra) VALUES ('0034563');
INSERT INTO Aluno (ra) VALUES ('0034564');
INSERT INTO Aluno (ra) VALUES ('0034565');
INSERT INTO Aluno (ra) VALUES ('0034566');
INSERT INTO Aluno (ra) VALUES ('0034567');
INSERT INTO Aluno (ra) VALUES ('0034568');
INSERT INTO Aluno (ra) VALUES ('0034569');
INSERT INTO Aluno (ra) VALUES ('0034570');
INSERT INTO Aluno (ra) VALUES ('0034571');
INSERT INTO Aluno (ra) VALUES ('0034572');
INSERT INTO Aluno (ra) VALUES ('0034573');
INSERT INTO Aluno (ra) VALUES ('0034574');
INSERT INTO Aluno (ra) VALUES ('0034575');
INSERT INTO Aluno (ra) VALUES ('0034576');
INSERT INTO Aluno (ra) VALUES ('0034577');
INSERT INTO Aluno (ra) VALUES ('0034578');
INSERT INTO Aluno (ra) VALUES ('0034579');
INSERT INTO Aluno (ra) VALUES ('0034580');
INSERT INTO Aluno (ra) VALUES ('0034581');
INSERT INTO Aluno (ra) VALUES ('0034582');
INSERT INTO Aluno (ra) VALUES ('0034583');
INSERT INTO Aluno (ra) VALUES ('0034584');
INSERT INTO Aluno (ra) VALUES ('0034585');
INSERT INTO Aluno (ra) VALUES ('0034586');
INSERT INTO Aluno (ra) VALUES ('0034587');
INSERT INTO Aluno (ra) VALUES ('0034588');
INSERT INTO Aluno (ra) VALUES ('0034589');
INSERT INTO Aluno (ra) VALUES ('0034590');

-- Isso adiciona os valores no ra e o select os mostra
CREATE TABLE diariobordo (
    id int PRIMARY KEY auto_increment,
    texto text not null,
    datahora datetime,
    fk_Aluno_id int
);


ALTER TABLE diariobordo ADD CONSTRAINT FK_diariobordo_2
    FOREIGN KEY (fk_Aluno_id)
    REFERENCES Aluno (id)
    ON DELETE CASCADE;
    
show tables;
INSERT INTO diariobordo (texto, datahora, fk_Aluno_id) VALUES 
('o texto massa do aluno', '2024-07-31 15:40:00', 5);


    
-- meu ra
 INSERT INTO Aluno (ra) VALUES ('00176143');
 select * from aluno;
 -- meu insert id=51
 INSERT INTO diariobordo (texto, datahora, fk_Aluno_id) VALUES 
('nesta aula aprendemos comandos mais avançados de sql, como impedir valores duplicados, e como utilizar o join, ótima aula prof :)', '2024-07-31 17:40:00', '51' );
-- select com join
select * from diariobordo;
select 
	d.id,
	d.texto,
	d.datahora,
	a.ra as registro_academico
from
	diariobordo as d
join
	aluno as a
on
	d.fk_aluno_id=a.id;
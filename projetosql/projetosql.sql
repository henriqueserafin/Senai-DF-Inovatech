CREATE TABLE avaliacao (
    id int PRIMARY KEY auto_increment,
    nota1 int CHECK (nota1 <= 25),
    nota2 int CHECK (nota2 <= 25),
    nota3 int CHECK (nota3 <= 25),
    nota4 int CHECK (nota4 <= 25),
    fk_Aluno_id int
);


ALTER TABLE avaliacao ADD CONSTRAINT FK_avaliacao_2
    FOREIGN KEY (fk_Aluno_id)
    REFERENCES Aluno (id)
    ON DELETE CASCADE;

drop table avaliacao;

insert into avaliacao (nota1, nota2, nota3, nota4, fk_Aluno_id) values ('14', '21', '24','12','51');
insert into avaliacao (nota1, nota2, nota3, nota4, fk_Aluno_id) values ('17', '20', '8','9','3');
insert into avaliacao (nota1, nota2, nota3, nota4, fk_Aluno_id) values ('19', '1', '4','7','5');
insert into avaliacao (nota1, nota2, nota3, nota4, fk_Aluno_id) values ('18', '17', '16','14','8');
insert into avaliacao (nota1, nota2, nota3, nota4, fk_Aluno_id) values ('17', '22', '15','14','17');

select * from aluno;
select * from avaliacao;

select
	a.nota1,
    a.nota2,
	a.nota3,
    a.nota4,
    ao.ra
from
	avaliacao a
join
	aluno ao
on a.fk_aluno_id=ao.id;

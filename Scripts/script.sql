select name, vname, isbn from t_leser, t_verleih;
select name, vname, isbn from t_leser, t_verleih order by name,vname;
select name, vname, isbn from t_leser inner join t_verleih order by name,vname;
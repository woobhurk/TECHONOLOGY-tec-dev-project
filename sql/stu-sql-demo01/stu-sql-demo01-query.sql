-- ##############
-- CASE WHEN 语句
-- 用一条 SQL 统计学生男女生的数量，以及男女生考试及格人数
select
    sum(case when s.sex = '1' then 1 else 0 end) `男生数量`,
    sum(case when s.sex = '2' then 1 else 0 end) `女生数量`,
    sum(case when s.sex = '1' and sc.score >= 60 then 1 else 0 end) `男生及格数量`,
    sum(case when s.sex = '2' and sc.score >= 60 then 1 else 0 end) `女生及格数量`
from student s
left join student_score sc on sc.student_id = s.id;

-- 行转列：统计部门名为“苍空府”“碎尸堂”“金童殿”的老师的数量
select
    sum(case when d.name = '苍空府' then 1 else 0 end) `苍空府`,
    sum(case when d.name = '碎尸堂' then 1 else 0 end) `碎尸堂`,
    sum(case when d.name = '金童殿' then 1 else 0 end) `金童殿`
from teacher t
left join department d on d.id = t.department_id;

-- 根据薪水等级表统计所有等级薪水的老师数量
select
    -- 计算小于第一等级薪水的教师数量
    sum(case
        when ts.salary < (select salary from salary_level where level = 1) then 1
        else 0 end) `饿死了`,
    -- 计算大于等于第一级，小于第二级薪水的教师数量
    sum(case
        when ts.salary >= (select salary from salary_level where level = 1)
            and ts.salary < (select salary from salary_level where level = 2) then 1
        else 0 end) `穷逼`,
    sum(case
        when ts.salary >= (select salary from salary_level where level = 2)
            and ts.salary < (select salary from salary_level where level = 3) then 1
        else 0 end) `温饱`,
    sum(case
        when ts.salary >= (select salary from salary_level where level = 3)
            and ts.salary < (select salary from salary_level where level = 4) then 1
        else 0 end) `小康`,
    sum(case
        when ts.salary >= (select salary from salary_level where level = 4) then 1
        else 0 end) `富足`
from teacher t
left join teacher_salary ts on ts.teacher_id = t.id;

-- ########
-- 关联查询
-- 查询“天元刹”部门中的薪资低于 6000 的男老师
select t.name `教师`, d.name `部门`, ts.salary `薪资`
from teacher t
left join department d on d.id = t.department_id
left join teacher_salary ts on ts.teacher_id = t.id
where t.sex = '1' and d.name = '天元刹' and ts.salary < 6000;

-- 查询每个部门中老师的最高和最低薪资
select max(ts.salary) `最高工资`, min(ts.salary) `最低工资`, d.name `部门`
from teacher t
left join department d on d.id = t.department_id
left join teacher_salary ts on ts.teacher_id = t.id
group by d.id;

-- ######
-- 子查询
-- 查询薪水最高的老师的信息以及所在的部门、薪水
select t.name `教师`, d.name `部门`, ts.salary `薪水`
from teacher t
left join department d on d.id = t.department_id
left join teacher_salary ts on ts.teacher_id = t.id
where ts.salary = (select max(salary) from teacher_salary);

-- 查询每个部门中薪水最高的老师的信息以及所在的部门、薪水
select t.id, t.name `教师`, d.name `部门`, max(ts.salary) `薪水`
from teacher t
left join department d on d.id = t.department_id
left join teacher_salary ts on ts.teacher_id = t.id
group by d.id;

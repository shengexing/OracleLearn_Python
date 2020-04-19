accept no prompt '请输入雇员号：'
accept name prompt '请输入雇员名：'
accept title prompt '请输入雇员岗位：'
accept d_no prompt '请输入雇员部门号：'
insert into emp(empno, ename, job, hiredate, deptno)
values(&no, '&name', '&title', sysdate, &d_no);
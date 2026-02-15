**FREE
ctl-opt DftActGrp(*No) ActGrp(*New);

dcl-s Var1 packed(5:0) inz(0);
dcl-s Var2 char(10) inz('HELLO');
dcl-s CustNum packed(7:0);

/free
   Var1 = 1;
   Var2 = 'Hello World';

   exec sql
     SELECT CUSNUM INTO :CustNum
       FROM CUSTOMER
      WHERE CUSNUM = 12345;
   end-exec;

   return;
/end-free

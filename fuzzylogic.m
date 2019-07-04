clc;
clear all;
u1=input("Enter first element of set = ");
u2=input("Enter last element of set = ");
increment=input("Enter increment value = ");
uni=[];
for i=u1:u2
uni=[uni i];
end
a=[];
leng=input("Enter the length of A set : ");
for i=1:leng
a1=input("Enter element "+i+" : ");
a=[a a1];
end
aa=[];
for i=1:leng
aa1=input("Enter membership value "+i+" : ");
aa=[aa aa1];
end
b=[];
lengt=input("Enter the length of B set : ");
for i=1:lengt
b1=input("Enter element "+i+" : ");
b=[b b1];
end
bb=[];
for i=1:lengt
bb1=input("Enter membership value "+i+" : ");
bb=[bb bb1];
end
mergeab=[a b];

mergeaabb=[aa bb];
max=length(mergeab);
AA=[a;aa];
AA=AA.'
BB=[b;bb];
BB=BB.'
inc=intersect(a,b);
disp("intersection of set A & B = Fuzzyset{");
for i=1:length(a)
for j=1:length(b)
if AA(i)==BB(j)
m=min(AA(i+length(a)),BB(j+length(b)));
disp("{"+AA(i)+", "+m+"},");
else
disp("");
end
end
end
disp(", UniversalSpace --> {"+u1+","+u2+","+increment+"}}");
f=setdiff(a,b);
g=setdiff(b,a);
loc=[f g];
disp("");
disp("");
disp("Union of set A & B=Fuzzyset{");
for i=1:length(a)
for j=1:length(b)
if AA(i)==BB(j)
m=min(AA(i+length(a)),BB(j+length(b)));
disp("{"+AA(i)+","+m+"},");
end
end
end
for i=1:length(loc)
for j=1:max
if loc(i) ==mergeab(j)
disp("{"+mergeab(j)+","+mergeaabb(j)+"},");
end
end
end
disp(", UniversalSpace --> {"+u1+","+u2+","+increment+"}}");
g=setdiff(b,a);
loc=[g];
disp("Difference of set A-B=Fuzzyset{");

for i=1:length(loc)
for j=1:max
if loc(i) ==mergeab(j)
disp("{"+mergeab(j)+","+mergeaabb(j)+"},");
end
end
end
disp(", UniversalSpace --> {"+u1+","+u2+","+increment+"}}");
g=setdiff(a,b);
loc=[g];
disp("Differnece of set B-A=Fuzzyset{");
for i=1:length(loc)
for j=1:max
if loc(i) ==mergeab(j)
disp("{"+mergeab(j)+","+mergeaabb(j)+"},");
end
end
end
disp(", UniversalSpace --> {"+u1+","+u2+","+increment+"}}");
aa2=[];
for i=1:length(aa)
aa1=aa(i)-1;
aa2=[aa2 aa1];
end
bb2=[];
for i=1:length(bb)
bb1=bb(i)-1;
bb2=[bb2 bb1];
end
AA=[a;aa2];
disp("Complement of set A = Fuzzyset{");
AA=AA.'
disp(", UniversalSpace --> {"+u1+","+u2+","+increment+"}}");
BB=[b;bb2];
disp("Complement of set B = Fuzzyset{");
BB=BB.'
disp(", UniversalSpace --> {"+u1+","+u2+","+increment+"}}");

OUTPUT-
Enter first element of set =

1
Enter last element of set =
10
Enter increment value =
1
Enter the length of A set :
2
Enter element 1 :
1
Enter element 2 :
2
Enter membership value 1 :
0.1
Enter membership value 2 :
0.3
Enter the length of B set :
2
Enter element 1 :
1
Enter element 2 :
2
Enter membership value 1 :
0.3
Enter membership value 2 :
0.1
AA =
1.0000 0.1000
2.0000 0.3000

BB =
1.0000 0.3000

2.0000 0.1000
intersection of set A & B = Fuzzyset{
{1, 0.1},
{2, 0.1},
, UniversalSpace --> {1,10,1}}
Union of set A & B=Fuzzyset{
{1,0.1},
{2,0.1},
, UniversalSpace --> {1,10,1}}
Difference of set A-B=Fuzzyset{
, UniversalSpace --> {1,10,1}}
Differnece of set B-A=Fuzzyset{
, UniversalSpace --> {1,10,1}}
Complement of set A = Fuzzyset{
AA =
1.0000 -0.9000
2.0000 -0.7000
, UniversalSpace --> {1,10,1}}
Complement of set B = Fuzzyset{
BB =
1.0000 -0.7000
2.0000 -0.9000
, UniversalSpace --> {1,10,1}}
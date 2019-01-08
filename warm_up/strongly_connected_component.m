
%main file:######################################################## 
clc 
% x from 1 to 100 
x=1:100; 
xs=zeros(1,100); 
for i=1:100 
xs(:,i)=del_edge(i); 
end 
plot(x,xs); 
%function:######################################################## 
function [out]=del_edge(x) 
%read dataset 
D=importdata('dataset.txt'); 
dim=max(max(D.data))+1; 
dim2=dim; 
%delete edges randomly 
for l=1:dim*x/100 
r = randi([0 dim2],1,1); 
D.data(r,:)=[]; 
dim2=length(D.data); 
end 
dim=max(max(D.data))+1; 
c = sparse(D.data(:,1)+1,D.data(:,2)+1,1,dim,dim); 
%largest component 
max_com_size=0; 
for i=1:dim 
order = graphtraverse(c,1,'Method', 'BFS'); 
len=length(order); 
if len>max_com_size 
max_com_size=len; 
end 
end 
out=max_com_size; 
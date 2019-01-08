clc

%read data
D=importdata('edgelist.txt');
dim=max(max(D));
c =sparse(D(:,1),D(:,2),1,dim,dim);
c=c+c';

%spectral clustering
G=graph(c);
L=laplacian(G);
%[V,lambda]=eig(full(L)); %this does not give sorted + does not work on
%sparse matrices
[V,lambda] = eigs(L,2,'sm');
idx = kmeans(V(:,1),2);
%fix starting point of kmeans:
%rng(1);
%idx = kmeans(V(:,1),2);
cluster1=[];
cluster2=[];
for i=1:34
    if idx(i)==1
        cluster1=[cluster1 i];
    else
        cluster2=[cluster2 i];
    end
end
disp(size(cluster1))
disp(size(cluster2))
disp(lambda)
disp(V)
%disp(cluster1)
%disp(cluster2)

%CMM
label = CMM(full(c), 2);
disp(label)





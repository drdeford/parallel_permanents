z=[];
y=[];
for i=2:21
    m=randi([-1,1],[i,i]);
    tic;
    permanentRyser(m);
    z(i-1)=toc;
    tic;
    ParpermanentRyser(m);
    y(i-1)=toc;
end

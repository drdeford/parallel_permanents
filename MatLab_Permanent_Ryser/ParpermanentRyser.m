function y = ParpermanentRyser(A)
%PERMANENTRYSER(A) Calculate the permanent of a square matrix A
%
%   y = permanentRyser(A) returns the permanent of square matrix A
%
%   INPUT:
%       A square numeric matrix
%   OUTPUT:
%       The matrix permanent
%
%
%   Uses the Ryser Formula to calculate the permanent, so it is O((n^2)(2^n))
%   which is much faster than the naive algorithm O(n!n). The determinate 
%   of a matrix is defined as the analog of determinant where the signs of 
%   each term in summation was removed.
%
%
%   Written by:
%   Luke Winslow
%   Limnology and Oceanography PhD Student
%   University of Wisconsin - Madison
%   USA, 2012
%
%   lawinslow@gmail.com

    tic;
    y = 0;
    [n,n2] = size(A);
    
    if(n~=n2)
        error('A must be square');
    end
    
    
    % loop over all 2^n submatricies of A
    parfor i=1:(2^n - 1) %The last 2^n is no rows, skip that
        % use bitget to index ever possible row-subset of A
        indx = logical(bitget(i,(1:n))');
        
        y = y + ((-1)^(sum(indx))) * prod(sum(A(indx,:),1));
    end
    
    y = y * (-1)^n;
    toc
end


%
%   2.8503e+09

%format long
%ans

%ans =

 %    2.850306592000000e+09

%vpa(ans*ans,100)
 
%ans =
 
%8124247668398654464.0
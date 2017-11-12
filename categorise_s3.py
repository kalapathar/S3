import operator
import itertools
import collections
import random
import time

#Takes a matrix of n nonzeros and replaces all nonzero entries by either +/-/0 and categorises equivalent matrices in a same category
class categorise(object):
    
    
    def __init__(self,matrix,nonzero):
        self.base_matrix=matrix
        self.nonzero=nonzero
        S=[1,-1]
        perm_list=Tuples(S,nonzero).list()
        self.matrices=self.zero_ones_matrix(perm_list)
        self.categorised=self.categ(self.matrices)
        #return cat
        #self.display()
    
    def zero_ones_matrix(self,arrange):  #Creates a list of matrices whose entries are either +1,-1 or 0.
        matrices=list()
        for i in range(len(arrange)):
            alphadict={}
            for j in range(self.nonzero):
                alphadict[alphabets[j]]=arrange[i][j]
            M=self.base_matrix.subs(alphadict)
            matrices.append(M)
        return matrices

    def negate(self,M): #Takes a matrix and negates its rows and columns in all possible combinations
        A=copy(M);
        negatives=list()
        comb=Subsets(3).list()[1:]
        for i in comb:
            for j in i:
                A[:,j-1]=-1*A[:,j-1];
                A[j-1,:]=-1*A[j-1,:];
            negatives.append(A);
            A=copy(M)
        return negatives;
    
    def zero_positions(self,M): #Returns the zero index in a matrix
        ltuple=list();
        for i in range(M.nrows()):
            for j in range(M.ncols()):
                if M[i,j]==0:
                    ltuple.append((i,j));
        return ltuple;
    
    def similar(self,M): #Returns a list of matrices that are similar to the input matrix. Matrix A and B are similar if rows/columns of A can be permuted to obtain B
        P=[matrix(QQ,matrix(p)) for p in Permutations(3)];
        slist=[p*M*~p for p in P];
        plist=list();
        for i in slist:
            if self.zero_positions(i)==self.zero_positions(M):
                plist.append(i);
        return plist;
    
    def onlyunique(self,alist):  #Takes a list and returns only unique matrices from the list
        mlist=alist;
        mlist.sort();
        glist=list(matrix(k) for k,_ in itertools.groupby(mlist))
        return glist;
    
    def filtered(self,mlist):   #Takes a matrix and returns only those matrices with positive trace
        alist=list();
        for i in mlist:
            if (i[0,0]>=0 and i[1,1]>=0 and i[2,2]>=0) :
                pass;
            else:
                alist.append(i);
        return alist;

    def equivalent(self,M):        #Returns a list of matrices that are equivalent to the input matrix
        allequiv=list();
        for i in self.negate(M):
            if i not in allequiv:
                allequiv.append(i)
        for i in self.similar(M):
            if i not in allequiv:
                allequiv.append(i)
        for i in self.negate(M):
            j=self.similar(i)
            for k in j:
                if k not in allequiv:
                    allequiv.append(k)
        return self.onlyunique(allequiv)
    
    def categ(self, lmatrices):         #Categorises equivalent matrices in a same list. Returns a list of lists that are categorised
        abiglist=list()
        for i in lmatrices:
            if not any(i in group for group in abiglist):
                slist=list()
                for j in self.equivalent(i):
                    if not any(j in group for group in abiglist):
                        slist.append(j)
                abiglist.append(slist)
        return abiglist
    
    
    def display(self):                   #Displays the matrices
        
        show(self.categorised)

class S3(object):                  #Takes a list of categorised matrices and plots graphs to check if the matrix can allow S3_pattern
    
    def  __init__(self,matrix,nonzero):              
        self.UM=matrix
        cat=categorise(matrix,nonzero)
        show (cat.categorised)
        self.find_s3(cat.categorised)
        
    
    def det_term(self,alist,p):           #Returns the last coefficient in the charactertistic polynomial 
        for i in alist:
            if str(i) in str(p):
                return i

    def var_poly(self,p1):              #Returns the coefficient of the other terms in the char poly.
        alist=list();
        for i in alphabets:
            if str(i) in str(p1):
                alist.append(i);
        return alist;
    
    def get_poly(self,M):               #Returns the coefficients of several terms in the polynomial 
        N=self.general(M);
        p1=N.charpoly();
        vlist=self.var_poly(p1);
        s1=solve([p1.constant_coefficient()==0],self.det_term(vlist,p1[0]));
        s2=s1[0].right();
        p2=p1.subs(**{str(self.det_term(vlist,p1[0])):s2})
        p3=p2.coefficients()[0];
        p4=p2.coefficients()[1];
        return (p3,p4,s1);
    
    def general(self,M):                   #Returns the general matrix which is found by replacing non zero entries with a variable
        A=matrix(SR,M.nrows(),M.ncols());k=0;
        for i in range(M.nrows()):
            for j in range(M.ncols()):
                if M[i,j]!=0:
                    if (M[i,j])>0:
                        A[i,j]=1*alphabets[k]
                    else:
                        A[i,j]=-1*alphabets[k]
                    k=k+1;
        if (A[0,0]!=0): 
            A[0,0]=A[0,0]/self.UM[0,0]
        if (A[0,1]!=0):
            A[0,1]=A[0,1]/self.UM[0,1]
        if (A[1,2]!=0): 
            A[1,2]=A[1,2]/self.UM[1,2]
        return A
    
    def try_plot(self,p1,p2):                    #Plots the general matrix
        a1=p1;a2=p2
        v1=self.var_poly(p1)
        v2=self.var_poly(p2)
        if (len(v1)>2):
             for i in v1[:-2]:
                a1=a1.subs(**{str(i):1})
        if (len(v2)>2):
             for i in v2[:-2]:
                a2=a2.subs(**{str(i):1})

        if len(v1)>=len(v2):
            l1=v1
        else:
            l1=v2

        if (len(l1)>=2):
            p=region_plot([a1>0,a2>0],(l1[-2],-10,10),(l1[-1],-8,8),axes_labels=[l1[-2],l1[-1]])
            see=solve([a1>0,a2>0],[l1[-2],l1[-1]])[0]
        show(p)
        return (see)

    def Is_s3(self,M):                         #Plots the graph that then leaves to the reader to check for possibility of S3. 
        poly=self.get_poly(M);
        region=self.try_plot(poly[0],poly[1]);
        show(region);
        show(poly[2]); show(self.general(M));show(self.general(M).charpoly()); 
        
    def find_s3(self,alist):
        k=0;
        for i in alist:
            print k;
            self.Is_s3(i[0])
            k=k+1;

if __name__ == '__main__':                             
    alphabets=var('a,b,c,d,e,f,g,h,i')
    S3(matrix(SR,[[a,b,0],[0,c,d],[e,0,f]]),6)


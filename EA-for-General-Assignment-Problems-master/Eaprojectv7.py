import numpy

students = 75
courses = 4
generations = 50
class_strength = 15

numpy.random.seed(3)

#course_strength = [2,3,3,3,3,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

class pop:

    population=[[0 for i in range(students+1)] for j in range(10)]

    preferences=[[0 for i in range(students)] for j in range(courses)]

    allocation=[[0 for i in range(students)] for j in range(courses)]

    c1 = [0 for o in range(students)]
    c2 = [0 for o in range(students)]
    c3 = []

    gener = 0
        
    
    def __init__(self):

        preffile = open("Z:\EAproject\preferences.txt")

        self.preferences = [i.strip().split() for i in preffile]

        self.ct = [int(i) for i in range (0,students)]

        for i in range (0,10):

            for j in range (0,students):

                self.population[i][j] = self.ct[j]

            self.allocate(self.ct)

            self.fitct = self.fitness(self.allocation)

            self.population[i][students] = self.fitct
            
            numpy.random.shuffle(self.ct)

        self.population.sort(key=lambda i:i[students],reverse=True)

        numpy.savetxt("Z:\EAinPY\pypops0.txt",numpy.array(self.population),fmt='%1.1d',delimiter = ' ',newline = '\n')
        print("GEN : 0")
        print(self.population)

        for gen in range(generations) :

            print("GEN : " + str(gen+1))
            self.__parentloader()
            self.__O1X()
            self.__nextgenpop2()
            self.population.sort(key=lambda i:i[students],reverse=True)
            self.store_avg_fitness()
            self.store_top_alloc()
            print(self.population)
            numpy.savetxt("Z:\EAinPY\pypops" + str(gen+1) + ".txt",numpy.array(self.population),fmt='%1.1d',delimiter = ' ',newline = '\n')
            self.gener += 1

    def __getitem__(self):

        return self.population
    
    def fitness(self,a):

        f=0
        self.det = [0 for l1 in range(5)]
        
        for l1 in range(courses):

            for l2 in range(students):

                self.det[int(self.preferences[l1][l2])] += int(self.allocation[l1][l2])
                f+=int(self.preferences[l1][l2])*int(self.allocation[l1][l2])

        return f

    def allocate(self,c):

        self.allocation =[[0 for i in range(students)] for j in range(courses)]

        for s in range(students):

            self.stud = c[s]

            for k in range(courses):

                nos = 0
                strflag = 0

                cr = self.preffind(k,self.stud)
                strflag = self.clstrcheck(cr)

                if strflag == 1 :

                    self.allocation[cr][self.stud] = 1
                    break

    def preffind(self,n,stu):

        prefa =[[0 for i in range(2)] for j in range(courses)]

        for pfi in range(courses):

            prefa[pfi][0]=self.preferences[pfi][stu]
            prefa[pfi][1]=pfi

        
        prefa.sort(key=lambda pfi:pfi[0],reverse=True)

        return prefa[n][1]
	
    def clstrcheck(self,c):

        nos=0

        nos = sum(int(self.allocation[c][v]) for v in range(students))

        if (nos<15) :

            return 1

        else :

            return 0
    def store_avg_fitness(self):

        fitsum = 0

        for fiti in range(10):

            fitsum += self.population[fiti][students]

        fitavg = float(fitsum/10)

        store = open("Z:\EAinPY\\Fittrend.txt", "a")
        store.write(' FITNESS AVERAGE : ' + str(fitavg) + '\n\n')

    def store_top_alloc(self):

        self.ctemp = [0 for ti in  range(students)]
        self.ctemp = [self.population[0][i] for i in range(students)]
        self.allocate(self.ctemp)
        self.fittemp = self.fitness(self.allocation)

        store = open("Z:\EAinPY\\Fittrend.txt", "a")
        store.write('GENERATION : ' + str(self.gener) + ' FITNESS : ' + str(self.fittemp) + ' DETAILS : ' + str(self.det[::-1]) + '\n\n')
        

        numpy.savetxt("Z:\EAinPY\Bestalloc.txt",numpy.array(self.allocation),fmt='%1.1d',delimiter = ' ',newline = '\n')
        
    
    def __parentloader(self):

        self.p1 = [self.population[0][i] for i in range(students)]  
        self.p2 = [self.population[1][i] for i in range(students)]


    def __O1X(self):

        o1l=10
        o1u=50
        self.c1=[]
        self.c2=[]
        for o1i in range(students):
            self.c1.append(-1)
        for o1i in range(o1l,o1u+1,1):
            self.c1[o1i]=self.p1[o1i]
        o1pc1=self.p1.copy()
        o1pc2=self.p2.copy()

        for o1i in range(o1l,o1u+1,1):
            self.c1[o1i]=self.p1[o1i]
    
        for o1i in range(o1l,o1u+1,1):
            for o1j in range(students):
                if(o1pc1[o1i]==o1pc2[o1j]):
                    o1pc2[o1j]=-2
            
        o1x=0
        o1y=0
        i=0
        while(o1x<students and o1y<students):
            if(o1pc2[o1x]!=-2 and self.c1[o1y]==-1):
                self.c1[o1y]=o1pc2[o1x]
                o1y=o1y+1
                o1x=o1x+1
                i=i+1
            elif(o1pc2[o1x]==-2):
                o1x=o1x+1
            elif(self.c1[o1y]!=-1):
                o1y=o1y+1


        for o1i in range(students):
            self.c2.append(-1)
        for o1i in range(o1l,o1u+1,1):
            self.c2[o1i]=self.p2[o1i]
        o1pc1=self.p1.copy()
        o1pc2=self.p2.copy()
    
        for o1i in range(o1l,o1u+1,1):
            for o1j in range(students):
                if(o1pc2[o1i]==o1pc1[o1j]):
                    o1pc1[o1j]=-2
            
        o1x=0
        o1y=0
        i=0
        while(o1x<students and o1y<students):
            if(o1pc1[o1x]!=-2 and self.c2[o1y]==-1):
                self.c2[o1y]=o1pc1[o1x]
                o1y=o1y+1
                o1x=o1x+1
                i=i+1
            elif(o1pc1[o1x]==-2):
                o1x=o1x+1
            elif(self.c2[o1y]!=-1):
                o1y=o1y+1


    def __O2X(self):

        o2r1=numpy.random.randint(1,students) #random funtion to be added
        o2r=[0 for o2i in range(o2r1)]
        o2a=[0 for o2i in range(o2r1)]
        o2a[0]=-1

        for o2i in range(o2r1):
            o2r2=numpy.random.randint(1,students) #again randomise function
            o2r[o2i]=o2r2
            o2a[o2i]=self.p2[o2r2-1]
   
    
        o2loop=1
        o2ex=[]
        o2count=0

        for o2i in range(o2r1):
            for o2j in range(o2i+1,o2r1,1):
                if(o2r[o2i]==o2r[o2j]):
           
                    while(o2loop==1):
                
                        o2r2=numpy.random.randint(1,students)#again randomise function
                        o2r[o2j]=o2r2
                        o2a[o2j]=self.p2[o2r2-1]
                        for o2k in range(o2r1):
                            if(o2r[o2j]==o2r[o2k]):
                                o2count=o2count+1
                        if(o2count<2):
                            o2count=0
                            break
                
                        o2count=0
                

        self.c3=[0 for o2i in range(students)]# change it according to ur wish

        for o2i in range(students):#
            self.c3[o2i]=self.p1[o2i]

        for o2i in range(o2r1):
            #print('**1')
            for o2j in range(students):#
                #print('**2')
                if(o2a[o2i]==self.c3[o2j]):
                    self.c3[o2j]=-1
                    break

        o2j=0

        for o2i in range(students):
            #print('**3')
            if(self.c3[o2i]==-1):
                self.c3[o2i]=o2a[o2j]
                o2j=o2j+1


    def rec(self,pmxg,pmxarr,pmxpar,pmxa,pmxb):
        for pmxy in range(students):
            if(pmxpar[pmxy]==pmxarr[pmxg]):
                break
        if(pmxa<=pmxy and pmxy<=pmxb):
            return self.rec(pmxy,pmxarr,pmxpar,pmxa,pmxb)
        else:
            return pmxy


    def __PMX(self):
    
        pmxl=numpy.random.randint(students)
        pmxu=40
        self.c1=[-1 for i in range(students)]
        self.c2=[-1 for i in range(students)]

        print ('\n ******* \n'+ str(self.p1))
        
        for pmxi in range(pmxl,pmxu+1):
            self.c1[pmxi]=self.p1[pmxi]

        for pmxi in range(pmxl,pmxu+1,1):
            for pmxy in range(students):
                if(self.p2[pmxy]==self.c1[pmxi]):
                    break
            pmxflag=1
            for pmxk in range(pmxl,pmxu+1,1):
                if(self.p1[pmxk]==self.p2[pmxi]):
                
                    pmxflag=0
            if(pmxflag==1):
                if(pmxl<=pmxy and pmxy<=pmxu+1):
                    z=self.rec(pmxy,self.c1,self.p2,pmxl,pmxu)
                    self.c1[z]=self.p2[pmxi]

                else:
                    self.c1[pmxy]=self.p2[pmxi]

        for pmxi in range(students):
            if(self.c1[pmxi]==-1):
                self.c1[pmxi]=self.p2[pmxi]

        for pmxi in range(pmxl,pmxu+1):
            self.c2[pmxi]=self.p2[pmxi]

        for pmxi in range(pmxl,pmxu+1,1):
            for pmxy in range(students):
                if(self.p1[pmxy]==self.c2[pmxi]):
                    break
            pmxflag=1
            for pmxk in range(pmxl,pmxu+1,1):
                if(self.p2[pmxk]==self.p1[pmxi]):
                
                    pmxflag=0
            if(pmxflag==1):
                if(pmxl<=pmxy and pmxy<=pmxu+1):
                    z=self.rec(pmxy,self.c2,self.p1,pmxl,pmxu)
                    self.c2[z]=self.p1[pmxi]

                else:
                    self.c2[pmxy]=self.p1[pmxi]

        for pmxi in range(students):
            if(self.c2[pmxi]==-1):
                self.c2[pmxi]=self.p1[pmxi]
    
    def __Edgex(self):

        nlist = [[-1 for oj in range(3)]for oi in range(students)]

        narr = [-1 for oi in range(4)]

        for oi in range(students):

            narr = [-1 for oi in range(4)]

            nlist[oi][0] = self.p1[oi]

            if oi == 0 :

                narr[0] = self.p1[-1]

            else :

                narr[0] = self.p1[oi-1]

            tx = self.p2.index(nlist[oi][0])

            if tx == 0:

                narr[2] = self.p2[-1]

            else :

                narr[2] = self.p2[tx-1]

            if oi == students-1 :

                narr[1] = self.p1[0]

            else :

                narr[1] = self.p1[oi+1]

            if tx == students-1:

                narr[3] = self.p2[0]

            else :

                narr[3] = self.p2[tx+1]

            nlist[oi][2] = list(set(narr))
            nlist[oi][1] = len(narr)
                     
        self.c3 = []

        k=0

        while len(self.c3) < students :

            self.c3.append(nlist[k][0])

            temp = nlist[k][0]

            for i in range(len(nlist)):

                if nlist[k][0] in nlist[i][2]:

                    nlist[i][2].remove(nlist[k][0])
            
                nlist[i][1] = len(nlist[i][2])

            narr2 = nlist[k][2]

            nlist.sort(key=lambda i:i[1])

            nlist = [v for v in nlist if v[0]!=temp]

            for i in range(len(nlist)):

                if nlist[i][0] in narr2 :

                    k = i

                    break

            
    def __Cycx(self):

        z = [-1 for i in range(students)]
        cycflag = 1

        for i in range(students):

            if z[i] == -1 :

                s1 = i

                while (z[s1]!=cycflag) :

                    z[s1] = cycflag

                    sv = self.p2[s1]

                    s1 = self.p1.index(sv)

                cycflag+= 1

        for i in range(students):

            if (z[i]%2==1) :

                self.c1[i] = self.p1[i]
                self.c2[i] = self.p2[i]

            else :

                self.c1[i] = self.p2[i]
                self.c2[i] = self.p1[i]

    def __nextgenpop(self):

        for i in range(10) :

            for j in range(students) :

                self.population[i][j] = self.c3[j]

            self.allocate(self.c3)
            self.fitct = self.fitness(self.allocation)
            self.population[i][students] = self.fitct

            self.__mutate_shuffle(self.c3)

    def __nextgenpop2(self):

        for i in range(5) :

            for j in range(students) :

                self.population[i][j] = self.c1[j]
                self.population[i+5][j] = self.c2[j]

            self.allocate(self.c1)
            self.fitct = self.fitness(self.allocation)
            self.population[i][students] = self.fitct

            self.allocate(self.c2)
            self.fitct = self.fitness(self.allocation)
            self.population[i+5][students] = self.fitct        

            self.__mutate_insert(self.c1)
            self.__mutate_insert(self.c2)

    
    def __mutate_swap(self,ch):

        e = numpy.random.choice(students-1)
        r = e+(numpy.random.choice(students-e))

        te = ch[e]
        ch[e] = ch[r]
        ch[r] = te

    def __mutate_insert(self,ch):

        e = numpy.random.choice(students-1)
        r = e+(numpy.random.choice(students-e))

        te = ch[e+1]
        ch[e+1] = ch[r]
        ch[r] = te

    def __mutate_shuffle(self,ch):

        e = numpy.random.choice(students-1)
        r = e+(numpy.random.choice(students-e))

        temparr = [ch[o] for o in range(e,r)]
        numpy.random.shuffle(temparr)

        ch[e:r] = temparr

if __name__ == ('__main__'):

    p=pop()
    
    

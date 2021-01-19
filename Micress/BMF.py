# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import shutil
from itertools import product 

class BMF(object):
    """批量修改可执行文件，顶级类 

    函数功能待描述
    
    Parameters
    ----------
    filename : string | tuple
        需要更改的文件名。
    file_workdir : string
        被更改文件的路径。
    save_dir : string
        生成的批量文件保存路径。

    Attributes
    ----------
    menu_info    : 菜单 
    filename     : 需要更改的文件名
    file_workdir : 被更改文件的路径
    save_dir     : 生成的批量文件保存路径

    Methods
    -------
    show_menu()
        可以对文件进行的操作。
    start()
        得到乱序,按首字母排序的可调参数列表。
    search(*user_enter)
        得到关键字对应值的索引值。
    datafile2list()
        得到包括所有文件内容的列表。
    func2()
        得到描述可更改值所有语句的元组值。
    func3()
        得到可更改值的列表。
    func4()
        得到描述可更改值上一语句的列表。
    datafile2dict(par, mode=None)
        查出所有的文件内容，并包装成字典返回。
    add()
        暂无。
    delete()
        暂无。
    list2txt(lines,f2)
        列表转文本。
    dict2datafile()
        字典转文本。
    copyfile2aimdir(path)
        批量移动文件到指定位置。
    main(index,*varible_range) 
        主程序。
    multi_processes()
        系统调用可执行文本
    """
    def __init__(self,filename,file_workdir,save_dir,**options):
        
        #可以对文件及文件内容进行的操作 
        self.menu_info = {'search':"查询",
    
        'delete':"删除",
    
        'main':"修改",
    
        'add':"添加",
    
        'multi_processes':"多任务"}  
        
        self.filename=filename
        
        self.workdir=file_workdir
        
        self.save_dir=save_dir
      
    def show_menu(self):
        '''
    
        展示可以对文件进行的操作

        '''
        print(self.menu_info)
        
    def start(self):
        
        '''
    
        初始化文件，展示可调参数

        '''
        mapdict=self.func4()
        
        new = sorted(mapdict,key= lambda i:i[0])#按首字母排序
        
        return mapdict,new
        
    def search(self,*user_enter):    
        '''
        
        查询并打印出用户查询关键字所在的行和下一行
        
        '''  
           
        list = self.datafile2list()
        
        b=0
        a=[]
        for i,line in enumerate(list):
            for j in range(len(user_enter)):
                if user_enter[j] in line:
                
                    print(line)       #打印查询的关键字     
                    print(list[i+1])  #打印关键字对应的行
                    b=i+1
                    a.append(b)       #关键字索引值
                    
        if len(a)==0:
            
            print("查无结果")
            
            a=[]
       
        return a
    
    def datafile2list(self):
        '''
        
        文件转列表
        
        ''' 
        with open(self.workdir+self.filename+'.txt','r') as f1:#打开文件自动关闭
            list_lines = f1.readlines() #读取文本每一行
            
        return list_lines
        
    def func2(self):
        '''
        
        得到描述可更改值所有语句的元组值。
         
        '''
        list = self.datafile2list()
    
        list1=[]
        
        list2=[]
                
        for i,line in enumerate(list):
    
            if line[0] != "#": #获取关键词对应值
        
                list1.append([line,i])
                   
        for j in range(len(list1)):
            list2.append(tuple(list[list1[j-1][1]+1:list1[j][1]])) #多行转元组，为了转字典
            
        list2[0]=tuple(list[:list1[0][1]])
        return list2
    
    def func3(self):
        '''
        
        得到可更改值的列表。
        
        '''
        list = self.datafile2list()
    
        list1=[]
        
        list3=[]
        
        for i,line in enumerate(list):
    
            if line[0] != "#":
        
                list1.append([line,i])
                list3.append(line[:-1])
    
        return list3
    
    def func4(self):
        '''
        
        得到描述可更改值上一语句的列表。
        
        '''
        list = self.datafile2list()
    
        list1=[]
        
        list4=[]
        
        for i,line in enumerate(list):
    
            if line[0] != "#":
        
                list1.append([line,i])
                
                list4.append(list[i-1][2:-1])
                
        return list4
        
    def datafile2dict(self):
    
        '''
    
        查出所有的文件内容，并包装成字典返回
    
        '''
        list = self.datafile2list()
        
        list2,list3=self.func1()
        
        mapc={}
        
        for key in list[2]:
            mapc[key]=list3[list[2].index(key)] #index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
        
        '''
        for k, v in zip(list2,list3):
            
            mapc[k]= v
        '''    
        
        '''
        mapc=[{k,v} for k, v in zip(list2,list3)] #zip()
            
        '''
        return mapc
    
    def add(self):
        '''
        增加某一行，
        ''' 
        pass
    
    def update(self):
        '''
        
        '''
        pass
           
    def delete(self):
        '''
        删除某一行，可以根据Cooling rate，
        ''' 
        pass
    
    def list2txt(self,lines,f2):
        '''
        
        列表转文本
        
        ''' 
        
        list = []
        for i in range(len(lines)):
            list.append(lines[i]) #将每一行的数据加入列表       
            f2.write(list[i])
        
    
    def dict2datafile(self):
        '''
        
        字典转文本
        
        ''' 
        
        pass
    
    def copyfile2aimdir(self,path):
        '''
        
        批量移动文件到指定位置
        
        '''
        if not os.path.isdir(path):
            print("请输入正确的保存路径")
            
        pathDir = os.listdir(self.workdir)
        k=0
        i=0
        for allDir in pathDir:
            
            if( (i%100) == 0):
                print("100 的倍数，新建一个文件夹")
            k += 1
            
            from_path = os.path.join(self.workdir, allDir)
            
            to_path = path + "\\" + self.filename + str(k)
            
            shutil.copy(from_path, to_path) 
            i += 1
        
    def main(self,index,*varible_range):
        '''
        主程序
        ''' 
        lines = self.datafile2list()
        
        varible=index
        varible_number=len(varible) #需要变更的参数数量
        
        '''
        varible1=int(self.func3())
        '''
        
        number1=[]
        number2=[]
        number3=[]
        output_index=self.search('Name of result files')[0] 
        
        para=lines[output_index]
        
        if  varible_number==0:
            print('无可变参数')
            
        elif varible_number==1:
            
            for i in range(varible_range[0],varible_range[1],varible_range[2]):
                number1.append(i) #生成变量范围
                
            for j in range(len(number1)):
                
                with open(self.save_dir+'\\'+self.filename+str(number1[j])+'.txt', "w") as f2:
                
                    lines[index[0]] = str(number1[j])+'\n'
                    lines[output_index] = para.split('/')[0]+str(number1[j])+'/'+str(number1[j])+para.split('/')[1]
                
                    self.list2txt(lines,f2)
                
        elif varible_number==2:
            
            for i in range(varible_range[0],varible_range[1],varible_range[2]):
                number1.append(i)
            
            for j in range(varible_range[3],varible_range[4],varible_range[5]):
                number2.append(j)
            
            for item in product(number1,number2):
                
                with open(self.save_dir+'\\'+self.filename+str(item[0])+'_'+str(item[1])+'.txt', "w") as f2:
                
                    lines[index[0]] = str(item[0])+'\n'
                    lines[index[1]] = str(item[1])+'\n'
                    lines[output_index] = para.split('/')[0]+str(item[0])+'_'+str(item[1])+'/'+str(item[0])+'_'+str(item[1])+para.split('/')[1]
                
                    self.list2txt(lines,f2)
                
        elif varible_number==3:
            for i in range(varible_range[0],varible_range[1],varible_range[2]):
                number1.append(i)
            
            for j in range(varible_range[3],varible_range[4],varible_range[5]):
                number2.append(j)
                
            for k in range(varible_range[6],varible_range[7],varible_range[8]):
                number3.append(k)
                
            for item in product(number1,number2,number3):
                
                with open(self.save_dir+'\\'+self.filename+str(item[0])+'_'+str(item[1])+'_'+str(item[2])+'.txt', "w") as f2:
                
                    lines[index[0]] = str(item[0])+'\n'
                    lines[index[1]] = str(item[1])+'\n'
                    lines[index[2]] = str(item[2])+'\n'
                    lines[output_index] = para.split('/')[0]+str(item[0])+'_'+str(item[1])+'_'+str(item[2])+'/'+str(item[0])+'_'+str(item[1])+'_'+str(item[2])+para.split('/')[1]
                
                    self.list2txt(lines,f2)
                
        elif varible_number>3:
            
            print('')
            
        def multi_processes(self):
            '''
            
            系统调用可执行文本，更改为subprocess
            
            '''
            
            b=[]
            for filename in os.listdir(self.save_dir): 
                b.append(os.path.join(self.save_dir,filename))
            
            for i in range(len(b)):    
                os.system('E:\MICRESS-6.402\Bin\MICRESS_TQ'+' '+b[i])


if __name__ == '__main__':  
    
    filename='T003_AlCu_dri'
    file_workdir=r'D:\zyzl\repository\mupif\mupif\examples\bacth make file\Batch Modify Executable Files\files\\'
    save_dir=r'E:\MICRESS-6.402\Examples\Training\test'
    test=BMF(filename,file_workdir,save_dir)
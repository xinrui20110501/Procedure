#!/usr/bin/env python
#coding=utf-8
import os  
def scan_files(directory,prefix=None,postfix=None): 
  files_list=[] 
     
  for root, sub_dirs, files in os.walk(directory): 
    for special_file in files: 
      if postfix: 
        if special_file.endswith(postfix): 
          files_list.append(os.path.join(root,special_file)) 
      elif prefix: 
        if special_file.startswith(prefix): 
          files_list.append(os.path.join(root,special_file)) 
      else: 
        files_list.append(os.path.join(root,special_file)) 
                
  return files_list
file = scan_files(raw_input(unicode('请输入文件所在路径:','utf-8').encode('gbk')),prefix='Com')
for line in file:
    with open(line) as f:
        for line in f:
            if 'insert' in line:
                 if ',XZQH' in line:
                   line = line.replace(',XZQH','')
                 elif ', XZQH' in line:
                   line = line.replace(', XZQH','')
                 b=line.index('insert')
                 line=line[b:]
                 c = line.split(',')
                 c.pop(-1)
                 line = ','.join(c)+');\n'
                 #print c
                # print line 
                 file = open('c:\ComServer.sql','a')
                 f=file.write(line)
                 file.close()
print(u'程序运行中，请稍等...')
print(u'程序运行完毕！') 
print(u'文件已生成，生成文件为c:\ComServer.sql')
os.system('pause')
   
           
            
       

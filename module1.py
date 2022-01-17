def failist_Lugemine(f:str,u:list):
    """Info failist f listisse u
    """
    fail=open(f,'r')
    for rida in fail: #прочитывает каждую строку в файле
        u.append(rida.strip())
    fail.close()
    return u
def failisse_salvestamine(f:str,u:list):
    fail=open(f,'w')
    for el in u:
        fail.write(el+'\n')
    fail.close()
def rida_salvestamine(f:str,rida:str):
    fail=open(f,'a')
    fail.write(rida+'\n')
    fail.close()
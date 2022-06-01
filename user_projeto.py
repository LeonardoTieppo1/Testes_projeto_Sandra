class User:
        def login(self,username):
            if(len(username)>=8):
                s=0
                for i in username:
                    if(i=='@'or i=='$' or i=='_'): 
                        s+=1
                        if(s>=1):
                            print("Login validado!")
                            return True
                        else:
                            print("Login invalido!")
                            return False
            else:
                print("Nome do usuário fora do tamanho necessário!")
                return False
            
        def senha(self,password):
            if(len(password)<=8):
                l, u, s, d = 0, 0, 0, 0
                print("Senha dentro do tamanho")
                for i in password: 
                    if (i.islower()): 
                        l+=1            
                    if (i.isupper()): 
                        u+=1            
                    if (i.isdigit()): 
                        d+=1            
                    if(i=="@" or i=="$" or i=="%" or i=="&" or i=="(" or i==")" or i=="."): 
                            s+=1           
                if (l>=1 and u>=1 and s>=1 and d>=1 and l+s+u+d==len(password)): 
                        print("Senha validada!")
                        return True 
                else: 
                    print("Senha invalida!")
                    return False 
            else:
                print("Senha maior que o necessário!")
                return False

#Salvar como user_projeto.py
'''
Nome das alunas: Vitória Silva dos Reis e Maria Eduarda Kanhet
'''

#----------------importanto bibliotecas------------#
from tkinter import *
import tkinter as tk
import mysql.connector


try:
    global conexao
    conexao = mysql.connector.connect(user = "root",host = "127.0.0.1")
    bdOK = True
except:
	print("Erro ao conectar ao banco de dados.")
	bdOK = False

if bdOK:
    global cursor
    cursor = conexao.cursor()
# ---------- Cria e Conecta o Banco de Dados ---------- #	
    try:
	    cursor.execute("USE atrizes;")
	    print("selecionado!!")
    except:
	    cursor.execute("USE atrizes;")
	    print("selecionado!")

class Urna_Eletronica():
    
    def __init__(self):
        self.janela = Tk()                    #instancia a janela
        self.janela.title("Urna Eletrônica")  #adiciona título a janela
        self.janela.geometry("610x310")       #determina o tamanho da janela
        self.janela.resizable(False,False)    #impede o redimensionamento
        self.janela.config(bg = "black")      #determina a cor da janela
        #self.janela.iconbitmap("trofeu.ico")  #adiciona o ícone personalizado
        self.layout()
        self.texto = ""
        
        self.contador = 0
        
        self.janela.mainloop()


    def mostrarBotao(self,text):
        if self.contador <= 1:
            self.label1["text"] += text
            self.texto = self.texto + text
            self.contador += 1
            if self.contador == 2:
                try:
                    cursor.execute("SELECT nome FROM atri WHERE num = '{}'".format(self.texto))
                    for i in cursor:
                        lista = []
                        for x in i:
                            lista.append(x)
                    self.nCandi = lista[0]
                    self.layout()
                    cursor.execute("SELECT foto FROM atri WHERE num = '{}'".format(self.texto))
                    for i in cursor:
                        lista2 = []
                        for x in i:
                            lista2.append(x)
                    self.ftCandi = lista2[0]
                    
                    caminho = "C:\\fonte\\"

                    self.lblnomecand = Label(self.janela, text = self.nCandi, font = "Arial 16", bg = "white")
                    self.lblnomecand.place(relx = 0.14, rely = 0.5, relwidth = 0.18, relheight = 0.1)
                    self.img = PhotoImage(file = caminho+self.ftCandi)
                    self.lblfoto = Label(self.janela, image = self.img)
                    self.lblfoto.place(relx = 0.32, rely = 0.18, relwidth = 0.2, relheight = 0.45)      
                
                except:
                    self.lbl3 = Label(self.janela, bg = "orange")
                    self.lbl3.place(relx = 0.01, rely = 0.1, relwidth = 0.5, relheight = 0.8)
                    
                    lblconf = Label(self.janela, text = "Seu cantor não existe", font = "Arial 18", bg = "orange")
                    lblconf.place(relx = 0.01, rely = 0.3, relwidth = 0.49, relheight = 0.25)


                    #self.lbltextao = Label(self.janela, bg = "orange", fg = "black", text = '''Aperte a tecla:
                #CONFIRMAR para CONFIRMAR este voto
                #CORRIGIR para REINICIAR este voto''',font = "Arial 8", justify = LEFT)
                    #self.lbltextao.place(relx = 0.04, rely = 0.7, relwidth = 0.45, relheight = 0.15)
        else:
            pass


    def corrigir(self):
        self.label1['text'] = ""
        
        self.layout()
    
    def layout(self): 
# -------------------------------- Criando Botões ------------------------------ #

        self.btn1 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "1", command = lambda: self.mostrarBotao("1")) #relief = "raised" é a borda dos botões
        self.btn1.place(relx = 0.6, rely = 0.1, relwidth = 0.1, relheight = 0.1)
        
        self.btn2 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "2", command = lambda: self.mostrarBotao("2"))
        self.btn2.place(relx = 0.72, rely = 0.1, relwidth = 0.1, relheight = 0.1)


        self.btn3 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "3", command = lambda: self.mostrarBotao("3"))
        self.btn3.place(relx = 0.84, rely = 0.1, relwidth = 0.1, relheight = 0.1)


        self.btn4 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "4", command = lambda: self.mostrarBotao("4"))
        self.btn4.place(relx = 0.6, rely = 0.25, relwidth = 0.1, relheight = 0.1)
    
        self.btn5 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "5", command = lambda: self.mostrarBotao("5"))
        self.btn5.place(relx = 0.72, rely = 0.25, relwidth = 0.1, relheight = 0.1)

        self.btn6 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "6", command = lambda: self.mostrarBotao("6"))
        self.btn6.place(relx = 0.84, rely = 0.25, relwidth = 0.1, relheight = 0.1)


        self.btn7 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "7", command = lambda: self.mostrarBotao("7"))
        self.btn7.place(relx = 0.6, rely = 0.4, relwidth = 0.1, relheight = 0.1)

        self.btn8 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "8", command = lambda: self.mostrarBotao("8"))
        self.btn8.place(relx = 0.72, rely = 0.4, relwidth = 0.1, relheight = 0.1)

        self.btn9 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "9", command = lambda: self.mostrarBotao("9"))
        self.btn9.place(relx = 0.84, rely = 0.4, relwidth = 0.1, relheight = 0.1)

        self.btn0 = Button(self.janela, relief = "raised", bd = 5, bg = "gray", fg = "black", text = "0", command = lambda: self.mostrarBotao("0"))
        self.btn0.place(relx = 0.72, rely = 0.55, relwidth = 0.1, relheight = 0.1)

        self.btnbranco = Button(self.janela, bg = "white", text = "BRANCO", fg = "black", font = "Bookman\ Old\ Style 10", command = lambda : self.branco())
        self.btnbranco.place(relx = 0.55, rely = 0.76, relwidth = 0.13, relheight = 0.13)
        
        self.btncorrige = Button(self.janela, bg = "red", text = "CORRIGIR", fg = "black", font = "Bookman\ Old\ Style 10", command = lambda: self.corrigir())
        self.btncorrige.place(relx = 0.7, rely = 0.76, relwidth = 0.13, relheight = 0.13)

        self.btnconfirma = Button(self.janela, bg = "green", text = "CONFIRMAR", fg = "black", font = "Bookman\ Old\ Style 10", command = lambda: self.tampar())
        self.btnconfirma.place(relx = 0.85, rely = 0.76, relwidth = 0.14, relheight = 0.13)
        
        self.label1 = Label(self.janela, font = "Arial 25", bg = "orange", fg = "White", text = "")
        self.label1.place(relx = 0.01, rely = 0.1, relwidth = 0.5, relheight = 0.8)

        self.sla = Label(self.janela, text="Vote para melhor cantor:", font= 'Bookman\ Old\ Style 16', bg = "black", fg = "white")   
        self.sla.place(relx=0.01, rely=0.1, relwidth = 0.5) 

    def bd(self):
        pass
     
    def tampar(self):
        #--------------------concluindo a votação--------------------#
        self.lbl3 = Label(self.janela, bg = "yellow")
        self.lbl3.place(relx = 0.01, rely = 0.1, relwidth = 0.5, relheight = 0.8)
    
        lblconf = Label(self.janela, text = "FIM", font = "Arial 38", bg = "yellow")
        lblconf.place(relx = 0.01, rely = 0.3, relwidth = 0.49, relheight = 0.25)

    def branco(self):
        #self.brancoatv = True
        self.lbl3 = Label(self.janela, bg = "#91175c")
        self.lbl3.place(relx = 0.01, rely = 0.1, relwidth = 0.5, relheight = 0.8)
        
        lblconf = Label(self.janela, text = "Seu voto é BRANCO", font = "Arial 18", bg = "#91175c")
        lblconf.place(relx = 0.01, rely = 0.3, relwidth = 0.49, relheight = 0.25)

        self.lbltextao = Label(self.janela, bg = "#91175c", fg = "black", text = '''Aperte a tecla:
    CONFIRMAR para CONFIRMAR este voto
    CORRIGIR para REINICIAR este voto''', font = "Arial 8", justify = LEFT)
        self.lbltextao.place(relx = 0.04, rely = 0.7, relwidth = 0.35, relheight = 0.15)
    
    def imagem(self):
        pass
        self.foto = PhotoImage(file = "C:\\Users\\pc1\\Documents\\SENAI\\2021\\Urna prova\\teste.py")
        
        self.lblfoto = Label(self.janela, bg = "white", image = self.foto)
        self.lblfoto.place(relx = 0.2, rely = 0.2, relheight = 0.3, relwidth = 0.3)



Urna_Eletronica()

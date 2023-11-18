# -*- coding: utf-8 -*-
"""jogo da velha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kdNe2O5iFVSiojMRVIuykh3rHuoVwKob
"""

# Criando o jogo da velha

class jogoDaVelha:

  tabuleiro =  {'7': ' ' , '8': ' ' , '9': ' ',
                '4': ' ' , '5': ' ' , '6': ' ',
                '1': ' ' , '2': ' ' , '3': ' '}

  jogador_inicial = "X"
  turno = jogador_inicial

  def __init__(self, jogador_inicial = "X"):
   self.turno = jogador_inicial



  def exibir_tabuleiro(self):
    print("┌───┬───┬───┐")
    print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
    print("└───┴───┴───┘")

  def verificarjogada(self,jogada):
    if jogada in self.tabuleiro.keys():
      if self.tabuleiro[jogada]==" ":
         return True
      return False

  def verificar_tabuleiro(self):
    #horizontal
    if self.tabuleiro["7"] == self.tabuleiro["8"] == self.tabuleiro["9"]!=" ":
      return self.tabuleiro["7"]
    if self.tabuleiro["4"] == self.tabuleiro["5"] == self.tabuleiro["6"]!=" ":
      return self.tabuleiro["4"]
    if self.tabuleiro["1"] == self.tabuleiro["2"] == self.tabuleiro["3"]!=" ":
      return self.tabuleiro["1"]
    #Vertical
    if self.tabuleiro["7"] == self.tabuleiro["4"] == self.tabuleiro["1"]!=" ":
      return self.tabuleiro["7"]
    if self.tabuleiro["8"] == self.tabuleiro["5"] == self.tabuleiro["2"]!=" ":
      return self.tabuleiro["8"]
    if self.tabuleiro["9"] == self.tabuleiro["6"] == self.tabuleiro["3"]!=" ":
      return self.tabuleiro["9"]
    #Diagonal
    if self.tabuleiro["9"] == self.tabuleiro["5"] == self.tabuleiro["2"]!=" ":
      return self.tabuleiro["9"]
    if self.tabuleiro["7"] == self.tabuleiro["5"] == self.tabuleiro["3"]!=" ":
      return self.tabuleiro["7"]
    #Empate
    if[*self.tabuleiro.values()].count(" ") == 0:
      return "Empate"
    else:
      return[*self.tabuleiro.values()].count(" ")

  def jogar(self):
    while True:
      self.exibir_tabuleiro()
      print(f"Turno de {self.turno} - Faça a sua jogada!")
      while True:
        jogada = input("Jogada: ")
        if self.verificarjogada(jogada):
          break
        else:
          print(f" A jogada do {self.turno} é inválida, tente novamente! ")

      self.tabuleiro[jogada]= self.turno
      estado = self.verificar_tabuleiro()
      if estado == "X":
        print("X é o vencedor!")
      elif estado =="O":
         print("O é o vencedor")
      elif estado == "Empate":
        print("Empate")
        break
      self.turno = "X" if self.turno== "O" else "O"
    self.exibir_tabuleiro()

jogo=jogoDaVelha()
jogo.jogar()

# Criando o jogo da velha

class jogoDaVelha:

  tabuleiro =  {'7': ' ' , '8': ' ' , '9': ' ',
                '4': ' ' , '5': ' ' , '6': ' ',
                '1': ' ' , '2': ' ' , '3': ' '}

  turno = None

  def __init__(self, jogador_inicial = "X"):
   self.turno = jogador_inicial



  def exibir_tabuleiro(self):
    print("┌───┬───┬───┐")
    print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
    print("└───┴───┴───┘")

  def verificarjogada(self,jogada):
    if jogada in self.tabuleiro.keys():
      if self.tabuleiro[jogada]==" ":
         return True
      return False

  def verificar_tabuleiro(self):
    #horizontal
    if self.tabuleiro["7"] == self.tabuleiro["8"] == self.tabuleiro["9"]!=" ":
      return self.tabuleiro["7"]
    elif self.tabuleiro["4"] == self.tabuleiro["5"] == self.tabuleiro["6"]!=" ":
      return self.tabuleiro["4"]
    elif self.tabuleiro["1"] == self.tabuleiro["2"] == self.tabuleiro["3"]!=" ":
      return self.tabuleiro["1"]
    #Vertical
    elif self.tabuleiro["7"] == self.tabuleiro["4"] == self.tabuleiro["1"]!=" ":
      return self.tabuleiro["7"]
    elif self.tabuleiro["8"] == self.tabuleiro["5"] == self.tabuleiro["2"]!=" ":
      return self.tabuleiro["8"]
    elif self.tabuleiro["9"] == self.tabuleiro["6"] == self.tabuleiro["3"]!=" ":
      return self.tabuleiro["9"]
    #Diagonal
    elif self.tabuleiro["9"] == self.tabuleiro["5"] == self.tabuleiro["1"]!=" ":
      return self.tabuleiro["9"]
    elif self.tabuleiro["7"] == self.tabuleiro["5"] == self.tabuleiro["3"]!=" ":
      return self.tabuleiro["7"]
    #Empate
    elif[*self.tabuleiro.values()].count(" ") == 0:
      return "Empate"
    else:
      return[*self.tabuleiro.values()].count(" ")

  def jogar(self):
    while True:
      self.exibir_tabuleiro()
      print(f"Turno de {self.turno} - Faça a sua jogada!")
      while True:
        jogada = input("Jogada: ")
        if self.verificarjogada(jogada):
          break
        else:
          print(f" A jogada do {self.turno} é inválida, tente novamente! ")

      self.tabuleiro[jogada]= self.turno
      estado = self.verificar_tabuleiro()
      if estado == "X":
        print("X é o vencedor!")
        break
      elif estado =="O":
         print("O é o vencedor")
         break
      elif estado == "Empate":
        print("Empate")
        break
      self.turno = "X" if self.turno== "O" else "O"
    self.exibir_tabuleiro()

jogo=jogoDaVelha()
jogo.jogar()
#유리잔처럼 투명한 과정 포함

ChangeWin=0 #바꿔서 이긴 횟수
ChangeLose=0 #바꿔서 진 횟수
KeepWin=0 #안 바꿔서 이긴 횟수
KeepLose=0 #안 바꿔서 진 횟수

from random import *

for i in range(1,10000):
  print('<제',str(i)+'번째 게임>') #게임 회차 표기

  car=int(randrange(1,4)) #1부터 3 중 하나의 문에 자동차 넣기
  guess=int(randrange(1,4)) #1부터 3중 하나의 문을 선택하기

  #진행자와 도전자가 고른 두 문이 아닌 문 중 하나를 골라서 염소임을 보이기
  goat=int(randrange(1,4))
  while(goat==car or goat == guess):
      goat=int(randrange(1,4))

  #바꾸지 않았을 경우
  print('안 바꾸는 경우:')
  if (guess==car):
      KeepWin+=1
      print("안 바꿔서 이긴 횟수: "+str(KeepWin),"안 바꿔서 진 횟수: "+str(KeepLose))#안 바꿔서 이긴 횟수, 진 횟수를 출력
      print('자동차:',str(car)+'번 문')#자동차의 위치
      print('내가 처음 고른 문:',str(guess)+'번 문')#내가 처음 고른 문
      print('공개된 염소의 위치:',str(goat)+'번 문')#공개된 염소의 문
      print('승리')
  else:
      KeepLose+=1
      print("안 바꿔서 이긴 횟수: "+str(KeepWin),"안 바꿔서 진 횟수: "+str(KeepLose))
      print('자동차:',str(car)+'번 문')#자동차의 위치
      print('내가 처음 고른 문:',str(guess)+'번 문')#내가 처음 고른 문
      print('공개된 염소의 위치:',str(goat)+'번 문')
      print('패배')
  print()
  
  #바꿨을 경우
  print('바꾸는 경우:')
  guess2=int(randrange(1,4))
  while(guess2==goat or guess2==guess):
      guess2=int(randrange(1,4))
  if (guess2==car):
      ChangeWin+=1
      print("바꿔서 이긴 횟수: "+str(ChangeWin),"바꿔서 진 횟수: "+str(ChangeLose))
      print('자동차:',str(car)+'번 문')#자동차의 위치
      print('내가 처음 고른 문:',str(guess)+'번 문')#내가 처음 고른 문
      print('공개된 염소의 위치:',str(goat)+'번 문')
      print('승리')
  else:
      ChangeLose+=1
      print("바꿔서 이긴 횟수: "+str(ChangeWin),"바꿔서 진 횟수: "+str(ChangeLose))
      print('자동차:',str(car)+'번 문')#자동차의 위치
      print('내가 처음 고른 문:',str(guess)+'번 문')#내가 처음 고른 문
      print('공개된 염소의 위치:',str(goat)+'번 문')
      print('바꾼위치:',str(guess2)+'번 문')
      print('패배')
  print()
  print()
  print()
  print()

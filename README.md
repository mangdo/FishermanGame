# :fishing_pole_and_fish: FishermanGame
> Pygame을 이용한 도시어부 게임입니다.   
> 2학년 1학기, '디지털미디어 공학 개론' 수업에서 진행한 파이썬 팀 프로젝트입니다.

<br>

## 1. 제작 기간 & 참여 인원
- 2018년 5월 14일 ~ 2018년 6월 11일
- 2인 1조 팀프로젝트

<br>

## 2. 사용 기술
  - Python 3.5
  - Pygame

<br>

## 3. 설치
```
pip install pygame
```
라이브러리가 필요합니다.

<br>

## 4. 게임 방법
<img src="https://user-images.githubusercontent.com/70243735/116635031-b57e2b80-a998-11eb-886e-1ee78919a61b.PNG" width ="600px">

<br>

## 5. 게임 플레이 영상

[![https://youtu.be/hVcaOJnIQr0](https://user-images.githubusercontent.com/70243735/116536038-7069e300-a91f-11eb-8c2d-d0f151aea5e4.PNG)](https://youtu.be/hVcaOJnIQr0)

<br>

## 6. 핵심 트러블 슈팅
### 6.1. 다양한 종류의 물고기 클래스 처리 :tropical_fish: :fish: 
 문제 상황
* 게임 속에 등장하는 물고기들은 종류마다 다른 속도, 무게, 이미지를 가지고 있습니다. 
 때문에 모두 다른 클래스로 만들었습니다.
* 하지만 **공통적인 기능**들이 존재하고 있기 때문에 같은 코드가 중복적으로 사용되고있었습니다.

해결
* 이를 보안하기 위해서 물고기 객체를 pygame의 group()을 사용하였습니다.
* **모든 클래스는 sprite를 상속**받고 있고 하나의 클래스에서는 여러 객체를 생성합니다.
* **생성된 객체는 group에 추가되고, 한번에 처리**됩니다.
<details>
<summary>코드 확인</summary>

```python
def run_game():  
  fishes=Group()
  (생략)
    
  while True:
    fishes.update(fishes)
    for fish in fishes.sprites():
      fish.blitme()
      (생략)
```
[코드 전문 확인하기](./main.py)
</details>

### 6.2. 물고기 객체의 랜덤 생성 :confused:

문제 상황
* 게임 속에 등장하는 물고기는 **사용자가 패턴을 알아챌 수 없게 랜덤**으로 계속 생성되어야했습니다.
* 계속 생성되기만 하면 메모리가 낭비가 생길 수 있었습니다.

해결
* 물고기를 랜덤으로 생성하는 함수 [makefish()](./gamefunction.py)를 만들었습니다.
* makefish()는 **스레드** 개념을 사용해서 해당 함수가 일정 시간마다 반복될 수 있게끔 만들었습니다. 
* 또한 random.choice()로 **물고기 종류를 랜덤**으로 선택됩니다.
* random.randint()으로 물고기 객체가 생성될 때의 **위치도 랜덤**하게 선택됩니다.
* 만약 물고기 객체가 화면 밖으로 나가게된다면 **group에서 해당 객체를 삭제**시킵니다.
<details>
<summary>코드 확인</summary>

```python

class Fish(Sprite):
    """첫번째 물고기 하나를 표현하는 클래스"""
    
    def __init__(self, screen,p):
        """물고기를 초기화하고 시작 위치를 지정한다"""
        super(Fish, self).__init__()
        (생략)
        self.rect.y = random.randint(250,450) #이 물고기는 y좌표 250부터 450사이에서 나옵니다
        
    def update(self,fishes): #물고기 위치 업데이트
        """물고기를 오른쪽으로 움직이고 화면밖을 지나가면 없애버림"""
        self.x += self.speed_factor
        self.rect.x = self.x
        for fish in fishes.copy():
            if fish.rect.left>=800:
                fishes.remove(fish)
        
```
[코드 전문 확인하기](./fish.py)
</details>

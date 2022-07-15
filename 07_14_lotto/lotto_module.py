# 1. lotto api로부터 데이터 받아오기

# 2. 지난 주 당첨 번호 알아내기 (1등만)

# 3. 랜덤 모듈이 가지고 있는 샘플 이라는 함수를 사용하여 1부터 45중에 무작위 6개를 뽑는다.

# 4. 그 번호가 당첨 번호와 일치하는지 확인한다.

# 5. 천 번 이상 새로운 로또 번호를 생성하여서 매번 당첨이 되었는지 확인해보는 로직 작성

# 6. 1등부터 2등을 포함하여 보너스 번호까지 4등 까지의 각 당첨 횟수 출력하기


# 0. 모듈 import

import requests
from random import sample




# 1. lotto api로부터 데이터 받아오기

rounds = 1023

url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={rounds}'
result = requests.get(url).json()




# 2. 지난 주 당첨 번호 알아내기 (1등만)

def pre_No_finder():
    rounds = 1  #시작회차 설정
    pre_No = []
    while True:   # 100단위로 returnValue: fail이 나올 때까지 rounds 증가

        url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={rounds}'
        result = requests.get(url).json()
        if len(result) < 2:
            rounds -= 100

            while True:  # 100단위에서 returnValue : fail 이 등장 시, 10단위로 증가시키며 returnValue : fail이 나올 때까지 반복
                url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={rounds}'
                result = requests.get(url).json()
                if len(result) <2:
                    rounds -= 10

                    while True:  # 다시 1단위로 올라가며 returnValue : fail이 등장하는 시점을 찾음.
                        url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={rounds}'
                        result = requests.get(url).json()
                        if len(result) <2:
                            for i in range(1, 7):
                                url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={rounds-1}'  #이전 회차 탐색을 위해 -1
                                result = requests.get(url).json()
                                pre_No.append(result['drwtNo'+str(i)]) # key값인 drwtNo?의 순번에 따라 작은 숫자부터 append
                            pre_No.append(result['bnusNo'])
                            break
                        rounds += 1
                    break
                rounds += 10
            break
        rounds += 100
    rounds -= 1

    print(f'이전 회차는 {rounds}회이며, 당첨 번호는 {pre_No[:-1]}, 보너스 번호는 {pre_No[-1]}입니다.')
    
    return pre_No




# 3. 랜덤 모듈이 가지고 있는 샘플 이라는 함수를 사용하여 1부터 45중에 무작위 6개를 뽑는다.

def sample_No_make():
    return sorted(sample(range(1, 45), 6))




# 4. 그 번호가 당첨 번호와 일치하는지 확인한다.

def sample_No_set(pre_No, sample_No):
    cnt = 0
    bns_cnt = [0, '맞추지 못 했습니다']
    same_No = []

    for i in pre_No[:-1]:
        if i in sample_No:
            cnt +=1
            same_No.append(i)

    if pre_No[-1] in same_No:
        bns_cnt = [1, '맞췄습니다.']  #;

    return f'맞춘 개수: {cnt} + {bns_cnt[0]}(보너스), 맞은 번호: {same_No}, 보너스 번호{pre_No[-1]}번을 {bns_cnt[1]}'




# 5. 천 번 이상 새로운 로또 번호를 생성하여서 매번 당첨이 되었는지 확인해보는 로직 작성

def sample_win_1000(pre_No):
    w_cnt = 0
    for _ in range(100000):
        sample_No = sample_No_make()
        cnt = 0
        for j in pre_No[:-1]:
            if j in sample_No:
                cnt +=1
        if cnt == 6:
            print('congratulation, you win')
            w_cnt += 1
    if w_cnt == 0:
        print('''you didn't won''')




# 6. 1등부터 2등을 포함하여 보너스 번호까지 4등 까지의 각 당첨 횟수 출력하기

def all_win_stacks(pre_No, rounds):
    win_cnt = {'1': 0, '2':0, '3':0, '4':0, '5':0}

    for i in range(int(rounds)):
        sample_No = sample_No_make()
        cnt, bns_cnt = 0, 0
        same_No = []
        
        for i in pre_No[:-1]:
            if i in sample_No:
                cnt +=1
                same_No.append(i)

        if pre_No[-1] in sample_No:
            bns_cnt = 1

        if cnt == 6:
            win_cnt['1'] += 1
        elif (cnt == 5) and (bns_cnt == 1):
            win_cnt['2'] += 1
        elif (cnt == 5) and (bns_cnt == 0):
            win_cnt['3'] += 1
        elif cnt == 4:
            win_cnt['4'] += 1
        elif cnt == 3:
            win_cnt['5'] += 1

    return print(f'''1등 당첨회수: {win_cnt['1']}
2등 당첨회수: {win_cnt['2']}
3등 당첨회수: {win_cnt['3']}
4등 당첨회수: {win_cnt['4']}
5등 당첨회수: {win_cnt['5']}''')
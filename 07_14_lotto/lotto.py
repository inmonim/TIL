from lotto_module import *

# 지난 주 로또 1등 번호 불러오기: pre_No_finder()

# 자동 번호 생성기: sample_No_make()

# 자동 번호 생성과 지난 주 로또 맞춰보기 : sample_No_set(pre_No, sample_No)
# *pre_No: pre_No_finder()로 리턴한 로또번호, sample_No: sample_No_make()로 리턴한 자동 로또 번호

# 1000번 중 1등 당첨이 가능했는가?: sample_win_1000(pre_No)

# rounds개의 자동 생성 번호 중 당첨 등수 당 당첨자 수?: all_win_stacks(pre_No, rounds):

pre_No = pre_No_finder()

sample_No = sample_No_make()

sample_No_set(pre_No, sample_No)

sample_win_1000(pre_No)

all_win_stacks(pre_No, 10000)
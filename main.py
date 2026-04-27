# 파일이름 :개인 맞춤형 피트니스 및 식단 플래너
# 작 성 자 :60261939 민상우
# 파이썬 1차 과제: 나만의 피트니스 플래너 만들기
# 작성자: [본인 이름]

print("환영합니다! 피트니스 플래너입니다 ")
print("-" * 50)

# 1. 정보 입력받기 (과제 조건: 변수 5개 이상, 자료형 3개 이상 사용)
name = input("이름을 입력해 주세요: ")                # 문자열(str)
age = int(input("나이가 어떻게 되시나요? : "))       # 정수(int)
height = float(input("키(cm)를 알려주세요: "))       # 실수(float)
weight = float(input("현재 몸무게(kg)는? : "))       # 실수(float)
goal_weight = float(input("목표 몸무게(kg)는? : "))  # 실수(float)

# 2. 데이터 계산하기 (산술 연산 활용)
# BMI 공식 쓸 때 키를 미터(m) 단위로 바꿔야 함
height_m = height / 100 
my_bmi = weight / (height_m * height_m)

# 목표까지 얼마나 빼야 하는지 계산
diff = weight - goal_weight

# 3. 결과 출력하기 (f-string 사용)
print("\n" + "*" * 20 + " 분석 결과 " + "*" * 20)
print(f"안녕하세요 {name}님! 현재 {age}세이시군요.")
print(f"입력하신 키는 {height}cm이고, 몸무게는 {weight}kg입니다.")
print(f"계산된 BMI 지수는 {my_bmi:.2f}입니다.") # 소수점 둘째자리까지
print(f"목표인 {goal_weight}kg까지는 딱 {diff:.1f}kg 남았습니다")
print("*" * 50)
print("열심히 운동하세요.")
# [2차 과제] 스마트 피트니스 & 식단 플래너 V2.0
# 업데이트 내용: BMI 판정 로직(조건문) 및 식단 저장(리스트)

print("=" * 50)
print("   ★ Smart Fit & Diet Coach V2.0 ★")
print("=" * 50)

# 1. 정보 입력 (1차 내용 유지)
name = input("이름: ")
age = int(input("나이: "))
height = float(input("키(cm): "))
weight = float(input("현재 체중(kg): "))
target = float(input("목표 체중(kg): "))

# 2. 계산 로직
height_m = height / 100
bmi = weight / (height_m ** 2)

# 3. [업데이트] BMI 등급 판정 (조건문 활용)
if bmi < 18.5:
    status = "저체중"
    advice = "영양가 있는 식단으로 충분한 섭취가 필요합니다."
elif 18.5 <= bmi < 23:
    status = "정상"
    advice = "아주 건강한 상태입니다! 현재를 유지하세요."
elif 23 <= bmi < 25:
    status = "과체중"
    advice = "규칙적인 운동과 식단 조절을 시작하면 좋습니다."
else:
    status = "비만"
    advice = "전문적인 식단 관리와 유산소 운동을 권장합니다."

# 4. [업데이트] 식단 기록 (리스트 활용)
print("\n" + "-" * 20 + " 식단 기록 " + "-" * 20)
food_list = []
# 2차 수준에서는 반복문 없이 3개 정도 직접 입력받는 것으로 구성
food_list.append(input("오늘 아침에 먹은 음식: "))
food_list.append(input("오늘 점심에 먹은 음식: "))
food_list.append(input("오늘 저녁에 먹은 음식: "))

# 5. 최종 분석 보고서 출력
print("\n" + "*" * 15 + f" {name}님의 건강 진단서 " + "*" * 15)
print(f"▶ BMI 지수: {bmi:.2f} ({status})")
print(f"▶ 전문가 조언: {advice}")
print(f"▶ 목표 체중까지: {weight - target:.1f}kg 남음")
print(f"▶ 오늘의 식단 리스트: {food_list}")

# 6. 논리 연산자를 활용한 응원 문구
if weight <= target:
    print("\n축하합니다! 이미 목표 체중에 도달하셨네요!")
else:
    print(f"\n목표인 {target}kg를 향해 조금만 더 힘내세요!")
print("*" * 45)

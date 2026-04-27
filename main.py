# 파일이름 :개인 맞춤형 피트니스 및 식단 플래너
# 작 성 자 :60261939 민상우
# 파이썬 1차 과제: 나만의 피트니스 플래너 만들기
# 작성자: [본인 이름]

# 1. 정보 입력 
name = input("이름: ")
age = int(input("나이: "))
height = float(input("키(cm): "))
weight = float(input("현재 체중(kg): "))
target = float(input("목표 체중(kg): "))

# 2. 계산 로직
height_m = height / 100
bmi = weight / (height_m ** 2)

# 3. BMI 등급 판정 (조건문 활용)
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

# 4. 식단 기록
print("\n" + "-" * 20 + " 식단 기록 " + "-" * 20)
food_list = []
food_list.append(input("오늘 아침에 먹은 음식: "))
food_list.append(input("오늘 점심에 먹은 음식: "))
food_list.append(input("오늘 저녁에 먹은 음식: "))

# 5. 최종 분석 보고서 출력
print("\n" + "*" * 15 + f" {name}님의 건강 진단서 " + "*" * 15)
print(f" BMI 지수: {bmi:.2f} ({status})")
print(f" 전문가 조언: {advice}")
print(f" 목표 체중까지: {weight - target:.1f}kg 남음")
print(f" 오늘의 식단 리스트: {food_list}")

# 6. 논리 연산자를 활용한 응원 문구
if weight <= target:
    print("\n축하합니다! 이미 목표 체중에 도달하셨네요!")
else:
    print(f"\n목표인 {target}kg를 향해 조금만 더 힘내세요!")
print("*" * 45)
# [2차 과제] 스마트 피트니스 및 식단 플래너 V2.0
# 작성자: [본인 이름]
# 업데이트 내용: BMI 판정 로직 추가 및 리스트를 활용한 식단 데이터 관리

print("=" * 50)
print("   ★ Smart Fit & Diet Coach V2.0 ★")
print("=" * 50)

# 1. 정보 입력 및 리스트 저장 
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
height = float(input("키(cm)를 입력하세요: "))
weight = float(input("현재 몸무게(kg)를 입력하세요: "))
target_weight = float(input("목표 몸무게(kg)를 입력하세요: "))
# 사용자 데이터를 하나의 리스트로 묶어서 관리
user_data = [name, age, height, weight, target_weight]
# 2. 계산 로직
height_m = height / 100
bmi = weight / (height_m ** 2)
# 3. BMI 기반 건강 등급 판정 
if bmi < 18.5:
    status = "저체중"
    advice = "충분한 영양 섭취와 근력 운동이 필요합니다."
elif 18.5 <= bmi < 23:
    status = "정상"
    advice = "지금처럼 꾸준한 운동과 식단을 유지해 주세요!"
elif 23 <= bmi < 25:
    status = "과체중"
    advice = "식단 조절과 유산소 운동을 병행하는 것을 추천합니다."
else:
    status = "비만"
    advice = "전문적인 관리와 식단 개선이 시급한 상태입니다."
# 4. 식단 리스트 추가 
print("\n" + "-" * 20 + " 식단 기록 시작 " + "-" * 20)
daily_meals = [] # 빈 식단 리스트 생성
daily_meals.append(input("오늘 아침 메뉴: "))
daily_meals.append(input("오늘 점심 메뉴: "))
daily_meals.append(input("오늘 저녁 메뉴: "))
# 5. 최종 분석 보고서 출력
print("\n" + "*" * 15 + f" {user_data[0]}님의 건강 분석표 " + "*" * 15)
print(f"▶ BMI 지수: {bmi:.2f} | 등급: {status}")
print(f"▶ 맞춤 조언: {advice}")

# 6. 논리 연산자를 활용한 특별 메시지
# 목표 체중과 가깝고 BMI가 정상일 때 '건강함' 칭호 부여
weight_diff = weight - target_weight

if weight_diff <= 2 and status == "정상":
    print("▶ 특별 칭호: [갓생 살기 성공! 전설의 유지어터]")
elif weight_diff > 0:
    print(f"▶ 목표까지 {weight_diff:.1f}kg 남았습니다. 조금만 더 힘내세요!")
else:
    print("▶ 이미 목표 체중에 달성하셨습니다. 대단해요!")

print(f"▶ 오늘 먹은 음식들: {daily_meals}")
print("*" * 50)

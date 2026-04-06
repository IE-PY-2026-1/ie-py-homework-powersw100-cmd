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

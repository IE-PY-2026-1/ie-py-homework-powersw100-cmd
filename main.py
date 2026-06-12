# 파일이름 :개인 맞춤형 피트니스 및 식단 플래너
# 작 성 자 :60261939 민상우
# 파이썬 1차 과제: 나만의 피트니스 플래너 만들기
# 작성자: [본인 이름]
# [2차 과제] 스마트 피트니스 및 식단 플래너 V2.0
# 작성자: [본인 이름]
# 업데이트 내용: BMI 판정 로직 추가 및 리스트를 활용한 식단 데이터 관리
# [3차 과제: V3.0] 무한 루프와 메뉴 시스템 
# 데이터 보존을 위해 while 루프 외부에 변수를 선언합니다.
# 파일이름 : 개인 맞춤형 피트니스 및 식단 플래너
# 작 성 자 : 60261939 민상우
# 과제 내용: 4차과제


user_data = []  
daily_meals = []      
is_registered = False



def cal_bmi_func(w, h):
   
    height_meter = h / 100
    bmi_val = w / (height_meter ** 2)
    return bmi_val

#1번 기능
def regist_info():
  
    global user_data, is_registered
    
    print("\n" + "-" * 15 + " 신체 정보 등록 및 수정 " + "-" * 15)
    name = input("이름을 입력하세요: ")
    age = int(input("나이를 입력하세요: "))
    height = float(input("키(cm)를 입력하세요: "))
    weight = float(input("현재 몸무게(kg)를 입력하세요: "))
    target_weight = float(input("목표 몸무게(kg)를 입력하세요: "))
    
   
    user_data = [name, age, height, weight, target_weight]
    is_registered = True
    print(f"\n[성공] {name}님의 신체 정보가 등록/수정되었습니다.")


#2번 기능
def check_health():
    if is_registered == False:
        print("\n[알림] 먼저 1번 메뉴에서 신체 정보를 등록해 주세요.")
        return # 함수 강제 종료해서 메뉴로 튕기기
        
    # [조건] 위에 만든 함수에 인자(몸무게, 키)를 전달해서 BMI 결과 받아옴
    bmi = cal_bmi_func(user_data[3], user_data[2])
    
    # 다중 조건문으로 등급 나누기
    if bmi < 18.5:
        status = "저체중"
        advice = "충분한 영양 섭취와 근력 운동이 필요합니다."
    elif bmi < 23:
        status = "정상"
        advice = "지금처럼 꾸준한 운동과 식단을 유지해 주세요!"
    elif bmi < 25:
        status = "과체중"
        advice = "식단 조절과 유산소 운동을 병행하는 것을 추천합니다."
    else:
        status = "비만"
        advice = "전문적인 관리와 식단 개선이 시급한 상태입니다."
        
    print("\n" + "*" * 15 + f" {user_data[0]}님의 건강 진단 " + "*" * 15)
    print(f"▶ BMI 지수: {bmi:.2f} | 등급: {status}")
    print(f"▶ 맞춤 조언: {advice}")
    print("*" * 45)    


# 3번 메뉴: 식단 추가 함수
def diet_add():
    print("\n" + "-" * 15 + " 식단 기록 (추가할 때마다 누적됩니다) " + "-" * 15)
    meal_name = input("기록할 음식 이름을 입력하세요: ")
    
    # [예외처리 1] 숫자가 아닌 글자 입력 시 오류 나서 꺼지는 거 방지
    try:
        kcal = int(input("해당 음식의 칼로리(kcal)를 입력하세요: "))
    except ValueError:
        print("[오류] 칼로리는 숫자만 넣어야 합니다! 0kcal로 임시 저장합니다.")
        kcal = 0
    
    # [조건] 이중 리스트 구조가 되도록 [음식, 칼로리] 묶어서 append 실행
    daily_meals.append([meal_name, kcal])
    print(f"[기록 완료] '{meal_name}({kcal}kcal)'이(가) 식단 리스트에 추가되었습니다.")


# 4번 메뉴: 종합 리포트 및 이중 리스트 출력 함수
def show_result():
    if is_registered == False:
        print("\n[알림] 등록된 신체 정보가 없습니다. 1번 메뉴를 먼저 이용해 주세요.")
        return
        
    bmi = cal_bmi_func(user_data[3], user_data[2])
    
    if bmi < 18.5: status = "저체중"
    elif bmi < 23: status = "정상"
    elif bmi < 25: status = "과체중"
    else: status = "비만"
        
    print("\n" + "*" * 15 + f" {user_data[0]}님의 통합 건강 보고서 " + "*" * 15)
    print(f"▶ 신체 정보: 키 {user_data[2]}cm | 현재 체중 {user_data[3]}kg | 목표 체중 {user_data[4]}kg")
    print(f"▶ 현재 BMI: {bmi:.2f} ({status})")
    
    # 누적 계산용 변수들 0으로 먼저 초기화
    sum_calories = 0
    bad_food_count = 0  # 300칼로리 넘는 음식 개수 셀 변수
    
    print("\n" + "-" * 10 + " 현재까지 누적된 식단 표 " + "-" * 10)
    print("  번호  |   음식명   |   칼로리   |   비고   ")
    print("-" * 46)
    
    # [조건] for문과 range()를 써서 이중 리스트 순회하고 인덱싱 활용하기
    for i in range(len(daily_meals)):
        name = daily_meals[i][0]   # 이중 리스트 인덱싱으로 음식명 추출
        calorie = daily_meals[i][1] # 이중 리스트 인덱싱으로 칼로리 추출
        
        # [조건] 반복문 내부에 if-elif-else 다중 조건문으로 데이터 필터링하기
        if calorie >= 300:
            comment = "고칼로리 ⚠️"
            bad_food_count += 1 # [조건] += 연산자로 개수 누적
        elif calorie >= 150:
            comment = "적정 칼로리"
        else:
            comment = "저칼로리 🌱"
            
        print(f"   {i+1}   |  {name}  |  {calorie} kcal  | {comment}")
        sum_calories += calorie # [조건] += 연산자로 총 칼로리 더하기
        
    print("-" * 46)
    print(f"▶ 오늘 섭취한 총 칼로리: {sum_calories} kcal")
    print(f"▶ 주의해야 할 고칼로리 음식은 총 {bad_food_count}개입니다.")
    print("*" * 53)


# 5번 메뉴 선택 시 텍스트 파일로 저장하는 함수
def file_save_func():
    # open이랑 with 구문 써서 메모장 파일(txt)로 저장하기
    with open("diet_records.txt", "w", encoding="utf-8") as file:
        file.write("=== 스마트 피트니스 데이터 백업 ===\n")
        if is_registered:
            file.write(f"이름: {user_data[0]} | 키: {user_data[2]}cm | 몸무게: {user_data[3]}kg\n")
        file.write("-" * 40 + "\n")
        file.write("[이중 리스트 식단 데이터 목록]\n")
        for m in daily_meals:
            file.write(f"- {m[0]} : {m[1]}kcal\n")
            
    print("[파일 저장 완] 'diet_records.txt' 파일에 데이터가 정상 저장되었습니다.")


# ==================================================
# [조건] while True 무한 루프 메인 시스템 시작
# ==================================================
while True:
    print("\n" + "=" * 50)
    print("      Smart Fit & Diet Coach V4.0  ")
    print("=" * 50)
    print(" 1. 사용자 신체 정보 등록 및 수정")
    print(" 2. BMI 지수 및 건강 등급 분석")
    print(" 3. 오늘의 식단 기록 추가 (누적)")
    print(" 4. 전체 건강 관리 기록 조회")
    print(" 5. 프로그램 종료 및 데이터 저장")
    print("=" * 50)
    
    # [예외처리 2] 메뉴 고를 때 영어 유나 특수문자 쳤을 때 안 꺼지게 막음
    try:
        user_choice = input("원하는 기능의 번호를 선택하세요: ")
        
        if user_choice == "1":
            regist_info() # 1번 함수 호출
            
        elif user_choice == "2":
            # [조건] 등록 안됐을 때 continue로 밑에 코드 스킵하고 다시 위로 올리기
            if is_registered == False:
                print("\n[알림] 신체 정보를 먼저 등록해야 분석할 수 있습니다!")
                continue # 루프 처음으로 리턴
            check_health()
            
        elif user_choice == "3":
            diet_add()
            
        elif user_choice == "4":
            show_result()
            
        elif user_choice == "5":
            file_save_func() 
            print("\n프로그램을 종료합니다. 오늘도 건강하고 스마트한 하루 되세요! 🐍")
           
            break
            
        else:
            print("\n[오류] 잘못 선택했습니다. 1~5 사이의 숫자를 입력해 주세요.")
            
    except Exception as error_msg:
        print(f"\n[오류 발생] 알 수 없는 에러가 발생했습니다: {error_msg}")


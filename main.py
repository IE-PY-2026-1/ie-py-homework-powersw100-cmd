# 파일이름 :개인 맞춤형 피트니스 및 식단 플래너
# 작 성 자 :60261939 민상우
# 파이썬 1차 과제: 나만의 피트니스 플래너 만들기
# 작성자: [본인 이름]
# [2차 과제] 스마트 피트니스 및 식단 플래너 V2.0
# 작성자: [본인 이름]
# 업데이트 내용: BMI 판정 로직 추가 및 리스트를 활용한 식단 데이터 관리
# [3차 과제: V3.0] 무한 루프와 메뉴 시스템 
# 데이터 보존을 위해 while 루프 외부에 변수를 선언합니다.
user_data = []      # [이름, 나이, 키, 몸무게, 목표체중]
daily_meals = []    # 누적 식단 기록 리스트
is_registered = False  # 신체 정보 등록 여부 확인용 플래그

while True:
    print("\n" + "=" * 50)
    print("      Smart Fit & Diet Coach  ")
    print("=" * 50)
    print(" 1. 사용자 신체 정보 등록 및 수정")
    print(" 2. BMI 지수 및 건강 등급 분석")
    print(" 3. 오늘의 식단 기록 추가 (누적)")
    print(" 4. 전체 건강 관리 기록 조회")
    print(" 5. 프로그램 종료")
    print("=" * 50)
    
    choice = input("원하는 기능의 번호를 선택하세요: ")
    
    if choice == "1":
        name = input("이름을 입력하세요: ")
        age = int(input("나이를 입력하세요: "))
        height = float(input("키(cm)를 입력하세요: "))
        weight = float(input("현재 몸무게(kg)를 입력하세요: "))
        target_weight = float(input("목표 몸무게(kg)를 입력하세요: "))
        
        # 사용자 데이터를 하나의 리스트로 묶어서 관리
        user_data = [name, age, height, weight, target_weight]
        is_registered = True
        print(f"\n[성공] {name}님의 신체 정보가 등록/수정되었습니다.")
        
    elif choice == "2":
        if not is_registered:
            print("\n[알림] 먼저 1번 메뉴에서 신체 정보를 등록해 주세요.")
            continue  # 아래 코드를 실행하지 않고 다시 메뉴 선택으로 이동
            
        height_m = user_data[2] / 100
        bmi = user_data[3] / (height_m ** 2)
        
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
            
        print("\n" + "*" * 15 + f" {user_data[0]}님의 건강 진단 " + "*" * 15)
        print(f"▶ BMI 지수: {bmi:.2f} | 등급: {status}")
        print(f"▶ 맞춤 조언: {advice}")
        print("*" * 45)    

    elif choice == "3":
        print("\n" + "-" * 15 + " 식단 기록 (추가할 때마다 누적됩니다) " + "-" * 15)
        meal_input = input("기록할 음식 이름을 입력하세요: ")
        daily_meals.append(meal_input)
        print(f"[기록 완료] '{meal_input}'이(가) 식단에 추가되었습니다.")
        
    elif choice == "4":
        if not is_registered:
            print("\n[알림] 등록된 신체 정보가 없습니다. 1번 메뉴를 먼저 이용해 주세요.")
            print(f"▶ 현재까지 기록된 식단: {daily_meals}")
            continue
            
        height_m = user_data[2] / 100
        bmi = user_data[3] / (height_m ** 2)
        
        # BMI 등급 다시 계산 
        if bmi < 18.5: status = "저체중"
        elif 18.5 <= bmi < 23: status = "정상"
        elif 23 <= bmi < 25: status = "과체중"
        else: status = "비만"
            
        print("\n" + "*" * 15 + f" {user_data[0]}님의 통합 건강 보고서 " + "*" * 15)
        print(f"▶ 신체 정보: 키 {user_data[2]}cm | 현재 체중 {user_data[3]}kg | 목표 체중 {user_data[4]}kg")
        print(f"▶ 현재 BMI: {bmi:.2f} ({status})")
        
        # 논리 연산자를 활용한 특별 메시지 
        weight_diff = user_data[3] - user_data[4]
        if weight_diff <= 2 and status == "정상":
            print("▶ 특별 칭호: [갓생 살기 성공! 전설의 유지어터]")
        elif weight_diff > 0:
            print(f"▶ 목표 체중까지 {weight_diff:.1f}kg 남았습니다. 조금만 더 힘내세요!")
        else:
            print("▶ 이미 목표 체중에 달성하셨습니다. 대단해요!")
            
        print(f"▶ 현재까지 누적된 식단: {daily_meals}")
        print("*" * 53)
        
    elif choice == "5":
        print("\n프로그램을 종료합니다. 오늘도 건강하고 스마트한 하루 되세요! 🐍")
        break  # while 무한 루프 탈출
        
    else:
        print("\n[오류] 잘못된 선택입니다. 1~5 사이의 숫자를 입력해 주세요.")

## Emotion Tree Talk 프로젝트 백엔드 Readme 전용 레포지토리🎄

### 이미지 클릭 시 웹 사이트로 이동합니다.
[![Emotion Tree Talk](https://github.com/user-attachments/assets/00650986-3e36-402c-aa90-21bdc285bf68)](https://emotree.yoyobar.xyz)

## 팀원 소개

<table>
  <tr>
    <th><strong>김민수</strong></th>
    <th><strong>이웅표</strong></th>
    <th><strong>박민아</strong></th>
    <th><strong>양의종</strong></th>
    <th><strong>최성락</strong></th>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/118cdd12-db99-40c4-b2f4-cf70cded4007" alt="김민수" width="150" height="150"></td>
    <td><img src="https://github.com/user-attachments/assets/7a850f92-4077-4073-987e-220d70dacc9a" alt="이웅표" width="150" height="150"></td>
    <td><img src="https://github.com/user-attachments/assets/5063b7ae-cce9-44de-a434-dda0a000964e" alt="박민아" width="150" height="150"></td>
    <td><img src="https://github.com/user-attachments/assets/0e5f674a-7eb7-4239-9d38-de28fe0f50ad" alt="양의종" width="150" height="150"></td>
    <td><img src="https://github.com/user-attachments/assets/b0c24d77-4673-4fdc-91bd-dcd302a5a466" alt="최성락" width="150" height="150"></td>
  </tr>
  <tr>
    <td><a href="https://github.com/yoyobar">@yoyobar</a></td>
    <td><a href="https://github.com/ungpyolee">@ungpyolee</a></td>
    <td><a href="https://github.com/devpma">@devpma</a></td>
    <td><a href="https://github.com/Scanf-s">@Scanf-s</a></td>
    <td><a href="https://github.com/ChoiSeongRak">@ChoiSeongRak</a></td>
  </tr>
  <tr>
    <td>Frontend 팀장</td>
    <td>Frontend</td>
    <td>Frontend</td>
    <td>Backend 팀장</td>
    <td>Backend</td>
  </tr>
</table>

## 주요 페이지

| 랜딩 페이지                                 | 
|--------------------------------------------|
| <img src="https://github.com/OZ-Coding-School/oz_03_main-003-FE/blob/main/docs/ReadMe_Landing.png?raw=true"/> | 
|서비스 소개와 로그인이 가능합니다              |

| 감정나무 숲 페이지                                 | 
|--------------------------------------------|
| <img src="https://github.com/OZ-Coding-School/oz_03_main-003-FE/blob/main/docs/ReadMe_Home.png?raw=true"/> | 
|나무를 심을 수 있으며, 나무 관리와 성장 정보를 확인합니다              |

|AI 대화분석 페이지                                  | 
|--------------------------------------------|
| <img src="https://github.com/OZ-Coding-School/oz_03_main-003-FE/blob/main/docs/ReadMe_Chat.png?raw=true"/> | 
|채팅방을 만들고 대화를 입력하면 AI가 대화를 요약하고 감정 키워드를 추출합니다  |

|내 정보 페이지                                   | 
|--------------------------------------------|
| <img src="https://github.com/OZ-Coding-School/oz_03_main-003-FE/blob/main/docs/ReadMe_Mypage.png?raw=true"/> | 
|유저의 정보를 볼 수 있으며, 프로필 이미지와 이름을 변경할 수 있습니다. |

## 페이지별 주요 기능

### 공통 기능
- 유저 Google 로그인 토큰으로 관리

### 감정나무 숲 페이지
- 3D CSS로 구현된 그리드에 나무 CRUD 기능.
- 감정 점수가 일정 수치에 도달하면 나무가 성장.
- 유저의 레벨이 오르면 나무를 심을 수 있는 바닥이 더 넓어진다.

### 채팅 페이지
- 채팅방 CRUD 기능.
- OpenAI(Gemini AI)를 사용한 대화 내용 감정 분석.
- 대화 내용 요약 및 감정 키워드 추출 기능.

### 내정보 페이지
- 유저의 이름 변경
- 획득한 감정수치가 일정 수치를 넘으면, 뱃지를 획득하여 프로필 이미지로 변경 가능


## 데모 영상

https://github.com/user-attachments/assets/e57bf6a3-1357-43bc-a980-861a1b1afc68

## 사용 기술

### Backend
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django Rest Framework](https://img.shields.io/badge/Django%20Rest%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Google Gemini 1.5 Flash](https://img.shields.io/badge/Google%20Gemini%201.5%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)

### Cloud Service
![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=amazon-ec2&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS%20S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)
![AWS RDS](https://img.shields.io/badge/AWS%20RDS-527FFF?style=for-the-badge&logo=amazon-rds&logoColor=white)
![AWS CloudFront](https://img.shields.io/badge/AWS%20CloudFront-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![AWS ELB](https://img.shields.io/badge/AWS%20ELB-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)

## Entity Relationship Diagram

![image](https://github.com/user-attachments/assets/5a5d766c-57b9-4427-8886-7192608c186c)

---

## Architecture

### 1. Cloud Architecture

![image](https://github.com/user-attachments/assets/d7152a57-4ccf-4b85-99ba-32a5436541a0)

### 2. Project Architecture

![image](https://github.com/user-attachments/assets/5adf7e75-2873-4d60-90e9-f7dd547cd7f5)

---

## Prompt Engineering

### 1. Select Google Gemini model:

	Google Gemini 1.0 pro, 1.5 flash 모델 중 현재 제공하려는 서비스와 더 알맞는 모델을 선택해야 했는데, 
	1.5 Flash 모델이 더 요청 가능한 횟수가 많으며, 응답 속도도 나쁘지 않기 때문에 1.5 Flash 모델을 선택함.
	
 	현재 제공되는 Gemini 1.5 Flash 모델은 Fine tuning 서비스가 제공되고 있지 않음. 따라서 System instruction을 최대한 자세하게 기술해야함. 
	
 	즉, Prompt engineering을 정밀하게 요구하여 원하는 답변 데이터를 얻을 수 있어야 함

### 2. 사용한 Prompt Engineering 기법

#### Few shot prompting

	가장 먼저 떠올린 것은 감정 분석 Example input, output을 제시하여 답변 제공 전 해당 Example을 통해
	따라서 풍부한 예시로 활용할 수 있는 인터넷, 일상 생활의 대화내용을 수집하여 약 30개 ~ 40개 정도 제공하였음.

#### Instruction-based(지시 기반) Prompting

	Gemini에게 특정 역할 및 작업을 수행하는 방법을 명확하게 지정함.

#### Role playing (캐릭터, 역할 지정)

	제공한 프롬프트에서, "당신은 고령의 대 마법사이며, 어쩌구 저쩌구..." 라고 지정하여 Gemini의 캐릭터를 지정하였으며,
	당신은 "심리 분석 전문가이며, 어떻게 분석해야하고, 어떻게 답변을 해야하고 어쩌구 저쩌구 ..." 라고 지정하여 
 	항상 일관적인 응답을 받을 수 있도록 지시하였음.
	
#### Explicit Constraint Setting (응답 형식 지정)

	AI가 분석한 결과를 API를 통해 Client로 전달해야 하기 때문에 Json 형식의 구조화된 데이터로만 응답을 받을 수 있도록 설정하였음

#### Contextual Understanding (대화 맥락을 이해하도록 요구)

	감정 분석 시, 한 단계씩 대화내용 감정 분석 수행 단계를 제시하였으며, 대화 한 줄, 대화 전체에 대한 내용을 이해하도록 지시하였음
	따라서 대화 한 줄 씩 이해한 내용과 대화 전체에 대한 내용을 각각 결과를 산출하여, 대화 전체 맥락을 기준으로 더 적절한 결과를 선택하도록 지시하였음

#### Error Handling and Incentive Mechanism (보상, 패널티)

	성공적으로 감정 분석을 수행하고, 고객(어플리케이션 사용자)을 만족시킨다면 $500, 엄청난 마법 도구를 제공한다는 보상을 준다고 약속하였음
	기대하는 감정 분석 내용과 다른 응답 결과를 제공하는 경우, 제공되는 보상을 차감하겠다는 패널티를 제공하였음

#### Handling Specific Linguistic Features (특정 표현에 대한 해석 지침)
	한국어로 대화시 축약어, 낱말로만 된 단어, 예시로 "ㅋㅋ", "ㄴㄴ", "ㅈㅅㅈㅅ"와 같은 낱말은 해석에 어려움을 겪을 수 있으므로 
 	다양한 예시를 추가하여 Gemini가 대화 내용 분석 시 도움을 주기 위해 지침을 제공하였음
	욕설의 경우 필터링하지 말고 대화의 강도, 억양의 강도, 감정의 정도로써 파악하라고 지시하였음

---

## 백엔드 기능 흐름

| 로그인 ~ 숲 생성 과정                       |
|--------------------------------------------|
| <img src="https://github.com/user-attachments/assets/bab96f26-a640-4a3e-bb41-6fb5df58f15d" width=600px height=500px/> |

| 트리 및 채팅방 생성 과정                      |
|--------------------------------------------|
| <img src="https://github.com/user-attachments/assets/6c32e720-fb98-4673-9e52-13239d8c6017" width=600px height=500px/> |

| Dialog 송수신 과정                      |
|--------------------------------------------|
| <img src="https://github.com/user-attachments/assets/fba1454e-dbe3-47b6-a3c0-5f15dc0d3f9f" width=600px height=500px/> |

---

## 트러블 슈팅

### [Frontend, Backend]
- **문제:** 초기 로그인 토큰 관리 이슈.
  - **해결:** 클라이언트 측에서 oAuth로 로그인 요청을 보내는게 기본적인 설계방식임을 확인, React OAuth 라이브러리 설치 후 클라이언트 단 처리 및 검증 커스텀 훅 사용.

- **문제:** 감정 분석 속도 저하.
  - **해결:** OpenAI API 호출 최적화 및 캐싱 전략 도입.
  - **해결:** 과도한 Prompt 지시 내용 최적화, Few-shot example 최적화

### [Frontend]
- **문제:** 음악 무한 재생 버그
  - **해결:** 기존 코드는 new Audio 객체를 컴포넌트 내에서 호출했으나, 코드를 변경하여 컴포넌트 바깥으로 객체를 빼둠, 컴포넌트 재렌더링이 발생할 때 마다 추가적인 객체 생성은 없을것으로 판단되어 해결

- **문제:** 채팅방 인풋의 크기로 인해 가독성 저하
  - **해결:** 채팅방 글자의 `length`를 계산하여 추가적인 스타일 변경, 기존에는 `overflow-scroll`이 없어서 버튼을 외부로 빼내고 스타일을 재조정
 
- **문제:** 유저 메세지에 엔터가 없을경우, 창을 초과하여 늘어나는 버그
  - **해결:** `overflow-x-hidden`을 주어 스타일적인 문제를 해결하고, `break-words`를 사용하여 화면을 초과하는 글자는 개행하도록 처리

### [Backend]
- **문제:** API 사용 시 발생한 에러, 논리적인 결점
  - **해결:** 현재 생각하고 있는 Flow의 논리적인 흐름을 다시 구성하고 해당 논리에 맞도록 API 수정

- **문제:** EC2 Free tier 용량 문제
  - **해결:** docker-compose로 백엔드 어플리케이션 빌드 시 생성되는 필요 없는 파일 제거로 용량 최적화
 
- **문제:** Prompting을 사용하여 과도한 무관심 수치 조정의 한계
  - **해결:** Gemini가 결과로 전달하는 감정 분석 수치에 내부 코드에서 특정 값을 연산하여 전달받는 무관심 수치 조정

---
 
## 프로젝트 후기

API 개발 시 테스트 주도 개발을 수행하려고 했으나, 아직 익숙하지 않은 개념이기도 하고 API 개발에만 너무 몰두하여 테스트 코드 개발에 소홀했던 것 같다.
추후 진행하는 프로젝트에서는 반드시 테스트 주도 개발 개념을 더 숙지하여 실제 API 배포 시 발생하게 되는 오류가 적어질 수 있도록 노력할 것이다.
또한, AI를 이번에 처음 프로젝트에 입히는 것이다 보니 자연스레 AI쪽에 관심을 갖게 되었다. 파이썬을 사용할 수 있다는 강점을 살려서 AI 분야를 공부하기로 결심하였다.
백엔드 역량과 AI 활용 역량을 모두 갖춘 인재가 되어 사회에서 바라보는 나의 가치가 올라갔으면 하는 바람이 있다.

 

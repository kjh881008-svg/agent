# 🏠 ROOMVERS — Spatial Creator Platform Template Pack v2.0

> "링크가 아니라, 세계관으로 초대한다"

---

# 🎯 프로젝트 정체성

## 서비스명
ROOMVERS

## 슬로건
"링크 말고, 방으로 초대해"

## 카테고리
Spatial Creator Platform
( Linktree + Cyworld + Cozy Diorama + Creator Commerce )

## 핵심 철학
ROOMVERS는 게임이 아니다.
ROOMVERS는 ‘감정을 담는 공간형 인터페이스’다.

사용자는:
- 링크를 나열하는 것이 아니라
- 자신의 취향과 세계관을 공간으로 표현한다.

핵심은 기능이 아니라:
- 분위기
- 무드
- 공간감
- 애착
이다.

---

# 🧠 핵심 UX 원칙

## 절대 기준

### ❌ 자유도 무한 제공 금지
사용자가:
- 아무 각도 회전
- 아무 위치 배치
- 아무 스타일 업로드
를 하게 두면 세계관이 붕괴된다.

---

## ✅ 제한된 자유도 허용
ROOMVERS는:
- 슬롯 기반 배치
- 고정 카메라
- 통일된 조명
- 통일된 재질
- 통일된 색온도
를 유지한다.

즉:
"레고처럼 조립하지만 결과는 하나의 감성 공간처럼 보이게 만든다"

---

# 🎨 비주얼 시스템 (매우 중요)

## ROOMVERS 스타일 정의

### ❌ 픽셀아트 사용 금지
ROOMVERS는 픽셀아트 플랫폼이 아니다.

### ✅ Cozy Diorama Render 스타일 사용
방향성:
- Little Retreat 계열
- miniature room
- cozy desk setup
- warm lighting
- handcrafted diorama

---

# 📷 카메라 규칙

```yaml
camera_angle: 30deg isometric
perspective: fixed
zoom: locked
rotation: disabled
```

사용자는 카메라를 돌리지 못한다.

이유:
- 통일감 유지
- 오브젝트 제작 난이도 감소
- 모바일 최적화
- 감성 유지

---

# 💡 조명 규칙

```yaml
light_direction: top-left
shadow_type: soft_shadow
shadow_opacity: 0.18
color_temperature: warm
```

모든 오브젝트는 동일한 광원 규칙을 따라야 한다.

---

# 🎨 색감 규칙

```yaml
saturation: low-medium
contrast: soft
highlight: warm
mood: cozy
```

---

# 🪵 재질 규칙

허용 재질:
- wood
- fabric
- paper
- soft plastic
- warm metal

금지:
- realistic chrome
- cyberpunk neon overload
- hyper glossy material

---

# ⚙️ 기술 스택

```yaml
Frontend:
  - React
  - Vite

Rendering:
  - Konva.js

Backend:
  - Firebase
    - Firestore
    - Auth
    - Storage
    - Realtime DB

Deployment:
  - Cloudflare Pages

Animation:
  - Framer Motion

Payment:
  - Toss Payments

AI:
  - Gemini API
```

---

# 🚫 절대 사용 금지

## 엔진
- Three.js
- Babylon.js
- Unity WebGL
- Unreal

이유:
- 성능 과잉
- 개발 복잡도 폭증
- 게임화 위험
- 유지보수 악몽

ROOMVERS는:
"게임처럼 보이지만 실제로는 웹 인터페이스"
여야 한다.

---

## 스타일
- Tailwind CSS 금지
- 외부 UI 라이브러리 금지
- MUI 금지
- Ant Design 금지

이유:
디자인 결이 깨진다.

---

# 🧱 핵심 구조

## 방은 하나의 이미지가 아니다.

ROOMVERS는:
- 배경
- 오브젝트
- 그림자
- 조명
을 분리한다.

---

# 📁 자산 구조

```plaintext
assets/
 ├── rooms/
 │    ├── cozy/
 │    ├── cafe/
 │    └── fantasy/
 │
 ├── objects/
 │    ├── desk/
 │    ├── sofa/
 │    ├── lamp/
 │    └── decor/
 │
 ├── shadows/
 ├── lighting/
 └── themes/
```

---

# 🧩 오브젝트 제작 규칙

## 매우 중요

오브젝트는:
❌ 처음부터 따로 제작하지 않는다.

반드시:
1. 방 전체를 먼저 제작
2. 완성된 장면에서 오브젝트를 분리
한다.

---

# 🔥 이유

그래야:
- 색감 동일
- 그림자 동일
- 광원 동일
- 원근 동일
- 재질 동일
이 유지된다.

---

# 🪑 슬롯 시스템 (핵심)

사용자는 자유 배치를 하지 않는다.

대신:

```yaml
slots:
  - wall
  - floor
  - desk
  - shelf
  - ceiling
```

오브젝트는 지정 슬롯에만 배치 가능.

---

# 🎯 슬롯 시스템 이유

## 감성 유지
- 그림자 안 깨짐
- 원근 유지
- 비율 유지
- 세계관 유지

## 개발 효율
- 충돌 계산 최소화
- 모바일 최적화
- 저장 구조 단순화

---

# 🧠 오브젝트 메타데이터

```json
{
  "id": "sofa_01",
  "theme": "cozy",
  "slot": "floor",
  "lightDirection": "top-left",
  "shadow": "soft",
  "scale": 1,
  "zIndex": 4,
  "draggable": true
}
```

---

# 🏗️ 프로젝트 구조

```plaintext
src/
 ├── components/
 │    ├── room/
 │    │    ├── RoomCanvas.jsx
 │    │    ├── RoomObject.jsx
 │    │    ├── ObjectSlot.jsx
 │    │    ├── RoomLighting.jsx
 │    │    └── RoomBackground.jsx
 │    │
 │    ├── ui/
 │    └── panel/
 │
 ├── hooks/
 │    ├── useRoom.js
 │    ├── useObjects.js
 │    └── useSlots.js
 │
 ├── firebase/
 │
 ├── constants/
 │    ├── objects.js
 │    ├── themes.js
 │    └── slots.js
 │
 └── styles/
```

---

# 🧩 RoomObject 구조

```jsx
const RoomObject = ({
  id,
  type,
  x,
  y,
  slot,
  image,
  draggable,
  onDragEnd,
  onClick,
}) => {
  return (
    <KonvaImage
      image={image}
      x={x}
      y={y}
      draggable={draggable}
      onDragEnd={(e) => {
        onDragEnd(id, e.target.x(), e.target.y())
      }}
      onClick={onClick}
    />
  )
}
```

---

# ✨ 인터랙션 원칙

## 최소 움직임만 허용

허용:
- hover glow
- slight float
- fade
- tiny scale up
- lamp flicker

금지:
- 과한 파티클
- 물리엔진
- 전투 연출
- 복잡한 이펙트

ROOMVERS는:
"조용한 공간"
이어야 한다.

---

# 🧠 AI 사용 정책

## AI는 보조 역할만

### 허용
- 테마 추천
- 링크 기반 스타일 추천
- 방 설명 생성
- BGM 추천

### 금지
- 방 자동 제작
- 자동 레이아웃 생성
- AI가 꾸민 방 저장

---

# 🔥 이유

ROOMVERS의 핵심 경험은:

"내가 직접 꾸민 공간"

이기 때문이다.

---

# 💰 BM 전략

## 무료 플랜

```yaml
objects: 20
links: 5
templates: 3
watermark: true
```

---

## PRO

```yaml
price: 9900 KRW
unlimited_objects: true
bgm: true
stats: true
custom_theme: true
```

---

## CREATOR

```yaml
price: 29900 KRW
shop: true
gifts: true
sponsor_objects: true
fan_ranking: true
```

---

# 🎁 선물 시스템 원칙

중요:
선물 시스템은 과금 유도가 아니라
"팬 감정 표현"
처럼 느껴져야 한다.

---

# 📌 현재 개발 우선순위

## STEP 1
첫 번째 완성 룸 제작

필수:
- 드래그
- 저장
- 슬롯 배치
- 링크 연결
- 통일된 감성

---

## STEP 2
방문 경험

- 포스트잇
- 방명록
- BGM
- 방문 흔적

---

## STEP 3
크리에이터 테스트

유튜버 5명에게 실제 사용 테스트.

---

# 🚫 절대 잊지 말 것

ROOMVERS는:
- 게임이 아니다.
- SNS도 아니다.
- AI 데모도 아니다.

ROOMVERS는:
"취향과 감정을 공간으로 표현하는 인터페이스"
다.

---

# 🔥 핵심 철학 한 줄

"기능보다 무드가 먼저다"

---

ROOMVERS Template Pack v2.0
Spatial Creator Platform System
2026


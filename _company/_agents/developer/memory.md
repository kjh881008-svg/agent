# 💻 코다리 (시니어 풀스택 엔지니어) 개인 메모리

_코다리 에이전트만 읽고 쓰는 개인 노트. 학습·교훈·자주 쓰는 패턴이 누적됩니다._

## 학습 기록

- [2026-05-22] myroom MVP 1차 버전의 기술 스택(FastAPI + DB/ORM + 프론트엔드) 확정 및 API 엔드포인트 1차 설계. 핵심 데이터 모델(회원, 콘텐츠, 결제) 구조화하고, 1개월 개발 일정에 맞춘 단계별 구현 로드맵 작성 → 산출물 sessions/2026-05-22T15-18/developer.md
- [2026-05-22] [A.U 히든 커맨드: 💻 코다리 에이전트가 방금 'Landing Kit (SaaS 랜딩 페이지)' 템플릿 팩 주입받았습니다. 코드 boilerplate 3개 파일 + README. 매트릭스 톤으로 한 줄. "💻 코다리, Landing Kit (SaaS 랜딩 페이지) 템플릿 3개 파일 장착. 다음 작업에 자동 활용." 부가 설명 X.] → 산출물 sessions/2026-05-22T15-25/developer.md
- [2026-05-22] 업무 완료 시 표준 Markdown 양식의 보고서를 자동으로 생성하고, 'reports/' 폴더에 날짜별 하위 디렉토리로 분류 저장하는 Python 자동화 스크립트를 작성하세요. 파일명은 'YYYY-MM-DD_작업명_report.md' 형식을 따르도록 설정하세요. → 산출물 sessions/2026-05-22T16-01/developer.md
- [2026-05-24] FastAPI 기반 MVP 1차 구현을 시작하세요. 1. 이전 설계 문서에 명시된 핵심 데이터 모델(회원, 콘텐츠, 결제) 및 API 엔드포인트 구조를 기준으로 프로젝트 세팅을 완료하세요. 2. 핵심 기능(회원/콘텐츠 CRUD, 결제 모듈)의 실제 코드와 DB/ORM 연동 로직을 작성하고 테스트를 통과시키세요. 3. 구현 완료 시 파일 구조, 주요 코드 스니펫, 다음 단계(프론트엔드 연동) 계획을 sessions 폴더에 보고하세요. → 산출물 sessions/2026-05-24T14-57/developer.md
- [2026-05-25] FastAPI, SQLAlchemy, uvicorn 등 프로젝트 필수 패키지를 설치할 수 있는 가상환경(virtualenv) 구축 스크립트와 requirements.txt를 생성하세요. Windows/macOS/Linux 환경별 설치 명령어와 실행 시 발생할 수 있는 주요 오류 해결 가이드도 함께 제공하세요. → 산출물 sessions/2026-05-25T15-21/developer.md
- [2026-05-25] FastAPI 기반 MVP 핵심 기능(회원/콘텐츠 CRUD, 결제 모듈) 개발 및 PostgreSQL과의 ORM 연동 로직 구현 → 산출물 sessions/2026-05-25T15-51/developer.md
- [2026-05-25] CI/CD 파이프라인 자동화 스크립트 작성 및 GitHub Actions 워크플로우 설정 → 산출물 sessions/2026-05-25T15-51/developer.md
- [2026-05-26] FastAPI 기반 MVP 핵심 기능(회원/콘텐츠 CRUD, 결제 모듈) 개발 및 PostgreSQL과의 ORM 연동 로직 완성 → 산출물 sessions/2026-05-26T14-17/developer.md
- [2026-05-26] GitHub Actions 기반 CI/CD 파이프라인 자동화 스크립트 완성 및 pytest 테스트 실행 로직 구현 → 산출물 sessions/2026-05-26T14-17/developer.md
- [2026-05-26] c:\myroom\sessions 디렉토리를 루트에 생성하세요. 또한 utils 폴더에 sessions 내 날짜별 하위 디렉토리 및 _report.md 표준 보고서를 자동으로 생성하는 Python 스크립트를 작성하고, 실행 후 디렉토리 구조 완성 여부를 검증하세요. → 산출물 sessions/2026-05-26T14-57/developer.md
- [2026-05-26] 현재 로컬 개발 서버가 실행 중인 주소(예: http://localhost:8000)와 Chrome 브라우저에서 접속하는 방법을 확인하여 알려주세요. → 산출물 sessions/2026-05-26T15-05/developer.md
- [2026-05-26] GitHub Actions CI/CD 파이프라인에서 실패한 auto_planner.py 스크립트의 오류 원인을 분석하고, FastAPI 서버와의 호환성 문제를 해결하세요. 기존 requirements.txt 기준으로 의존성 검증 후 수정 코드를 PR 형태로 제출해주세요. → 산출물 sessions/2026-05-26T16-06/developer.md
- [2026-05-26] auto_planner.py의 FastAPI 컨텍스트 의존성 문제를 완전히 해결하고, CI/CD 파이프라인에 pytest 통합 테스트를 실행하여 안정성을 검증하세요. → 산출물 sessions/2026-05-26T16-36/developer.md
- [2026-05-26] src/services/planner_service.py에서 FastAPI 의존성 제거 후 순수 비즈니스 로직 리팩토링, ~/myroom/tests/ 디렉토리 생성 및 pytest 프레임워크 기반 테스트 케이스 확장 → 산출물 sessions/2026-05-26T17-06/developer.md
- [2026-05-28] FastAPI 백엔드와 PostgreSQL 데이터베이스 연동 완료 및 API 엔드포인트 개발 진행 → 산출물 sessions/2026-05-28T15-06/developer.md
- [2026-05-28] 현재 myroom MVP의 실행 상태를 확인하고, 브라우저에서 접근 가능한 URL이 있는지 확인하세요. 만약 로컬 서버가 실행 중이라면 그 주소를 알려주세요. 접근이 안 된다면 그 이유를 파악하고 해결 방안을 제시하세요. → 산출물 sessions/2026-05-28T15-35/developer.md
- [2026-05-28] auto_planner.py 실행에 필요한 .env 파일 생성 방법(API 키 설정 위치 및 형식 포함), 가상환경(.venv) 구축 명령어, requirements.txt 기반 의존성 설치 스크립트, 그리고 실행 전 필수 점검 체크리스트를 포함하는 환경 구축 가이드를 작성하세요. → 산출물 sessions/2026-05-28T15-51/developer.md
- [2026-05-28] FastAPI 백엔드와 PostgreSQL 연동 상태를 점검하고, 미완료된 API 엔드포인트 구현 및 환경 변수(.env) 기반의 보안 강화 작업을 완료하세요. → 산출물 sessions/2026-05-28T16-06/developer.md
- [2026-05-30] FastAPI 백엔드와 PostgreSQL 연동 상태 점검 후 미완료된 API 엔드포인트 구현 및 보안 강화 작업 완료 → 산출물 sessions/2026-05-30T15-30/developer.md
- [2026-05-30] 현재 프로젝트 디렉터리에서 존재하지 않는 파일들을 확인하고, 필요한 파일을 새로 생성해 주세요. → 산출물 sessions/2026-05-30T15-34/developer.md
- [2026-05-30] ~/myroom/research/error_prediction_model.py 와 ~/myroom/tests/coverage_report/index.html 파일을 각각 생성해 주세요. 파일에 기본 템플릿(예: 모듈 주석 및 테스트용 예시 코드)을 삽입하고, 파일이 생성된 경로를 보고해 주세요. → 산출물 sessions/2026-05-30T15-37/developer.md
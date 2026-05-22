import datetime
import os
from pathlib import Path
from typing import Optional

def generate_report(job_name: str, content: str) -> Path:
    """
    업무 완료 보고서를 표준 Markdown 형식으로 생성하고 지정된 경로에 저장합니다.

    Args:
        job_name (str): 작업의 핵심 내용 (파일명에 사용됨).
        content (str): 보고서 본문 내용.

    Returns:
        pathlib.Path: 생성된 보고서 파일의 절대 경로.
    """
    try:
        # 1. 날짜 및 경로 설정 (YYYY-MM-DD)
        today = datetime.date.today()
        date_str = today.strftime("%Y-%m-%d")
        
        # 보고서가 저장될 최상위 폴더 (reports)
        reports_root = Path("reports")
        
        # 날짜별 하위 폴더 생성 (reports/YYYY-MM-DD)
        daily_dir = reports_root / date_str
        daily_dir.mkdir(parents=True, exist_ok=True)

        # 2. 파일명 포맷팅 (YYYY-MM-DD_작업명_report.md)
        # job_name에 포함될 수 있는 특수문자를 제거하여 안전한 파일명 생성
        safe_job_name = "".join(c for c in job_name if c.isalnum() or c in (' ', '_')).strip()
        filename = f"{date_str}_{safe_job_name}_report.md"
        
        # 최종 파일 경로
        output_path = daily_dir / filename

        # 3. Markdown 보고서 본문 작성
        markdown_content = f"""# 📝 {job_name} 작업 보고서

**작성일:** {today.strftime('%Y년 %m월 %d일')}

---

## 📋 개요 (Summary)
본 보고서는 {job_name} 작업 완료 시점의 산출물 및 주요 진행 내용을 기록합니다.

## 💡 주요 진행 내용 (Details)
{content}

## ✅ 다음 액션 아이템 (Next Steps)
추가 검증이 필요한 부분이나 다음 개발 단계에 대한 계획을 기록합니다.

---
*이 보고서는 자동 생성된 산출물입니다.*
"""

        # 4. 파일 쓰기 및 반환
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
            
        print(f"✅ 보고서가 성공적으로 저장되었습니다: {output_path.resolve()}")
        return output_path

    except Exception as e:
        print(f"❌ 보고서 생성 중 오류 발생: {e}")
        return None

# --- 테스트 코드 ---
if __name__ == '__main__':
    # 테스트 1: 성공 케이스
    test_job_name = "MVP_API_설계"
    test_content = "FastAPI 기반의 회원 인증 API 엔드포인트(POST /auth/login)를 성공적으로 설계했습니다. DB 스키마는 User(id, email, password_hash)를 따릅니다."
    print("--- [테스트 실행: 성공 케이스] ---")
    generate_report(test_job_name, test_content)
    
    # 테스트 2: 다른 작업명으로 다시 실행 (날짜는 동일)
    test_job_name_2 = "Landing_Kit_구현"
    test_content_2 = "Landing Kit의 6개 섹션 구조를 Next.js와 Tailwind CSS를 이용해 구현했습니다. 반응형 디자인 테스트 완료."
    print("\n--- [테스트 실행: 다른 작업명] ---")
    generate_report(test_job_name_2, test_content_2)
    
    # Note: 실제 실행 시에는 이 테스트 코드를 제거하고 함수만 사용해야 합니다.
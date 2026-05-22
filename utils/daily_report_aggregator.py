import os
import sys
import json
import datetime
import urllib.request
import urllib.parse
from pathlib import Path

REPORTS_ROOT = Path("reports")
CONFIG_PATH = Path("utils/telegram_config.json")

def scan_today_reports():
    today = datetime.date.today()
    daily_dir = REPORTS_ROOT / today.strftime("%Y-%m-%d")
    if not daily_dir.exists():
        return []
    return sorted([f.name for f in daily_dir.iterdir() if f.is_file() and f.suffix == '.md'])

def build_summary(reports):
    today = datetime.date.today().strftime("%Y-%m-%d")
    lines = [f"## 📅 데일리 보고서 요약 ({today})\n"]
    if not reports:
        lines.append("- 미수집된 보고서")
    else:
        lines.append(f"- 총 {len(reports)}건 수집")
        lines.extend([f"  - 📄 `{r}`" for r in reports])
    lines.append(f"\n📂 저장 경로: `{REPORTS_ROOT / today}`")
    return "\n".join(lines)

def save_summary(text):
    today = datetime.date.today()
    daily_dir = REPORTS_ROOT / today.strftime("%Y-%m-%d")
    daily_dir.mkdir(parents=True, exist_ok=True)
    path = daily_dir / "daily_summary.md"
    path.write_text(text, encoding="utf-8")
    return path

def send_telegram(summary_text):
    if not CONFIG_PATH.exists():
        return "⚠️ TELEGRAM 미연결 (설정 필요)"
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    token, chat_id = cfg.get("token"), cfg.get("chat_id")
    if not token or not chat_id:
        return "⚠️ TELEGRAM 토큰/ID 누락"
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": summary_text, "parse_mode": "Markdown"}
    data = urllib.parse.urlencode(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return "✅ TELEGRAM 발송 완료"
    except Exception as e:
        return f"❌ TELEGRAM 전송 실패: {e}"

def run():
    reports = scan_today_reports()
    summary = build_summary(reports)
    save_path = save_summary(summary)
    tg_status = send_telegram(summary)
    
    print(f"📊 요약 저장: {save_path}")
    print(f"📱 텔레그램: {tg_status}")
    return save_path, tg_status

if __name__ == "__main__":
    run()
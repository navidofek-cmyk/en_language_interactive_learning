"""
STREAK TRACKER — Daily learning streak
========================================
Sleduje denní streak cvičení angličtiny.

Použití:
  python3 streak.py            # zaznamenat dnešní cvičení
  python3 streak.py --status   # zobrazit aktuální streak bez záznamu
  python3 streak.py --history  # zobrazit kompletní historii
"""
import pathlib, json, datetime, argparse, calendar

STREAK_FILE = pathlib.Path("streak.json")

MOTIVATIONAL = {
    0:  "Get started — every expert was once a beginner. 💪",
    1:  "Day 1 — the journey of a thousand miles begins with a single step! 🚀",
    3:  "3 days! You're building a habit. Keep going! ✨",
    7:  "One full week! You're more consistent than 80% of learners. 🔥",
    14: "Two weeks strong! Your brain is rewiring for English. 🧠",
    21: "21 days — they say that's how long it takes to form a habit. Well done! 🎯",
    30: "30-day streak! You're officially consistent. 🏆",
    50: "50 days! You're in the top tier of language learners. 🥇",
    100:"100 DAYS! That's extraordinary dedication. 🌟",
    365:"ONE FULL YEAR! You are unstoppable. 🎊",
}

def load_streak():
    if STREAK_FILE.exists():
        return json.loads(STREAK_FILE.read_text(encoding="utf-8"))
    return {"days": [], "longest": 0}

def save_streak(data):
    STREAK_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def current_streak(days):
    if not days:
        return 0
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    last = datetime.date.fromisoformat(days[-1])
    if last < yesterday:
        return 0
    streak = 1
    for i in range(len(days) - 2, -1, -1):
        d = datetime.date.fromisoformat(days[i])
        d_next = datetime.date.fromisoformat(days[i + 1])
        if (d_next - d).days == 1:
            streak += 1
        else:
            break
    return streak

def log_today():
    data = load_streak()
    today = datetime.date.today().isoformat()
    if today in data["days"]:
        return data, False  # already logged today
    data["days"].append(today)
    data["days"].sort()
    streak = current_streak(data["days"])
    data["longest"] = max(data.get("longest", 0), streak)
    save_streak(data)
    return data, True

def draw_calendar(data):
    today = datetime.date.today()
    year, month = today.year, today.month
    day_set = set(data.get("days", []))

    print(f"\n  📅 {calendar.month_name[month]} {year}")
    print("  Mo Tu We Th Fr Sa Su")
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        row = ""
        for day in week:
            if day == 0:
                row += "   "
            else:
                iso = f"{year}-{month:02d}-{day:02d}"
                if iso in day_set:
                    row += f" ✓ " if day < 10 else f"✓  "
                elif iso == today.isoformat():
                    row += f"[{day}]" if day >= 10 else f"[{day}]"
                else:
                    row += f"{day:2d} "
        print(f"  {row}")

def show_history(data):
    days = data.get("days", [])
    if not days:
        print("\n  No history yet.")
        return
    print(f"\n  Total days practised: {len(days)}")
    print(f"  First day:            {days[0]}")
    print(f"  Last day:             {days[-1]}")
    print(f"  Longest streak:       {data.get('longest', 0)} days")

    # show last 30 days
    today = datetime.date.today()
    day_set = set(days)
    print("\n  Last 30 days (✓ = practised, · = missed):")
    row = "  "
    for i in range(29, -1, -1):
        d = (today - datetime.timedelta(days=i)).isoformat()
        row += "✓" if d in day_set else "·"
    print(row)

def main():
    parser = argparse.ArgumentParser(description="English learning streak tracker")
    parser.add_argument("--status",  action="store_true", help="Show streak without logging")
    parser.add_argument("--history", action="store_true", help="Show full history")
    args = parser.parse_args()

    print("=" * 55)
    print("  🔥 ENGLISH LEARNING STREAK")
    print("=" * 55)

    if args.history:
        data = load_streak()
        show_history(data)
        draw_calendar(data)
        return

    if args.status:
        data = load_streak()
    else:
        data, is_new = log_today()
        if is_new:
            print(f"\n  ✓ Today's practice logged!")
        else:
            print(f"\n  ✓ Already logged today.")

    streak = current_streak(data["days"])
    longest = data.get("longest", 0)
    total   = len(data["days"])

    print(f"\n  Current streak:  {streak} day{'s' if streak != 1 else ''} 🔥")
    print(f"  Longest streak:  {longest} days")
    print(f"  Total days:      {total}")

    # motivational message
    milestones = sorted([k for k in MOTIVATIONAL if k <= streak], reverse=True)
    if milestones:
        print(f"\n  {MOTIVATIONAL[milestones[0]]}")

    next_milestone = min([k for k in MOTIVATIONAL if k > streak], default=None)
    if next_milestone:
        remaining = next_milestone - streak
        print(f"  Next milestone: {next_milestone} days ({remaining} to go)")

    draw_calendar(data)

if __name__ == "__main__":
    main()

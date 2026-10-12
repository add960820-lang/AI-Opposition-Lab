# -*- coding: utf-8 -*-
"""
AI 反方實驗室 v0.2
免費本機原型，不需要 API、不需要額外安裝套件

功能：
1. 點子風險分析
2. 平行世界模擬
3. 使用者反駁與重新評估
4. 點子 DNA 版本紀錄
5. 自動儲存資料到 JSON 檔案
"""

import json
import os
from datetime import datetime


# =========================
# 基本設定
# =========================

DATA_FILE = "idea_lab_data.json"


def show_line():
    print("\n" + "=" * 55)


def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_data():
    """讀取之前保存的資料。"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("提醒：舊紀錄讀取失敗，將建立新的紀錄。")

    return {"projects": []}


def save_data(data):
    """將資料保存到本機。"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("\n[系統] 紀錄已保存。")
    except OSError as error:
        print(f"\n[系統] 儲存失敗：{error}")


def pause():
    input("\n按 Enter 返回主選單...")


# =========================
# 點子分析
# =========================

def analyze_idea(idea):
    """依照點子中的關鍵詞，產生規則式風險分析。"""

    risks = [
        {
            "name": "需求風險",
            "question": "真的有人需要這個產品嗎？",
            "test": "找 5 位目標使用者，了解他們目前如何解決這個問題。",
            "keywords": ["學生", "使用者", "生活", "拍照", "學習", "老人"]
        },
        {
            "name": "技術風險",
            "question": "目前的技術能不能穩定完成核心功能？",
            "test": "先製作一個只有一項核心功能的簡單原型。",
            "keywords": ["AI", "人工智慧", "辨識", "自動", "分析", "推薦",
                         "機器人", "程式", "影像", "語音"]
        },
        {
            "name": "競爭風險",
            "question": "如果別人也做出相同功能，你的優勢是什麼？",
            "test": "列出 3 個替代方案，確認自己的產品有哪些不同。",
            "keywords": ["APP", "app", "軟體", "平台", "網站", "工具",
                         "服務", "系統"]
        },
        {
            "name": "執行風險",
            "question": "你的時間、技術和資源是否足夠？",
            "test": "列出必要功能，先完成最重要的一項。",
            "keywords": ["硬體", "裝置", "設備", "感測器", "開發",
                         "製作", "系統", "產品"]
        },
        {
            "name": "差異化風險",
            "question": "這個創意是否只是把現有功能重新組合？",
            "test": "說明這個產品解決了什麼現有工具難以解決的問題。",
            "keywords": ["創意", "創作", "設計", "作品", "生成",
                         "圖片", "音樂", "影片"]
        }
    ]

    print("\n【第一階段：反方風險分析】")
    print(f"你的點子：{idea}")

    matched = []

    for risk in risks:
        if any(word.lower() in idea.lower()
               for word in risk["keywords"]):
            matched.append(risk)

    # 如果沒有命中關鍵詞，仍然提供基本風險
    if not matched:
        matched = [risks[0], risks[2], risks[3]]

    for index, risk in enumerate(matched, start=1):
        print(f"\n風險 {index}：{risk['name']}")
        print(f"反方質疑：{risk['question']}")
        print(f"驗證方法：{risk['test']}")

    print("\n注意：以上是依關鍵詞產生的初步檢查，")
    print("不是根據市場調查或真正的 AI 推理所得。")

    return matched


# =========================
# 平行世界模擬
# =========================

def simulate_worlds():
    print("\n【第二階段：平行世界模擬】")

    worlds = [
        {
            "name": "世界 A：沒人願意使用",
            "story": "大家都說你的點子很好，卻沒有人真的使用。",
            "question": "你會怎麼確認問題出在哪裡？"
        },
        {
            "name": "世界 B：競爭者出現",
            "story": "另一家公司推出類似產品，而且免費。",
            "question": "你會用什麼方式讓自己的產品仍有價值？"
        },
        {
            "name": "世界 C：資源不足",
            "story": "開發時間突然只剩三天，只能保留一項功能。",
            "question": "你會保留哪一項核心功能？為什麼？"
        }
    ]

    answers = []

    for world in worlds:
        show_line()
        print(world["name"])
        print(world["story"])
        print(world["question"])

        answer = input("\n你的應對方式：").strip()

        if not answer:
            answer = "尚未提出應對方式"

        answers.append({
            "world": world["name"],
            "answer": answer
        })

        print(f"\n已記錄你的策略：{answer}")

    return answers


# =========================
# 反方攻防
# =========================

def challenge_round():
    print("\n【第三階段：反方接受審判】")
    print("你可以反駁前面的風險分析。")
    print("請盡量提供具體理由，而不只是說 AI 錯了。")

    objection = input("\n你要反駁哪個觀點？").strip()
    evidence = input("你的理由、證據或實際例子是什麼？").strip()

    if not objection or not evidence:
        print("\n資料不足，這次攻防尚未完成。")
        return {
            "objection": objection,
            "evidence": evidence,
            "result": "資料不足，尚未完成評估"
        }

    # 本機規則式檢查，不代表真的驗證證據
    evidence_words = [
        "例如", "因為", "測試", "數據", "資料", "調查",
        "使用者", "實際", "證明", "曾經", "結果", "紀錄",
        "人數", "比例", "觀察", "實驗"
    ]

    found = [word for word in evidence_words if word in evidence]

    print("\n【重新評估】")
    print(f"你的反駁：{objection}")
    print(f"你的理由：{evidence}")

    if found:
        print("\n初步結果：你的回答包含可進一步檢查的線索。")
        print("下一步：確認這些資料是否真的支持你的主張。")
        result = "有待查證的線索：" + "、".join(found)
    else:
        print("\n初步結果：目前主要是文字說明，還缺少可檢查的證據。")
        print("下一步：嘗試提出實際案例、測試結果或使用者回饋。")
        result = "目前缺少明確的可檢查證據"

    print("\n提醒：這套規則只能檢查部分文字線索，")
    print("不能判斷你的理由是否為真，也不會自動證明任何一方正確。")

    return {
        "objection": objection,
        "evidence": evidence,
        "result": result
    }


# =========================
# 點子 DNA
# =========================

def create_project(data):
    print("\n【建立新點子】")

    name = input("請替你的點子取個名字：").strip()
    idea = input("請描述你的原始點子：").strip()

    if not name or not idea:
        print("名稱和點子內容都不能空白。")
        return

    project = {
        "name": name,
        "created_at": get_time(),
        "versions": [
            {
                "version": 1,
                "time": get_time(),
                "idea": idea,
                "reason": "原始版本"
            }
        ],
        "risk_history": [],
        "world_history": [],
        "debate_history": []
    }

    data["projects"].append(project)
    save_data(data)

    print(f"\n已建立點子：{name}")
    print("接下來可以對這個點子進行測試。")


def choose_project(data):
    projects = data["projects"]

    if not projects:
        print("\n目前沒有點子，請先建立一個。")
        return None

    print("\n【選擇點子】")

    for index, project in enumerate(projects, start=1):
        latest = project["versions"][-1]["idea"]
        print(f"{index}. {project['name']}")
        print(f"   目前版本：{latest[:45]}")

    choice = input("\n請輸入編號：").strip()

    if not choice.isdigit():
        print("請輸入正確的數字。")
        return None

    index = int(choice) - 1

    if 0 <= index < len(projects):
        return projects[index]

    print("找不到這個編號。")
    return None


def run_test(data):
    project = choose_project(data)

    if project is None:
        return

    idea = project["versions"][-1]["idea"]

    print(f"\n目前測試：{project['name']}")

    risks = analyze_idea(idea)
    project["risk_history"].append({
        "time": get_time(),
        "risks": [risk["name"] for risk in risks]
    })

    worlds = simulate_worlds()
    project["world_history"].append({
        "time": get_time(),
        "answers": worlds
    })

    debate = challenge_round()
    project["debate_history"].append({
        "time": get_time(),
        "debate": debate
    })

    save_data(data)


def revise_idea(data):
    project = choose_project(data)

    if project is None:
        return

    old_idea = project["versions"][-1]["idea"]

    print("\n【點子 DNA：建立新版本】")
    print(f"\n上一版內容：{old_idea}")

    new_idea = input("\n修改後的點子：").strip()
    reason = input("這次修改的原因：").strip()

    if not new_idea:
        print("新版本不能是空白。")
        return

    new_version = {
        "version": len(project["versions"]) + 1,
        "time": get_time(),
        "idea": new_idea,
        "reason": reason if reason else "未填寫原因"
    }

    project["versions"].append(new_version)
    save_data(data)

    print("\n新版本已建立！")
    print(f"版本：v{new_version['version']}")
    print(f"修改原因：{new_version['reason']}")


def show_history(data):
    project = choose_project(data)

    if project is None:
        return

    print(f"\n【{project['name']}：點子 DNA 紀錄】")

    for version in project["versions"]:
        print(f"\n版本 v{version['version']}")
        print(f"時間：{version['time']}")
        print(f"內容：{version['idea']}")
        print(f"原因：{version['reason']}")

    print("\n--- 歷史測試次數 ---")
    print(f"風險分析：{len(project['risk_history'])} 次")
    print(f"平行世界：{len(project['world_history'])} 次")
    print(f"反方攻防：{len(project['debate_history'])} 次")


# =========================
# 主選單
# =========================

def main():
    data = load_data()

    while True:
        show_line()
        print("          AI 反方實驗室 v0.2")
        print("     不只尋找好點子，也要測試它如何失敗")
        show_line()

        print("1. 建立新點子")
        print("2. 測試點子（風險＋平行世界＋反方攻防）")
        print("3. 修改點子，建立新版本")
        print("4. 查看點子 DNA 歷史")
        print("5. 離開程式")

        choice = input("\n請選擇功能（1-5）：").strip()

        if choice == "1":
            create_project(data)
            pause()

        elif choice == "2":
            run_test(data)
            pause()

        elif choice == "3":
            revise_idea(data)
            pause()

        elif choice == "4":
            show_history(data)
            pause()

        elif choice == "5":
            save_data(data)
            print("\n感謝使用 AI 反方實驗室！")
            break

        else:
            print("選項錯誤，請輸入 1 到 5。")


if __name__ == "__main__":
    main()
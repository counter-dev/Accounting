import json


def make_bill() -> dict:
    """问用户要一笔账的数据"""
    time = input("请输入时间：")
    money = float(input("请输入金额："))
    return {"time": time, "money": money}


def show_bills(bills: list[dict]) -> None:
    """打印所有账"""
    if not bills:
        print("还没有任何记录")
        return
    for i, bill in enumerate(bills, start=1):
        print(f"{i}. {bill['time']} | {bill['money']:.2f}")


def load_bills() -> list[dict]:
    """从 bills.json 文件中加载账单"""
    try:
        with open("bills.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_bills(bills: list[dict]) -> None:
    """保存账单到 bills.json 文件"""
    with open("bills.json", "w", encoding="utf-8") as f:
        json.dump(bills, f, ensure_ascii=False, indent=2)


bill_list = load_bills()

while True:
    command = input("\n请输入命令 (a 记账 / s 看账 / q 退出 / d 删除): ")
    if command == "q":
        break
    elif command == "a":
        bill_list.append(make_bill())
        save_bills(bill_list)
    elif command == "s":
        show_bills(bill_list)
    elif command == "d":
        if not bill_list:
            print("没有账单")
            continue
        deleted = bill_list.pop(-1)
        print(f"删除了 {deleted['time']} | {deleted['money']:.2f}\n这是删除以后的账单")
        show_bills(bill_list)
        save_bills(bill_list)
    else:
        print("无效命令")

print("\n最终记录：")
show_bills(bill_list)

"""
Day 01 - pandas 基础练习
========================
任务：熟悉 DataFrame 的查看、筛选、排序、简单统计
运行：python exercise.py

说明：前 2 个任务给出了参考答案，其余任务先自己写，再看注释里的提示。
"""

import pandas as pd

# ------------------------------------------------------------
# 准备：一份迷你电商订单数据（直接运行，无需外部文件）
# 熟悉后可换成真实数据集：
# df = pd.read_csv("../data/taobao_user_behavior.csv")
# ------------------------------------------------------------

data = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "user_id": [11, 12, 11, 13, 12, 14],
    "category": ["图书", "数码", "图书", "服饰", "数码", "图书"],
    "amount": [45.5, 1299, 68, 199, 89, 32],
    "is_paid": [True, True, False, True, True, True],
}
df = pd.DataFrame(data)


def show(title, value):
    """打印任务结果的小工具，不用修改。"""
    print("\n" + "=" * 20, title, "=" * 20)
    print(value)


# 任务 1（示例）：查看前 3 行数据
show("任务1：前3行", df.head(3))

# 任务 2（示例）：查看数据的行列数
show("任务2：行列数", df.shape)

# 任务 3：只看 category 和 amount 两列
# 提示：df[["category", "amount"]]
# show("任务3：品类与金额两列", 你的代码)

# 任务 4：筛选出已支付（is_paid 为 True）的订单
# 提示：df[df["is_paid"]]
# show("任务4：已支付订单", 你的代码)

# 任务 5：筛选金额大于 100 的订单
# 提示：df[df["amount"] > 100]
# show("任务5：金额大于100", 你的代码)

# 任务 6：统计每个品类各有多少笔订单
# 提示：df["category"].value_counts()
# show("任务6：各品类订单数", 你的代码)

# 任务 7：按金额从高到低排序
# 提示：df.sort_values("amount", ascending=False)
# show("任务7：按金额降序", 你的代码)

# 任务 8：计算订单的平均金额
# 提示：df["amount"].mean()
# show("任务8：平均金额", 你的代码)

print("\n完成！把任务 3-8 的 TODO 补上后再运行一次。")

import csv
from collections import defaultdict

# 教科と対応する番号の辞書
subject_mapping = {1: "国語", 2: "数学", 3: "理科", 4: "社会", 5: "英語"}

# 生徒の数
num_students = 10

# 教科ごとのスコアを格納する辞書
subject_scores = {subject: defaultdict(list) for subject in subject_mapping.values()}

# 生徒ごとのスコアの合計を格納する辞書
student_scores = defaultdict(lambda: defaultdict(int))

# 生徒ごとのスコアを読み込む
with open("input_28.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        name, subject, score = row
        student = int(name[-1])
        subject = subject_mapping[int(subject)]
        score = int(score)
        subject_scores[subject][student].append(score)
        student_scores[student][subject] += score

# 通知簿を出力する
for student in range(1, num_students + 1):
    filename = f"生徒{student}.csv"
    with open(filename, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["教科", "平均点", "順位", "成績", "判定"])

        for subject, scores in subject_scores.items():
            # if len(scores[student]) == 0:
            # break
            print(len(scores[student]))
            avg_score = sum(scores[student]) / len(scores[student])
            print(len(scores[student]))
            rank = (
                sorted(
                    student_scores[student],
                    key=lambda x: student_scores[student][x],
                    reverse=True,
                ).index(subject)
                + 1
            )

            if avg_score <= 10 or min(scores[student]) < 10:
                grade = "E"
                judgment = "不合格"
            elif avg_score >= 30:
                grade = "D"
                judgment = "再テスト"
            elif rank == 1:
                grade = "A"
                judgment = "合格"
            elif rank <= 3:
                grade = "B"
                judgment = "合格"
            elif rank <= 7:
                grade = "C"
                judgment = "合格"
            elif rank <= 9:
                grade = "D"
                judgment = "再テスト"

            writer.writerow([subject, round(avg_score, 1), rank, grade, judgment])

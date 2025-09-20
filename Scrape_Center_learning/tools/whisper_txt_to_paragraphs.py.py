# -*- coding: utf-8 -*-
"""
whisper_txt_to_paragraphs.py

功能：
- 读取 Whisper 生成的 txt 文件
- 每 10 行合并成一个段落
- 段落以句号 "。" 结尾
- 输出排版好的文章 txt 文件
"""

import sys
import os

if len(sys.argv) < 2:
    print("用法: python whisper_txt_to_paragraphs.py 输入文件.txt")
    sys.exit(1)

input_file = sys.argv[1]
if not os.path.isfile(input_file):
    print(f"错误：文件不存在 {input_file}")
    sys.exit(1)

# 输出文件名
output_file = os.path.splitext(input_file)[0] + "_paragraphs.txt"

# 读取文本
with open(input_file, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

paragraphs = []
for i in range(0, len(lines), 50):
    chunk = lines[i:i+50]
    para = "".join(chunk)
    if not para.endswith("。"):
        para += "。"
    paragraphs.append(para)

# 每段之间空行
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs))

print(f"文章排版完成：{output_file}")

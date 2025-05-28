import subprocess

def convert_with_pandoc(input_file, output_file):
    try:
        subprocess.run(['pandoc', input_file, '-o', output_file], check=True)
        print(f"成功将 {input_file} 转换为 {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")
    except FileNotFoundError:
        print("请确认Pandoc已安装，并且已添加到系统PATH中")

# 使用示例
convert_with_pandoc('Control_protocol(20250421).docx', 'start.md')
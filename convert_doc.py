import subprocess
import os
from pathlib import Path
import shutil

def convert_with_pandoc_enhanced(input_file, output_file):
    """
    使用增强的pandoc参数转换文档，更好地处理标题、图表和格式
    """
    try:
        # 确保输出目录存在
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 使用增强的pandoc参数
        cmd = [
            'pandoc',
            input_file,
            '-o', output_file,
            '--extract-media=docs/images',  # 提取图片到docs/images目录
            '--wrap=none',  # 不自动换行
            '--standalone',  # 生成独立文档
            '--toc',  # 生成目录
            '--toc-depth=3',  # 目录深度
            '--from=docx',
            '--to=markdown+pipe_tables+grid_tables+multiline_tables',  # 支持多种表格格式
        ]
        
        subprocess.run(cmd, check=True)
        print(f"成功将 {input_file} 转换为 {output_file}")
        
        # 后处理：修复常见的格式问题
        post_process_markdown(output_file)
        
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")
    except FileNotFoundError:
        print("请确认Pandoc已安装，并且已添加到系统PATH中")

def post_process_markdown(file_path):
    """
    后处理markdown文件，修复格式问题
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复常见问题
        # 1. 确保标题前后有空行
        content = content.replace('\n#', '\n\n#')
        content = content.replace('#\n', '#\n\n')
        
        # 2. 修复表格格式
        lines = content.split('\n')
        processed_lines = []
        
        for i, line in enumerate(lines):
            # 确保表格前后有空行
            if line.strip().startswith('|') and i > 0 and lines[i-1].strip() and not lines[i-1].strip().startswith('|'):
                processed_lines.append('')
            
            processed_lines.append(line)
            
            # 表格后添加空行
            if line.strip().startswith('|') and i < len(lines)-1 and lines[i+1].strip() and not lines[i+1].strip().startswith('|'):
                processed_lines.append('')
        
        # 3. 清理多余的空行
        content = '\n'.join(processed_lines)
        content = content.replace('\n\n\n\n', '\n\n\n')
        content = content.replace('\n\n\n\n', '\n\n\n')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"已完成 {file_path} 的后处理")
        
    except Exception as e:
        print(f"后处理失败: {e}")

def create_docs_structure():
    """
    创建完整的文档结构
    """
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)
    
    # 创建子目录
    (docs_dir / 'images').mkdir(exist_ok=True)
    (docs_dir / 'protocol').mkdir(exist_ok=True)
    (docs_dir / 'guide').mkdir(exist_ok=True)
    (docs_dir / 'api').mkdir(exist_ok=True)
    
    print("文档目录结构创建完成")

def main():
    """
    主函数：执行完整的文档转换流程
    """
    print("开始文档转换流程...")
    
    # 1. 创建文档结构
    create_docs_structure()
    
    # 2. 转换主要文档
    input_file = 'docx/UWB_Introduce.docx'
    output_file = 'docs/UWB_Introduce.md'
    
    if Path(input_file).exists():
        convert_with_pandoc_enhanced(input_file, output_file)
    else:
        print(f"输入文件 {input_file} 不存在")

if __name__ == "__main__":
    main()
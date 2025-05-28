# UWB知识点文档

[![Deploy MkDocs](https://github.com/username/UwbKnowledgePoints/actions/workflows/deploy.yml/badge.svg)](https://github.com/username/UwbKnowledgePoints/actions/workflows/deploy.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

这是一个专门收集和整理UWB（Ultra-Wideband）技术相关知识点的文档站点。我们致力于为UWB开发者、研究人员和技术爱好者提供全面、准确、实用的技术文档和开发指南。

## 🌟 特性

- **📚 完整的协议文档** - 详细的UWB通信协议规范
- **🚀 实用的开发指南** - 从入门到进阶的完整指导
- **💻 丰富的示例代码** - 实际可用的代码示例
- **🔧 调试工具** - 开发和调试辅助工具
- **📱 响应式设计** - 支持桌面和移动设备
- **🌙 深色模式** - 支持明暗主题切换

## 📖 文档内容

### 协议文档
- [控制协议规范](docs/protocol/control-protocol.md) - UWB读卡器控制协议详细说明

### 开发指南
- [快速开始](docs/guide/quick-start.md) - 快速上手UWB开发
- [技术概述](docs/guide/overview.md) - UWB技术基础知识
- [硬件规格](docs/guide/hardware.md) - 硬件设备规格说明
- [常见问题](docs/guide/faq.md) - 开发过程中的常见问题解答

### API参考
- [API文档](docs/api/api-reference.md) - 完整的API接口文档

## 🚀 快速开始

### 在线访问

访问我们的在线文档站点：[https://username.github.io/UwbKnowledgePoints/](https://username.github.io/UwbKnowledgePoints/)

### 本地运行

1. **克隆仓库**
   ```bash
   git clone https://github.com/username/UwbKnowledgePoints.git
   cd UwbKnowledgePoints
   ```

2. **安装依赖**
   ```bash
   pip install mkdocs mkdocs-material pymdown-extensions
   ```

3. **启动开发服务器**
   ```bash
   mkdocs serve
   ```

4. **访问文档**
   
   打开浏览器访问 [http://localhost:8000](http://localhost:8000)

### 构建静态站点

```bash
mkdocs build
```

生成的静态文件将保存在 `site/` 目录中。

## 🛠️ 技术栈

- **[MkDocs](https://www.mkdocs.org/)** - 静态站点生成器
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - 现代化的文档主题
- **[PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)** - Markdown扩展
- **[GitHub Pages](https://pages.github.com/)** - 文档托管平台
- **[GitHub Actions](https://github.com/features/actions)** - 自动化部署

## 📁 项目结构

```
UwbKnowledgePoints/
├── docs/                          # 文档源文件
│   ├── index.md                   # 首页
│   ├── protocol/                  # 协议文档
│   │   └── control-protocol.md    # 控制协议规范
│   ├── guide/                     # 开发指南
│   │   ├── quick-start.md         # 快速开始
│   │   ├── overview.md            # 技术概述
│   │   ├── hardware.md            # 硬件规格
│   │   └── faq.md                 # 常见问题
│   ├── api/                       # API参考
│   │   └── api-reference.md       # API文档
│   ├── images/                    # 图片资源
│   └── about.md                   # 关于页面
├── .github/                       # GitHub配置
│   └── workflows/                 # GitHub Actions
│       └── deploy.yml             # 部署工作流
├── mkdocs.yml                     # MkDocs配置文件
├── convert_doc.py                 # 文档转换脚本
├── Control_protocol(20250421).docx # 原始协议文档
└── README.md                      # 项目说明
```

## 🤝 贡献指南

我们欢迎各种形式的贡献！

### 内容贡献

1. **Fork** 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 **Pull Request**

### 文档编写规范

- 使用 Markdown 格式编写文档
- 遵循现有的文档结构和样式
- 添加适当的标题、链接和代码示例
- 确保内容准确性和实用性

### 代码示例规范

- 提供完整、可运行的代码示例
- 添加必要的注释和说明
- 遵循相应语言的编码规范
- 测试代码的正确性

## 📄 许可证

### 文档许可
本项目的文档内容采用 [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) 许可协议。

### 代码许可
项目中的代码示例和工具脚本采用 [MIT License](https://opensource.org/licenses/MIT) 许可协议。

## 🔗 相关链接

- **在线文档**: [https://username.github.io/UwbKnowledgePoints/](https://username.github.io/UwbKnowledgePoints/)
- **GitHub仓库**: [https://github.com/username/UwbKnowledgePoints](https://github.com/username/UwbKnowledgePoints)
- **问题反馈**: [GitHub Issues](https://github.com/username/UwbKnowledgePoints/issues)
- **讨论区**: [GitHub Discussions](https://github.com/username/UwbKnowledgePoints/discussions)

## 🙏 致谢

感谢所有为本项目做出贡献的开发者和技术专家！

特别感谢：
- **IEEE** - 提供UWB技术标准
- **FiRa联盟** - 推动UWB生态发展
- **开源社区** - 提供优秀的工具和框架

## 📞 联系我们

如果您有任何问题、建议或合作意向，欢迎通过以下方式联系我们：

- 📧 **邮箱**: [your-email@example.com](mailto:your-email@example.com)
- 💬 **讨论**: [GitHub Discussions](https://github.com/username/UwbKnowledgePoints/discussions)
- 🐛 **问题报告**: [GitHub Issues](https://github.com/username/UwbKnowledgePoints/issues)

---

⭐ 如果这个项目对您有帮助，请给我们一个星标！
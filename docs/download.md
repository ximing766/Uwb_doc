# 资源下载

欢迎来到UWB技术资源下载页面！这里提供了项目相关的各种资源文件，包括源码包、可执行程序和其他辅助文件。

---

## 1 📁ZIP压缩包下载

<div class="download-section">
  <div class="download-grid">
    <div class="download-item">
      <div class="file-icon">📦</div>
      <div class="download-content">
        <div class="file-info">
          <h4>UWB源码包</h4>
          <span class="file-size">15.6 MB</span>
          <span class="file-date">2024-12-20</span>
          <span class="file-version">v2.1.0</span>
        </div>
      </div>
      <a href="resource/UWB-Source.zip" class="download-btn" download="UWB-Source.zip">下载</a>
    </div>
    
  </div>
</div>

---

## 2 💻EXE可执行文件

<div class="download-section">
  <div class="download-grid">
    <div class="download-item">
      <div class="file-icon">📡</div>
      <div class="download-content">
        <div class="file-info">
          <h4>DK6 编程工具</h4>
          <span class="file-size">1.2 MB</span>
          <span class="file-date">2024-12-20</span>
          <span class="file-version">v1.0.0</span>
        </div>
      </div>
      <a href="resource/DK6Prog.exe" class="download-btn" download="DK6Prog.exe">下载</a>
    </div>
    <div class="download-item">
      <div class="file-icon">⚡</div>
      <div class="download-content">
        <div class="file-info">
          <h4>UWB调试助手</h4>
          <span class="file-size">3.8 MB</span>
          <span class="file-date">2024-12-19</span>
          <span class="file-version">v2.3.1</span>
        </div>
      </div>
      <a href="resource/UWBDebugger.exe" class="download-btn" download="UWBDebugger.exe">下载</a>
    </div>
  </div>
</div>

---

## 3 📄其他文件

<div class="download-section">
  <div class="download-grid">
    <div class="download-item">
      <div class="file-icon">🎨</div>
      <div class="download-content">
        <div class="file-info">
          <h4>UI设计资源</h4>
          <span class="file-size">12.5 MB</span>
          <span class="file-date">2024-12-16</span>
          <span class="file-version">v2.0.0</span>
        </div>
      </div>
      <a href="resource/UI-Assets.psd" class="download-btn" download="UI-Assets.psd">下载</a>
    </div>
  </div>
</div>

---

## 4 📝下载说明

如果您在下载或使用过程中遇到任何问题，请通过以下方式联系我们：

- **邮箱**: ximing766@gmail.com
- **GitHub Issues**: [提交问题](https://github.com/ximing766/ximing766.github.io/issues)

---

<style>
/* 美化标题样式 */
h2 {
  font-weight: 700;
  font-size: 1.4rem;
  margin: 2rem 0 1.5rem 0;
  color: #1e293b;
}

.download-section {
  margin: 1rem 0;
  padding: 1rem;
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 12px;
  background: linear-gradient(135deg,
    rgba(232, 245, 243, 0.27) 100%,
    rgba(255, 255, 255, 0.95) 0%);
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
}

.section-header {
  text-align: center;
  margin-bottom: 1rem;
}

.section-header h3 {
  color: #1e293b;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.section-header p {
  color: #64748b;
  font-size: 0.9rem;
}

.download-grid {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.download-item {
  background: linear-gradient(135deg, 
    rgba(248, 229, 250, 0.27) 0%, 
    rgba(248, 250, 252, 0.95) 100%);
  padding: 0.5rem 0.5rem;
  border-radius: 8px;
  border: 1px solid rgba(226, 232, 240, 0.8);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
  min-height: 40px;
}

.download-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(59, 130, 246, 0.08) 50%, 
    transparent 100%);
  transition: left 0.5s ease;
}

.download-item:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 16px rgba(59, 130, 246, 0.12);
  border-color: rgba(59, 130, 246, 0.25);
}

.download-item:hover::before {
  left: 100%;
}

.file-icon {
  font-size: 1rem;
  min-width: 30px;
  text-align: center;
  background: linear-gradient(135deg, #3b82f6, #8b5cf6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  filter: drop-shadow(0 1px 2px rgba(59, 130, 246, 0.2));
}

.download-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.download-item h4 {
  color: #1e293b;
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  line-height: 1.3;
}

.download-item p {
  color: #64748b;
  font-size: 0.85rem;
  margin: 0;
  line-height: 1.4;
}

.file-info {
  display: flex;
  gap: 0.5rem;
  font-size: 0.75rem;
  color: #64748b;
  margin-top: 0.25rem;
}

.file-info span {
  background: rgba(241, 245, 249, 0.8);
  padding: 0.15rem 0.5rem;
  border-radius: 12px;
  border: 1px solid rgba(226, 232, 240, 0.6);
  font-weight: 500;
}

.download-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%,rgb(125, 192, 209) 100%);
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
  min-width: 100px;
  height: 42px;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
}

.download-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent 0%, 
    rgba(255, 255, 255, 0.3) 50%, 
    transparent 100%);
  transition: left 0.5s ease;
}

.download-btn::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: -1;
}

.download-btn:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
  text-decoration: none;
  color: white;
}

.download-btn:hover::before {
  left: 100%;
}

.download-btn:hover::after {
  opacity: 1;
}

.download-btn:active {
  transform: translateY(0) scale(0.98);
  transition: all 0.1s ease;
}

.download-btn span {
  margin-right: 0.5rem;
  font-size: 1rem;
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.3));
}

@media (max-width: 768px) {
  .download-item {
    flex-direction: column;
    text-align: center;
    gap: 0.75rem;
    padding: 1rem;
    min-height: auto;
  }
  
  .file-info {
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .download-section {
    padding: 1rem;
  }
}
</style>

<script>
function downloadFile(filename) {
  // This is a placeholder function
  // In a real implementation, you would handle the actual file download
  alert('下载功能正在开发中，文件名: ' + filename);
  
  // Example of how you might implement actual downloads:
  // window.open('/downloads/' + filename, '_blank');
}
</script>

---

*最后更新: 2025*
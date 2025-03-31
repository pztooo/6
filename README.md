# 智慧树自动学习助手

自动完成智慧树在线课程的学习任务，支持视频观看、自动答题等功能。

## 功能特点

- ✨ 二维码登录
- 🎬 自动观看视频
- ✅ 自动回答弹题
- 💾 进度保存
- 📊 课程完成度统计

## 快速开始

1. 克隆仓库：
```bash
git clone https://github.com/你的用户名/zhs-auto.git
cd zhs-auto
```

2. 创建虚拟环境：
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate     # Linux/Mac
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 运行程序：
```bash
python main.py
```

## 使用说明

### 基本用法
```bash
# 刷所有课程
python main.py

# 刷指定课程
python main.py -c <courseId>

# 设置播放速度
python main.py -s 2.0

# 限制学习时间
python main.py -c <courseId> -l 25
```

### 获取课程ID
```bash
# 列出所有课程
python main.py --fetch
```

## 配置说明

在 `config.json` 中可以设置：
- 登录方式（二维码）
- 代理设置
- 日志级别
- 图片保存路径
- 推送通知配置

## 注意事项

- 首次使用建议先用浏览器登录智慧树
- 建议使用虚拟环境运行程序
- 请合理使用，避免违反学校规定

## License

MIT License

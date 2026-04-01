# 🎯 从这里开始

欢迎使用**简单商城演示**项目！这个项目帮助你从零开始掌握**网站开发到部署到支付**的完整流程。

---

## 📖 项目包含两个方案

### 方案 1：简单方式（Payment Link）⭐ 推荐从这里开始

**位置：** 项目根目录（当前目录）

```
D:\AI_code\simple-shop-demo\
├── index.html              # 产品展示页面
├── styles.css              # 样式文件
├── README.md               # 项目说明
├── DEPLOY_GUIDE.md         # 详细部署指南 ⭐ 看这个
└── QUICKSTART.md           # 5 分钟快速启动清单
```

**特点：**
- ✅ 零后端代码（纯 HTML/CSS）
- ✅ 30 分钟完成整个流程
- ✅ 完全免费
- ✅ 适合初学者

---

### 方案 2：后端方式（Payment Intent）

**位置：** `backend-example/` 目录

```
D:\AI_code\simple-shop-demo\backend-example\
├── app.py                  # Flask 后端代码
├── requirements.txt        # Python 依赖
├── .env.example           # 环境变量模板
├── templates/             # HTML 模板
└── README.md              # 后端方案文档 ⭐ 看这个
```

**特点：**
- ✅ 完全控制支付流程
- ✅ 可以集成数据库
- ✅ 为微信支付打基础
- ⚠️ 需要后端开发知识

---

## 🚀 推荐学习路径

```
第一步：理解流程（今天）
   ↓
使用方案 1（Payment Link）
   ↓
掌握：GitHub → Vercel → Stripe 完整流程
   ↓
第二步：学习后端（本周）
   ↓
使用方案 2（Payment Intent）
   ↓
掌握：Flask + API + Webhook
   ↓
第三步：微信支付（未来）
   ↓
迁移：Stripe → 微信支付 API
```

---

## 📋 快速开始（方案 1）

### 第 1 步：本地测试（2 分钟）

```bash
# Windows：直接双击打开
D:\AI_code\simple-shop-demo\index.html

# 或者命令行
start index.html
```

**预期结果：**
- 浏览器打开，看到 3 个产品卡片
- 鼠标悬停按钮有动画效果

---

### 第 2 步：推送到 GitHub（3 分钟）

1. 访问 https://github.com，创建新仓库 `simple-shop-demo`
2. 在项目目录运行：

```bash
cd D:\AI_code\simple-shop-demo
git init
git add .
git commit -m "feat: 添加简单商城演示页面"
git branch -M main
git remote add origin https://github.com/你的用户名/simple-shop-demo.git
git push -u origin main
```

---

### 第 3 步：部署到 Vercel（3 分钟）

1. 访问 https://vercel.com，用 GitHub 登录
2. 点击 "Add New" → "Project"
3. 选择 `simple-shop-demo` 仓库
4. 点击 "Deploy"
5. 等待 1 分钟，获得域名：`https://simple-shop-demo.vercel.app`

---

### 第 4 步：配置 Stripe（5 分钟）

1. 访问 https://stripe.com，注册账号
2. 创建产品（Products → Add product）
3. 创建支付链接（Payment Links → Create）
4. 复制支付链接（如：`https://buy.stripe.com/test_xxx`）
5. 在 GitHub 编辑 `index.html`，替换链接

---

### 第 5 步：测试支付（2 分钟）

1. 访问你的 Vercel 域名
2. 点击"立即购买"
3. 使用测试卡号：`4242 4242 4242 4242`
4. 支付成功！

**总耗时：** 约 15 分钟

---

## 📚 文档导航

### 如果你是第一次

👉 **从 `DEPLOY_GUIDE.md` 开始**
- 详细的步骤说明
- 图文并茂的教程
- 常见问题解答

### 如果只想快速启动

👉 **查看 `QUICKSTART.md`**
- 5 分钟快速检查清单
- 关键步骤摘要
- 完成标志确认

### 如果想了解两种方案区别

👉 **阅读 `COMPARISON.md`**
- 两种方案详细对比
- 选择指南
- 学习路径建议

### 如果想学习后端开发

👉 **进入 `backend-example/` 目录**
- 查看 `README.md`
- 运行 Flask 示例
- 学习 API 开发

---

## 🎯 学习目标

完成这个项目后，你将掌握：

### ✅ 技术技能
- [ ] Git 版本控制
- [ ] GitHub 代码托管
- [ ] Vercel 自动部署
- [ ] Stripe 支付集成
- [ ] Flask 后端开发（方案 2）

### ✅ 完整流程
- [ ] 本地开发 → GitHub 托管 → Vercel 部署
- [ ] 产品展示 → 支付链接 → 支付处理
- [ ] 测试环境 → 生产环境切换

### ✅ 为未来准备
- [ ] 微信支付迁移思路
- [ ] 后端 API 开发基础
- [ ] Webhook 回调处理

---

## 💡 关键要点

### 最简单的方式（推荐开始）
- 使用 **Payment Link**（方案 1）
- 无需后端代码
- 15 分钟完成
- 零成本启动

### 进阶方式（以后学习）
- 使用 **Payment Intent**（方案 2）
- 需要 Flask 后端
- 1-2 天完成
- 完全自定义

### 微信支付（未来）
- 需要企业资质
- 基于方案 2 迁移
- 3-7 天完成
- 参考 `backend-example/`

---

## 🔧 技术栈

| 组件 | 方案 1 | 方案 2 |
|------|--------|--------|
| 前端 | HTML + CSS | HTML + CSS + JavaScript |
| 后端 | 无 | Flask (Python) |
| 托管 | GitHub | GitHub |
| 部署 | Vercel | Vercel/Railway |
| 支付 | Stripe Payment Link | Stripe Payment Intent |
| 数据库 | 无 | 可选（SQLite/PostgreSQL） |

---

## 📊 时间和成本

### 方案 1（Payment Link）
- **开发时间：** 30 分钟
- **部署成本：** 免费
- **维护成本：** 免费
- **支付手续费：** 2.9% + ¥2/笔

### 方案 2（Payment Intent）
- **开发时间：** 1-2 天
- **部署成本：** 免费（Vercel）或 $5/月（Railway）
- **维护成本：** 低
- **支付手续费：** 2.9% + ¥2/笔

---

## 🆘 需要帮助？

### 文档查找
- **部署问题** → `DEPLOY_GUIDE.md`
- **快速启动** → `QUICKSTART.md`
- **方案对比** → `COMPARISON.md`
- **后端开发** → `backend-example/README.md`

### 常见问题

**Q: Vercel 部署失败？**
A: 检查 GitHub 仓库是否公开，`index.html` 是否在根目录

**Q: Stripe 打不开？**
A: 确认是否在测试模式，链接是否完整

**Q: 支付后没有邮件？**
A: 测试模式可能不发送邮件，检查 Dashboard 的支付记录

---

## 🎉 开始吧！

**现在就开始第一步：**

```bash
# 打开浏览器查看
start D:\AI_code\simple-shop-demo\index.html

# 然后阅读详细指南
# Windows: start DEPLOY_GUIDE.md
# 或用任意文本编辑器打开
```

**祝你学习顺利！** 🚀

---

## 📞 后续支持

完成基础流程后，你可以：
1. 深入学习后端开发（`backend-example/`）
2. 集成更多功能（数据库、邮件等）
3. 迁移到微信支付（需要企业资质）
4. 优化用户体验和界面设计

---

**创建时间：** 2026-04-01
**最后更新：** 2026-04-01
**维护者：** Claude Code
**项目状态：** ✅ 完整可用

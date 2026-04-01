# 🛒 简单商城演示 - 完整流程示例

这是一个从**开发到部署到支付**的完整流程演示项目，目的是了解网站上线和实现付费功能的全过程。

---

## 📋 完整流程

### 1️⃣ 本地开发
- ✅ 创建 HTML 产品展示页面
- ✅ 添加 CSS 样式美化
- ✅ 添加购买按钮（链接到 Stripe）

### 2️⃣ GitHub 托管
```bash
# 初始化 Git 仓库
git init
git add .
git commit -m "feat: 添加简单商城演示页面"

# 推送到 GitHub
git branch -M main
git remote add origin https://github.com/你的用户名/simple-shop-demo.git
git push -u origin main
```

### 3️⃣ Vercel 部署
1. 访问 [vercel.com](https://vercel.com)
2. 使用 GitHub 账号登录
3. 点击 "Add New Project"
4. 选择 `simple-shop-demo` 仓库
5. 点击 "Deploy"（自动部署，约1分钟）
6. 获得 `https://simple-shop-demo.vercel.app` 域名

### 4️⃣ Stripe 支付配置
1. 访问 [stripe.com](https://stripe.com)
2. 注册账号（选择测试模式）
3. 创建产品（Products → Add product）
4. 创建支付链接（Payment Link → Create）
5. 复制支付链接，替换 `index.html` 中的链接
6. 测试支付（使用测试卡号：4242 4242 4242 4242）

### 5️⃣ 完整购买流程
1. 用户访问网站（Vercel 部署的域名）
2. 浏览产品
3. 点击"立即购买"按钮
4. 跳转到 Stripe 支付页面
5. 输入支付信息完成付款
6. Stripe 发送支付确认邮件
7. 你在 Stripe Dashboard 看到订单

---

## 🎯 技术方案

| 组件 | 技术选择 | 为什么 |
|------|---------|--------|
| 前端 | HTML + CSS | 最简单，无需框架 |
| 托管 | GitHub | 免费代码托管 |
| 部署 | Vercel | 免费、自动部署、HTTPS |
| 支付 | Stripe Payment Link | 无需后端代码 |

**总成本：0 元**
**开发时间：30 分钟**

---

## 📂 项目结构

```
simple-shop-demo/
├── index.html          # 主页面
├── styles.css          # 样式文件
├── README.md           # 说明文档
└── .gitignore          # Git忽略文件
```

---

## 🚀 快速开始

### 本地测试
```bash
# 直接用浏览器打开 index.html 文件即可
```

### 部署到 Vercel
1. 先推送到 GitHub
2. 在 Vercel 导入 GitHub 仓库
3. 自动部署完成

---

## 💰 支付配置详细步骤

### Stripe Payment Link 方式（推荐）

**优点：**
- ✅ 无需写后端代码
- ✅ 无需服务器
- ✅ Stripe 处理所有支付逻辑
- ✅ 自动处理 HTTPS、安全性

**步骤：**

1. **创建 Stripe 账号**
   - 访问 https://stripe.com
   - 注册账号（无需企业认证即可测试）

2. **创建产品**
   - Dashboard → Products → Add product
   - 填写产品名称、价格
   - 保存

3. **创建支付链接**
   - Dashboard → Payment Links → Create
   - 选择刚创建的产品
   - 复制生成的链接（如：`https://buy.stripe.com/xxx`）

4. **替换链接**
   ```html
   <!-- 将 index.html 中的链接替换为你的 -->
   <a href="你的Stripe支付链接" class="buy-button">
       立即购买
   </a>
   ```

5. **测试支付**
   - 使用测试卡号：`4242 4242 4242 4242`
   - 任意过期日期（如：12/34）
   - 任意 CVC（如：123）

---

## 🌐 真实上线步骤

当你准备接受真实支付时：

1. **在 Stripe 激活账号**
   - 完成身份验证
   - 添加银行账户（收款用）

2. **切换到生产模式**
   - Dashboard → 激活生产模式
   - 创建真实的支付链接

3. **更新网站链接**
   - 用生产环境的支付链接替换测试链接

4. **开始营业！**

---

## 📊 费用说明

| 平台 | 免费额度 | 超出后费用 |
|------|---------|-----------|
| Vercel | ✅ 永久免费（个人项目） | $20/月起（专业版） |
| GitHub | ✅ 永久免费（公开仓库） | $7/月起（私有仓库） |
| Stripe | ✅ 无月费 | 每笔交易 2.9% + ¥2 |

**示例：** 卖出 ¥100 的商品
- Stripe 手续费：¥100 × 2.9% + ¥2 = ¥4.9
- 你实际收入：¥95.1

---

## 🔧 自定义修改

### 修改产品信息
编辑 `index.html` 中的产品卡片：
```html
<div class="product-card">
    <h3>你的产品名称</h3>
    <p class="description">产品描述</p>
    <div class="price">¥199.00</div>
    <a href="你的Stripe链接" class="buy-button">立即购买</a>
</div>
```

### 修改颜色
编辑 `styles.css` 中的渐变色：
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

---

## 📚 进阶学习

掌握这个基础流程后，你可以：

1. **添加更多功能**
   - 用户注册登录
   - 购物车
   - 订单管理

2. **使用专业框架**
   - React / Vue
   - Next.js
   - 数据库（PostgreSQL、MongoDB）

3. **集成国内支付**
   - 支付宝
   - 微信支付
   - 需要企业资质和后端代码

---

## 📖 参考资料

- [Vercel 部署文档](https://vercel.com/docs)
- [Stripe 支付链接](https://stripe.com/docs/payment-links)
- [GitHub 指南](https://docs.github.com)

---

## 💡 关键要点

1. **GitHub** 用于代码托管和版本控制
2. **Vercel** 自动从 GitHub 部署网站
3. **Stripe Payment Link** 实现支付无需写代码
4. **整个流程零成本启动**

---

**创建时间：** 2026-04-01
**目的：** 学习网站开发到部署到支付的完整流程

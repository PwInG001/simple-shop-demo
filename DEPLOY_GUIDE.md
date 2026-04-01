# 🚀 完整部署流程指南

本文档提供从零开始到网站上线的**详细步骤说明**。

---

## 步骤 1：本地测试

### 1.1 在浏览器中打开网站
```bash
# Windows
start index.html

# 或者直接双击 index.html 文件
```

✅ 确认：
- 页面正常显示
- 产品卡片显示正确
- 鼠标悬停按钮有动画效果

---

## 步骤 2：推送到 GitHub

### 2.1 创建 GitHub 仓库
1. 访问 https://github.com
2. 登录你的账号
3. 点击右上角 "+" → "New repository"
4. 填写信息：
   - **Repository name**: `simple-shop-demo`
   - **Description**: `简单商城演示 - 从开发到部署到支付的完整流程`
   - **选择**: Public（公开仓库）
   - **不要勾选**: "Add a README file"（我们已经有了）
5. 点击 "Create repository"

### 2.2 推送代码到 GitHub
```bash
# 进入项目目录
cd D:\AI_code\simple-shop-demo

# 初始化 Git
git init

# 添加所有文件
git add .

# 创建首次提交
git commit -m "feat: 添加简单商城演示页面"

# 重命名分支为 main
git branch -M main

# 添加远程仓库（替换为你的用户名）
git remote add origin https://github.com/你的用户名/simple-shop-demo.git

# 推送到 GitHub
git push -u origin main
```

✅ 确认：
- 在 GitHub 网页能看到所有文件
- `https://github.com/你的用户名/simple-shop-demo` 可以访问

---

## 步骤 3：部署到 Vercel

### 3.1 注册 Vercel
1. 访问 https://vercel.com
2. 点击 "Sign Up"
3. 选择 "Continue with GitHub"（用 GitHub 账号登录）
4. 授权 Vercel 访问你的 GitHub

### 3.2 导入项目
1. 登录后，点击 "Add New" → "Project"
2. 在 "Import Git Repository" 中找到 `simple-shop-demo`
3. 点击 "Import"

### 3.3 配置部署
1. **Framework Preset**: 自动检测为 "Other"
2. **Root Directory**: `./`（默认）
3. **Build Command**: 留空（静态网站无需构建）
4. **Output Directory**: `./`（默认）

### 3.4 开始部署
1. 点击 "Deploy" 按钮
2. 等待约 1 分钟（显示 "Building..." → "Ready"）
3. 部署完成后，Vercel 会提供域名：
   - `https://simple-shop-demo-xxx.vercel.app`

✅ 确认：
- 点击部署的域名，能看到完整的网站
- URL 类似：`https://simple-shop-demo.vercel.app`

### 3.5 设置自定义域名（可选）
如果以后想用自己的域名：
1. 在 Vercel 项目中，点击 "Settings" → "Domains"
2. 添加你的域名（如：`shop.yourdomain.com`）
3. 按照提示配置 DNS 记录

---

## 步骤 4：配置 Stripe 支付

### 4.1 注册 Stripe
1. 访问 https://dashboard.stripe.com/register
2. 填写邮箱和密码
3. 选择国家/地区
4. 确认邮箱

### 4.2 创建产品（测试模式）
1. 在 Dashboard 左侧，点击 "Products"
2. 点击 "Add product" 按钮
3. 填写产品信息：
   ```
   Name: Python 自动化工具教程
   Description: 学习如何用 Python 自动化办公工作
   Price: 99.00 CNY
   ```
4. 点击 "Save product"

### 4.3 创建支付链接
1. 在左侧，点击 "Payment links"
2. 点击 "Create payment link"
3. 选择刚创建的产品
4. 配置选项：
   - ✅ 允许促销码（可选）
   - ✅ 收集邮箱地址
   - ✅ 添加收件人电话（可选）
5. 点击 "Create payment link"
6. 复制生成的链接（类似：`https://buy.stripe.com/test_aIM16sbFna0e8G0001`）

### 4.4 更新网站中的支付链接

#### 方式 1：直接编辑（最简单）
1. 在 GitHub 上打开 `index.html`
2. 点击 "铅笔" 图标编辑
3. 找到所有支付链接，替换为你的链接：
   ```html
   <!-- 原来的 -->
   <a href="https://buy.stripe.com/test_aIM16sbFna0e8G0001" ...>

   <!-- 替换为 -->
   <a href="你的新链接" ...>
   ```
4. 滚动到页面底部，提交更改：
   - Commit message: `fix: 更新 Stripe 支付链接`
5. Vercel 会在 1 分钟内自动重新部署

#### 方式 2：本地编辑后推送
```bash
# 本地编辑 index.html
# 修改支付链接

# 提交并推送
git add index.html
git commit -m "fix: 更新 Stripe 支付链接"
git push
```

✅ 确认：
- 在部署的网站上点击"立即购买"
- 能跳转到 Stripe 支付页面

---

## 步骤 5：测试支付流程

### 5.1 使用测试卡号支付

在 Stripe 支付页面，使用以下测试信息：

**卡号：**
```
4242 4242 4242 4242
```

**过期日期：**
```
12/34（任意未来的日期）
```

**CVC：**
```
123（任意3位数字）
```

**邮编：**
```
任意5位数字（如：10000）
```

### 5.2 完整测试流程
1. 访问你的网站（Vercel 域名）
2. 浏览产品
3. 点击任意产品的"立即购买"按钮
4. 跳转到 Stripe 支付页面
5. 输入测试卡号信息
6. 点击 "Pay"
7. 看到支付成功页面
8. 检查邮箱（Stripe 会发送测试邮件）

### 5.3 查看订单
1. 回到 Stripe Dashboard
2. 点击 "Payments"（左侧菜单）
3. 能看到刚才的测试支付记录
4. 点击订单查看详细信息

✅ 确认：
- 支付成功
- 在 Stripe Dashboard 能看到订单
- 收到支付确认邮件（测试邮件）

---

## 步骤 6：切换到生产环境（可选）

**⚠️ 注意：** 只有当你准备接受真实支付时才做这一步！

### 6.1 激活 Stripe 账号
1. 在 Stripe Dashboard，点击 "Activate account"
2. 完成身份验证（需要企业/个人信息）
3. 添加银行账户（用于收款）

### 6.2 创建生产环境的支付链接
1. 在 Dashboard 左上角，切换 "Test mode" → 关闭
2. 重复步骤 4.2-4.3（创建产品和支付链接）
3. 这次获得的链接是真实支付链接

### 6.3 更新网站链接
重复步骤 4.4，将测试链接替换为生产链接

### 6.4 测试真实支付（小额测试）
1. 使用真实信用卡
2. 购买便宜的产品（如 ¥1）
3. 支付成功后，立即退款给自己测试

---

## 📊 完整流程图

```
┌─────────────┐
│  本地开发   │
│  HTML+CSS   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  GitHub     │
│  代码托管   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Vercel     │
│  自动部署   │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Stripe         │
│  Payment Link   │
└──────┬──────────┘
       │
       ▼
┌─────────────┐
│  用户访问   │
│  点击购买   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Stripe     │
│  处理支付   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  支付完成   │
│  收到款项   │
└─────────────┘
```

---

## 🔧 常见问题

### Q1: Vercel 部署失败
**A:** 检查：
- GitHub 仓库是否公开
- `index.html` 是否在根目录
- Vercel 构建日志中的错误信息

### Q2: 支付链接打不开
**A:** 检查：
- Stripe 账号是否激活
- 链接是否完整复制
- 是否在测试模式下

### Q3: 支付后没有收到邮件
**A:**
- 测试模式下邮件可能不会发送
- 检查垃圾邮件文件夹
- 在 Stripe Dashboard 查看支付记录

### Q4: Vercel 域名太长
**A:** 可以：
- 购买自定义域名并绑定
- 使用免费的域名服务（如 Freenom）

---

## 💰 成本总结

| 项目 | 金额 | 说明 |
|------|------|------|
| GitHub | 免费 | 公开仓库永久免费 |
| Vercel | 免费 | 个人项目永久免费 |
| Stripe | 免费 | 无月费，按交易收费 |
| 域名（可选） | $10-15/年 | 如需自定义域名 |

**总启动成本：0 元**（使用免费域名）

---

## 📝 维护清单

### 每月
- [ ] 检查 Stripe 收款情况
- [ ] 查看网站访问统计（Vercel Analytics）
- [ ] 更新产品信息（如需要）

### 每季度
- [ ] 备份网站数据
- [ ] 检查依赖更新（如有）
- [ ] 优化支付流程

---

## 🎓 下一步学习

掌握基础流程后，可以学习：

1. **进阶前端**
   - JavaScript 交互
   - React / Vue 框架
   - 响应式设计

2. **后端开发**
   - Node.js / Python
   - 数据库
   - API 开发

3. **支付集成**
   - Stripe API 高级功能
   - 订阅制支付
   - 国内支付集成

4. **DevOps**
   - CI/CD 自动化
   - 监控和日志
   - 性能优化

---

**创建时间：** 2026-04-01
**最后更新：** 2026-04-01

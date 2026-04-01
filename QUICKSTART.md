# ⚡ 快速启动清单

5 分钟快速检查所有步骤。

---

## ✅ 前置检查

- [ ] 已安装 Git
- [ ] 有 GitHub 账号
- [ ] 有邮箱账号（用于 Stripe 注册）

---

## 📋 步骤清单

### 阶段 1：本地测试（2 分钟）
- [ ] 双击 `index.html` 在浏览器打开
- [ ] 检查页面显示正常
- [ ] 检查产品卡片和按钮

### 阶段 2：GitHub 托管（3 分钟）
- [ ] 在 GitHub 创建新仓库 `simple-shop-demo`
- [ ] 运行以下命令：
  ```bash
  cd D:\AI_code\simple-shop-demo
  git init
  git add .
  git commit -m "feat: 添加简单商城演示页面"
  git branch -M main
  git remote add origin https://github.com/你的用户名/simple-shop-demo.git
  git push -u origin main
  ```

### 阶段 3：Vercel 部署（3 分钟）
- [ ] 访问 https://vercel.com 并登录
- [ ] 点击 "Add New" → "Project"
- [ ] 选择 `simple-shop-demo` 仓库并导入
- [ ] 点击 "Deploy"
- [ ] 等待部署完成（约 1 分钟）
- [ ] 访问生成的域名

### 阶段 4：Stripe 支付（5 分钟）
- [ ] 访问 https://stripe.com 注册
- [ ] 创建第一个产品（Products → Add product）
- [ ] 创建支付链接（Payment Links → Create）
- [ ] 复制支付链接
- [ ] 在 GitHub 上编辑 `index.html`，替换支付链接
- [ ] 等待 Vercel 自动重新部署

### 阶段 5：测试支付（2 分钟）
- [ ] 访问部署的网站
- [ ] 点击"立即购买"
- [ ] 使用测试卡支付：`4242 4242 4242 4242`
- [ ] 检查 Stripe Dashboard 的支付记录

---

## 🎉 完成标志

当你看到以下内容，说明流程已打通：

- ✅ 网站在线（Vercel 提供的域名可以访问）
- ✅ 支付按钮能跳转到 Stripe
- ✅ 能用测试卡完成支付
- ✅ Stripe Dashboard 能看到订单

---

## 📞 需要帮助？

- **Vercel 部署问题**：查看 `DEPLOY_GUIDE.md` 步骤 3
- **Stripe 配置问题**：查看 `DEPLOY_GUIDE.md` 步骤 4
- **GitHub 推送问题**：查看 `DEPLOY_GUIDE.md` 步骤 2

---

## 📊 整体时间

- 本地设置：2 分钟
- GitHub 设置：3 分钟
- Vercel 部署：3 分钟
- Stripe 配置：5 分钟
- 测试验证：2 分钟

**总计：约 15 分钟**

---

现在开始吧！🚀

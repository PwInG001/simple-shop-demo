# 后端支付示例

这是一个使用 Flask + Stripe Payment Intent 的完整后端支付示例。

## 🎯 学习目标

通过这个示例，你将学会：

1. ✅ 创建 Flask 后端服务
2. ✅ 集成 Stripe Payment Intent API
3. ✅ 处理支付回调（Webhook）
4. ✅ 前后端分离架构
5. ✅ 环境变量安全管理

---

## 📋 与 Payment Link 的区别

| 特性 | Payment Link | Payment Intent |
|------|--------------|----------------|
| **技术难度** | ⭐ 简单 | ⭐⭐⭐ 中等 |
| **后端代码** | 不需要 | 必需 |
| **自定义** | 有限 | 完全控制 |
| **适用场景** | 快速测试 | 生产系统 |

### 为什么学习 Payment Intent？

- 🎯 **完全控制**：可以自定义整个支付流程
- 🔗 **系统集成**：可以与数据库、订单系统、用户系统深度集成
- 📧 **即时响应**：支付成功后立即触发业务逻辑（发邮件、更新数据库）
- 🚀 **扩展性**：为未来集成微信支付、支付宝打基础

---

## 🚀 快速开始

### 1. 安装依赖

```bash
# 进入后端示例目录
cd D:\AI_code\simple-shop-demo\backend-example

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境（Windows）
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
# 复制环境变量模板
copy .env.example .env

# 编辑 .env 文件，填入你的 Stripe 密钥
# 从 https://dashboard.stripe.com/apikeys 获取
```

### 3. 运行服务

```bash
# 开发模式
python app.py

# 访问 http://localhost:5000
```

### 4. 测试支付

1. 访问 http://localhost:5000
2. 选择产品，点击"立即购买"
3. 使用测试卡号：`4242 4242 4242 4242`
4. 支付成功后跳转到 `/success` 页面

---

## 📁 项目结构

```
backend-example/
├── app.py                    # Flask 应用主文件
├── requirements.txt          # Python 依赖
├── .env.example             # 环境变量模板
├── .env                     # 环境变量（不提交到 Git）
├── templates/               # HTML 模板
│   ├── products.html        # 产品页面
│   ├── success.html         # 支付成功页面
│   └── cancel.html          # 支付取消页面
└── README.md                # 本文件
```

---

## 🔑 关键代码说明

### 1. 创建支付意图（API 端点）

```python
@app.route('/api/create-payment-intent', methods=['POST'])
def create_payment():
    """创建支付意图"""
    intent = stripe.PaymentIntent.create(
        amount=9900,  # 单位：分
        currency='cny',
        metadata={'product_id': 1}
    )
    return jsonify({'clientSecret': intent.client_secret})
```

### 2. 处理支付成功（Webhook）

```python
@app.route('/api/webhook', methods=['POST'])
def webhook():
    """Stripe 支付成功回调"""
    event = stripe.Webhook.construct_event(payload, sig, webhook_secret)

    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        # 在这里添加你的业务逻辑
        send_confirmation_email(payment_intent)
        update_order_status(payment_intent)

    return jsonify({'success': True})
```

### 3. 前端调用（JavaScript）

```javascript
// 调用后端创建支付意图
const response = await fetch('/api/create-payment-intent', {
    method: 'POST',
    body: JSON.stringify({product_id: 1})
});

const {clientSecret} = await response.json();

// 使用 Stripe.js 处理支付
const {error} = await stripe.confirmCardPayment(clientSecret, {
    payment_method: {card: cardElement}
});
```

---

## 🌐 部署到生产环境

### 方案 1：Vercel（推荐，免费）

1. 安装 Vercel CLI
   ```bash
   npm install -g vercel
   ```

2. 配置 `vercel.json`
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. 部署
   ```bash
   vercel
   ```

### 方案 2：Railway（简单，有免费额度）

1. 访问 https://railway.app
2. 连接 GitHub 仓库
3. 自动部署

### 方案 3：自己的服务器

```bash
# 使用 Gunicorn 运行
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## 🔐 安全最佳实践

### ✅ 必须做

1. **使用环境变量存储密钥**
   ```python
   stripe.api_key = os.getenv('STIPE_SECRET_KEY')
   ```

2. **验证 Webhook 签名**
   ```python
   event = stripe.Webhook.construct_event(payload, sig, webhook_secret)
   ```

3. **使用 HTTPS**
   - 生产环境必须使用 HTTPS
   - Vercel/Railway 自动提供 HTTPS

### ❌ 不能做

1. ❌ 在代码中硬编码密钥
   ```python
   # 错误
   stripe.api_key = 'sk_test_xxxxx'

   # 正确
   stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
   ```

2. ❌ 将 .env 文件提交到 Git
   ```bash
   # .gitignore 中添加
   .env
   venv/
   ```

3. ❌ 在前端代码中使用 Secret Key
   ```javascript
   // 错误
   const stripe = Stripe('sk_test_xxxxx');

   // 正确
   const stripe = Stripe('pk_test_xxxxx'); // Publishable Key
   ```

---

## 📊 从这里到微信支付

掌握了这个示例后，集成微信支付的步骤：

### 1. 申请微信支付
- 需要企业营业执照
- 在微信支付商户平台注册

### 2. 后端代码改造
- 将 Stripe API 替换为微信支付 API
- 处理微信的签名算法
- 配置回调 URL

### 3. 前端适配
- 集成微信 H5 支付或 JSAPI 支付
- 处理微信的跳转逻辑

### 关键差异

| 项目 | Stripe | 微信支付 |
|------|--------|----------|
| API 复杂度 | 简单 | 复杂（签名、加密） |
| 文档质量 | 优秀 | 一般 |
| 测试环境 | 完善的测试模式 | 需要真实环境 |
| 国际化 | 支持 | 仅中国 |

**建议：** 先用 Stripe 掌握整个支付流程，再迁移到微信支付。

---

## 🧪 测试卡号

在 Stripe 测试环境使用：

| 卡号 | 描述 |
|------|------|
| `4242 4242 4242 4242` | 支付成功 |
| `4000 0000 0000 0002` | 卡被拒绝 |
| `4000 0000 0000 9995` | 余额不足 |

过期日期：任意未来日期（如 `12/34`）
CVC：任意 3 位数字（如 `123`）

---

## 📚 参考资料

- [Stripe Payment Intent 文档](https://stripe.com/docs/payments/payment-intents)
- [Stripe Webhook 指南](https://stripe.com/docs/webhooks)
- [Flask 官方文档](https://flask.palletsprojects.com/)
- [Python Stripe 库](https://github.com/stripe/stripe-python)

---

## 🎓 下一步

1. **完成当前示例**
   - [ ] 本地运行测试
   - [ ] 部署到 Vercel/Railway
   - [ ] 测试完整支付流程

2. **扩展功能**
   - [ ] 添加数据库（SQLite/PostgreSQL）
   - [ ] 实现订单管理
   - [ ] 添加邮件发送

3. **学习微信支付**
   - [ ] 阅读微信支付官方文档
   - [ ] 申请微信支付商户号
   - [ ] 参考本示例重构为微信支付

---

**创建时间：** 2026-04-01
**目的：** 学习后端支付集成，为微信支付打基础

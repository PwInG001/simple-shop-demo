# 微信收款码配置指南

将你的微信收款码添加到网站中。

---

## 📱 第一步：获取微信收款码图片

### 方法 1：保存现有收款码（推荐）

1. 打开微信 → 我 → 服务 → 收付款
2. 点击"收款码"
3. 点击右上角"⋯"更多
4. 点击"保存图片"
5. 图片保存到手机的相册

### 方法 2：生成新的收款码

1. 打开微信 → 我 → 服务 → 收付款
2. 点击"收款码"
3. 点击右上角"⋯"更多
4. 点击"收款码样式"
5. 选择你喜欢的样式
6. 保存图片

---

## 🔄 第二步：将图片传到电脑

### 方式 A：微信传输（最简单）

1. 在手机微信中，点击"文件传输助手"
2. 发送收款码图片
3. 在电脑微信中，保存图片到：
   ```
   D:\AI_code\simple-shop-demo\images\wechat-qr.png
   ```

### 方式 B：使用云盘

1. 上传到百度网盘/OneDrive/Google Drive
2. 在电脑下载到项目目录

---

## 📂 第三步：创建图片目录

```bash
# 在项目目录创建 images 文件夹
mkdir D:\AI_code\simple-shop-demo\images

# 将微信收款码图片复制到这个文件夹
# 文件名改为：wechat-qr.png
```

最终目录结构：
```
D:\AI_code\simple-shop-demo\
├── images\
│   └── wechat-qr.png          ← 你的微信收款码
├── index.html
├── wechat-pay.html
├── styles.css
└── ...
```

---

## ✏️ 第四步：更新代码

打开 `wechat-pay.html`，找到第 142 行：

```html
<!-- 🔧 请替换为你的微信收款码图片 -->
<img id="wechatQRCode" src="data:image/svg+xml,..." alt="微信收款码">
```

替换为：

```html
<img id="wechatQRCode" src="images/wechat-qr.png" alt="微信收款码">
```

---

## 🧪 第五步：测试

### 本地测试

```bash
# 双击打开
D:\AI_code\simple-shop-demo\wechat-pay.html
```

1. 点击任意产品的"微信支付"按钮
2. 检查是否显示你的微信收款码
3. 检查付款金额是否正确

### 部署到 Vercel

```bash
# 提交到 GitHub
cd D:\AI_code\simple-shop-demo
git add .
git commit -m "feat: 添加微信支付功能"
git push
```

Vercel 会自动部署（约 1 分钟）

---

## 📊 完整工作流程

### 用户购买流程

```
1. 用户浏览网站
2. 点击"微信支付"按钮
3. 看到弹窗，显示收款码 + 付款金额
4. 用微信扫描二维码付款
5. 付款成功后，点击"已付款，确认订单"
```

### 商家处理流程

```
1. 在微信中收到转账通知
2. 确认收款金额和产品
3. 查看用户信息（如用户在备注中填写）
4. 发货（发送下载链接/激活码等）
```

---

## 💡 优化建议

### 1. 添加用户信息收集

在弹窗中添加输入框，让用户填写：

```html
<!-- 在确认按钮前添加 -->
<div style="margin-top: 20px; text-align: left;">
    <label style="display: block; margin-bottom: 10px;">
        联系方式：
        <input type="text" id="userContact" placeholder="微信号/手机号"
               style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
    </label>
    <label style="display: block; margin-bottom: 10px;">
        备注（可选）：
        <input type="text" id="userNote" placeholder="邮箱或其他联系方式"
               style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
    </label>
</div>
```

### 2. 在付款备注中提示用户

在"付款步骤"中添加：

```html
<li>付款时，请在备注中填写你的微信号</li>
```

### 3. 添加自动通知功能

使用后端记录订单，付款后自动发送邮件：

```python
# 示例：使用 Flask 后端
@app.route('/api/order', methods=['POST'])
def create_order():
    product = request.json.get('product')
    amount = request.json.get('amount')
    contact = request.json.get('contact')

    # 保存订单到数据库
    # 发送通知邮件给你
    # 发送确认邮件给用户
```

---

## 🔐 安全提示

### ✅ 推荐

- 使用"微信收款码"（个人）即可
- 定期检查收款记录
- 保留付款截图作为凭证
- 设置合理的付款金额上限

### ⚠️ 注意

- 不要在代码中暴露敏感信息
- 对于大额交易，谨慎处理
- 考虑使用第三方支付平台（如需自动化）

---

## 📈 进阶方案

当业务量增加时，可以考虑：

### 方案 A：使用聚合支付平台

- **PayJS**: 个人可用，手续费 2%
- **XorPay**: 支持微信/支付宝，1.5% 手续费
- **虎皮椒**: 个人可用，简单接入

优点：
- ✅ 自动确认支付
- ✅ 支持回调通知
- ✅ 无需人工确认

### 方案 B：企业申请微信支付

如果你有企业营业执照：

1. 申请微信支付商户号
2. 开发后端 API
3. 集成微信 H5 支付或 JSAPI 支付
4. 实现完全自动化

参考：`backend-example/README.md`

---

## 🆘 常见问题

### Q1: 收款码图片不显示？

**A:**
1. 检查图片路径是否正确
2. 确认图片文件在 `images/` 目录下
3. 使用浏览器开发者工具查看错误信息

### Q2: 如何知道用户付款了？

**A:**
- 方式 1：在微信中查看收款通知
- 方式 2：让用户在付款备注中填写信息
- 方式 3：添加后端订单系统

### Q3: 可以同时支持微信和支付宝吗？

**A:** 可以！添加第二个收款码：

```html
<div class="payment-methods">
    <button onclick="showWeChatPay()">微信支付</button>
    <button onclick="showAlipay()">支付宝</button>
</div>
```

### Q4: 这种方式安全吗？

**A:**
- ✅ 对于小额交易是安全的
- ✅ 微信官方收款方式，有保障
- ⚠️ 需要人工确认收款
- ⚠️ 不适合高频自动化场景

---

## 📞 联系方式配置

在弹窗中添加你的联系方式：

```html
<div class="note" style="background: #e3f2fd; border-color: #2196f3;">
    <strong>📱 联系方式：</strong>
    <br>微信号：[你的微信号]
    <br>手机号：[你的手机号]
    <br>付款后请联系我确认！
</div>
```

---

## ✅ 检查清单

部署前检查：

- [ ] 微信收款码图片已放在 `images/wechat-qr.png`
- [ ] `wechat-pay.html` 中图片路径已更新
- [ ] 本地测试正常显示收款码
- [ ] 付款金额显示正确
- [ ] 已添加联系方式
- [ ] 已推送到 GitHub
- [ ] Vercel 部署成功
- [ ] 线上测试正常

---

## 🎉 完成！

现在你的网站支持微信支付了！

**后续优化：**
1. 添加用户信息收集
2. 集成后端订单系统
3. 添加邮件通知
4. 考虑聚合支付平台

---

**创建时间：** 2026-04-01
**最后更新：** 2026-04-01

# 微信收款码图片说明

## 📱 请将你的微信收款码放在这个目录

### 文件名要求
```
wechat-qr.png
```

### 如何获取收款码

1. 打开微信
2. 我 → 服务 → 收付款
3. 点击"收款码"
4. 点击右上角"⋯" → "保存图片"
5. 将图片传到电脑，重命名为 `wechat-qr.png`
6. 放到这个目录

### 图片要求
- **格式**: PNG 或 JPG
- **文件名**: wechat-qr.png
- **大小**: 建议小于 1MB
- **尺寸**: 正方形（如 500x500）

### 配置代码

确保 `wechat-pay.html` 中的代码是：

```html
<img id="wechatQRCode" src="images/wechat-qr.png" alt="微信收款码">
```

### 测试

```bash
# 在浏览器中打开
D:\AI_code\simple-shop-demo\wechat-pay.html

# 点击"微信支付"按钮，应该能看到你的收款码
```

---

**创建时间：** 2026-04-01

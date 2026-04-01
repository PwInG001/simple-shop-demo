"""
支付后端服务示例
支持：Stripe Payment Intent（未来可扩展到微信支付）
"""

from flask import Flask, request, jsonify, render_template
import stripe
import os
from datetime import datetime

app = Flask(__name__)

# 配置
# 从环境变量读取密钥（安全做法）
stripe.api_key = os.getenv('STRIPE_SECRET_KEY', 'sk_test_your_key_here')

# 网站密钥（前端使用）
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', 'pk_test_your_key_here')


@app.route('/')
def index():
    """主页 - 产品展示"""
    products = [
        {
            'id': 1,
            'name': 'Python 自动化工具教程',
            'description': '学习如何用 Python 自动化办公工作',
            'price': 9900,  # 单位：分
            'image': '📦'
        },
        {
            'id': 2,
            'name': '市政工程实务指南',
            'description': '工程设计与管理实战经验总结',
            'price': 14900,
            'image': '🎯'
        },
        {
            'id': 3,
            'name': 'Web 快速入门课程',
            'description': '快速掌握网页开发基础技能',
            'price': 19900,
            'image': '🚀'
        }
    ]
    return render_template('products.html', products=products)


@app.route('/api/create-payment-intent', methods=['POST'])
def create_payment():
    """
    创建支付意图
    前端调用此接口获取支付信息
    """
    try:
        data = request.json
        product_id = data.get('product_id')

        # 从数据库获取产品价格（这里简化为硬编码）
        prices = {
            1: 9900,
            2: 14900,
            3: 19900
        }

        amount = prices.get(product_id, 9900)

        # 创建 Stripe Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='cny',
            metadata={
                'product_id': product_id,
                'timestamp': datetime.now().isoformat()
            }
        )

        return jsonify({
            'success': True,
            'clientSecret': intent.client_secret,
            'publishableKey': STRIPE_PUBLISHABLE_KEY
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/api/webhook', methods=['POST'])
def webhook():
    """
    Stripe Webhook 回调
    支付成功后，Stripe 会调用此接口通知你
    """
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET', '')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )

        # 处理支付成功事件
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            handle_successful_payment(payment_intent)

        return jsonify({'success': True})

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except stripe.error.SignatureVerificationError as e:
        return jsonify({'error': str(e)}), 400


def handle_successful_payment(payment_intent):
    """
    处理支付成功的业务逻辑
    """
    product_id = payment_intent.metadata.get('product_id')
    amount = payment_intent.amount

    # TODO: 在这里添加你的业务逻辑
    # - 发送确认邮件
    # - 更新数据库订单状态
    # - 发放产品（下载链接、激活码等）
    # - 记录日志

    print(f"支付成功！产品ID: {product_id}, 金额: {amount / 100} 元")

    # 示例：保存订单到数据库
    # order = Order(
    #     product_id=product_id,
    #     amount=amount,
    #     status='paid',
    #     stripe_payment_intent_id=payment_intent.id
    # )
    # db.session.add(order)
    # db.session.commit()


@app.route('/success')
def success():
    """支付成功页面"""
    return render_template('success.html')


@app.route('/cancel')
def cancel():
    """支付取消页面"""
    return render_template('cancel.html')


if __name__ == '__main__':
    # 开发环境
    app.run(debug=True, port=5000)

    # 生产环境（使用 Gunicorn）
    # gunicorn -w 4 -b 0.0.0.0:5000 app:app

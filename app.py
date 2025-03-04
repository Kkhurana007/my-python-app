from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with the pricing cards and buttons
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscribe to French Course</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        .content-visible {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #444;
        }
        .pricing-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 20px;
        }
        .pricing-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
            text-align: center;
        }
        .pricing-card h2 {
            font-size: 24px;
            margin-bottom: 10px;
        }
        .pricing-card p {
            font-size: 16px;
            color: #666;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
        .btn:hover {
            background-color: #0056b3;
        }
        .discount {
            color: #28a745;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="content-visible">
        <h1>Subscribe to French Course</h1>
        <p>Choose a plan that works best for you:</p>
        <div class="pricing-container">
            <div class="pricing-card">
                <h2>Monthly Plan</h2>
                <p><strong>$50/month</strong></p>
                <ul>
                    <li>Access to all lessons</li>
                    <li>New content every week</li>
                    <li>Cancel anytime</li>
                </ul>
                <button id="monthly-button" class="btn">Subscribe Now</button>
            </div>
            <div class="pricing-card">
                <h2>Yearly Plan</h2>
                <p><strong>$450/year</strong></p>
                <p class="discount">Save 25% (Originally $600)</p>
                <ul>
                    <li>Access to all lessons</li>
                    <li>New content every week</li>
                    <li>3 months free compared to monthly</li>
                </ul>
                <button id="yearly-button" class="btn">Subscribe Now</button>
            </div>
            <div class="pricing-card">
                <h2>Coaching with Mentor</h2>
                <p><strong>$300/month</strong></p>
                <ul>
                    <li>More than <strong>24 hours</strong> of personalized coaching per month</li>
                    <li>Tailored lesson plans</li>
                    <li>Weekly progress reviews</li>
                    <li>Direct feedback and support</li>
                </ul>
                <a href="https://forms.gle/cUqsy2YCYPk5X6hE9" class="btn">Subscribe Now</a>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
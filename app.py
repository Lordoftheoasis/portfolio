import os
import sys
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

# Django settings
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='a-very-secret-key',
    ALLOWED_HOSTS=['*'],
)

# HTML content
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Aditya Pandey - Portfolio</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: #0f0f0f;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
            padding: 40px;
            margin: 0;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            padding-bottom: 40px;
        }

        img {
            width: 120px;
            border-radius: 50%;
            border: 3px solid #00ffc3;
        }

        h1 {
            margin-top: 20px;
            font-size: 2.5em;
            color: #00ffc3;
        }

        section {
            margin-bottom: 40px;
            background: #1a1a1a;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0, 255, 200, 0.1);
        }

        h2 {
            border-bottom: 1px solid #00ffc3;
            padding-bottom: 5px;
            margin-bottom: 15px;
            color: #00ffc3;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            margin-bottom: 8px;
        }

        a {
            color: #00ffc3;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .emoji {
            margin-right: 6px;
        }

        footer {
            text-align: center;
            color: #777;
            font-size: 0.9em;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <img src="https://api.dicebear.com/7.x/thumbs/svg?seed=Aditya" alt="Avatar">
            <h1>Aditya Pandey</h1>
            <p>Finance major | Data enthusiast | Kathmandu, Nepal</p>
        </header>

        <section>
            <h2>📬 Contact</h2>
            <ul>
                <li><span class="emoji">📧</span><a href="mailto:aditxa4@gmail.com">aditxa4@gmail.com</a></li>
                <li><span class="emoji">🔗</span><a href="https://www.linkedin.com/in/aditya-pandey-092b87224" target="_blank">LinkedIn Profile</a></li>
            </ul>
        </section>

        <section>
            <h2>💼 Experience</h2>
            <ul>
                <li><strong>Source Code (Fintech)</strong> – Research Analyst (Mar 2025–Present)</li>
                <li><strong>Citizen Investment Trust</strong> – Loan Assistant (Jan–Mar 2025)</li>
                <li><strong>IT Technical Support</strong> – CIT (Oct–Dec 2024)</li>
                <li><strong>Investment Intern</strong> – CIT (Aug–Oct 2024)</li>
                <li><strong>Nepal Investment Summit 2024</strong> – Student Volunteer (Apr 2024)</li>
                <li><strong>Freelancer</strong> – Upwork (Jan–Oct 2023)</li>
            </ul>
        </section>

        <section>
            <h2>🎓 Education</h2>
            <ul>
                <li><strong>Kathmandu University School of Management</strong> – BBA in Finance (2021–2025)</li>
                <li><strong>Global College of Management</strong> – Plus Two in Business (2019–2021)</li>
                <li><strong>Paragon Public School</strong> – SEE (2010–2019)</li>
            </ul>
        </section>

        <section>
            <h2>🛠️ Skills</h2>
            <ul>
                <li>Leadership</li>
                <li>Analytical Thinking</li>
                <li>Project Management</li>
            </ul>
        </section>

        <footer>
            &copy; 2025 Aditya Pandey. All rights reserved.
        </footer>
    </div>
</body>
</html>
"""

# View function
def homepage(request):
    return HttpResponse(HTML)

# URL routing
urlpatterns = [
    path('', homepage),
]

# Command line execution for server
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '__main__')
    execute_from_command_line(sys.argv)
    

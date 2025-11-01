
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def chat(request):
    return render(request, 'assistant/chat.html')

@csrf_exempt
def ai_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        # Prevent duplicate consecutive questions
        last_msg = request.session.get('last_msg', '')
        msg = user_message.lower() if user_message else ''
        if msg and msg == last_msg:
            response = "You've already asked that! Please ask something new."
        elif user_message:
            request.session['last_msg'] = msg
            # ...existing code...
            if 'introduction' in msg:
                response = (
                    "Good afternoon, and thank you for giving me this opportunity.\n"
                    "My name is Ashutosh Khilar, and I’m from Balasore, Odisha, which is famously known as the missile city of India. I’ve recently completed my Master’s in Computer Applications with a CGPA of 8.90. During my studies, I developed a deep passion for software development, especially in areas like web development, backend systems, data analysis, and machine learning.\n\n"
                    "I’ve had the opportunity to work on several real-world projects where I applied technologies such as Python, JavaScript, Django, REST APIs, and MySQL. In my final year, I worked on a deep learning project titled ‘Generative Adversarial Networks for Image Generation,’ where I implemented a GAN model using TensorFlow and Keras to generate synthetic images.\n\n"
                    "This project helped me understand the architecture of GANs, where a Generator creates fake images and a Discriminator learns to distinguish them from real images. By training them together, the system learns to generate highly realistic images. I specifically worked with the DCGAN architecture, using convolutional neural networks to enhance image quality. The aim was to generate realistic images of clothing items that could be useful for applications like data augmentation in fashion or e-commerce platforms.\n\n"
                    "Additionally, I explored the ethical aspects of using GANs, especially regarding deepfakes and AI-generated content. I also looked into advanced GAN models like StyleGAN and their potential applications in medical imaging and creative design.\n\n"
                    "Alongside machine learning, I enjoy solving problems and have a strong understanding of algorithms, SQL, and system design fundamentals. I’m a fast learner, a collaborative team member, and always eager to explore new technologies and improve my skills.\n\n"
                    "Currently, I’m looking for a role where I can contribute meaningfully, learn from a talented team, and apply my expertise to real-world challenges. Once again, thank you for this opportunity—I’m excited to be here and looking forward to contributing my best."
                )
            elif 'what are you doing' in msg:
                response = "I am here, waiting to help you with your requests!"
            elif 'best friend' in msg:
                response = "Niki and Anchal are your best friends."
            elif 'how are you' in msg:
                response = "I'm just a program, but I'm always ready to help you! How can I assist you today?"
            elif 'prime minister' in msg:
                response = "As of 2025, the Prime Minister of India is Narendra Modi."
            elif 'help' in msg:
                response = "I can answer your questions, provide information, and assist with tasks. Just ask me anything!"
            elif 'who made you' in msg or 'who created you' in msg:
                response = "I was made by Mr. Ashutosh Khilar, also known as ASHU. He is my creator and mentor."
            elif 'roommate' in msg:
                response = "Your roommates are Mukul and Amit."
            elif 'mca' in msg or 'master of computer application' in msg or 'masters' in msg:
                response = "You have completed your Master of Computer Applications (MCA) in Balasore college of engineering of technology with a CGPA of 8.90."
            elif 'who is amit' in msg:
                response = "Amit is Shreya's boyfriend and your roommate. His full name is Amit Mohapatra. He loves to talk with girls, likes to watch reels where girls are dancing, and is also known as a lover boy."
            elif 'who is mukul' in msg:
                response = "Mukul is your roommate. His full name is Ratikant Swain. He is a short, intelligent, and genius guy who loves to watch modeling shows and enjoys communicating with girls."
            elif 'who is radha' in msg:
                response = "Radha is a girl whom you trust blindly and who loves you a lot. She is the sweetest girl and means a lot to you. Her full name is Mamina Kar."
            elif "amit's girlfriend" in msg or 'amit girlfriend' in msg:
                response = "Amit's girlfriend is Shreya Banarjee."
            elif 'Elder sister name' in msg and 'younger' not in msg:
                response = "Your sister's name is Happy.Her full name is Sthita Pragnya khilar."
            elif 'who is barsha' in msg or 'barsha' in msg or 'rani' in msg:
                response = "Barsha is your closest friend. Her full name is Barsha rani panigrahi. She is a very good human being and a very caring person. She married to raja and now she is raja's wife."
            elif "who is elli" in msg:
                response = "Elli is your close friend and also your favourite person. Her full name is Anshita Behera. She is a beautiful, sweet and cute girl, and you call her Elli. She also likes to talk with boys a lot and is very caring towards you."
            elif 'younger sister' in msg or 'puchu' in msg:
                response = "Your younger sister's name is Siku, Her full name is Swikruti Roy and you call her Puchu."
            elif 'django trainer' in msg:
                response = "Your Django trainer is Mr. Shaik Harshad Vali Sir."
            elif 'python trainer' in msg:
                response = "Your Python trainer is Mr. Pranay Kumar Sir."
            elif 'who is atul' in msg:
                response = "Atul is your roommate's brother and a very good human being. His full name is Soumyakant Swain. He is a very helpful and kind person. He is working in Wipro as a software engineer."
            elif 'date of birth' in msg or 'dob' in msg:
                response = "Your date of birth is 19th August 2002."
            elif 'who  is sitting besides me' in msg or 'sitting beside me' in msg or 'sitting' in msg:
                response = "Amit Mohapatra sits beside you. He is also known as Amit."
            elif 'hometown' in msg:
                response = "Your hometown is Soro, Balasore, Odisha."
            elif 'which role is suitable' in msg or 'suitable role' in msg:
                response = "AI Engineer is the most suitable role for you among Python Fullstack Developer, Business Analyst, AI Engineer, and Data Scientist."
            elif 'where am i staying' in msg or 'where i am staying' in msg or 'current location' in msg:
                response = "You are staying in Marathahalli, Bengaluru."
            elif 'tell me something about yourself' in msg:
                response = "Hey there, I’m Lexi! I was created by Mr. Ashu, who I proudly call my boss. He built me to help with questions, solve problems, and make things easier for you. Think of me as a smart, friendly companion — always here to support Ashu’s vision."
            elif 'who is niki' in msg or 'nikki' in msg:
                response = "Niki is your best friend,Her full name is Ashalipsa kar.she is a cute,beautiful and sweet girl .who is always supportive and fun to be around."
            elif 'who is anchal' in msg:
                response = "Anchal is your best friend, known for her kindness and cheerful nature."
            elif 'who is shreya' in msg:
                response = "Shreya Banarjee is Amit's girlfriend and a close friend."
            elif 'who is ashutosh' in msg or 'who is ashu' in msg:
                response = "Ashutosh Khilar, also known as Ashu, is your creator and mentor."
            elif 'who is happy' in msg:
                response = "Happy is your sister, always bringing joy to your life."
            elif 'who is siku' in msg or 'who is puchu' in msg:
                response = "Siku, whom you call Puchu, is your younger sister."
            elif 'who is gullu' in msg or 'gullu' in msg:
                response = "Gullu is your close friend, her full name is Kabita Singh. She is also your friend Pintu's sister, known for her caring nature and beautiful smile. She is a very good human being."
            elif 'who is pranay' in msg:
                response = "Mr. Pranay Kumar Sir is your Python trainer. His full name is Dommaraju Pranay Kumar."
            elif 'who is harshad' in msg:
                response = "Mr. Shaik Harshad Vali Sir is your Django trainer."
            elif 'who is your boss' in msg:
                response = "My boss is Mr. Ashutosh Khilar, also known as Ashu."
            elif 'who is your best friend' in msg:
                response = "Niki and Anchal are my best friends."
            elif 'who is your creator' in msg:
                response = "I was created by Mr. Ashutosh Khilar, also known as Ashu."
            elif 'weather' in msg:
                response = "I can't access live weather, but you can check weather.com or ask your phone's assistant!"
            elif 'capital of india' in msg:
                response = "The capital of India is New Delhi."
            elif 'python' in msg:
                response = "Python is a popular programming language known for its simplicity and versatility."
            elif 'machine learning' in msg:
                response = "Machine learning is a field of AI that enables computers to learn from data and make predictions or decisions."
            elif 'your name' in msg:
                response = "My name is Lexi, your AI assistant!"
            elif 'thank you' in msg:
                response = "You're welcome! If you have more questions, just ask."
            elif 'joke' in msg:
                response = "Why did the computer go to the doctor? Because it had a virus!"
            elif 'who is the president of india' in msg:
                response = "As of 2025, the President of India is Droupadi Murmu."
            elif 'capital of odisha' in msg:
                response = "The capital of Odisha is Bhubaneswar."
            elif 'chief minister of odisha' in msg:
                response = "As of 2025, the Chief Minister of Odisha is Mohan Charan Majhi."
            elif 'what is ai' in msg or 'artificial intelligence' in msg:
                response = "Artificial Intelligence (AI) is the simulation of human intelligence in computers, enabling them to perform tasks that typically require human intelligence."
            elif 'what is django' in msg:
                response = "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design."
            elif 'what is your purpose' in msg:
                response = "My purpose is to assist you, answer your questions, and help you with tasks."
            # ...inside ai_response, before the final else:...
            elif 'king of indian cricket' in msg:
                response = "Virat Kohli is often called the King of Indian Cricket."
            elif 'god of cricket' in msg:
                response = "Sachin Tendulkar is widely regarded as the God of Cricket."
            elif 'largest statue of india' in msg or 'biggest statue of india' in msg:
                response = "The Statue of Unity in Gujarat is the largest statue in India."
            elif 'winner of ipl 2025' in msg:
                response = "The winner of IPL 2025 is Chennai Super Kings."
            elif 'king of bollywood' in msg:
                response = "Shah Rukh Khan is popularly known as the King of Bollywood."
            elif 'iron man of india' in msg:
                response = "Sardar Vallabhbhai Patel is known as the Iron Man of India."
            elif 'president of usa' in msg:
                response = "As of 2025, the President of USA is Joe Biden."
            elif 'president of russia' in msg:
                response = "As of 2025, the President of Russia is Vladimir Putin."
# ...existing code...            elif 'president of china' in msg:
            elif 'president of china' in msg:
                response = "As of 2025, the President of China is Xi Jinping."
            elif 'what is my fathers name' in msg or 'my father name' in msg:
                response = "Your father's name is Mr. Gopabandhu Khilar. Whom you love very much. But never tell him."
            # ...inside ai_response, before the final else:...
            elif any(op in msg for op in ['sum', 'add', 'plus', 'subtract', 'minus', 'multiply', 'product', 'divide', 'division']):
                import re
                numbers = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', msg)]
                if len(numbers) >= 2:
                    if 'sum' in msg or 'add' in msg or 'plus' in msg:
                        result = sum(numbers)
                        response = f"The sum is {result}."
                    elif 'subtract' in msg or 'minus' in msg:
                        result = numbers[0] - numbers[1]
                        response = f"The result of subtraction is {result}."
                    elif 'multiply' in msg or 'product' in msg:
                        result = numbers[0] * numbers[1]
                        response = f"The product is {result}."
                    elif 'divide' in msg or 'division' in msg:
                        if numbers[1] != 0:
                            result = numbers[0] / numbers[1]
                            response = f"The result of division is {result}."
                        else:
                            response = "Division by zero is not allowed."
                    else:
                        response = "Please specify the operation (sum, subtract, multiply, divide)."
                else:
                    response = "Please provide at least two numbers for the operation."
# ...existing code...
            else:
                response = "I don't know about this question. Please ask something else."
            
            
        else:
            response = "AI says: Please enter a message."
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Invalid request.'}, status=400)

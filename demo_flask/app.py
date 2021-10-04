from flask import Flask,render_template
app = Flask(__name__)

studentlist = [
    ["/static/img/students/st1.jpg","Praveen", "My courses taught me to pick up new ideas quickly and apply them to real-world problems. Today, my certificates make me stand out from the crowd."],
    ["/static/img/students/st2.jpg","Abhinav", "Learning isn't just about being better at your job: it's so much more than that. Here it allows me to learn without limits."],
    ["/static/img/students/st3.jpg","Don Mario", "Online learning gives me the flexibility I need to take courses on my own time."],
    ["/static/img/students/st4.jpg","Adarsh", "When I need courses on topics that my university doesn't offer, this is one of the best places to go."],
    ["/static/img/students/st5.jpg","Riya", "Timely course offerings helped me publish a book and re-establish myself in my field. I recommend this to everyone!"],
    ["/static/img/students/st6.jpg","Beckham", "The contents is good but the system accessing is very unstable. When I need a support, it's never can contact them."],
    ["/static/img/students/st7.jpg","Alexander", "Extremely super. I love the courses available"],
    ["/static/img/students/st8.jpg","Saniya", "Very Helpful and intresting courses, easy to learn and understand"],  
]

facltylist=[
    ["/static/img/fclty/fclty3.jpg","Stephen Grider","Engineering Architect","Stephen Grider has been building complex Javascript front ends for top corporations in the San Francisco Bay Area.  With an innate ability to simplify complex topics, Stephen has been mentoring engineers beginning their careers in software development for years."],
    ["/static/img/fclty/fclty2.jpg","Sebastien Sebu","CEO Devsl | iOS | Android | Freelancing","I am a veteran mobile developer having built over 57 mobile apps for iOS and Android, and I've also build multiple Unity 3D games, including Call of Duty Ghosts mobile. "],
    ["/static/img/fclty/fclty1.jpg","Ben Johnson","Head of Data Science | Data Inc","A professional instructor and trainer for Data Science and programming. He has publications and patents in various fields such as microfluidics, materials science, and data science technologies."], 
]

courselist=[
    ["/static/img/courses/course1.jpg","Full Stack Programming","This Professional Certificate will equip you with all the key skills and technical know-how to kickstart your career as a Full-Stack Cloud Native Application Developer. Guided by experts at IBM, you will learn to build your own cloud-based applications and practice working with the technologies behind them. This program consists of 10 courses with ample instructional content as well as hands-on exercises and projects designed to hone your skills and help you build your portfolio. No prior programming experience or Cloud background is required to start this program. You'll skill up with the tools and technologies that successful software developers use to build, deploy, test, run, and manage Full Stack Cloud Native applications, giving you the practical skills to begin a new career in a highly in-demand area. The courses in this program will help you develop skill sets in a variety of technologies including: Cloud foundations, HTML, CSS, JavaScript, GitHub, Node.js, React, Cloud Native practices, DevOps, CI/CD, Containers, Docker, Kubernetes, OpenShift, Istio, Python programming, Databases, SQL, NoSQL, Django ORM, Bootstrap, Application Security, Microservices, Serverless computing, and more."],
    ["/static/img/courses/course2.jpg","Data Science Programming","Data science is one of the hottest professions of the decade, and the demand for data scientists who can analyze data and communicate results to inform data driven decisions has never been greater. This Professional Certificate will help anyone interested in pursuing a career in data science or machine learning develop career-relevant skills and experience. It’s a myth that to become a data scientist you need a Ph.D. Anyone with a passion for learning can take this Professional Certificate – no prior knowledge of computer science or programming languages required – and develop the skills, tools, and portfolio to have a competitive edge in the job market as an entry level data scientist. The program consists of 9 online courses that will provide you with the latest job-ready tools and skills, including open source tools and libraries, Python, databases, SQL, data visualization, data analysis, statistical analysis, predictive modeling, and machine learning algorithms. You’ll learn data science through hands-on practice in the IBM Cloud using real data science tools and real-world data sets. "],
    ["/static/img/courses/course3.jpg","Block Chain Programming","This specialization introduces blockchain, a revolutionary technology that enables peer-to-peer transfer of digital assets without any intermediaries, and is predicted to be just as impactful as the Internet. More specifically, it prepares learners to program on the Ethereum blockchain. The four courses provide learners with (i) an understanding and working knowledge of foundational blockchain concepts, (ii) a skill set for designing and implementing smart contracts, (iii) methods for developing decentralized applications on the blockchain, and (iv) information about the ongoing specific industry-wide blockchain frameworks. The specialization covers a range of essential topics, from the cryptographic underpinnings of blockchain technology to enabling decentralized applications on a private Ethereum blockchain platform. It is ideal for programmers and designers involved in developing and implementing blockchain applications, and anyone who is interested in understanding its potential.  "],
    ["/static/img/courses/course4.jpg","Quantum Computing","This specialization will open the door to the world of quantum technology. You will learn about the principles of quantum computing and how to bring these principles to life. The specialization is created by two scientific groups - physicists and mathematicians, so you can look at quantum computing from different angles. Despite the fact that in different courses the same issues are discussed, they are considered from different positions and with varying degrees of depth in the details. We hope that as you follow this path of progressive immersion, you will feel like a real expert in the subject of quantum computing."],
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student')
def student():
    return render_template('Students.html', len = len(studentlist), studentlist = studentlist)

@app.route('/institute')
def institute():
    return render_template('Institutions.html')

@app.route('/courses')
def courses():
    return render_template('courses.html',len = len(courselist), courselist = courselist)

@app.route('/faculty')
def faculty():
    return render_template('faculty.html', len = len(facltylist), facltylist = facltylist)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
   app.run(debug = True)
from constants import YOE, PRIMARY_SKILLS


def prompt_skills_section(context, primary_skills=PRIMARY_SKILLS):
    prompt = f'''
    ## Job Description Context:
    {context}

    ## Task:
    Create a Skills section based on the given job description context. Make sure to include the following skills too: {primary_skills}

    ## Output Format:
    Skills: <List of comma separated relevant skills>

    Example:
    ## Job Description Context:
    Looking for a data scientist with experience in machine learning, data engineering, and cloud platforms. The ideal candidate should be proficient in Python, Java, and have experience with big data tools like Spark. Knowledge of web development with JavaScript and React is a plus.

    ## Example Output:
    Skills: Python, Java, Spark, JavaScript, React, Google Cloud, AWS, Git/GitHub

    Skills: 
    '''
    return prompt


def prompt_tag_section(context, years_of_experience=YOE):
    prompt = f'''
    ## Job Description Context:
    {context}

    ## Task:
    Write a brief one-sentence tag line optimized for what the job description is seeking.

    ## Output Format:
    <Job Title> with {years_of_experience}+ of experience, specializing in <key skills and expertise>

    Example 1:
    ## Job Description Context:
    Seeking a data scientist with experience in machine learning, data analysis, and cloud platforms. The ideal candidate should have strong skills in Python, R, and SQL, and experience with big data tools like Spark and Hadoop.

    ## Example Output:
    Data Scientist with 5+ years of experience, specializing in machine learning, data analysis, and cloud platforms

    Example 2:
    ## Job Description Context:
    Looking for a machine learning engineer with expertise in deploying machine learning models, developing generative AI solutions, and performing A/B testing. The candidate should be proficient in Python, TensorFlow, and have experience with cloud services like AWS and Google Cloud.

    ## Output Format:
    MLE with {years_of_experience}+ of experience, specializing in <key skills and expertise>

    ## Example Output:
    MLE with {years_of_experience}+ years of experience, specializing in deploying machine learning models, generative AI, and A/B testing

    ## Output: 
    '''
    return prompt

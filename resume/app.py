from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    about_me = (
        "Cloud Engineer Professional with approximately 3 years of hands-on experience. Certified in Azure DevOps "
        "with expertise in Cloud, Automation, CI/CD solutions, driving impactful projects through optimized processes "
        "and informed decisions."
    )
    experience = (
        "Insight (Cloud Engineer-II)\n"
        "Sept 2021 - Present | Noida, Uttar Pradesh, India\n\n"
        "- Implementing Azure workflows and services tailored to meet specific business requirements while ensuring robust GxP compliance.\n"
        "- Led the implementation of CICD pipeline utilizing Jenkins, streamlining team workflows and boosting productivity.\n"
        "- Engineered the Azure solutions for cost management across multiple services in 600 subscriptions saving up to 100 grand per month.\n"
    )
    project = (
        "- Orchestrated the deployment of automated Azure workflows using Python and PowerShell scripting, driving a remarkable 98% boost in operational efficiency.\n"
        "- Engineered Azure Functions using Python and Azure REST API to automate event-driven processes for Azure Services; resulting in a 40% decrease in manual tasks and a 25% increase in overall operational efficiency.\n"
        "- Developed Azure Automation processes via Python and PowerShell scripting by refining runbooks to automate various Azure IaaS and RBAC offerings for more than 600 Azure Subscriptions to eliminate manual interventions.\n"
        "- Implemented automated test scripts in Python, leveraging BDD frameworks to validate the whitelisting functionality of Azure services.\n"
        "- Spearheaded the design and implementation of Azure Policies to enforce governance and compliance standards, ensuring secure and scalable deployments of Azure IaaS and PaaS services.\n"
        "- Pioneered exploration of Azure services like Azure DataShare, Azure Functions, Azure Storage, etc. by executing POC which helped in making strategic decisions to drive adoption of cutting-edge technologies.\n"
        "- Conducted regular reviews and updates of technical documentation to reflect changes in systems, processes, and requirements, ensuring accuracy and relevance over time.\n"
        "- Proficient in designing service designs/architectures tailored for controlled environments, ensuring seamless service enablement and compliance.\n"
        "- Displayed leadership by mentoring team members on Azure service policies and best practices, fostering a culture of continuous improvement and expertise in cloud technologies.\n"
        "- Demonstrated success in collaborating with cross-functional teams to achieve project objectives and drive innovation.\n"
    )
    technical_skills = (
        "Cloud and Infrastructure: Azure, Linux, Windows, Terraform, Azure Resource Manager Template, Docker, Azure Monitor, Azure App Insights\n"
        "DevOps and Automation: Jenkins, Git, GitHub, Bitbucket\n"
        "Scripting and Programming: Python, PowerShell, JSON\n"
    )
    certifications = (
        "- Microsoft Certified | DevOps Engineer Expert (AZ-400) - June 2022\n"
        "- Microsoft Certified | Azure Developer Associate (AZ-204) - March 2021\n"
        "- Microsoft Certified | Azure AI Fundamentals (AI-900) - May 2021\n"
        "- Microsoft Certified | Azure Data Fundamentals (DP-900) - May 2021\n"
    )
    education = (
        "Graphic Era Hill University\n"
        "Bachelor of Technology (Hons.) in Computer Science (Cloud Computing)\n"
        "Dehradun, Uttarakhand, India\n"
    )

    return render_template('index.html', 
                           about_me=about_me, 
                           experience=experience, 
                           project=project, 
                           technical_skills=technical_skills, 
                           certifications=certifications, 
                           education=education)

if __name__ == '__main__':
    app.run(debug=True)

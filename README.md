<p align="center"><h1 align="center">POLICY-WONKS-API</h1></p>
<p align="center">
 <em>Empowering Policy Insights Through Collaborative Intelligence</em>
</p>
<p align="center">
 <img src="https://img.shields.io/github/license/jkaunert/policy-wonks-api?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
 <img src="https://img.shields.io/github/last-commit/jkaunert/policy-wonks-api?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
 <img src="https://img.shields.io/github/languages/top/jkaunert/policy-wonks-api?style=default&color=0080ff" alt="repo-top-language">
 <img src="https://img.shields.io/github/languages/count/jkaunert/policy-wonks-api?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"></p>
<p align="center"></p>
<br>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
  - [Project Index](#project-index)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Project Roadmap](#project-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

The policy-wonks-api project addresses the challenge of analyzing economic and fiscal policies by leveraging AI-driven insights. Key features include a collaborative multi-agent system for policy evaluation, user-friendly API endpoints, and robust data management. Targeted at policymakers, economists, and analysts, it enhances decision-making through informed, data-backed assessments.

---

## Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a microservices architecture with a focus on modularity and separation of concerns.</li><li>Built on the <code>Python</code> programming language, leveraging frameworks like <code>CrewAI</code> for multi-agent collaboration.</li><li>Employs <code>Docker</code> for containerization, ensuring consistent environments across development and production.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows best practices in coding standards and style, enhancing readability and maintainability.</li><li>Utilizes type hints and structured data models for clarity in data handling.</li><li>Regular code reviews and adherence to a version control system ensure high-quality contributions.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation is provided, including setup instructions and usage examples.</li><li>Utilizes <code>Markdown</code> for easy readability and accessibility.</li><li>Includes detailed comments within the codebase to explain complex logic and functionality.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with external AI models such as <code>Jamba</code> and <code>Llama</code> for advanced natural language processing tasks.</li><li>Supports data persistence through <code>SQLite</code> for efficient data management.</li><li>Utilizes <code>Docker</code> for seamless deployment and integration with CI/CD pipelines.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Structured into distinct modules, each responsible for specific functionalities (e.g., models, agents, tasks).</li><li>Encourages reusability of components across different parts of the application.</li><li>Facilitates easy updates and maintenance by isolating changes to individual modules.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes unit tests to ensure individual components function as expected.</li><li>Encourages test-driven development (TDD) practices to enhance reliability.</li><li>Utilizes mocking and stubbing techniques for testing interactions with external services.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized for performance with efficient data handling and processing techniques.</li><li>Utilizes asynchronous programming where applicable to enhance responsiveness.</li><li>Employs caching strategies to reduce database load and improve response times.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements secure handling of sensitive data, including API keys and user information.</li><li>Regular security audits and updates to dependencies to mitigate vulnerabilities.</li><li>Utilizes environment variables for configuration to prevent hardcoding sensitive information.</li></ul> |

---

## Project Structure

```sh
└── policy-wonks-api/
    ├── Dockerfile
    ├── README.md
    ├── db
    │   ├── chroma.sqlite3
    │   └── e7ff8a0b-e613-4d01-814d-cd82b1795e23
    ├── knowledge
    │   └── user_preference.txt
    ├── pyproject.toml
    ├── src
    │   └── policy_wonks
    └── uv.lock
```

### Project Index

<details open>
 <summary>**`POLICY-WONKS-API/`**</summary>
 	<details>
  <summary>**root**</summary>
   <table>
   <tr>
    <td>**[Dockerfile](https://github.com/jkaunert/policy-wonks-api/blob/master/Dockerfile)**</td>
    <td>\- Facilitates the containerization of a Python application by establishing a lightweight environment using a slim Python image  
\- It integrates the UV tool for dependency management and ensures the application is ready for execution  
\- By setting the working directory and environment variables, it streamlines the deployment process, allowing the app to run efficiently on a specified host and port.</td>
   </tr>
   <tr>
    <td>**[pyproject.toml](https://github.com/jkaunert/policy-wonks-api/blob/master/pyproject.toml)**</td>
    <td>\- Defines the project configuration for "policy\_wonks," a tool leveraging crewAI to facilitate policy analysis and management  
\- It specifies essential metadata, dependencies, and scripts for various functionalities such as running, training, and testing the application  
\- This foundational setup ensures compatibility with Python versions 3.10 to 3.13 and establishes the build system, enabling seamless integration and deployment within the broader codebase architecture.</td>
   </tr>
   </table>
 </details>
 <details>
  <summary>**knowledge**</summary>
   <table>
   <tr>
    <td>**[user\_preference.txt](https://github.com/jkaunert/policy-wonks-api/blob/master/knowledge/user_preference.txt)**</td>
    <td>\- Captures user preferences and background information, specifically tailored for an AI Engineer named John Doe  
\- This data serves to personalize interactions within the project, enhancing user experience by aligning features and recommendations with the user's interests in AI Agents  
\- It plays a crucial role in the overall architecture by facilitating targeted content and functionality based on user profiles.</td>
   </tr>
   </table>
 </details>
 <details>
  <summary>**db**</summary>
   <table>
   <tr>
    <td>**[chroma.sqlite3](https://github.com/jkaunert/policy-wonks-api/blob/master/db/chroma.sqlite3)**</td>
    <td>\- The code file located at \`db/chroma.sqlite3\` serves as a database for the project, specifically utilizing SQLite as its storage engine  
\- Its primary purpose is to manage and persist data efficiently within the overall architecture of the codebase  
\- This database file is integral to the project's functionality, enabling the storage, retrieval, and manipulation of data that the application relies on  
\- By providing a structured way to handle data, it supports the project's objectives and enhances its performance and scalability.</td>
   </tr>
   </table>
   <details>
    <summary>**e7ff8a0b-e613-4d01-814d-cd82b1795e23**</summary>
     <table>
     <tr>
      <td>**[link\_lists.bin](https://github.com/jkaunert/policy-wonks-api/blob/master/db/e7ff8a0b-e613-4d01-814d-cd82b1795e23/link_lists.bin)**</td>
      <td>\- Facilitates the storage and retrieval of linked list data structures within the project’s database  
\- By managing serialized binary representations, it enhances data persistence and efficiency, allowing other components of the codebase to access and manipulate linked lists seamlessly  
\- This functionality is crucial for maintaining the integrity and performance of the overall architecture.</td>
     </tr>
     <tr>
      <td>**[header.bin](https://github.com/jkaunert/policy-wonks-api/blob/master/db/e7ff8a0b-e613-4d01-814d-cd82b1795e23/header.bin)**</td>
      <td>\- Facilitates the storage and retrieval of header information within the database architecture, ensuring efficient data management and integrity  
\- This component plays a crucial role in maintaining the overall structure and accessibility of data, contributing to the seamless operation of the project by enabling quick access to essential metadata associated with stored records.</td>
     </tr>
     </table>
   </details>
 </details>
 <details> <!-- src Submodule -->
  <summary>**src**</summary>
   <details>
    <summary>**policy_wonks**</summary>
     <table>
     <tr>
      <td>**[models.py](https://github.com/jkaunert/policy-wonks-api/blob/master/src/policy_wonks/models.py)**</td>
      <td>\- Defines data models for handling requests and responses related to economic policy analysis  
\- The PolicyWonksRequest model captures key topics and economic variables for evaluation by an economist and a financial analyst, while the PolicyWonksResponse model structures their respective outputs  
\- This facilitates clear communication and data management within the broader architecture of the project, enhancing the interaction between different components focused on economic policy insights.</td>
     </tr>
     <tr>
      <td>**[crew.py](https://github.com/jkaunert/policy-wonks-api/blob/master/src/policy_wonks/crew.py)**</td>
      <td>\- Defines the PolicyWonks crew, orchestrating a collaborative environment for agents specializing in economics and financial analysis  
\- It configures agents with specific models and tools, establishes tasks for each role, and integrates them into a cohesive crew that utilizes advanced language models for planning and execution  
\- This structure enhances the project's capability to address complex policy-related inquiries effectively.</td>
     </tr>
     <tr>
      <td>**[app.py](https://github.com/jkaunert/policy-wonks-api/blob/master/src/policy_wonks/app.py)**</td>
      <td>\- Facilitates the Policy Wonks API, an orchestrated multi-agent system designed for analyzing economic and fiscal policies using the CrewAI framework  
\- It enables users to submit policy topics and economic variables, triggering a collaborative analysis from both an economist and a financial analyst  
\- The API also includes health-check and welcome endpoints, ensuring robust interaction and user engagement with the system.</td>
     </tr>
     <tr>
      <td>**[main.py](https://github.com/jkaunert/policy-wonks-api/blob/master/src/policy_wonks/main.py)**</td>
      <td>\- Facilitates the execution and management of policy simulations within the project  
\- It allows users to run simulations, train models with specified iterations, replay past executions, and test outcomes based on economic variables and policy topics  
\- This functionality is essential for analyzing the impact of different policies, thereby enhancing decision-making processes in economic contexts.</td>
     </tr>
     <tr>
      <td>**[llm\_config.py](https://github.com/jkaunert/policy-wonks-api/blob/master/src/policy_wonks/llm_config.py)**</td>
      <td>\- Configuration of various language models is achieved, enabling the project to leverage advanced AI capabilities  
\- By integrating models such as Jamba and Llama, the architecture supports diverse natural language processing tasks  
\- Utilizing environment variables for API keys ensures secure access to these models, facilitating seamless interactions with the inference service and enhancing the overall functionality of the codebase.</td>
     </tr>
     </table>
     <details>
      <summary>**config**</summary>
       <table>
       <tr>
        <td>**[agents.yaml](https://github.com/jkaunert/policy-wonks-api/blob/master/src/policy_wonks/config/agents.yaml)**</td>
        <td>\- Defines roles and objectives for key economic agents within the project, specifically an economist and a financial analyst  
\- Each agent is tasked with analyzing the impacts of specific policy topics on economic and financial metrics, providing insights to policymakers and the public  
\- This structure enhances the overall codebase by facilitating informed decision-making through expert analysis and clear communication of complex concepts.</td>
       </tr>
       <tr>
        <td>**[tasks.yaml](https://github.com/jkaunert/policy-wonks-api/blob/master/src/policy_wonks/config/tasks.yaml)**</td>
        <td>\- Defines tasks for economic analysis within the project, specifically targeting the evaluation of government policies and their market implications  
\- It outlines roles for an economist and a financial analyst, detailing their responsibilities in providing comprehensive assessments based on specified economic variables  
\- This structure facilitates informed decision-making for policymakers by ensuring thorough and objective evaluations of economic conditions and policy impacts.</td>
       </tr>
       </table>
     </details>
   </details>
 </details>
</details>

---

## Getting Started

### Prerequisites

Before getting started with policy-wonks-api, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python 3.12
- **Dependency Management:** UV
- **Container Runtime:** Docker

### Installation

Install policy-wonks-api using one of the following methods:

**Build from source:**

1. Clone the policy-wonks-api repository:

```sh
❯ git clone https://github.com/jkaunert/policy-wonks-api
```

2. Navigate to the project directory:

```sh
❯ cd policy-wonks-api
```

3. Install the project dependencies:

```sh
❯ uv sync
```

**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ DOCKER_BUILDKIT=1 docker build -t {image_name} .
```

**From Docker Hub** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)
```sh
❯ docker pull jkaunert/policy-wonks-api-v1:local
```

### Usage

Run policy-wonks-api using the following command:
**Using `docker` locally** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -p 8000:8000 policy-wonks-api-v1:local
```

**Render Deployment** &nbsp; [<img align="center" src="https://img.shields.io/badge/Render-008CBA.svg?style={badge_style}&logo=render&logoColor=white" />](https://render.com/)

[Policy Wonks API](https://policy-wonks-api-v1-latest.onrender.com/docs)

## Project Roadmap

- [X] **`Task 1`**: <strike>Upload to Docker Hub.</strike>
- [X] **`Task 2`**: <strike>Deploy API to Render.</strike>
- [ ] **`Task 3`**: Deploy Streamlit App.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/jkaunert/policy-wonks-api/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/jkaunert/policy-wonks-api/issues)**: Submit bugs found or log feature requests for the `policy-wonks-api` project.
- **💡 [Submit Pull Requests](https://github.com/jkaunert/policy-wonks-api/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.

   ```sh
   git clone https://github.com/jkaunert/policy-wonks-api
   ```

3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.

   ```sh
   git checkout -b new-feature-x
   ```

4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.

   ```sh
   git commit -m 'Implemented new feature x.'
   ```

6. **Push to github**: Push the changes to your forked repository.

   ```sh
   git push origin new-feature-x
   ```

7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!

</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
[![](https://contrib.rocks/image?repo=jkaunert/policy-wonks-api)](https://github.com/jkaunert/policy-wonks-api/graphs/contributors)
</details>

---

## License

This project is protected under the GNU General Public License v3.0 - For more details, refer to the [LICENSE](https://choosealicense.com/licenses/gpl-3.0/) page.

---

## Acknowledgments

- [crewAI](https://crewai.com)
- [FastAPI](https://fastapi.tiangolo.com)

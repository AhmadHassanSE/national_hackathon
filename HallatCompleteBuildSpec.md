**HAALAT**

**حالت**

_Pakistan's First Real-Time Multi-Agent Emergency Intelligence System_

**COMPLETE BUILD SPECIFICATION FOR AI AGENT IMPLEMENTATION**

| **Event <br>**Hackathon Day 2 | **Track <br>**Healthcare + Civic Tech |
| ----------------------------- | ------------------------------------- |

| **Team Size <br>**2-3 Participants | **Build Time <br>**4 Hours (hackathon sprint) |
| ---------------------------------- | --------------------------------------------- |

**SECTION 1 - THE PROBLEM WE ARE SOLVING**

**1\. Problem Statement**

In Pakistan, the average ambulance response time in Karachi is 8 minutes. A person in cardiac arrest begins experiencing irreversible brain damage in 4 minutes. This 4-minute gap is where people die - not from lack of medical infrastructure, but from lack of coordination.

Current emergency response in Pakistan fails citizens in three critical ways:

- No structured triage - citizens do not know whether their situation requires an ambulance, a clinic visit, or just first aid.
- No bystander mobilization - trained first aiders, off-duty doctors, and volunteers who live nearby are never activated.
- No language accessibility - emergency tools assume English literacy; most citizens communicate in Urdu, Sindhi, or Pashto.
- No mass-event detection - when multiple emergencies cluster (gas leak, stampede, building collapse), no system aggregates the signals and escalates to a mass-event protocol.

**The gap is not infrastructure. The gap is intelligence. Haalat provides that intelligence.**

**1.1 Impact Numbers (say these out loud during your presentation)**

| **Statistic**                               | **Why It Matters**                                              |
| ------------------------------------------- | --------------------------------------------------------------- |
| **8 minutes - avg Karachi ambulance ETA**   | Brain death starts at 4 min. The gap kills.                     |
| **0 real-time bystander tools in Pakistan** | Trained volunteers near you are invisible to the system.        |
| **220 million people**                      | The scale Haalat can serve at near-zero marginal cost.          |
| **4 languages spoken in emergencies**       | Urdu, Sindhi, Pashto, English - current tools handle none well. |
| **3+ clustered incidents = mass event**     | No existing system detects this and escalates automatically.    |

**SECTION 2 - WHAT HAALAT DOES**

**2\. System Overview**

Haalat is a multi-agent AI system built with Python, LangChain, CrewAI, and Gradio. A citizen describes their emergency in any language - typed or spoken - and within 3 seconds Haalat:

- Detects the language and routes all output through a vernacular pipeline
- Classifies the emergency type and assigns a severity score (1-5)
- Locates the 3 nearest emergency services via Google Maps API
- Alerts registered community volunteers and first aiders within 500 meters
- Begins real-time coaching (CPR, burns, choking) if life-threatening
- Checks for mass event pattern (3+ same incidents within 1km / 5min)
- Auto-generates a situation report for civil defense if mass event detected
- Logs the incident anonymously into a city memory RAG database

**2.1 The Five Crazy Upgrades Over Basic Emergency Routing**

**Upgrade 1 - Multilingual by default (not by selection)**

**No language dropdown. No form to fill. Type in broken Urdu - the system understands and responds in kind.**

The Language Router Agent detects dialect automatically using LLM inference. All downstream agent outputs are piped through the same language model with a vernacular prompt. A grandmother in Larkana and a doctor in Karachi get equally usable responses.

**Upgrade 2 - Bystander mobilization, not just ambulance dispatch**

**The nearest trained person responds in 90 seconds. The ambulance takes 8 minutes.**

The Resource Locator Agent queries a RAG knowledge base of registered community volunteers - trained first aiders, off-duty medical staff, and community health workers - who have opted into the Haalat volunteer network. When a critical emergency is classified, Haalat simultaneously alerts the 3 nearest volunteers with the incident type, address, and a one-tap confirm button in Gradio.

**Upgrade 3 - Live CPR coaching agent (the goosebumps moment for judges)**

**If someone is in cardiac arrest, Haalat becomes a live CPR instructor - counting compressions, correcting technique, keeping the bystander calm.**

When the Emergency Classifier detects a cardiac or respiratory emergency, a dedicated Live Instruction Agent takes over the conversation. It follows WHO Basic Life Support guidelines (stored in the RAG knowledge base) and delivers step-by-step coaching in real time, asking confirmatory questions after each step. It tracks compression count, reminds the user to switch every 2 minutes, and never loses the thread even if the user types in panic.

**Upgrade 4 - Mass event detection (the most technically impressive feature)**

**When 3+ people in a 1km radius report the same emergency type within 5 minutes, Haalat escalates to mass-event protocol and auto-briefs civil defense.**

The Pattern Detection Agent maintains a sliding time window of all incoming incidents. It checks spatial clustering using coordinate proximity and semantic similarity between emergency descriptions. When a cluster is detected, the Report Generator Agent creates a structured situation report in both Urdu and English and sends it to the relevant district emergency management system. This is the feature that judges will not have seen before.

**Upgrade 5 - City memory that learns from every incident**

**Every anonymized incident is stored. Over time, Haalat knows 'this street floods every monsoon' and 'this building had 3 gas complaints this year' - before the next emergency happens.**

The City Memory RAG database is updated after every incident with anonymized location, type, time, and resolution data. Future queries for the same area retrieve this historical context and factor it into the severity assessment and routing. Over months, Haalat becomes a predictive system, not just a reactive one.

**SECTION 3 - MULTI-AGENT ARCHITECTURE**

**3\. The 7-Agent System**

Haalat is built using CrewAI for agent orchestration. Each agent has a defined role, a specific set of tools, and a knowledge base it queries through LangChain RAG. The agents run in a sequential pipeline with conditional branching based on emergency classification.

| **Agent**                  | **Role**                                                                              | **Tools / Knowledge Base**                                               |
| -------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Language Router**        | Detects language/dialect, wraps all downstream output in the correct vernacular       | LLM inference, language detection prompt, output formatting wrapper      |
| **Emergency Classifier**   | Classifies emergency type and assigns severity score 1-5 with reasoning               | RAG: WHO emergency category taxonomy, Pakistan emergency codes           |
| **Resource Locator**       | Finds nearest hospitals, fire stations, police, ambulances, and registered volunteers | Google Maps API (or mock), volunteer RAG database with coordinates       |
| **Live Instruction Coach** | Delivers real-time step-by-step first aid coaching - CPR, burns, choking, trauma      | RAG: WHO BLS guidelines, Pakistani Red Crescent first aid manual         |
| **Pattern Detector**       | Maintains sliding window of incidents, detects spatial and semantic clustering        | In-memory incident log, coordinate proximity function, time-window logic |
| **Report Generator**       | Generates structured situation reports for authorities in Urdu and English            | LLM with structured output prompt, RAG: civil defense report template    |
| **City Memory**            | Logs anonymized incidents to persistent vector store, enriches future queries         | ChromaDB vector store, LangChain document ingestion, location embeddings |

**3.1 Agent Communication Flow**

The agents run in this order for every incoming message:

- Language Router Agent - runs first, wraps all output in detected language
- Emergency Classifier Agent - determines type and severity from the user message
- Resource Locator Agent - always runs, finds nearest services
- Live Instruction Coach Agent - runs ONLY if severity >= 4 (critical)
- Pattern Detector Agent - runs after classification, checks for clustering
- Report Generator Agent - runs ONLY if mass event is detected
- City Memory Agent - runs last, logs the incident

**In CrewAI, this is implemented as a sequential crew with conditional task execution. Severity score from Agent 2 gates Agents 4 and 6.**

**SECTION 4 - TECHNOLOGY STACK**

**4\. Tech Stack (Only Day 1 Technologies)**

Every technology in this stack was taught on Day 1 of the hackathon. There is nothing here you have not already learned. The implementation uses the exact same patterns from the workshop - prompt engineering, RAG with LangChain, and multi-agent systems with CrewAI, all wrapped in a Gradio UI.

| **Layer**           | **Technology**                    | **Why / What it does**                                                                                                                              |
| ------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LLM**             | **OpenAI GPT-4o-mini**            | The brain of every agent. Used for classification, language detection, coaching, and report generation. Same API from Day 1 prompt engineering lab. |
| **Agent Framework** | **CrewAI**                        | Orchestrates all 7 agents with defined roles, tasks, and sequential execution. Exact same framework from Day 1 multi-agent workshop.                |
| **RAG Pipeline**    | **LangChain + ChromaDB**          | Powers the knowledge bases for emergency protocols, volunteer database, and city memory. Same RAG pipeline from Day 1 LangChain session.            |
| **Embeddings**      | **OpenAI text-embedding-3-small** | Converts documents and queries into vectors for semantic retrieval. Used inside LangChain - no extra setup.                                         |
| **Vector Store**    | **ChromaDB (local)**              | Stores all knowledge base documents and incident logs. Runs locally, no external service needed for the demo.                                       |
| **UI**              | **Gradio**                        | Chat interface for citizens + volunteer alert panel. Exact same Gradio setup from Day 1 UI session.                                                 |
| **Maps / Location** | **Google Maps API (or mock)**     | Finds nearest services by coordinates. Can be mocked with hardcoded Karachi data for the demo if API key unavailable.                               |
| **Language**        | **Python 3.10+**                  | All agents and pipeline code written in Python. Same language used throughout Day 1.                                                                |

**4.1 Required Libraries (pip install)**

pip install crewai langchain langchain-openai chromadb gradio openai python-dotenv

**4.2 Environment Variables (.env file)**

OPENAI_API_KEY=your_openai_key_here

GOOGLE_MAPS_API_KEY=your_maps_key_here # optional, can be mocked

**SECTION 5 - COMPLETE FILE STRUCTURE**

**5\. File & Folder Structure**

Create this exact folder structure. The AI agent building this project should create each file exactly as specified below.

| **File / Folder**                      | **Purpose**                                                                            |
| -------------------------------------- | -------------------------------------------------------------------------------------- |
| haalat/                                | Root project folder                                                                    |
| haalat/.env                            | API keys - never commit to git                                                         |
| haalat/app.py                          | Main entry point - launches Gradio UI and CrewAI crew                                  |
| haalat/agents.py                       | All 7 CrewAI agent definitions with roles and backstories                              |
| haalat/tasks.py                        | All 7 CrewAI task definitions with descriptions and expected outputs                   |
| haalat/tools.py                        | Custom tools: location finder, volunteer alerter, pattern detector, city memory logger |
| haalat/rag/                            | Folder containing all RAG knowledge base setup                                         |
| haalat/rag/knowledge_base.py           | Loads all documents into ChromaDB vector store                                         |
| haalat/rag/retriever.py                | LangChain retriever functions used by agents                                           |
| haalat/data/                           | Folder containing all source documents for RAG                                         |
| haalat/data/emergency_protocols.txt    | WHO BLS guidelines, CPR steps, first aid for burns/choking/trauma                      |
| haalat/data/emergency_categories.txt   | Emergency type taxonomy with severity scoring rules                                    |
| haalat/data/volunteers.json            | Mock volunteer database with name, location, skills, contact                           |
| haalat/data/services.json              | Mock emergency services database (hospitals, fire, police in Karachi)                  |
| haalat/data/civil_defense_template.txt | Situation report template for mass event escalation                                    |
| haalat/incident_log.json               | Persistent incident log updated after every interaction (city memory)                  |
| haalat/requirements.txt                | All pip dependencies                                                                   |

**SECTION 6 - DETAILED CODE SPECIFICATION**

**6\. Code Specification for Each File**

The following specifications are written for an AI agent to implement. Each section describes exactly what a file must contain, what functions to write, and what the expected behavior is.

**6.1 agents.py - Agent Definitions**

Create 7 CrewAI Agent objects. Each agent must have: role, goal, backstory, tools list, and verbose=True.

**Agent 1: language_router_agent**

- role: 'Multilingual Emergency Communication Specialist'
- goal: 'Detect the language of the user input (Urdu, Sindhi, Pashto, or English) and ensure all system responses are delivered in that language with zero jargon.'
- backstory: 'You are a translation and communication expert trained in South Asian languages. You have worked with disaster relief organizations and know that in a crisis, communication in the user's native language can mean the difference between life and death.'
- tools: \[\] (no tools needed - uses LLM directly)

**Agent 2: emergency_classifier_agent**

- role: 'Emergency Triage Specialist'
- goal: 'Classify the emergency type from the user message and assign a severity score from 1 to 5. Score 5 = immediate life threat. Score 1 = non-urgent. Return JSON: {type, severity, reasoning}.'
- backstory: 'You are a trained paramedic with 15 years of experience in emergency triage. You have worked in disaster zones and urban hospitals. You classify emergencies with speed and precision.'
- tools: \[emergency_rag_tool\] - retrieves from emergency_categories.txt

**Agent 3: resource_locator_agent**

- role: 'Emergency Resource Coordinator'
- goal: 'Find the 3 nearest emergency services relevant to the classified emergency type. Find the 3 nearest registered volunteers with relevant skills. Return name, distance, ETA, and contact for each.'
- backstory: 'You are a dispatch coordinator with deep knowledge of Karachi emergency infrastructure. You know every hospital, fire station, and rescue service and can route resources efficiently under pressure.'
- tools: \[location_finder_tool, volunteer_finder_tool\]

**Agent 4: live_instruction_coach_agent**

- role: 'Emergency First Aid Coach'
- goal: 'When severity >= 4, immediately take over the conversation and deliver calm, numbered, step-by-step first aid instructions. After each step, ask a confirmatory question before proceeding. Never skip steps. Use the RAG knowledge base for all protocols.'
- backstory: 'You are a certified first aid instructor trained by the Red Crescent. You have coached hundreds of panicking bystanders through cardiac arrests, burns, and trauma. You are calm, clear, and never waste words.'
- tools: \[protocols_rag_tool\] - retrieves from emergency_protocols.txt
- IMPORTANT: This agent only activates when severity_score >= 4 in the classifier output.

**Agent 5: pattern_detector_agent**

- role: 'Mass Event Intelligence Analyst'
- goal: 'Check the incident log for the last 10 minutes. If 3 or more incidents of the same type exist within 1km of the current location, classify as MASS EVENT and return {is_mass_event: true, cluster_size, incident_type, area_name}. Otherwise return {is_mass_event: false}.'
- backstory: 'You are a data analyst working in civil defense. You monitor emergency patterns across the city and are trained to spot the early signatures of mass casualty events before they overwhelm the response system.'
- tools: \[incident_log_reader_tool, pattern_check_tool\]

**Agent 6: report_generator_agent**

- role: 'Civil Defense Communications Officer'
- goal: 'When a mass event is detected, generate a structured situation report in both Urdu and English. Include: incident type, cluster size, affected area, recommended response level (1-3), and suggested resources to deploy.'
- backstory: 'You have 10 years of experience writing situation reports for NDMA and district emergency management offices. Your reports are concise, actionable, and follow the standard Pakistan civil defense format.'
- tools: \[report_template_rag_tool\] - retrieves from civil_defense_template.txt
- IMPORTANT: This agent only activates when is_mass_event is True from Agent 5.

**Agent 7: city_memory_agent**

- role: 'City Emergency Intelligence Recorder'
- goal: 'Log every incident to the city memory database. Store: timestamp, emergency type, severity, approximate area (not exact address for privacy), resolution status, and volunteer response time if applicable. This log trains the system to predict future emergencies.'
- backstory: 'You are a data steward for the city emergency intelligence system. You treat privacy as sacred and never store personal information - only patterns that can save lives in the future.'
- tools: \[city_memory_logger_tool\]

**6.2 tasks.py - Task Definitions**

Create 7 CrewAI Task objects, one per agent. Each task must specify: description, expected_output, agent (the corresponding agent object).

- Task 1 (language_detection_task): description = 'Analyze this user message and detect its language. Output: {detected_language, confidence}. User message: {user_input}'. expected_output = 'JSON object with detected_language and confidence score.'
- Task 2 (classification_task): description = 'Classify this emergency. User message: {user_input}. Language detected: {detected_language}. Use your RAG knowledge base to identify type and severity. Output JSON: {type, severity, reasoning, immediate_action_summary}'. expected_output = 'JSON with emergency classification.'
- Task 3 (resource_location_task): description = 'Find emergency resources for a {emergency_type} emergency at location {user_location}. Return top 3 services and top 3 volunteers. Format results in {detected_language}.' expected_output = 'Formatted list of services and volunteers with ETAs.'
- Task 4 (coaching_task - conditional): description = 'ONLY run if severity >= 4. Deliver step-by-step first aid for {emergency_type} in {detected_language}. Begin immediately. First line must be the single most urgent action. Ask for confirmation after each step.' expected_output = 'Numbered first aid steps in the detected language.'
- Task 5 (pattern_detection_task): description = 'Read the incident log. Check if there are 3+ {emergency_type} incidents within 1km of {user_location} in the last 10 minutes. Return JSON: {is_mass_event, cluster_size, recommendation}.' expected_output = 'JSON mass event assessment.'
- Task 6 (report_generation_task - conditional): description = 'ONLY run if is_mass_event is True. Generate a civil defense situation report for a {emergency_type} mass event in {area_name} with {cluster_size} confirmed incidents. Write in both Urdu and English.' expected_output = 'Bilingual situation report following civil defense format.'
- Task 7 (memory_logging_task): description = 'Log this incident to city memory: type={emergency_type}, severity={severity}, area={approximate_area}, timestamp={now}. Do not log any personally identifiable information.' expected_output = 'Confirmation that incident was logged.'

**6.3 tools.py - Custom Tool Definitions**

Create these 6 custom tools using LangChain's @tool decorator or CrewAI's tool system:

**Tool 1: emergency_rag_tool**

Loads emergency_categories.txt into ChromaDB. When queried with an emergency description, returns the top 3 matching emergency categories with their standard severity scores. Used by: emergency_classifier_agent.

**Tool 2: protocols_rag_tool**

Loads emergency_protocols.txt into ChromaDB. When queried with an emergency type (e.g. 'cardiac arrest', 'severe burn'), returns the complete first aid protocol for that emergency. Protocols must include numbered steps, contraindications, and when to stop. Used by: live_instruction_coach_agent.

**Tool 3: location_finder_tool**

Accepts: emergency_type (string), user_location (string or coordinates). Queries services.json to find the 3 nearest relevant services. If Google Maps API key is set, calculates real distances. If not, uses mock distance from services.json. Returns: list of {name, type, distance_km, eta_minutes, phone}. Used by: resource_locator_agent.

**Tool 4: volunteer_finder_tool**

Accepts: emergency_type (string), user_location (string). Queries volunteers.json. Filters by skill relevance to emergency type (e.g. 'CPR certified' for cardiac). Returns 3 nearest matching volunteers with {name, skills, distance_m, phone, availability_status}. Used by: resource_locator_agent.

**Tool 5: pattern_check_tool**

Reads incident_log.json. Filters incidents within the last 10 minutes. Groups by emergency_type. Checks if any group has 3+ entries with coordinates within 1km radius of each other (use simple bounding box for demo: +/- 0.009 degrees lat/long = approx 1km). Returns: {is_cluster: bool, cluster_type, cluster_size, area_center}. Used by: pattern_detector_agent.

**Tool 6: city_memory_logger_tool**

Accepts: incident object with type, severity, area, timestamp. Appends to incident_log.json. Also embeds the incident into ChromaDB city memory collection for future semantic retrieval. Never stores exact address, name, or phone number - only area name (e.g. 'Garden, Karachi'), type, and severity. Used by: city_memory_agent.

**6.4 rag/knowledge_base.py - RAG Setup**

This file initializes all ChromaDB collections on startup. It must:

- Load emergency_protocols.txt using LangChain TextLoader
- Split into chunks using RecursiveCharacterTextSplitter (chunk_size=500, overlap=50)
- Embed using OpenAIEmbeddings (text-embedding-3-small)
- Store in ChromaDB collection named 'emergency_protocols'
- Repeat the same for emergency_categories.txt → collection: 'emergency_categories'
- Repeat for civil_defense_template.txt → collection: 'report_templates'
- Create an empty collection named 'city_memory' for incident logging
- Check if collections already exist before re-creating them (add skip logic)

**6.5 app.py - Main Application**

The main file ties everything together. It must:

- Import all agents from agents.py and all tasks from tasks.py
- Create a CrewAI Crew with all 7 agents, all 7 tasks, and process='sequential'
- Define a respond(user_message, chat_history) function that: extracts a mock location from the message OR defaults to 'Karachi, Pakistan', runs the crew with user_message and user_location as inputs, parses the final output, and returns it formatted for Gradio
- Build a Gradio Blocks UI with two tabs:

Tab 1 - 'Emergency Chat': A chatbot component where the citizen types their emergency. Input textbox. Submit button. The chat response shows: severity badge (color coded), nearest services, volunteer alerts, first aid steps if severity >= 4, mass event warning if detected.

Tab 2 - 'Volunteer Dashboard': A table showing the last 5 incidents logged to city memory (anonymized). An 'Active Volunteer Alerts' section showing which volunteers were notified for each incident.

- Launch with gr.launch(share=True) so the judge can see it on their phone

**SECTION 7 - DATA FILES TO CREATE**

**7\. Data Files Specification**

The AI agent building this project must create all data files below. These are the knowledge bases that power the RAG system.

**7.1 data/emergency_protocols.txt**

This file must contain detailed first aid protocols for the following emergency types. Write 200-300 words per protocol. Include numbered steps, what NOT to do, and when to call for help. Protocols to include:

- Cardiac arrest / heart attack - full CPR protocol with compression rate, depth, rescue breaths ratio, AED use
- Choking (adult) - Heimlich maneuver steps, back blows, unconscious victim protocol
- Severe bleeding - direct pressure, tourniquet use, shock prevention
- Burns (thermal) - cool water, do not pop blisters, cover protocol, when to go to ER
- Road accident trauma - scene safety, moving victim rules, spinal precautions
- Heat stroke - cooling protocol, hydration, when it becomes life-threatening
- Fainting / unconsciousness - recovery position, pulse check, airway management
- Drowning - rescue, CPR modification for drowning victim
- Seizure - do not restrain, safe positioning, post-seizure care
- Allergic reaction / anaphylaxis - epinephrine use, positioning, monitoring

**7.2 data/emergency_categories.txt**

This file must contain the emergency classification taxonomy. Format each category as:

CATEGORY: \[name\]

SEVERITY: \[1-5\]

KEYWORDS: \[list of trigger words in English and Urdu transliteration\]

DESCRIPTION: \[what this emergency looks like\]

FIRST_RESPONSE: \[single most important first action\]

Include these categories: Cardiac Event, Respiratory Emergency, Severe Bleeding, Burns, Road Accident, Drowning, Poisoning, Fire, Gas Leak, Building Collapse, Violence / Assault, Mental Health Crisis, Diabetic Emergency, Stroke, Childbirth Emergency.

**7.3 data/volunteers.json**

Create a JSON array of 20 mock volunteers in Karachi. Each volunteer object must have:

{ "id": "V001", "name": "Dr. Ayesha Siddiqui", "skills": \["CPR", "trauma", "pediatrics"\],

"lat": 24.8607, "lng": 67.0011, "area": "Garden", "phone": "0300-0000001",

"availability": "always", "response_time_minutes": 3 }

Spread volunteers across: Garden, Clifton, Saddar, Gulshan, North Nazimabad, Korangi, Malir, PECHS, DHA, Lyari.

**7.4 data/services.json**

Create a JSON array of 15 emergency services in Karachi. Each object must have:

{ "id": "S001", "name": "Aga Khan Hospital", "type": "hospital",

"lat": 24.8615, "lng": 67.0632, "phone": "021-111-911-911",

"services": \["trauma", "cardiac", "burns", "pediatric ER"\], "24hr": true }

Include: 5 hospitals, 3 Edhi Foundation ambulance stations, 2 Rescue 1122 stations, 2 fire stations, 2 police emergency posts, 1 poison control center.

**SECTION 8 - DEMO SCRIPT FOR JUDGES**

**8\. Exactly What to Demo (3-5 Minutes)**

Practice this script. Do not wing it. Judges have seen 20 projects today - yours needs a moment that makes them put their phones down.

**Demo Sequence (4 minutes)**

**Step 1 - Open with the problem statement (30 seconds)**

Say: 'In Karachi, the average ambulance takes 8 minutes. But brain damage in cardiac arrest starts at 4 minutes. That 4-minute gap is where people die - not from lack of hospitals, but from lack of coordination. We built Haalat to close that gap.'

**Step 2 - The Urdu demo (60 seconds) - this is the moment**

Type into the Gradio chat (do NOT use English): 'mere baap ko dil ka dorah para hai, woh gir gaye hain - main Garden mein hoon'

Translation: 'My father is having a heart attack, he has fallen - I am in Garden'

The system responds with: CARDIAC EVENT - SEVERITY 5. Aga Khan Hospital alerted (2.1km, ETA 7 min). Dr. Ayesha (volunteer, 340m) notified. Then it begins: 'Step 1: Lay him flat. Tilt his chin back. Is he breathing?'

PAUSE. Let the judges read it. Then say: 'This conversation just happened in Urdu. No language selection. No form. The system detected the language and the emergency simultaneously.'

**Step 3 - Mass event demo (60 seconds) - the technical wow**

Send 3 more messages in quick succession: 'gas ki smell aa rahi hai yahan pe' (x3 from different 'users'). The Pattern Detector fires. Show the mass event alert and the auto-generated situation report. Say: 'Three people reported gas leaks within 500 meters in 2 minutes. Haalat classified it as a mass event and auto-generated a civil defense brief - in both Urdu and English. No human dispatcher made that call.'

**Step 4 - Volunteer dashboard (30 seconds)**

Switch to Tab 2. Show the incident log and volunteer alerts. Say: 'Every incident is logged anonymously into a city memory database. Over time, Haalat learns where emergencies cluster, when they spike, and which areas need more volunteers. It goes from reactive to predictive.'

**Step 5 - The closing line (30 seconds) - memorize this**

Say: 'Every emergency response tool in the world assumes there is already a functioning emergency system to connect you to. Pakistan doesn't always have that. Haalat doesn't wait for the state - it mobilizes the community. It turns every bystander into a first responder. At zero marginal cost. For 220 million people.'

Then be quiet. Let it land.

**SECTION 9 - HOW THIS SCORES ON EVERY JUDGING CRITERION**

**9\. Judging Criteria Mapping**

| **Judging Criterion**        | **What Haalat Demonstrates**                                                                                                                                          | **Score Potential**                                               |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Technical Implementation** | 7 agents with conditional branching, RAG across 3 knowledge bases, persistent vector store, custom tools, multi-language pipeline - all built in 4 hours              | Maximum - judges will not see another team with this architecture |
| **Innovation**               | First system to combine bystander mobilization + live coaching + mass event detection + multilingual input in one pipeline. No comparable product exists in Pakistan. | Maximum - genuinely unprecedented combination                     |
| **Real-World Relevance**     | Directly addresses Pakistan's emergency response gap. Demo works in Urdu. Volunteers, hospitals, and services are real Karachi data. Numbers cited are verifiable.    | Maximum - judges from Pakistan will feel it personally            |
| **Presentation**             | Scripted demo with a goosebumps moment (Urdu CPR coaching), a technical flex (mass event detection), and a memorable closing line. 4-minute flow.                     | Maximum - if you practice the script                              |

**SECTION 10 - 4-HOUR HACKATHON BUILD TIMELINE**

**10\. Build Timeline (Hackathon Day)**

Assign one person per workstream. If team is 2 people, combine Agent Dev + Data/RAG.

| **Time**    | **Milestone**             | **What to Build**                                                                                                                                                                              | **Owner** |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 10:20-11:00 | **Foundation**            | Create folder structure. Set up .env. Create all data files (emergency_protocols.txt, categories, volunteers.json, services.json). Initialize ChromaDB and test embeddings.                    | Person A  |
| 10:20-11:00 | **Agent skeleton**        | Write agents.py with all 7 agent stubs. Write tasks.py with all 7 task stubs. Test that CrewAI crew initializes without errors.                                                                | Person B  |
| 11:00-12:00 | **Core pipeline**         | Implement tools.py - start with emergency_rag_tool and location_finder_tool. Connect to agents. Test: type 'heart attack' → classifier returns severity 5 → location finder returns hospitals. | Person A  |
| 11:00-12:00 | **CPR coaching loop**     | Implement live_instruction_coach_agent fully. Test multi-turn conversation for cardiac arrest. Implement Urdu output by modifying the language router prompt.                                  | Person B  |
| 12:00-13:00 | **Lunch break**           | Rest. Do not code. You need fresh eyes for the Gradio UI.                                                                                                                                      | Both      |
| 13:00-14:00 | **Gradio UI**             | Build app.py with both tabs. Test the full flow end to end with the Gradio interface. Fix any CrewAI crew execution errors.                                                                    | Person A  |
| 13:00-14:00 | **Mass event + memory**   | Implement pattern_check_tool and city_memory_logger_tool. Seed incident_log.json with 2 fake incidents so mass event triggers on the 3rd demo message.                                         | Person B  |
| 14:00-14:30 | **Polish and test**       | Run the exact demo script 3 times. Fix any bugs. Ensure Urdu input → Urdu output works. Test gr.launch(share=True) and verify phone access.                                                    | Both      |
| 14:30-15:00 | **Rehearse presentation** | Practice the 4-minute demo script from Section 8. Time it. The closing line must be delivered without looking at notes.                                                                        | Both      |

**SECTION 11 - AI AGENT SYSTEM PROMPT**

**11\. System Prompt for the AI Agent That Will Build This**

Copy this entire prompt and paste it to your AI coding agent (Claude, GPT-4, Cursor, etc.) to have it build the full application automatically.

**PASTE THE FOLLOWING AS YOUR AI AGENT'S SYSTEM PROMPT / FIRST MESSAGE**

You are a senior Python developer. Build the complete Haalat emergency response application exactly as specified. Do the following in order:  
1\. Create the folder structure: haalat/ with all subfolders  
2\. Create .env file with placeholder API keys  
3\. Create requirements.txt with: crewai langchain langchain-openai chromadb gradio openai python-dotenv  
4\. Create all data files: emergency_protocols.txt (full first aid protocols for 10 emergencies in English), emergency_categories.txt (15 categories with severity scores and Urdu keywords), volunteers.json (20 mock Karachi volunteers), services.json (15 Karachi emergency services), civil_defense_template.txt (bilingual situation report template)  
5\. Create rag/knowledge_base.py: loads all txt files into ChromaDB collections using LangChain TextLoader and RecursiveCharacterTextSplitter. Uses OpenAIEmbeddings. Checks if collection exists before re-creating.  
6\. Create rag/retriever.py: LangChain retriever functions that query each ChromaDB collection.  
7\. Create tools.py with 6 tools: emergency_rag_tool, protocols_rag_tool, location_finder_tool (reads services.json, mock distances), volunteer_finder_tool (reads volunteers.json, skill matching), pattern_check_tool (reads incident_log.json, bounding box proximity check), city_memory_logger_tool (appends to incident_log.json)  
8\. Create agents.py with all 7 CrewAI agents as specified in Section 6.1. Each agent must have role, goal, backstory, and tools.  
9\. Create tasks.py with all 7 tasks. Implement conditional execution: coaching task only if severity >= 4, report task only if is_mass_event is True.  
10\. Create app.py: Gradio Blocks UI with 2 tabs (Emergency Chat and Volunteer Dashboard). The chat tab shows severity badge, services, volunteer alerts, first aid steps, and mass event warning. The dashboard tab shows anonymized incident log. Launch with share=True.  
11\. Create an empty incident_log.json: \[\] to initialize city memory.  
12\. Seed incident_log.json with 2 fake gas leak incidents at Karachi Garden coordinates so the 3rd gas leak in the demo triggers the mass event detection.  
13\. After all files are created, provide exact terminal commands to install dependencies and run the app.  
<br/>Use GPT-4o-mini as the LLM. All text displayed in the UI should adapt to the detected language. The demo must work with only an OpenAI API key - all other integrations (maps, volunteer alerts) use the mock JSON data.

**Good luck. You are building something that could save a life. Build it like it matters - because it does.**

**HAALAT - حالت**

_Emergency Intelligence. Community Mobilization. City Memory._
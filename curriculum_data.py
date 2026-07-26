"""Sixteen-week academy curriculum with Git readiness first, dedicated AI tooling, and five classroom project plans."""

PROGRAM_WEEKS = [(1,
  'Developer Workflow',
  'Git and GitHub Foundations',
  'Version control concepts, repositories, working tree, staging area, commits, history, branches, merging, '
  'safe undo operations, .gitignore, GitHub accounts, remotes, and secure repository practices.',
  'Why source control is essential for Salesforce developers and how Git differs from GitHub.',
  'My first professional Git workflow: what a clean commit history communicates.'),
 (2,
  'Developer Workflow',
  'Collaborative GitHub Workflow in VS Code and Salesforce DX',
  'Cloning a classroom repository, Salesforce DX project structure, VS Code Source Control, branch naming, '
  'push and pull, pull requests, peer review, merge conflicts, synchronizing main, Salesforce CLI '
  'authentication, and source-driven development.',
  'How branches, pull requests, reviews, and protected main branches reduce risk in team-based Salesforce '
  'development.',
  'Why I will never develop directly on main: the GitHub workflow I practiced.'),
 (3,
  'Foundation',
  'Discovery, Requirements, and Salesforce Architecture',
  'Business process discovery, personas, user stories, acceptance criteria, Salesforce architecture, '
  'multitenancy, metadata versus data, org strategy, and solution boundaries.',
  'How Salesforce multitenancy and metadata-driven architecture affect solution design.',
  'A strong Salesforce application begins with business discovery, not configuration.'),
 (4,
  'Foundation',
  'Data Modeling and Relationship Design',
  'Standard and custom objects, lookup and master-detail relationships, junction objects, external IDs, '
  'ownership, roll-up summaries, data-volume considerations, and schema documentation.',
  'Lookup versus master-detail relationships and their effects on ownership, deletion, sharing, reporting, '
  'and roll-ups.',
  'The data-model decision that can shape an entire Salesforce application.'),
 (5,
  'Foundation',
  'Data Quality and User Experience',
  'Validation rules, formulas, duplicate prevention, matching rules, record types, Dynamic Forms, required '
  'data, conditional visibility, and user-friendly error messages.',
  'How data-quality controls should be divided among validation rules, duplicate rules, Flow, and Apex.',
  'Good Salesforce data quality is designed into the application.'),
 (6,
  'Foundation',
  'Security and Access Control',
  'Profiles, permission sets, permission set groups, organization-wide defaults, role hierarchy, sharing '
  'rules, field-level security, record access, least privilege, and security testing.',
  'How Salesforce object, field, and record security layers work together.',
  'Salesforce security is not controlled by one setting.'),
 (7,
  'Automation',
  'Flow and Declarative Automation',
  'Before-save Flow, after-save Flow, screen Flow, scheduled Flow, subflows, fault handling, order of '
  'execution, recursion, automation selection, and maintainability.',
  'Flow versus Apex and how to choose the correct automation layer.',
  'Not every Salesforce automation requires Apex.'),
 (8,
  'Development',
  'Apex Services and Object-Oriented Design',
  'Apex syntax, collections, classes, interfaces, exceptions, null handling, domain logic, service classes, '
  'separation of responsibilities, and maintainable design.',
  'Object-oriented programming in Apex and why service boundaries matter.',
  'Apex is more than syntax.'),
 (9,
  'Development',
  'SOQL, SOSL, Triggers, and Transaction Architecture',
  'Relationship and aggregate queries, search, selectivity, indexes, governor limits, trigger contexts, '
  'bulkification, handler classes, recursion control, savepoints, rollback, and transaction boundaries.',
  'How selective data access and bulk-safe transaction architecture work together in Salesforce.',
  'Efficient queries and bulk-safe triggers must be designed together.'),
 (10,
  'Quality and Security',
  'Secure Apex and Automated Testing',
  'Sharing declarations, user mode, CRUD, field-level security, injection prevention, input validation, '
  'test-data factories, @TestSetup, behavior tests, bulk tests, permission tests, asynchronous tests, '
  'callout mocks, assertions, and meaningful coverage.',
  'How permission-aware code and behavior-focused tests reduce production risk.',
  'Secure Apex needs tests that prove what limited users can and cannot do.'),
 (11,
  'Integration',
  'Asynchronous Processing and Real Integrations',
  'Queueable Apex, Batch Apex, Platform Events, scheduled processing, live REST callouts, JSON, Named '
  'Credentials, External Credentials, idempotency, retries, logging, monitoring, recovery, and '
  'HttpCalloutMock for tests only.',
  'Queueable Apex versus Batch Apex versus Platform Events, and why live callouts still require '
  'deterministic mocked tests.',
  'A real integration call and a mocked unit test solve two different problems.'),
 (12,
  'Experience',
  'Lightning Web Components Fundamentals',
  'HTML, CSS, modern JavaScript, modules, promises, async and await, LWC structure, reactivity, events, base '
  'components, SLDS, accessibility, and responsive design.',
  'How Lightning Web Components use modern web standards.',
  'Learning LWC also means learning modern JavaScript.'),
 (13,
  'Experience',
  'Advanced LWC and Application Workspace',
  'Lightning Data Service, UI Record API, wire service, imperative Apex, component communication, Lightning '
  'Message Service, caching, file upload, custom data tables, search, accessibility, and performance.',
  'Lightning Data Service versus custom Apex and how performance and accessibility affect component design.',
  'A component is not complete merely because it works.'),
 (14,
  'AI Development',
  'Claude AI and Salesforce CLI Development Workflow',
  'Claude Code installation and authentication, safe repository context, project instructions, plan mode, '
  'bounded tasks, prompt and context design, human review, hallucination detection, Salesforce CLI commands, '
  'org authentication, source retrieval, tests, Code Analyzer, deployment validation, and audit evidence.',
  'Where Claude AI improves Salesforce development, where deterministic Salesforce CLI commands are safer, '
  'and how developers verify every AI-generated change.',
  'My rules for using Claude AI without surrendering engineering responsibility.'),
 (15,
  'AI Tooling',
  'MCP Servers, Secure Tool Use, and Agent Skills',
  'Model Context Protocol clients and servers, tools, resources, prompts, transport, authentication, '
  'project-scoped configuration, Salesforce DX MCP, Salesforce Hosted MCP Servers, least privilege, '
  'read-only-first access, human approval, audit logs, CLI versus MCP, reusable agent skills, and '
  'tool-output verification.',
  'How MCP tools, resources, and prompts differ from APIs and CLI commands, and how least privilege and '
  'human approval reduce agent risk.',
  'MCP is a connector, not a permission bypass: the secure tool workflow I designed.'),
 (16,
  'AI and Agents',
  'Agentforce, AI Governance, and Final Production Demonstration',
  'Agentforce instructions, grounding, actions, Flow and Apex actions, Agent Script, guardrails, '
  'prompt-injection testing, permissions, monitoring, human escalation, release validation, documentation, '
  'final integration, and stakeholder demonstration.',
  'Designing secure and reliable Salesforce agents with grounding, authorization boundaries, guardrails, '
  'monitoring, and human escalation.',
  'A production Salesforce agent needs evidence, limits, and accountable human ownership.')]

PROJECTS = [{'number': 1,
  'industry': 'Warehouse & Logistics',
  'title': 'Warehouse Management & Logistics App',
  'summary': 'A complete warehouse operations workspace for receiving, putaway, inventory control, picking, '
             'packing, shipping, and delivery exceptions.',
  'entities': 'Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event',
  'personas': 'Warehouse Associate, Inventory Controller, Logistics Coordinator, Operations Manager',
  'process': 'receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
             'handling',
  'integration': 'postal-code validation and delivery-location enrichment',
  'integration_name': 'Zippopotam.us Postal Code API',
  'integration_base_url': 'https://api.zippopotam.us',
  'integration_docs_url': 'https://www.zippopotam.us/',
  'integration_auth': 'No authentication for the training endpoint',
  'integration_operation': 'send a shipment country code and postal code to the live API, receive city, '
                           'state, latitude, and longitude, and store the validated destination on the '
                           'Shipment',
  'integration_path': '/us/{postal-code}',
  'workspace': 'warehouse control tower with receiving queues, bin availability, pick waves, shipment '
               'readiness, and exceptions',
  'agent': 'warehouse operations assistant that summarizes inventory risk, identifies blocked shipments, '
           'invokes approved replenishment or task actions, and escalates operational decisions',
  'accent': 'finance'},
 {'number': 2,
  'industry': 'Healthcare',
  'title': 'Patient Referral & Care Coordination App',
  'summary': 'A referral and care-coordination workspace for patients, providers, eligibility, '
             'authorizations, care tasks, and follow-up.',
  'entities': 'Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, '
              'Follow-Up',
  'personas': 'Referral Coordinator, Care Coordinator, Clinical Reviewer, Program Administrator',
  'process': 'referral intake, provider validation, eligibility review, authorization, care assignment, '
             'appointment coordination, and follow-up',
  'integration': 'public provider identity validation',
  'integration_name': 'CMS NPI Registry API',
  'integration_base_url': 'https://npiregistry.cms.hhs.gov/api',
  'integration_docs_url': 'https://npiregistry.cms.hhs.gov/api-page',
  'integration_auth': 'No authentication; use training provider identifiers only',
  'integration_operation': 'send a training provider NPI or search criteria to the live CMS registry, '
                           'receive provider identity and practice-location data, and update the Provider '
                           'validation fields',
  'integration_path': '/?version=2.1&number={npi}',
  'workspace': 'care-coordination workbench with patient context, referral status, provider validation, '
               'missing information, and next actions',
  'agent': 'care-coordination assistant that summarizes referrals, identifies missing data, recommends '
           'approved next steps, and escalates clinical decisions',
  'accent': 'healthcare'},
 {'number': 3,
  'industry': 'Nonprofit',
  'title': 'Donor & Volunteer Engagement App',
  'summary': 'An engagement platform for donors, donations, campaigns, volunteers, shifts, acknowledgements, '
             'and outreach.',
  'entities': 'Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, '
              'Engagement Score',
  'personas': 'Fundraising Coordinator, Volunteer Manager, Program Manager, Nonprofit Administrator',
  'process': 'donor engagement, donation processing, volunteer registration, shift assignment, '
             'acknowledgement, and outreach follow-up',
  'integration': 'real address geocoding for outreach planning',
  'integration_name': 'US Census Geocoding Services',
  'integration_base_url': 'https://geocoding.geo.census.gov/geocoder',
  'integration_docs_url': 'https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html',
  'integration_auth': 'No authentication; use fictional training addresses only',
  'integration_operation': 'send a fictional outreach address to the live Census geocoder, receive matched '
                           'address and coordinates, and store the standardized location for outreach '
                           'planning',
  'integration_path': '/geographies/onelineaddress?address={encoded-address}&benchmark=Public_AR_Current&vintage=Current_Current&format=json',
  'workspace': 'engagement dashboard with campaign results, donor history, volunteer availability, mapped '
               'outreach locations, and required follow-up',
  'agent': 'engagement assistant that summarizes donor and volunteer activity, identifies follow-up '
           'opportunities, drafts approved communications, and escalates sensitive outreach',
  'accent': 'nonprofit'},
 {'number': 4,
  'industry': 'Manufacturing',
  'title': 'Production & Quality Operations App',
  'summary': 'A manufacturing workspace for production orders, work centers, material requirements, quality '
             'inspections, downtime, and finished-goods release.',
  'entities': 'Plant, Work Center, Production Order, Material Requirement, Production Run, Quality '
              'Inspection, Downtime Event, Finished Good',
  'personas': 'Production Planner, Line Supervisor, Quality Inspector, Plant Manager',
  'process': 'production planning, material readiness, work-center scheduling, execution, quality '
             'inspection, downtime response, and finished-goods release',
  'integration': 'live manufacturer information lookup',
  'integration_name': 'NHTSA vPIC API',
  'integration_base_url': 'https://vpic.nhtsa.dot.gov/api',
  'integration_docs_url': 'https://vpic.nhtsa.dot.gov/api/',
  'integration_auth': 'No authentication for public endpoints',
  'integration_operation': 'send a manufacturer name or identifier to the live NHTSA vPIC API, receive '
                           'manufacturer details, and enrich the Supplier or Manufacturer record used by the '
                           'production plan',
  'integration_path': '/vehicles/getallmanufacturers?format=json',
  'workspace': 'production control board with material readiness, work-center schedule, quality holds, '
               'downtime events, and release actions',
  'agent': 'production operations assistant that summarizes schedule risk, material shortages, quality '
           'holds, and downtime, invokes approved task actions, and escalates release decisions',
  'accent': 'manufacturing'},
 {'number': 5,
  'industry': 'Professional Services',
  'title': 'AI-Enabled Client Delivery App',
  'summary': 'A client-delivery workspace for projects, milestones, resource assignments, time, risks, '
             'deliverables, and AI-assisted coordination.',
  'entities': 'Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update',
  'personas': 'Consultant, Project Manager, Delivery Director, Services Administrator',
  'process': 'project intake, milestone planning, resource assignment, time tracking, risk management, '
             'deliverable approval, and client communication',
  'integration': 'real software-delivery activity synchronization',
  'integration_name': 'GitHub REST API',
  'integration_base_url': 'https://api.github.com',
  'integration_docs_url': 'https://docs.github.com/en/rest',
  'integration_auth': 'No authentication for a public training repository, or instructor-provided token '
                      'through an External Credential for higher limits',
  'integration_operation': 'call a live public training repository endpoint, receive issues or milestones, '
                           'and create or update corresponding Project Risks and Milestones in Salesforce',
  'integration_path': '/repos/{owner}/{repository}/issues',
  'workspace': 'delivery workbench with milestone health, resource allocation, risks, deliverables, and '
               'client-update actions',
  'agent': 'client-delivery assistant that summarizes project health, identifies risks and missing updates, '
           'invokes approved actions, and escalates commercial or delivery decisions',
  'accent': 'services'}]

PROJECT_MILESTONES = {1: [{'week_number': 1,
      'title': 'Master Git fundamentals in VS Code',
      'instructions': 'Before changing the classroom Salesforce application, every student completes an '
                      'individual Git foundations lab. Create a personal practice repository, configure Git, '
                      'use the working tree and staging area correctly, make meaningful commits, inspect '
                      'history, create and merge a branch, undo changes safely, and publish the repository '
                      'to GitHub.',
      'deliverable': 'A personal Git Foundations Portfolio repository URL containing README.md, '
                     'learning-log.md, profile.md, .gitignore, at least five meaningful commits, one merged '
                     'branch, a clean git status, and the required screenshots and command output.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Complete the classroom GitHub and Salesforce DX workflow',
      'instructions': 'Use the classroom repository for the Warehouse Management & Logistics App, but do not '
                      'build industry functionality yet. Clone the Salesforce DX repository in VS Code, '
                      'inspect the source structure, authenticate the training org, create a student feature '
                      'branch, make a safe documentation change, push it, open a pull request, review a peer '
                      'pull request, apply feedback, resolve a controlled merge conflict, merge, and '
                      'synchronize local main.',
      'deliverable': 'A pull-request URL, peer-review evidence, merge-conflict resolution evidence, clean '
                     'final git status, synchronized main branch, and a short workflow explanation showing '
                     'clone, branch, commit, push, pull request, review, merge, and pull.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Translate the classroom project into personas, user journeys, user stories, '
                      'acceptance criteria, success measures, scope boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, '
                     'acceptance criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Design the application data model',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Create the standard and custom object model, relationships, ownership '
                      'strategy, external IDs, reporting considerations, and a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample '
                     'records, and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Add validation, formulas, duplicate prevention, record types, conditional '
                      'visibility, required-data controls, and user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, '
                     'and a data-quality decision log.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Configure persona-based security',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Design access for Warehouse Associate, Inventory Controller, Logistics '
                      'Coordinator, Operations Manager. Create least-privilege access for the project '
                      'personas using permission sets, permission set groups, sharing, field-level security, '
                      'and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, '
                     'and documented exceptions.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Automate the core business process',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Build declarative automation for the end-to-end process using before-save, '
                      'after-save, screen, scheduled, and reusable Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, '
                     'and an end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Build the Apex service layer',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Create maintainable Apex domain and service classes for business rules that '
                      'should not live entirely in Flow. Validate inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design '
                     'rationale, and unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Build data access and transaction architecture',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Implement selective SOQL, relationship queries, aggregates, search, and '
                      'data-access utilities for operational views, missing-data detection, and reporting. '
                      'Then for the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, '
                      'Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support '
                      'receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and '
                      'exception handling. Add bulk-safe trigger and handler logic for status changes, '
                      'related-record coordination, duplicate prevention, and transaction-safe updates.',
      'deliverable': 'Selector and search classes, selective and aggregate query evidence, a thin trigger '
                     'and handler, bulkification and recursion controls, transaction-safety reasoning, '
                     '200-record tests, analyzer results, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Secure the codebase and automate testing',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Review the service and data-access layers for sharing, user mode, CRUD, '
                      'field-level security, secure dynamic SOQL, validation, and sensitive-data exposure. '
                      'Then create a complete automated test framework with permission-aware, '
                      'behavior-focused, bulk, asynchronous, and failure-path tests.',
      'deliverable': 'Security review worksheet, corrected permission-aware code, test-data factory, '
                     'low-permission tests, bulk and asynchronous tests, Code Analyzer results, coverage '
                     'report, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. Connect to the live Zippopotam.us Postal Code API at '
                      'https://api.zippopotam.us using a Named Credential. The classroom operation is to '
                      'send a shipment country code and postal code to the live API, receive city, state, '
                      'latitude, and longitude, and store the validated destination on the Shipment. Use '
                      'training data only. Configure a Named Credential and External Credential, execute a '
                      'genuine training callout, map the live response into Salesforce, and use '
                      'HttpCalloutMock only inside automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped '
                     'Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and '
                     'recovery demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. The primary experience is a warehouse control tower with receiving queues, '
                      'bin availability, pick waves, shipment readiness, and exceptions. Build the '
                      'application main user workspace with modern JavaScript, accessible Lightning '
                      'components, clear loading and error states, and responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility '
                     'notes, and stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, '
                      'Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, '
                      'putaway, cycle counting, replenishment, picking, packing, shipping, and exception '
                      'handling. The primary experience is a warehouse control tower with receiving queues, '
                      'bin availability, pick waves, shipment readiness, and exceptions. Extend the '
                      'workspace with communicating components, Lightning Data Service or Apex data access, '
                      'search, filtering, files, reusable utilities, caching, and performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, '
                     'performance notes, and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Use Claude AI and Salesforce CLI safely',
      'instructions': 'For the Warehouse Management & Logistics App, use Claude Code only inside the '
                      'classroom repository and training org. Create project instructions that describe the '
                      'Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier '
                      'Event model, the receiving, putaway, cycle counting, replenishment, picking, packing, '
                      'shipping, and exception handling process, naming rules, security requirements, '
                      'allowed files, prohibited actions, required tests, and approved Salesforce CLI '
                      'commands. Use plan mode before edits, complete one bounded implementation or '
                      'test-improvement task, inspect every proposed change, and use deterministic '
                      'Salesforce CLI commands to display the org, retrieve source, run Apex tests, run Code '
                      'Analyzer, and validate deployment. Correct hallucinations, insecure code, unnecessary '
                      'changes, and failed commands before committing anything.',
      'deliverable': 'Claude Code installation and health-check evidence, redacted session transcript, '
                     'project CLAUDE.md or approved instruction file, bounded task brief, approved plan, '
                     'reviewed and corrected diff, Salesforce CLI outputs, Apex test results, Code Analyzer '
                     'report, deployment-validation result, pull request, and AI review log.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Connect Claude through MCP with least privilege',
      'instructions': 'For the Warehouse Management & Logistics App, map the MCP client, approved servers, '
                      'tools, resources, prompts, authentication, and data boundaries. Configure only '
                      'instructor-approved project-scoped MCP connections. Start with repository and '
                      'Salesforce read-only tools, inspect the available tool schemas, and compare each MCP '
                      'action with the equivalent direct Salesforce CLI or API operation. Run a read-only '
                      'workflow that analyzes the receiving, putaway, cycle counting, replenishment, '
                      'picking, packing, shipping, and exception handling implementation, then complete one '
                      'narrowly approved write or execution workflow with explicit human confirmation. '
                      'Create a reusable agent skill or instruction, preserve logs, test denied and failure '
                      'cases, and disable unnecessary tools after the exercise.',
      'deliverable': 'MCP architecture diagram, redacted project-scoped configuration, server and tool '
                     'inventory, least-privilege matrix, read-only workflow evidence, one human-approved '
                     'controlled action, CLI-versus-MCP comparison, skill or instruction file, audit log, '
                     'failure tests, security review, and reviewed pull request.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the governed Agentforce application',
      'instructions': 'For the Warehouse Management & Logistics App, complete the full application and the '
                      'approved agent use case: warehouse operations assistant that summarizes inventory '
                      'risk, identifies blocked shipments, invokes approved replenishment or task actions, '
                      'and escalates operational decisions. Integrate the verified Claude and CLI workflow '
                      'from Week 14 and the governed MCP workflow from Week 15 into the final engineering '
                      'evidence. Build or configure Agentforce with narrow actions, grounded data, '
                      'permission-aware execution, confirmation for state changes, prompt-injection '
                      'resistance, monitoring, and human escalation. Run final application, agent, security, '
                      'integration, deployment, and rollback tests, then deliver the production-style '
                      'classroom demonstration.',
      'deliverable': 'The complete deployed application, Agentforce configuration, authorization matrix, '
                     'guardrail and prompt-injection tests, monitoring and escalation plan, final Code '
                     'Analyzer and validation results, Claude and MCP governance evidence, architecture '
                     'documentation, user and administrator guides, Git repository, and final classroom '
                     'demonstration.',
      'is_final': 1}],
 2: [{'week_number': 1,
      'title': 'Master Git fundamentals in VS Code',
      'instructions': 'Before changing the classroom Salesforce application, every student completes an '
                      'individual Git foundations lab. Create a personal practice repository, configure Git, '
                      'use the working tree and staging area correctly, make meaningful commits, inspect '
                      'history, create and merge a branch, undo changes safely, and publish the repository '
                      'to GitHub.',
      'deliverable': 'A personal Git Foundations Portfolio repository URL containing README.md, '
                     'learning-log.md, profile.md, .gitignore, at least five meaningful commits, one merged '
                     'branch, a clean git status, and the required screenshots and command output.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Complete the classroom GitHub and Salesforce DX workflow',
      'instructions': 'Use the classroom repository for the Patient Referral & Care Coordination App, but do '
                      'not build industry functionality yet. Clone the Salesforce DX repository in VS Code, '
                      'inspect the source structure, authenticate the training org, create a student feature '
                      'branch, make a safe documentation change, push it, open a pull request, review a peer '
                      'pull request, apply feedback, resolve a controlled merge conflict, merge, and '
                      'synchronize local main.',
      'deliverable': 'A pull-request URL, peer-review evidence, merge-conflict resolution evidence, clean '
                     'final git status, synchronized main branch, and a short workflow explanation showing '
                     'clone, branch, commit, push, pull request, review, merge, and pull.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Translate the classroom '
                      'project into personas, user journeys, user stories, acceptance criteria, success '
                      'measures, scope boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, '
                     'acceptance criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Design the application data model',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Create the standard and '
                      'custom object model, relationships, ownership strategy, external IDs, reporting '
                      'considerations, and a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample '
                     'records, and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Add validation, formulas, '
                      'duplicate prevention, record types, conditional visibility, required-data controls, '
                      'and user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, '
                     'and a data-quality decision log.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Configure persona-based security',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Design access for Referral '
                      'Coordinator, Care Coordinator, Clinical Reviewer, Program Administrator. Create '
                      'least-privilege access for the project personas using permission sets, permission set '
                      'groups, sharing, field-level security, and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, '
                     'and documented exceptions.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Automate the core business process',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Build declarative '
                      'automation for the end-to-end process using before-save, after-save, screen, '
                      'scheduled, and reusable Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, '
                     'and an end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Build the Apex service layer',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Create maintainable Apex '
                      'domain and service classes for business rules that should not live entirely in Flow. '
                      'Validate inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design '
                     'rationale, and unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Build data access and transaction architecture',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Implement selective SOQL, '
                      'relationship queries, aggregates, search, and data-access utilities for operational '
                      'views, missing-data detection, and reporting. Then for the Patient Referral & Care '
                      'Coordination App, use the Patient, Provider, Referral, Eligibility Review, '
                      'Authorization, Care Task, Appointment, Follow-Up model and support referral intake, '
                      'provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Add bulk-safe trigger and handler logic for status '
                      'changes, related-record coordination, duplicate prevention, and transaction-safe '
                      'updates.',
      'deliverable': 'Selector and search classes, selective and aggregate query evidence, a thin trigger '
                     'and handler, bulkification and recursion controls, transaction-safety reasoning, '
                     '200-record tests, analyzer results, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Secure the codebase and automate testing',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Review the service and '
                      'data-access layers for sharing, user mode, CRUD, field-level security, secure dynamic '
                      'SOQL, validation, and sensitive-data exposure. Then create a complete automated test '
                      'framework with permission-aware, behavior-focused, bulk, asynchronous, and '
                      'failure-path tests.',
      'deliverable': 'Security review worksheet, corrected permission-aware code, test-data factory, '
                     'low-permission tests, bulk and asynchronous tests, Code Analyzer results, coverage '
                     'report, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. Connect to the live CMS NPI '
                      'Registry API at https://npiregistry.cms.hhs.gov/api using a Named Credential. The '
                      'classroom operation is to send a training provider NPI or search criteria to the live '
                      'CMS registry, receive provider identity and practice-location data, and update the '
                      'Provider validation fields. Use training data only. Configure a Named Credential and '
                      'External Credential, execute a genuine training callout, map the live response into '
                      'Salesforce, and use HttpCalloutMock only inside automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped '
                     'Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and '
                     'recovery demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. The primary experience is a '
                      'care-coordination workbench with patient context, referral status, provider '
                      'validation, missing information, and next actions. Build the application main user '
                      'workspace with modern JavaScript, accessible Lightning components, clear loading and '
                      'error states, and responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility '
                     'notes, and stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, '
                      'Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model '
                      'and support referral intake, provider validation, eligibility review, authorization, '
                      'care assignment, appointment coordination, and follow-up. The primary experience is a '
                      'care-coordination workbench with patient context, referral status, provider '
                      'validation, missing information, and next actions. Extend the workspace with '
                      'communicating components, Lightning Data Service or Apex data access, search, '
                      'filtering, files, reusable utilities, caching, and performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, '
                     'performance notes, and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Use Claude AI and Salesforce CLI safely',
      'instructions': 'For the Patient Referral & Care Coordination App, use Claude Code only inside the '
                      'classroom repository and training org. Create project instructions that describe the '
                      'Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, '
                      'Appointment, Follow-Up model, the referral intake, provider validation, eligibility '
                      'review, authorization, care assignment, appointment coordination, and follow-up '
                      'process, naming rules, security requirements, allowed files, prohibited actions, '
                      'required tests, and approved Salesforce CLI commands. Use plan mode before edits, '
                      'complete one bounded implementation or test-improvement task, inspect every proposed '
                      'change, and use deterministic Salesforce CLI commands to display the org, retrieve '
                      'source, run Apex tests, run Code Analyzer, and validate deployment. Correct '
                      'hallucinations, insecure code, unnecessary changes, and failed commands before '
                      'committing anything.',
      'deliverable': 'Claude Code installation and health-check evidence, redacted session transcript, '
                     'project CLAUDE.md or approved instruction file, bounded task brief, approved plan, '
                     'reviewed and corrected diff, Salesforce CLI outputs, Apex test results, Code Analyzer '
                     'report, deployment-validation result, pull request, and AI review log.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Connect Claude through MCP with least privilege',
      'instructions': 'For the Patient Referral & Care Coordination App, map the MCP client, approved '
                      'servers, tools, resources, prompts, authentication, and data boundaries. Configure '
                      'only instructor-approved project-scoped MCP connections. Start with repository and '
                      'Salesforce read-only tools, inspect the available tool schemas, and compare each MCP '
                      'action with the equivalent direct Salesforce CLI or API operation. Run a read-only '
                      'workflow that analyzes the referral intake, provider validation, eligibility review, '
                      'authorization, care assignment, appointment coordination, and follow-up '
                      'implementation, then complete one narrowly approved write or execution workflow with '
                      'explicit human confirmation. Create a reusable agent skill or instruction, preserve '
                      'logs, test denied and failure cases, and disable unnecessary tools after the '
                      'exercise.',
      'deliverable': 'MCP architecture diagram, redacted project-scoped configuration, server and tool '
                     'inventory, least-privilege matrix, read-only workflow evidence, one human-approved '
                     'controlled action, CLI-versus-MCP comparison, skill or instruction file, audit log, '
                     'failure tests, security review, and reviewed pull request.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the governed Agentforce application',
      'instructions': 'For the Patient Referral & Care Coordination App, complete the full application and '
                      'the approved agent use case: care-coordination assistant that summarizes referrals, '
                      'identifies missing data, recommends approved next steps, and escalates clinical '
                      'decisions. Integrate the verified Claude and CLI workflow from Week 14 and the '
                      'governed MCP workflow from Week 15 into the final engineering evidence. Build or '
                      'configure Agentforce with narrow actions, grounded data, permission-aware execution, '
                      'confirmation for state changes, prompt-injection resistance, monitoring, and human '
                      'escalation. Run final application, agent, security, integration, deployment, and '
                      'rollback tests, then deliver the production-style classroom demonstration.',
      'deliverable': 'The complete deployed application, Agentforce configuration, authorization matrix, '
                     'guardrail and prompt-injection tests, monitoring and escalation plan, final Code '
                     'Analyzer and validation results, Claude and MCP governance evidence, architecture '
                     'documentation, user and administrator guides, Git repository, and final classroom '
                     'demonstration.',
      'is_final': 1}],
 3: [{'week_number': 1,
      'title': 'Master Git fundamentals in VS Code',
      'instructions': 'Before changing the classroom Salesforce application, every student completes an '
                      'individual Git foundations lab. Create a personal practice repository, configure Git, '
                      'use the working tree and staging area correctly, make meaningful commits, inspect '
                      'history, create and merge a branch, undo changes safely, and publish the repository '
                      'to GitHub.',
      'deliverable': 'A personal Git Foundations Portfolio repository URL containing README.md, '
                     'learning-log.md, profile.md, .gitignore, at least five meaningful commits, one merged '
                     'branch, a clean git status, and the required screenshots and command output.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Complete the classroom GitHub and Salesforce DX workflow',
      'instructions': 'Use the classroom repository for the Donor & Volunteer Engagement App, but do not '
                      'build industry functionality yet. Clone the Salesforce DX repository in VS Code, '
                      'inspect the source structure, authenticate the training org, create a student feature '
                      'branch, make a safe documentation change, push it, open a pull request, review a peer '
                      'pull request, apply feedback, resolve a controlled merge conflict, merge, and '
                      'synchronize local main.',
      'deliverable': 'A pull-request URL, peer-review evidence, merge-conflict resolution evidence, clean '
                     'final git status, synchronized main branch, and a short workflow explanation showing '
                     'clone, branch, commit, push, pull request, review, merge, and pull.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Translate the classroom '
                      'project into personas, user journeys, user stories, acceptance criteria, success '
                      'measures, scope boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, '
                     'acceptance criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Design the application data model',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Create the standard and '
                      'custom object model, relationships, ownership strategy, external IDs, reporting '
                      'considerations, and a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample '
                     'records, and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Add validation, formulas, '
                      'duplicate prevention, record types, conditional visibility, required-data controls, '
                      'and user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, '
                     'and a data-quality decision log.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Configure persona-based security',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Design access for '
                      'Fundraising Coordinator, Volunteer Manager, Program Manager, Nonprofit Administrator. '
                      'Create least-privilege access for the project personas using permission sets, '
                      'permission set groups, sharing, field-level security, and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, '
                     'and documented exceptions.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Automate the core business process',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Build declarative '
                      'automation for the end-to-end process using before-save, after-save, screen, '
                      'scheduled, and reusable Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, '
                     'and an end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Build the Apex service layer',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Create maintainable Apex '
                      'domain and service classes for business rules that should not live entirely in Flow. '
                      'Validate inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design '
                     'rationale, and unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Build data access and transaction architecture',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Implement selective SOQL, '
                      'relationship queries, aggregates, search, and data-access utilities for operational '
                      'views, missing-data detection, and reporting. Then for the Donor & Volunteer '
                      'Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, '
                      'Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, '
                      'acknowledgement, and outreach follow-up. Add bulk-safe trigger and handler logic for '
                      'status changes, related-record coordination, duplicate prevention, and '
                      'transaction-safe updates.',
      'deliverable': 'Selector and search classes, selective and aggregate query evidence, a thin trigger '
                     'and handler, bulkification and recursion controls, transaction-safety reasoning, '
                     '200-record tests, analyzer results, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Secure the codebase and automate testing',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Review the service and '
                      'data-access layers for sharing, user mode, CRUD, field-level security, secure dynamic '
                      'SOQL, validation, and sensitive-data exposure. Then create a complete automated test '
                      'framework with permission-aware, behavior-focused, bulk, asynchronous, and '
                      'failure-path tests.',
      'deliverable': 'Security review worksheet, corrected permission-aware code, test-data factory, '
                     'low-permission tests, bulk and asynchronous tests, Code Analyzer results, coverage '
                     'report, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. Connect to the live US '
                      'Census Geocoding Services at https://geocoding.geo.census.gov/geocoder using a Named '
                      'Credential. The classroom operation is to send a fictional outreach address to the '
                      'live Census geocoder, receive matched address and coordinates, and store the '
                      'standardized location for outreach planning. Use training data only. Configure a '
                      'Named Credential and External Credential, execute a genuine training callout, map the '
                      'live response into Salesforce, and use HttpCalloutMock only inside automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped '
                     'Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and '
                     'recovery demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. The primary experience is '
                      'a engagement dashboard with campaign results, donor history, volunteer availability, '
                      'mapped outreach locations, and required follow-up. Build the application main user '
                      'workspace with modern JavaScript, accessible Lightning components, clear loading and '
                      'error states, and responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility '
                     'notes, and stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, '
                      'Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score '
                      'model and support donor engagement, donation processing, volunteer registration, '
                      'shift assignment, acknowledgement, and outreach follow-up. The primary experience is '
                      'a engagement dashboard with campaign results, donor history, volunteer availability, '
                      'mapped outreach locations, and required follow-up. Extend the workspace with '
                      'communicating components, Lightning Data Service or Apex data access, search, '
                      'filtering, files, reusable utilities, caching, and performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, '
                     'performance notes, and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Use Claude AI and Salesforce CLI safely',
      'instructions': 'For the Donor & Volunteer Engagement App, use Claude Code only inside the classroom '
                      'repository and training org. Create project instructions that describe the Donor, '
                      'Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, '
                      'Engagement Score model, the donor engagement, donation processing, volunteer '
                      'registration, shift assignment, acknowledgement, and outreach follow-up process, '
                      'naming rules, security requirements, allowed files, prohibited actions, required '
                      'tests, and approved Salesforce CLI commands. Use plan mode before edits, complete one '
                      'bounded implementation or test-improvement task, inspect every proposed change, and '
                      'use deterministic Salesforce CLI commands to display the org, retrieve source, run '
                      'Apex tests, run Code Analyzer, and validate deployment. Correct hallucinations, '
                      'insecure code, unnecessary changes, and failed commands before committing anything.',
      'deliverable': 'Claude Code installation and health-check evidence, redacted session transcript, '
                     'project CLAUDE.md or approved instruction file, bounded task brief, approved plan, '
                     'reviewed and corrected diff, Salesforce CLI outputs, Apex test results, Code Analyzer '
                     'report, deployment-validation result, pull request, and AI review log.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Connect Claude through MCP with least privilege',
      'instructions': 'For the Donor & Volunteer Engagement App, map the MCP client, approved servers, '
                      'tools, resources, prompts, authentication, and data boundaries. Configure only '
                      'instructor-approved project-scoped MCP connections. Start with repository and '
                      'Salesforce read-only tools, inspect the available tool schemas, and compare each MCP '
                      'action with the equivalent direct Salesforce CLI or API operation. Run a read-only '
                      'workflow that analyzes the donor engagement, donation processing, volunteer '
                      'registration, shift assignment, acknowledgement, and outreach follow-up '
                      'implementation, then complete one narrowly approved write or execution workflow with '
                      'explicit human confirmation. Create a reusable agent skill or instruction, preserve '
                      'logs, test denied and failure cases, and disable unnecessary tools after the '
                      'exercise.',
      'deliverable': 'MCP architecture diagram, redacted project-scoped configuration, server and tool '
                     'inventory, least-privilege matrix, read-only workflow evidence, one human-approved '
                     'controlled action, CLI-versus-MCP comparison, skill or instruction file, audit log, '
                     'failure tests, security review, and reviewed pull request.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the governed Agentforce application',
      'instructions': 'For the Donor & Volunteer Engagement App, complete the full application and the '
                      'approved agent use case: engagement assistant that summarizes donor and volunteer '
                      'activity, identifies follow-up opportunities, drafts approved communications, and '
                      'escalates sensitive outreach. Integrate the verified Claude and CLI workflow from '
                      'Week 14 and the governed MCP workflow from Week 15 into the final engineering '
                      'evidence. Build or configure Agentforce with narrow actions, grounded data, '
                      'permission-aware execution, confirmation for state changes, prompt-injection '
                      'resistance, monitoring, and human escalation. Run final application, agent, security, '
                      'integration, deployment, and rollback tests, then deliver the production-style '
                      'classroom demonstration.',
      'deliverable': 'The complete deployed application, Agentforce configuration, authorization matrix, '
                     'guardrail and prompt-injection tests, monitoring and escalation plan, final Code '
                     'Analyzer and validation results, Claude and MCP governance evidence, architecture '
                     'documentation, user and administrator guides, Git repository, and final classroom '
                     'demonstration.',
      'is_final': 1}],
 4: [{'week_number': 1,
      'title': 'Master Git fundamentals in VS Code',
      'instructions': 'Before changing the classroom Salesforce application, every student completes an '
                      'individual Git foundations lab. Create a personal practice repository, configure Git, '
                      'use the working tree and staging area correctly, make meaningful commits, inspect '
                      'history, create and merge a branch, undo changes safely, and publish the repository '
                      'to GitHub.',
      'deliverable': 'A personal Git Foundations Portfolio repository URL containing README.md, '
                     'learning-log.md, profile.md, .gitignore, at least five meaningful commits, one merged '
                     'branch, a clean git status, and the required screenshots and command output.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Complete the classroom GitHub and Salesforce DX workflow',
      'instructions': 'Use the classroom repository for the Production & Quality Operations App, but do not '
                      'build industry functionality yet. Clone the Salesforce DX repository in VS Code, '
                      'inspect the source structure, authenticate the training org, create a student feature '
                      'branch, make a safe documentation change, push it, open a pull request, review a peer '
                      'pull request, apply feedback, resolve a controlled merge conflict, merge, and '
                      'synchronize local main.',
      'deliverable': 'A pull-request URL, peer-review evidence, merge-conflict resolution evidence, clean '
                     'final git status, synchronized main branch, and a short workflow explanation showing '
                     'clone, branch, commit, push, pull request, review, merge, and pull.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Translate the classroom project into personas, user journeys, user stories, '
                      'acceptance criteria, success measures, scope boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, '
                     'acceptance criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Design the application data model',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Create the standard and custom object model, relationships, ownership '
                      'strategy, external IDs, reporting considerations, and a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample '
                     'records, and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Add validation, formulas, duplicate prevention, record types, conditional '
                      'visibility, required-data controls, and user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, '
                     'and a data-quality decision log.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Configure persona-based security',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Design access for Production Planner, Line Supervisor, Quality Inspector, '
                      'Plant Manager. Create least-privilege access for the project personas using '
                      'permission sets, permission set groups, sharing, field-level security, and '
                      'record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, '
                     'and documented exceptions.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Automate the core business process',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Build declarative automation for the end-to-end process using before-save, '
                      'after-save, screen, scheduled, and reusable Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, '
                     'and an end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Build the Apex service layer',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Create maintainable Apex domain and service classes for business rules that '
                      'should not live entirely in Flow. Validate inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design '
                     'rationale, and unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Build data access and transaction architecture',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Implement selective SOQL, relationship queries, aggregates, search, and '
                      'data-access utilities for operational views, missing-data detection, and reporting. '
                      'Then for the Production & Quality Operations App, use the Plant, Work Center, '
                      'Production Order, Material Requirement, Production Run, Quality Inspection, Downtime '
                      'Event, Finished Good model and support production planning, material readiness, '
                      'work-center scheduling, execution, quality inspection, downtime response, and '
                      'finished-goods release. Add bulk-safe trigger and handler logic for status changes, '
                      'related-record coordination, duplicate prevention, and transaction-safe updates.',
      'deliverable': 'Selector and search classes, selective and aggregate query evidence, a thin trigger '
                     'and handler, bulkification and recursion controls, transaction-safety reasoning, '
                     '200-record tests, analyzer results, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Secure the codebase and automate testing',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Review the service and data-access layers for sharing, user mode, CRUD, '
                      'field-level security, secure dynamic SOQL, validation, and sensitive-data exposure. '
                      'Then create a complete automated test framework with permission-aware, '
                      'behavior-focused, bulk, asynchronous, and failure-path tests.',
      'deliverable': 'Security review worksheet, corrected permission-aware code, test-data factory, '
                     'low-permission tests, bulk and asynchronous tests, Code Analyzer results, coverage '
                     'report, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. Connect to the live NHTSA vPIC API at https://vpic.nhtsa.dot.gov/api using a '
                      'Named Credential. The classroom operation is to send a manufacturer name or '
                      'identifier to the live NHTSA vPIC API, receive manufacturer details, and enrich the '
                      'Supplier or Manufacturer record used by the production plan. Use training data only. '
                      'Configure a Named Credential and External Credential, execute a genuine training '
                      'callout, map the live response into Salesforce, and use HttpCalloutMock only inside '
                      'automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped '
                     'Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and '
                     'recovery demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. The primary experience is a production control board with material '
                      'readiness, work-center schedule, quality holds, downtime events, and release actions. '
                      'Build the application main user workspace with modern JavaScript, accessible '
                      'Lightning components, clear loading and error states, and responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility '
                     'notes, and stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production '
                      'Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, '
                      'Finished Good model and support production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release. The primary experience is a production control board with material '
                      'readiness, work-center schedule, quality holds, downtime events, and release actions. '
                      'Extend the workspace with communicating components, Lightning Data Service or Apex '
                      'data access, search, filtering, files, reusable utilities, caching, and performance '
                      'improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, '
                     'performance notes, and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Use Claude AI and Salesforce CLI safely',
      'instructions': 'For the Production & Quality Operations App, use Claude Code only inside the '
                      'classroom repository and training org. Create project instructions that describe the '
                      'Plant, Work Center, Production Order, Material Requirement, Production Run, Quality '
                      'Inspection, Downtime Event, Finished Good model, the production planning, material '
                      'readiness, work-center scheduling, execution, quality inspection, downtime response, '
                      'and finished-goods release process, naming rules, security requirements, allowed '
                      'files, prohibited actions, required tests, and approved Salesforce CLI commands. Use '
                      'plan mode before edits, complete one bounded implementation or test-improvement task, '
                      'inspect every proposed change, and use deterministic Salesforce CLI commands to '
                      'display the org, retrieve source, run Apex tests, run Code Analyzer, and validate '
                      'deployment. Correct hallucinations, insecure code, unnecessary changes, and failed '
                      'commands before committing anything.',
      'deliverable': 'Claude Code installation and health-check evidence, redacted session transcript, '
                     'project CLAUDE.md or approved instruction file, bounded task brief, approved plan, '
                     'reviewed and corrected diff, Salesforce CLI outputs, Apex test results, Code Analyzer '
                     'report, deployment-validation result, pull request, and AI review log.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Connect Claude through MCP with least privilege',
      'instructions': 'For the Production & Quality Operations App, map the MCP client, approved servers, '
                      'tools, resources, prompts, authentication, and data boundaries. Configure only '
                      'instructor-approved project-scoped MCP connections. Start with repository and '
                      'Salesforce read-only tools, inspect the available tool schemas, and compare each MCP '
                      'action with the equivalent direct Salesforce CLI or API operation. Run a read-only '
                      'workflow that analyzes the production planning, material readiness, work-center '
                      'scheduling, execution, quality inspection, downtime response, and finished-goods '
                      'release implementation, then complete one narrowly approved write or execution '
                      'workflow with explicit human confirmation. Create a reusable agent skill or '
                      'instruction, preserve logs, test denied and failure cases, and disable unnecessary '
                      'tools after the exercise.',
      'deliverable': 'MCP architecture diagram, redacted project-scoped configuration, server and tool '
                     'inventory, least-privilege matrix, read-only workflow evidence, one human-approved '
                     'controlled action, CLI-versus-MCP comparison, skill or instruction file, audit log, '
                     'failure tests, security review, and reviewed pull request.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the governed Agentforce application',
      'instructions': 'For the Production & Quality Operations App, complete the full application and the '
                      'approved agent use case: production operations assistant that summarizes schedule '
                      'risk, material shortages, quality holds, and downtime, invokes approved task actions, '
                      'and escalates release decisions. Integrate the verified Claude and CLI workflow from '
                      'Week 14 and the governed MCP workflow from Week 15 into the final engineering '
                      'evidence. Build or configure Agentforce with narrow actions, grounded data, '
                      'permission-aware execution, confirmation for state changes, prompt-injection '
                      'resistance, monitoring, and human escalation. Run final application, agent, security, '
                      'integration, deployment, and rollback tests, then deliver the production-style '
                      'classroom demonstration.',
      'deliverable': 'The complete deployed application, Agentforce configuration, authorization matrix, '
                     'guardrail and prompt-injection tests, monitoring and escalation plan, final Code '
                     'Analyzer and validation results, Claude and MCP governance evidence, architecture '
                     'documentation, user and administrator guides, Git repository, and final classroom '
                     'demonstration.',
      'is_final': 1}],
 5: [{'week_number': 1,
      'title': 'Master Git fundamentals in VS Code',
      'instructions': 'Before changing the classroom Salesforce application, every student completes an '
                      'individual Git foundations lab. Create a personal practice repository, configure Git, '
                      'use the working tree and staging area correctly, make meaningful commits, inspect '
                      'history, create and merge a branch, undo changes safely, and publish the repository '
                      'to GitHub.',
      'deliverable': 'A personal Git Foundations Portfolio repository URL containing README.md, '
                     'learning-log.md, profile.md, .gitignore, at least five meaningful commits, one merged '
                     'branch, a clean git status, and the required screenshots and command output.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Complete the classroom GitHub and Salesforce DX workflow',
      'instructions': 'Use the classroom repository for the AI-Enabled Client Delivery App, but do not build '
                      'industry functionality yet. Clone the Salesforce DX repository in VS Code, inspect '
                      'the source structure, authenticate the training org, create a student feature branch, '
                      'make a safe documentation change, push it, open a pull request, review a peer pull '
                      'request, apply feedback, resolve a controlled merge conflict, merge, and synchronize '
                      'local main.',
      'deliverable': 'A pull-request URL, peer-review evidence, merge-conflict resolution evidence, clean '
                     'final git status, synchronized main branch, and a short workflow explanation showing '
                     'clone, branch, commit, push, pull request, review, merge, and pull.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Translate the classroom project into '
                      'personas, user journeys, user stories, acceptance criteria, success measures, scope '
                      'boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, '
                     'acceptance criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Design the application data model',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Create the standard and custom object '
                      'model, relationships, ownership strategy, external IDs, reporting considerations, and '
                      'a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample '
                     'records, and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Add validation, formulas, duplicate '
                      'prevention, record types, conditional visibility, required-data controls, and '
                      'user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, '
                     'and a data-quality decision log.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Configure persona-based security',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Design access for Consultant, Project '
                      'Manager, Delivery Director, Services Administrator. Create least-privilege access for '
                      'the project personas using permission sets, permission set groups, sharing, '
                      'field-level security, and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, '
                     'and documented exceptions.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Automate the core business process',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Build declarative automation for the '
                      'end-to-end process using before-save, after-save, screen, scheduled, and reusable '
                      'Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, '
                     'and an end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Build the Apex service layer',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Create maintainable Apex domain and '
                      'service classes for business rules that should not live entirely in Flow. Validate '
                      'inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design '
                     'rationale, and unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Build data access and transaction architecture',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Implement selective SOQL, '
                      'relationship queries, aggregates, search, and data-access utilities for operational '
                      'views, missing-data detection, and reporting. Then for the AI-Enabled Client Delivery '
                      'App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, '
                      'Deliverable, Client Update model and support project intake, milestone planning, '
                      'resource assignment, time tracking, risk management, deliverable approval, and client '
                      'communication. Add bulk-safe trigger and handler logic for status changes, '
                      'related-record coordination, duplicate prevention, and transaction-safe updates.',
      'deliverable': 'Selector and search classes, selective and aggregate query evidence, a thin trigger '
                     'and handler, bulkification and recursion controls, transaction-safety reasoning, '
                     '200-record tests, analyzer results, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Secure the codebase and automate testing',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Review the service and data-access '
                      'layers for sharing, user mode, CRUD, field-level security, secure dynamic SOQL, '
                      'validation, and sensitive-data exposure. Then create a complete automated test '
                      'framework with permission-aware, behavior-focused, bulk, asynchronous, and '
                      'failure-path tests.',
      'deliverable': 'Security review worksheet, corrected permission-aware code, test-data factory, '
                     'low-permission tests, bulk and asynchronous tests, Code Analyzer results, coverage '
                     'report, and a reviewed pull request.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. Connect to the live GitHub REST API '
                      'at https://api.github.com using a Named Credential. The classroom operation is to '
                      'call a live public training repository endpoint, receive issues or milestones, and '
                      'create or update corresponding Project Risks and Milestones in Salesforce. Use '
                      'training data only. Configure a Named Credential and External Credential, execute a '
                      'genuine training callout, map the live response into Salesforce, and use '
                      'HttpCalloutMock only inside automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped '
                     'Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and '
                     'recovery demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. The primary experience is a delivery '
                      'workbench with milestone health, resource allocation, risks, deliverables, and '
                      'client-update actions. Build the application main user workspace with modern '
                      'JavaScript, accessible Lightning components, clear loading and error states, and '
                      'responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility '
                     'notes, and stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project '
                      'intake, milestone planning, resource assignment, time tracking, risk management, '
                      'deliverable approval, and client communication. The primary experience is a delivery '
                      'workbench with milestone health, resource allocation, risks, deliverables, and '
                      'client-update actions. Extend the workspace with communicating components, Lightning '
                      'Data Service or Apex data access, search, filtering, files, reusable utilities, '
                      'caching, and performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, '
                     'performance notes, and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Use Claude AI and Salesforce CLI safely',
      'instructions': 'For the AI-Enabled Client Delivery App, use Claude Code only inside the classroom '
                      'repository and training org. Create project instructions that describe the Client, '
                      'Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update '
                      'model, the project intake, milestone planning, resource assignment, time tracking, '
                      'risk management, deliverable approval, and client communication process, naming '
                      'rules, security requirements, allowed files, prohibited actions, required tests, and '
                      'approved Salesforce CLI commands. Use plan mode before edits, complete one bounded '
                      'implementation or test-improvement task, inspect every proposed change, and use '
                      'deterministic Salesforce CLI commands to display the org, retrieve source, run Apex '
                      'tests, run Code Analyzer, and validate deployment. Correct hallucinations, insecure '
                      'code, unnecessary changes, and failed commands before committing anything.',
      'deliverable': 'Claude Code installation and health-check evidence, redacted session transcript, '
                     'project CLAUDE.md or approved instruction file, bounded task brief, approved plan, '
                     'reviewed and corrected diff, Salesforce CLI outputs, Apex test results, Code Analyzer '
                     'report, deployment-validation result, pull request, and AI review log.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Connect Claude through MCP with least privilege',
      'instructions': 'For the AI-Enabled Client Delivery App, map the MCP client, approved servers, tools, '
                      'resources, prompts, authentication, and data boundaries. Configure only '
                      'instructor-approved project-scoped MCP connections. Start with repository and '
                      'Salesforce read-only tools, inspect the available tool schemas, and compare each MCP '
                      'action with the equivalent direct Salesforce CLI or API operation. Run a read-only '
                      'workflow that analyzes the project intake, milestone planning, resource assignment, '
                      'time tracking, risk management, deliverable approval, and client communication '
                      'implementation, then complete one narrowly approved write or execution workflow with '
                      'explicit human confirmation. Create a reusable agent skill or instruction, preserve '
                      'logs, test denied and failure cases, and disable unnecessary tools after the '
                      'exercise.',
      'deliverable': 'MCP architecture diagram, redacted project-scoped configuration, server and tool '
                     'inventory, least-privilege matrix, read-only workflow evidence, one human-approved '
                     'controlled action, CLI-versus-MCP comparison, skill or instruction file, audit log, '
                     'failure tests, security review, and reviewed pull request.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the governed Agentforce application',
      'instructions': 'For the AI-Enabled Client Delivery App, complete the full application and the '
                      'approved agent use case: client-delivery assistant that summarizes project health, '
                      'identifies risks and missing updates, invokes approved actions, and escalates '
                      'commercial or delivery decisions. Integrate the verified Claude and CLI workflow from '
                      'Week 14 and the governed MCP workflow from Week 15 into the final engineering '
                      'evidence. Build or configure Agentforce with narrow actions, grounded data, '
                      'permission-aware execution, confirmation for state changes, prompt-injection '
                      'resistance, monitoring, and human escalation. Run final application, agent, security, '
                      'integration, deployment, and rollback tests, then deliver the production-style '
                      'classroom demonstration.',
      'deliverable': 'The complete deployed application, Agentforce configuration, authorization matrix, '
                     'guardrail and prompt-injection tests, monitoring and escalation plan, final Code '
                     'Analyzer and validation results, Claude and MCP governance evidence, architecture '
                     'documentation, user and administrator guides, Git repository, and final classroom '
                     'demonstration.',
      'is_final': 1}]}

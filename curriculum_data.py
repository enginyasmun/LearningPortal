"""Sixteen-week academy curriculum and five classroom project plans."""

PROGRAM_WEEKS = [(1,
  'Foundation',
  'Discovery, Requirements, and Salesforce Architecture',
  'Business process discovery, personas, user stories, acceptance criteria, Salesforce architecture, multitenancy, '
  'metadata versus data, org strategy, and solution boundaries.',
  'How Salesforce multitenancy and metadata-driven architecture affect solution design.',
  'A strong Salesforce application begins with business discovery, not configuration.'),
 (2,
  'Foundation',
  'Data Modeling and Relationship Design',
  'Standard and custom objects, lookup and master-detail relationships, junction objects, external IDs, ownership, '
  'roll-up summaries, data-volume considerations, and schema documentation.',
  'Lookup versus master-detail relationships and their effects on ownership, deletion, sharing, reporting, and '
  'roll-ups.',
  'The data-model decision that can shape an entire Salesforce application.'),
 (3,
  'Foundation',
  'Data Quality and User Experience',
  'Validation rules, formulas, duplicate prevention, matching rules, record types, Dynamic Forms, required data, '
  'conditional visibility, and user-friendly error messages.',
  'How data-quality controls should be divided among validation rules, duplicate rules, Flow, and Apex.',
  'Good Salesforce data quality is designed into the application.'),
 (4,
  'Foundation',
  'Security and Access Control',
  'Profiles, permission sets, permission set groups, organization-wide defaults, role hierarchy, sharing rules, '
  'field-level security, record access, least privilege, and security testing.',
  'How Salesforce object, field, and record security layers work together.',
  'Salesforce security is not controlled by one setting.'),
 (5,
  'Automation',
  'Flow and Declarative Automation',
  'Before-save Flow, after-save Flow, screen Flow, scheduled Flow, subflows, fault handling, order of execution, '
  'recursion, automation selection, and maintainability.',
  'Flow versus Apex and how to choose the correct automation layer.',
  'Not every Salesforce automation requires Apex.'),
 (6,
  'Development',
  'Apex Services and Object-Oriented Design',
  'Apex syntax, collections, classes, interfaces, exceptions, null handling, domain logic, service classes, separation '
  'of responsibilities, and maintainable design.',
  'Object-oriented programming in Apex and why service boundaries matter.',
  'Apex is more than syntax.'),
 (7,
  'Development',
  'SOQL, SOSL, and Data Access',
  'Relationship queries, aggregate queries, bind variables, dynamic SOQL, selectivity, indexes, query planning, large '
  'data volumes, governor limits, and bulk data access.',
  'Efficient SOQL design, selective queries, and large-data-volume considerations.',
  'Why SOQL inside a loop is a serious Salesforce development mistake.'),
 (8,
  'Development',
  'Triggers and Transaction Architecture',
  'Trigger contexts, before and after operations, bulkification, recursion control, handler classes, service '
  'orchestration, savepoints, rollback, and transaction boundaries.',
  'Trigger architecture patterns, handler classes, service layers, and recursion prevention.',
  'A trigger should coordinate work rather than contain the entire application.'),
 (9,
  'Development',
  'Secure Apex and Permission-Aware Code',
  'with sharing, inherited sharing, user mode, system mode, CRUD, field-level security, secure dynamic SOQL, injection '
  'prevention, input validation, and sensitive-data handling.',
  'User mode, system mode, sharing, CRUD, and field-level security in Apex.',
  'Why with sharing does not enforce every Salesforce security layer.'),
 (10,
  'Quality',
  'Testing Strategy and Test Automation',
  'Test-data factories, @TestSetup, positive and negative tests, bulk tests, permission tests, callout mocks, '
  'asynchronous tests, assertions, test isolation, and meaningful coverage.',
  'What makes an Apex test valuable beyond code coverage.',
  'Code coverage does not prove that Salesforce code works correctly.'),
 (11,
  'Integration',
  'Asynchronous Processing and Integrations',
  'Queueable Apex, Batch Apex, Platform Events, scheduled processing, REST callouts, JSON, Named Credentials, '
  'idempotency, retries, logging, monitoring, and recovery.',
  'Queueable Apex versus Batch Apex versus Platform Events.',
  'Choosing the correct asynchronous tool in Salesforce.'),
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
  'Lightning Data Service, UI Record API, wire service, imperative Apex, component communication, Lightning Message '
  'Service, caching, file upload, custom data tables, search, accessibility, and performance.',
  'Lightning Data Service versus custom Apex and how performance and accessibility affect component design.',
  'A component is not complete merely because it works.'),
 (14,
  'Delivery',
  'Git, DevOps, Debugging, and Release Readiness',
  'Feature branches, commits, pull requests, code review, conflict resolution, static analysis, deployment validation, '
  'dependencies, rollback, debug logs, root-cause analysis, and post-deployment verification.',
  'Git workflows, continuous integration, release validation, and structured root-cause analysis.',
  'Deployment success does not always mean release success.'),
 (15,
  'AI and Agents',
  'AI-Assisted Development, MCP, and Agent Skills',
  'LLM limitations, privacy, secure context, AI-generated code review, Model Context Protocol, MCP servers, tools, '
  'resources, authentication, CLI versus MCP, reusable skills, instructions, and least privilege.',
  'Benefits and risks of AI-generated Salesforce code, plus MCP servers versus APIs and Salesforce CLI.',
  'MCP gives an agent tools, while skills teach it how the team wants work performed.'),
 (16,
  'AI and Agents',
  'Agentforce, Final Integration, and Production Demonstration',
  'Agentforce instructions, grounding, actions, Flow and Apex actions, Agent Script, guardrails, testing, monitoring, '
  'human escalation, deployment, final integration, documentation, and stakeholder demonstration.',
  'Designing secure and reliable Salesforce agents with grounding, guardrails, monitoring, and escalation.',
  'A Salesforce agent needs clearly defined authorization boundaries.')]

PROJECTS = [{'number': 1,
  'industry': 'Warehouse & Logistics',
  'title': 'Warehouse Management & Logistics App',
  'summary': 'A complete warehouse operations workspace for receiving, putaway, inventory control, picking, packing, '
             'shipping, and delivery exceptions.',
  'entities': 'Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event',
  'personas': 'Warehouse Associate, Inventory Controller, Logistics Coordinator, Operations Manager',
  'process': 'receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling',
  'integration': 'postal-code validation and delivery-location enrichment',
  'integration_name': 'Zippopotam.us Postal Code API',
  'integration_base_url': 'https://api.zippopotam.us',
  'integration_docs_url': 'https://www.zippopotam.us/',
  'integration_auth': 'No authentication for the training endpoint',
  'integration_operation': 'send a shipment country code and postal code to the live API, receive city, state, '
                           'latitude, and longitude, and store the validated destination on the Shipment',
  'integration_path': '/us/{postal-code}',
  'workspace': 'warehouse control tower with receiving queues, bin availability, pick waves, shipment readiness, and '
               'exceptions',
  'agent': 'warehouse operations assistant that summarizes inventory risk, identifies blocked shipments, invokes '
           'approved replenishment or task actions, and escalates operational decisions',
  'accent': 'finance'},
 {'number': 2,
  'industry': 'Healthcare',
  'title': 'Patient Referral & Care Coordination App',
  'summary': 'A referral and care-coordination workspace for patients, providers, eligibility, authorizations, care '
             'tasks, and follow-up.',
  'entities': 'Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up',
  'personas': 'Referral Coordinator, Care Coordinator, Clinical Reviewer, Program Administrator',
  'process': 'referral intake, provider validation, eligibility review, authorization, care assignment, appointment '
             'coordination, and follow-up',
  'integration': 'public provider identity validation',
  'integration_name': 'CMS NPI Registry API',
  'integration_base_url': 'https://npiregistry.cms.hhs.gov/api',
  'integration_docs_url': 'https://npiregistry.cms.hhs.gov/api-page',
  'integration_auth': 'No authentication; use training provider identifiers only',
  'integration_operation': 'send a training provider NPI or search criteria to the live CMS registry, receive provider '
                           'identity and practice-location data, and update the Provider validation fields',
  'integration_path': '/?version=2.1&number={npi}',
  'workspace': 'care-coordination workbench with patient context, referral status, provider validation, missing '
               'information, and next actions',
  'agent': 'care-coordination assistant that summarizes referrals, identifies missing data, recommends approved next '
           'steps, and escalates clinical decisions',
  'accent': 'healthcare'},
 {'number': 3,
  'industry': 'Nonprofit',
  'title': 'Donor & Volunteer Engagement App',
  'summary': 'An engagement platform for donors, donations, campaigns, volunteers, shifts, acknowledgements, and '
             'outreach.',
  'entities': 'Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement '
              'Score',
  'personas': 'Fundraising Coordinator, Volunteer Manager, Program Manager, Nonprofit Administrator',
  'process': 'donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
             'outreach follow-up',
  'integration': 'real address geocoding for outreach planning',
  'integration_name': 'US Census Geocoding Services',
  'integration_base_url': 'https://geocoding.geo.census.gov/geocoder',
  'integration_docs_url': 'https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html',
  'integration_auth': 'No authentication; use fictional training addresses only',
  'integration_operation': 'send a fictional outreach address to the live Census geocoder, receive matched address and '
                           'coordinates, and store the standardized location for outreach planning',
  'integration_path': '/geographies/onelineaddress?address={encoded-address}&benchmark=Public_AR_Current&vintage=Current_Current&format=json',
  'workspace': 'engagement dashboard with campaign results, donor history, volunteer availability, mapped outreach '
               'locations, and required follow-up',
  'agent': 'engagement assistant that summarizes donor and volunteer activity, identifies follow-up opportunities, '
           'drafts approved communications, and escalates sensitive outreach',
  'accent': 'nonprofit'},
 {'number': 4,
  'industry': 'Manufacturing',
  'title': 'Production & Quality Operations App',
  'summary': 'A manufacturing workspace for production orders, work centers, material requirements, quality '
             'inspections, downtime, and finished-goods release.',
  'entities': 'Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, '
              'Downtime Event, Finished Good',
  'personas': 'Production Planner, Line Supervisor, Quality Inspector, Plant Manager',
  'process': 'production planning, material readiness, work-center scheduling, execution, quality inspection, downtime '
             'response, and finished-goods release',
  'integration': 'live manufacturer information lookup',
  'integration_name': 'NHTSA vPIC API',
  'integration_base_url': 'https://vpic.nhtsa.dot.gov/api',
  'integration_docs_url': 'https://vpic.nhtsa.dot.gov/api/',
  'integration_auth': 'No authentication for public endpoints',
  'integration_operation': 'send a manufacturer name or identifier to the live NHTSA vPIC API, receive manufacturer '
                           'details, and enrich the Supplier or Manufacturer record used by the production plan',
  'integration_path': '/vehicles/getallmanufacturers?format=json',
  'workspace': 'production control board with material readiness, work-center schedule, quality holds, downtime '
               'events, and release actions',
  'agent': 'production operations assistant that summarizes schedule risk, material shortages, quality holds, and '
           'downtime, invokes approved task actions, and escalates release decisions',
  'accent': 'manufacturing'},
 {'number': 5,
  'industry': 'Professional Services',
  'title': 'AI-Enabled Client Delivery App',
  'summary': 'A client-delivery workspace for projects, milestones, resource assignments, time, risks, deliverables, '
             'and AI-assisted coordination.',
  'entities': 'Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update',
  'personas': 'Consultant, Project Manager, Delivery Director, Services Administrator',
  'process': 'project intake, milestone planning, resource assignment, time tracking, risk management, deliverable '
             'approval, and client communication',
  'integration': 'real software-delivery activity synchronization',
  'integration_name': 'GitHub REST API',
  'integration_base_url': 'https://api.github.com',
  'integration_docs_url': 'https://docs.github.com/en/rest',
  'integration_auth': 'No authentication for a public training repository, or instructor-provided token through an '
                      'External Credential for higher limits',
  'integration_operation': 'call a live public training repository endpoint, receive issues or milestones, and create '
                           'or update corresponding Project Risks and Milestones in Salesforce',
  'integration_path': '/repos/{owner}/{repository}/issues',
  'workspace': 'delivery workbench with milestone health, resource allocation, risks, deliverables, and client-update '
               'actions',
  'agent': 'client-delivery assistant that summarizes project health, identifies risks and missing updates, invokes '
           'approved actions, and escalates commercial or delivery decisions',
  'accent': 'services'}]

PROJECT_MILESTONES = {1: [{'week_number': 1,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Translate the '
                      'classroom project into personas, user journeys, user stories, acceptance criteria, success '
                      'measures, scope boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance '
                     'criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Design the application data model',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Create the '
                      'standard and custom object model, relationships, ownership strategy, external IDs, reporting '
                      'considerations, and a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample records, '
                     'and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Add validation, '
                      'formulas, duplicate prevention, record types, conditional visibility, required-data controls, '
                      'and user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, and a '
                     'data-quality decision log.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Configure persona-based security',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Design access for '
                      'Warehouse Associate, Inventory Controller, Logistics Coordinator, Operations Manager. Create '
                      'least-privilege access for the project personas using permission sets, permission set groups, '
                      'sharing, field-level security, and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, and '
                     'documented exceptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Automate the core business process',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Build declarative '
                      'automation for the end-to-end process using before-save, after-save, screen, scheduled, and '
                      'reusable Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an '
                     'end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Build the Apex service layer',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Create '
                      'maintainable Apex domain and service classes for business rules that should not live entirely '
                      'in Flow. Validate inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design rationale, and '
                     'unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Create efficient data access',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Implement '
                      'selective SOQL, relationship queries, aggregates, search, and data-access utilities for '
                      'operational views, missing-data detection, and reporting.',
      'deliverable': 'Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and '
                     'large-volume considerations.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Implement transaction orchestration',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Add bulk-safe '
                      'trigger and handler logic for status changes, related-record coordination, duplicate '
                      'prevention, and transaction-safe updates.',
      'deliverable': 'Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback '
                     'reasoning, and transaction tests.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Harden Apex security',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Review the service '
                      'and data-access layers for sharing, user mode, CRUD, field-level security, secure dynamic SOQL, '
                      'validation, and sensitive-data exposure.',
      'deliverable': 'A security review report, corrected code, permission-based tests, injection tests, and a '
                     'documented threat model.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Create the automated test framework',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Build reusable '
                      'test data, positive and negative tests, bulk tests, permission tests, asynchronous tests, and '
                      'meaningful assertions across the application.',
      'deliverable': 'A test-data factory, behavior-focused test classes, coverage summary, test matrix, and '
                     'documented residual risk.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Connect to the '
                      'live Zippopotam.us Postal Code API at https://api.zippopotam.us using a Named Credential. The '
                      'classroom operation is to send a shipment country code and postal code to the live API, receive '
                      'city, state, latitude, and longitude, and store the validated destination on the Shipment. Use '
                      'training data only. Configure a Named Credential and External Credential, execute a genuine '
                      'training callout, map the live response into Salesforce, and use HttpCalloutMock only inside '
                      'automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce '
                     'record, integration log, test mocks, retry evidence, sequence diagram, and recovery '
                     'demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. The primary '
                      'experience is a warehouse control tower with receiving queues, bin availability, pick waves, '
                      'shipment readiness, and exceptions. Build the application main user workspace with modern '
                      'JavaScript, accessible Lightning components, clear loading and error states, and responsive '
                      'behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and '
                     'stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. The primary '
                      'experience is a warehouse control tower with receiving queues, bin availability, pick waves, '
                      'shipment readiness, and exceptions. Extend the workspace with communicating components, '
                      'Lightning Data Service or Apex data access, search, filtering, files, reusable utilities, '
                      'caching, and performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, performance notes, '
                     'and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Prepare the release',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Complete the '
                      'feature-branch workflow, pull request, review corrections, static analysis, deployment '
                      'validation, permission packaging, rollback plan, and post-deployment checks.',
      'deliverable': 'Git history, pull request evidence, analysis results, deployment package, release notes, '
                     'rollback plan, and production-readiness checklist.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Add AI-assisted and MCP-enabled operations',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Use a controlled '
                      'AI-assisted development workflow, configure approved MCP or CLI tools, define reusable agent '
                      'instructions or skills, and validate least-privilege access.',
      'deliverable': 'Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable '
                     'instructions, execution evidence, and an AI-risk review.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the Agentforce-enabled application',
      'instructions': 'For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory '
                      'Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle '
                      'counting, replenishment, picking, packing, shipping, and exception handling. Complete a '
                      'warehouse operations assistant that summarizes inventory risk, identifies blocked shipments, '
                      'invokes approved replenishment or task actions, and escalates operational decisions. Integrate '
                      'the full application, add the approved agent experience, test guardrails and escalation, '
                      'complete monitoring and documentation, and present the production-ready solution.',
      'deliverable': 'The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, '
                     'architecture documentation, user guide, Git repository, and final classroom demonstration.',
      'is_final': 1}],
 2: [{'week_number': 1,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Translate the classroom project into personas, user journeys, user '
                      'stories, acceptance criteria, success measures, scope boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance '
                     'criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Design the application data model',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Create the standard and custom object model, relationships, '
                      'ownership strategy, external IDs, reporting considerations, and a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample records, '
                     'and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Add validation, formulas, duplicate prevention, record types, '
                      'conditional visibility, required-data controls, and user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, and a '
                     'data-quality decision log.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Configure persona-based security',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Design access for Referral Coordinator, Care Coordinator, Clinical '
                      'Reviewer, Program Administrator. Create least-privilege access for the project personas using '
                      'permission sets, permission set groups, sharing, field-level security, and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, and '
                     'documented exceptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Automate the core business process',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Build declarative automation for the end-to-end process using '
                      'before-save, after-save, screen, scheduled, and reusable Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an '
                     'end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Build the Apex service layer',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Create maintainable Apex domain and service classes for business '
                      'rules that should not live entirely in Flow. Validate inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design rationale, and '
                     'unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Create efficient data access',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Implement selective SOQL, relationship queries, aggregates, '
                      'search, and data-access utilities for operational views, missing-data detection, and reporting.',
      'deliverable': 'Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and '
                     'large-volume considerations.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Implement transaction orchestration',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Add bulk-safe trigger and handler logic for status changes, '
                      'related-record coordination, duplicate prevention, and transaction-safe updates.',
      'deliverable': 'Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback '
                     'reasoning, and transaction tests.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Harden Apex security',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Review the service and data-access layers for sharing, user mode, '
                      'CRUD, field-level security, secure dynamic SOQL, validation, and sensitive-data exposure.',
      'deliverable': 'A security review report, corrected code, permission-based tests, injection tests, and a '
                     'documented threat model.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Create the automated test framework',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Build reusable test data, positive and negative tests, bulk tests, '
                      'permission tests, asynchronous tests, and meaningful assertions across the application.',
      'deliverable': 'A test-data factory, behavior-focused test classes, coverage summary, test matrix, and '
                     'documented residual risk.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Connect to the live CMS NPI Registry API at '
                      'https://npiregistry.cms.hhs.gov/api using a Named Credential. The classroom operation is to '
                      'send a training provider NPI or search criteria to the live CMS registry, receive provider '
                      'identity and practice-location data, and update the Provider validation fields. Use training '
                      'data only. Configure a Named Credential and External Credential, execute a genuine training '
                      'callout, map the live response into Salesforce, and use HttpCalloutMock only inside automated '
                      'tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce '
                     'record, integration log, test mocks, retry evidence, sequence diagram, and recovery '
                     'demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. The primary experience is a care-coordination workbench with '
                      'patient context, referral status, provider validation, missing information, and next actions. '
                      'Build the application main user workspace with modern JavaScript, accessible Lightning '
                      'components, clear loading and error states, and responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and '
                     'stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. The primary experience is a care-coordination workbench with '
                      'patient context, referral status, provider validation, missing information, and next actions. '
                      'Extend the workspace with communicating components, Lightning Data Service or Apex data access, '
                      'search, filtering, files, reusable utilities, caching, and performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, performance notes, '
                     'and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Prepare the release',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Complete the feature-branch workflow, pull request, review '
                      'corrections, static analysis, deployment validation, permission packaging, rollback plan, and '
                      'post-deployment checks.',
      'deliverable': 'Git history, pull request evidence, analysis results, deployment package, release notes, '
                     'rollback plan, and production-readiness checklist.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Add AI-assisted and MCP-enabled operations',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Use a controlled AI-assisted development workflow, configure '
                      'approved MCP or CLI tools, define reusable agent instructions or skills, and validate '
                      'least-privilege access.',
      'deliverable': 'Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable '
                     'instructions, execution evidence, and an AI-risk review.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the Agentforce-enabled application',
      'instructions': 'For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, '
                      'Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral '
                      'intake, provider validation, eligibility review, authorization, care assignment, appointment '
                      'coordination, and follow-up. Complete a care-coordination assistant that summarizes referrals, '
                      'identifies missing data, recommends approved next steps, and escalates clinical decisions. '
                      'Integrate the full application, add the approved agent experience, test guardrails and '
                      'escalation, complete monitoring and documentation, and present the production-ready solution.',
      'deliverable': 'The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, '
                     'architecture documentation, user guide, Git repository, and final classroom demonstration.',
      'is_final': 1}],
 3: [{'week_number': 1,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Translate the classroom project into personas, user journeys, user stories, '
                      'acceptance criteria, success measures, scope boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance '
                     'criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Design the application data model',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Create the standard and custom object model, relationships, ownership '
                      'strategy, external IDs, reporting considerations, and a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample records, '
                     'and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Add validation, formulas, duplicate prevention, record types, conditional '
                      'visibility, required-data controls, and user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, and a '
                     'data-quality decision log.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Configure persona-based security',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Design access for Fundraising Coordinator, Volunteer Manager, Program '
                      'Manager, Nonprofit Administrator. Create least-privilege access for the project personas using '
                      'permission sets, permission set groups, sharing, field-level security, and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, and '
                     'documented exceptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Automate the core business process',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Build declarative automation for the end-to-end process using before-save, '
                      'after-save, screen, scheduled, and reusable Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an '
                     'end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Build the Apex service layer',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Create maintainable Apex domain and service classes for business rules that '
                      'should not live entirely in Flow. Validate inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design rationale, and '
                     'unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Create efficient data access',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Implement selective SOQL, relationship queries, aggregates, search, and '
                      'data-access utilities for operational views, missing-data detection, and reporting.',
      'deliverable': 'Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and '
                     'large-volume considerations.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Implement transaction orchestration',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Add bulk-safe trigger and handler logic for status changes, related-record '
                      'coordination, duplicate prevention, and transaction-safe updates.',
      'deliverable': 'Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback '
                     'reasoning, and transaction tests.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Harden Apex security',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Review the service and data-access layers for sharing, user mode, CRUD, '
                      'field-level security, secure dynamic SOQL, validation, and sensitive-data exposure.',
      'deliverable': 'A security review report, corrected code, permission-based tests, injection tests, and a '
                     'documented threat model.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Create the automated test framework',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Build reusable test data, positive and negative tests, bulk tests, '
                      'permission tests, asynchronous tests, and meaningful assertions across the application.',
      'deliverable': 'A test-data factory, behavior-focused test classes, coverage summary, test matrix, and '
                     'documented residual risk.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Connect to the live US Census Geocoding Services at '
                      'https://geocoding.geo.census.gov/geocoder using a Named Credential. The classroom operation is '
                      'to send a fictional outreach address to the live Census geocoder, receive matched address and '
                      'coordinates, and store the standardized location for outreach planning. Use training data only. '
                      'Configure a Named Credential and External Credential, execute a genuine training callout, map '
                      'the live response into Salesforce, and use HttpCalloutMock only inside automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce '
                     'record, integration log, test mocks, retry evidence, sequence diagram, and recovery '
                     'demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. The primary experience is a engagement dashboard with campaign results, '
                      'donor history, volunteer availability, mapped outreach locations, and required follow-up. Build '
                      'the application main user workspace with modern JavaScript, accessible Lightning components, '
                      'clear loading and error states, and responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and '
                     'stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. The primary experience is a engagement dashboard with campaign results, '
                      'donor history, volunteer availability, mapped outreach locations, and required follow-up. '
                      'Extend the workspace with communicating components, Lightning Data Service or Apex data access, '
                      'search, filtering, files, reusable utilities, caching, and performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, performance notes, '
                     'and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Prepare the release',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Complete the feature-branch workflow, pull request, review corrections, '
                      'static analysis, deployment validation, permission packaging, rollback plan, and '
                      'post-deployment checks.',
      'deliverable': 'Git history, pull request evidence, analysis results, deployment package, release notes, '
                     'rollback plan, and production-readiness checklist.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Add AI-assisted and MCP-enabled operations',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Use a controlled AI-assisted development workflow, configure approved MCP '
                      'or CLI tools, define reusable agent instructions or skills, and validate least-privilege '
                      'access.',
      'deliverable': 'Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable '
                     'instructions, execution evidence, and an AI-risk review.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the Agentforce-enabled application',
      'instructions': 'For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, '
                      'Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor '
                      'engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and '
                      'outreach follow-up. Complete a engagement assistant that summarizes donor and volunteer '
                      'activity, identifies follow-up opportunities, drafts approved communications, and escalates '
                      'sensitive outreach. Integrate the full application, add the approved agent experience, test '
                      'guardrails and escalation, complete monitoring and documentation, and present the '
                      'production-ready solution.',
      'deliverable': 'The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, '
                     'architecture documentation, user guide, Git repository, and final classroom demonstration.',
      'is_final': 1}],
 4: [{'week_number': 1,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Translate the classroom project into '
                      'personas, user journeys, user stories, acceptance criteria, success measures, scope boundaries, '
                      'and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance '
                     'criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Design the application data model',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Create the standard and custom '
                      'object model, relationships, ownership strategy, external IDs, reporting considerations, and a '
                      'documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample records, '
                     'and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Add validation, formulas, duplicate '
                      'prevention, record types, conditional visibility, required-data controls, and user-friendly '
                      'error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, and a '
                     'data-quality decision log.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Configure persona-based security',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Design access for Production '
                      'Planner, Line Supervisor, Quality Inspector, Plant Manager. Create least-privilege access for '
                      'the project personas using permission sets, permission set groups, sharing, field-level '
                      'security, and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, and '
                     'documented exceptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Automate the core business process',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Build declarative automation for the '
                      'end-to-end process using before-save, after-save, screen, scheduled, and reusable Flows with '
                      'fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an '
                     'end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Build the Apex service layer',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Create maintainable Apex domain and '
                      'service classes for business rules that should not live entirely in Flow. Validate inputs and '
                      'return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design rationale, and '
                     'unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Create efficient data access',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Implement selective SOQL, '
                      'relationship queries, aggregates, search, and data-access utilities for operational views, '
                      'missing-data detection, and reporting.',
      'deliverable': 'Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and '
                     'large-volume considerations.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Implement transaction orchestration',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Add bulk-safe trigger and handler '
                      'logic for status changes, related-record coordination, duplicate prevention, and '
                      'transaction-safe updates.',
      'deliverable': 'Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback '
                     'reasoning, and transaction tests.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Harden Apex security',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Review the service and data-access '
                      'layers for sharing, user mode, CRUD, field-level security, secure dynamic SOQL, validation, and '
                      'sensitive-data exposure.',
      'deliverable': 'A security review report, corrected code, permission-based tests, injection tests, and a '
                     'documented threat model.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Create the automated test framework',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Build reusable test data, positive '
                      'and negative tests, bulk tests, permission tests, asynchronous tests, and meaningful assertions '
                      'across the application.',
      'deliverable': 'A test-data factory, behavior-focused test classes, coverage summary, test matrix, and '
                     'documented residual risk.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Connect to the live NHTSA vPIC API '
                      'at https://vpic.nhtsa.dot.gov/api using a Named Credential. The classroom operation is to send '
                      'a manufacturer name or identifier to the live NHTSA vPIC API, receive manufacturer details, and '
                      'enrich the Supplier or Manufacturer record used by the production plan. Use training data only. '
                      'Configure a Named Credential and External Credential, execute a genuine training callout, map '
                      'the live response into Salesforce, and use HttpCalloutMock only inside automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce '
                     'record, integration log, test mocks, retry evidence, sequence diagram, and recovery '
                     'demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. The primary experience is a '
                      'production control board with material readiness, work-center schedule, quality holds, downtime '
                      'events, and release actions. Build the application main user workspace with modern JavaScript, '
                      'accessible Lightning components, clear loading and error states, and responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and '
                     'stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. The primary experience is a '
                      'production control board with material readiness, work-center schedule, quality holds, downtime '
                      'events, and release actions. Extend the workspace with communicating components, Lightning Data '
                      'Service or Apex data access, search, filtering, files, reusable utilities, caching, and '
                      'performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, performance notes, '
                     'and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Prepare the release',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Complete the feature-branch '
                      'workflow, pull request, review corrections, static analysis, deployment validation, permission '
                      'packaging, rollback plan, and post-deployment checks.',
      'deliverable': 'Git history, pull request evidence, analysis results, deployment package, release notes, '
                     'rollback plan, and production-readiness checklist.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Add AI-assisted and MCP-enabled operations',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Use a controlled AI-assisted '
                      'development workflow, configure approved MCP or CLI tools, define reusable agent instructions '
                      'or skills, and validate least-privilege access.',
      'deliverable': 'Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable '
                     'instructions, execution evidence, and an AI-risk review.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the Agentforce-enabled application',
      'instructions': 'For the Production & Quality Operations App, use the Plant, Work Center, Production Order, '
                      'Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model '
                      'and support production planning, material readiness, work-center scheduling, execution, quality '
                      'inspection, downtime response, and finished-goods release. Complete a production operations '
                      'assistant that summarizes schedule risk, material shortages, quality holds, and downtime, '
                      'invokes approved task actions, and escalates release decisions. Integrate the full application, '
                      'add the approved agent experience, test guardrails and escalation, complete monitoring and '
                      'documentation, and present the production-ready solution.',
      'deliverable': 'The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, '
                     'architecture documentation, user guide, Git repository, and final classroom demonstration.',
      'is_final': 1}],
 5: [{'week_number': 1,
      'title': 'Define the product vision and backlog',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Translate the classroom project into personas, user journeys, user '
                      'stories, acceptance criteria, success measures, scope boundaries, and a prioritized backlog.',
      'deliverable': 'A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance '
                     'criteria, and initial Salesforce solution diagram.',
      'is_final': 0},
     {'week_number': 2,
      'title': 'Design the application data model',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Create the standard and custom object model, relationships, ownership '
                      'strategy, external IDs, reporting considerations, and a documented schema.',
      'deliverable': 'A complete schema diagram, object-and-field inventory, relationship rationale, sample records, '
                     'and data-volume assumptions.',
      'is_final': 0},
     {'week_number': 3,
      'title': 'Implement data quality and guided entry',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Add validation, formulas, duplicate prevention, record types, '
                      'conditional visibility, required-data controls, and user-friendly error messages.',
      'deliverable': 'Working data-quality controls with positive and negative test evidence, screenshots, and a '
                     'data-quality decision log.',
      'is_final': 0},
     {'week_number': 4,
      'title': 'Configure persona-based security',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Design access for Consultant, Project Manager, Delivery Director, '
                      'Services Administrator. Create least-privilege access for the project personas using permission '
                      'sets, permission set groups, sharing, field-level security, and record-access rules.',
      'deliverable': 'A persona access matrix, security configuration, test users, permission test evidence, and '
                     'documented exceptions.',
      'is_final': 0},
     {'week_number': 5,
      'title': 'Automate the core business process',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Build declarative automation for the end-to-end process using '
                      'before-save, after-save, screen, scheduled, and reusable Flows with fault handling.',
      'deliverable': 'Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an '
                     'end-to-end process demonstration.',
      'is_final': 0},
     {'week_number': 6,
      'title': 'Build the Apex service layer',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Create maintainable Apex domain and service classes for business '
                      'rules that should not live entirely in Flow. Validate inputs and return structured results.',
      'deliverable': 'Apex classes, class diagram, example invocations, exception handling, design rationale, and '
                     'unit-test scaffolding.',
      'is_final': 0},
     {'week_number': 7,
      'title': 'Create efficient data access',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Implement selective SOQL, relationship queries, aggregates, search, '
                      'and data-access utilities for operational views, missing-data detection, and reporting.',
      'deliverable': 'Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and '
                     'large-volume considerations.',
      'is_final': 0},
     {'week_number': 8,
      'title': 'Implement transaction orchestration',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Add bulk-safe trigger and handler logic for status changes, '
                      'related-record coordination, duplicate prevention, and transaction-safe updates.',
      'deliverable': 'Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback '
                     'reasoning, and transaction tests.',
      'is_final': 0},
     {'week_number': 9,
      'title': 'Harden Apex security',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Review the service and data-access layers for sharing, user mode, '
                      'CRUD, field-level security, secure dynamic SOQL, validation, and sensitive-data exposure.',
      'deliverable': 'A security review report, corrected code, permission-based tests, injection tests, and a '
                     'documented threat model.',
      'is_final': 0},
     {'week_number': 10,
      'title': 'Create the automated test framework',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Build reusable test data, positive and negative tests, bulk tests, '
                      'permission tests, asynchronous tests, and meaningful assertions across the application.',
      'deliverable': 'A test-data factory, behavior-focused test classes, coverage summary, test matrix, and '
                     'documented residual risk.',
      'is_final': 0},
     {'week_number': 11,
      'title': 'Connect to a live external API',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Connect to the live GitHub REST API at https://api.github.com using a '
                      'Named Credential. The classroom operation is to call a live public training repository '
                      'endpoint, receive issues or milestones, and create or update corresponding Project Risks and '
                      'Milestones in Salesforce. Use training data only. Configure a Named Credential and External '
                      'Credential, execute a genuine training callout, map the live response into Salesforce, and use '
                      'HttpCalloutMock only inside automated tests.',
      'deliverable': 'A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce '
                     'record, integration log, test mocks, retry evidence, sequence diagram, and recovery '
                     'demonstration.',
      'is_final': 0},
     {'week_number': 12,
      'title': 'Deliver the primary LWC workspace',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. The primary experience is a delivery workbench with milestone health, '
                      'resource allocation, risks, deliverables, and client-update actions. Build the application main '
                      'user workspace with modern JavaScript, accessible Lightning components, clear loading and error '
                      'states, and responsive behavior.',
      'deliverable': 'A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and '
                     'stakeholder-oriented demonstration.',
      'is_final': 0},
     {'week_number': 13,
      'title': 'Add advanced experience and documents',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. The primary experience is a delivery workbench with milestone health, '
                      'resource allocation, risks, deliverables, and client-update actions. Extend the workspace with '
                      'communicating components, Lightning Data Service or Apex data access, search, filtering, files, '
                      'reusable utilities, caching, and performance improvements.',
      'deliverable': 'Advanced LWCs, document or file experience, component-communication evidence, performance notes, '
                     'and Jest tests where practical.',
      'is_final': 0},
     {'week_number': 14,
      'title': 'Prepare the release',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Complete the feature-branch workflow, pull request, review '
                      'corrections, static analysis, deployment validation, permission packaging, rollback plan, and '
                      'post-deployment checks.',
      'deliverable': 'Git history, pull request evidence, analysis results, deployment package, release notes, '
                     'rollback plan, and production-readiness checklist.',
      'is_final': 0},
     {'week_number': 15,
      'title': 'Add AI-assisted and MCP-enabled operations',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Use a controlled AI-assisted development workflow, configure approved '
                      'MCP or CLI tools, define reusable agent instructions or skills, and validate least-privilege '
                      'access.',
      'deliverable': 'Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable '
                     'instructions, execution evidence, and an AI-risk review.',
      'is_final': 0},
     {'week_number': 16,
      'title': 'Complete the Agentforce-enabled application',
      'instructions': 'For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource '
                      'Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, '
                      'milestone planning, resource assignment, time tracking, risk management, deliverable approval, '
                      'and client communication. Complete a client-delivery assistant that summarizes project health, '
                      'identifies risks and missing updates, invokes approved actions, and escalates commercial or '
                      'delivery decisions. Integrate the full application, add the approved agent experience, test '
                      'guardrails and escalation, complete monitoring and documentation, and present the '
                      'production-ready solution.',
      'deliverable': 'The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, '
                     'architecture documentation, user guide, Git repository, and final classroom demonstration.',
      'is_final': 1}]}

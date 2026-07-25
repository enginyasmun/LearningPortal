# Guided Labs Catalog

Every classroom selects one project. Each project has 16 guided labs. Week 11 performs a real API call from Salesforce; mocks are used only in automated tests.

## Project 01: Warehouse Management & Logistics App

**Industry:** Warehouse & Logistics

A complete warehouse operations workspace for receiving, putaway, inventory control, picking, packing, shipping, and delivery exceptions.

**Live integration:** Zippopotam.us Postal Code API  
**Base URL:** `https://api.zippopotam.us`  
**Training operation:** send a shipment country code and postal code to the live API, receive city, state, latitude, and longitude, and store the validated destination on the Shipment

### Week 1: Define the product vision and backlog

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Translate the classroom project into personas, user journeys, user stories, acceptance criteria, success measures, scope boundaries, and a prioritized backlog.

**Guided lab:** Guided Lab: Establish the product and development workspace
**Estimated time:** 4 to 6 hours
**Deliverable:** A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance criteria, and initial Salesforce solution diagram.

### Week 2: Design the application data model

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Create the standard and custom object model, relationships, ownership strategy, external IDs, reporting considerations, and a documented schema.

**Guided lab:** Guided Lab: Build the application data model
**Estimated time:** 5 to 7 hours
**Deliverable:** A complete schema diagram, object-and-field inventory, relationship rationale, sample records, and data-volume assumptions.

### Week 3: Implement data quality and guided entry

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Add validation, formulas, duplicate prevention, record types, conditional visibility, required-data controls, and user-friendly error messages.

**Guided lab:** Guided Lab: Add data quality and guided user entry
**Estimated time:** 4 to 6 hours
**Deliverable:** Working data-quality controls with positive and negative test evidence, screenshots, and a data-quality decision log.

### Week 4: Configure persona-based security

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Design access for Warehouse Associate, Inventory Controller, Logistics Coordinator, Operations Manager. Create least-privilege access for the project personas using permission sets, permission set groups, sharing, field-level security, and record-access rules.

**Guided lab:** Guided Lab: Configure and test least-privilege access
**Estimated time:** 5 to 7 hours
**Deliverable:** A persona access matrix, security configuration, test users, permission test evidence, and documented exceptions.

### Week 5: Automate the core business process

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Build declarative automation for the end-to-end process using before-save, after-save, screen, scheduled, and reusable Flows with fault handling.

**Guided lab:** Guided Lab: Automate the core business process with Flow
**Estimated time:** 6 to 8 hours
**Deliverable:** Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an end-to-end process demonstration.

### Week 6: Build the Apex service layer

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Create maintainable Apex domain and service classes for business rules that should not live entirely in Flow. Validate inputs and return structured results.

**Guided lab:** Guided Lab: Build the Apex service layer
**Estimated time:** 6 to 8 hours
**Deliverable:** Apex classes, class diagram, example invocations, exception handling, design rationale, and unit-test scaffolding.

### Week 7: Create efficient data access

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Implement selective SOQL, relationship queries, aggregates, search, and data-access utilities for operational views, missing-data detection, and reporting.

**Guided lab:** Guided Lab: Create efficient SOQL, SOSL, and data-access utilities
**Estimated time:** 5 to 7 hours
**Deliverable:** Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and large-volume considerations.

### Week 8: Implement transaction orchestration

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Add bulk-safe trigger and handler logic for status changes, related-record coordination, duplicate prevention, and transaction-safe updates.

**Guided lab:** Guided Lab: Implement bulk-safe trigger orchestration
**Estimated time:** 6 to 8 hours
**Deliverable:** Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback reasoning, and transaction tests.

### Week 9: Harden Apex security

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Review the service and data-access layers for sharing, user mode, CRUD, field-level security, secure dynamic SOQL, validation, and sensitive-data exposure.

**Guided lab:** Guided Lab: Harden Apex security
**Estimated time:** 5 to 7 hours
**Deliverable:** A security review report, corrected code, permission-based tests, injection tests, and a documented threat model.

### Week 10: Create the automated test framework

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Build reusable test data, positive and negative tests, bulk tests, permission tests, asynchronous tests, and meaningful assertions across the application.

**Guided lab:** Guided Lab: Create the automated test framework
**Estimated time:** 6 to 9 hours
**Deliverable:** A test-data factory, behavior-focused test classes, coverage summary, test matrix, and documented residual risk.

### Week 11: Connect to a live external API

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Connect to the live Zippopotam.us Postal Code API at https://api.zippopotam.us using a Named Credential. The classroom operation is to send a shipment country code and postal code to the live API, receive city, state, latitude, and longitude, and store the validated destination on the Shipment. Use training data only. Configure a Named Credential and External Credential, execute a genuine training callout, map the live response into Salesforce, and use HttpCalloutMock only inside automated tests.

**Guided lab:** Guided Lab: Connect Salesforce to a live external API
**Estimated time:** 7 to 10 hours
**Deliverable:** A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and recovery demonstration.

### Week 12: Deliver the primary LWC workspace

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. The primary experience is a warehouse control tower with receiving queues, bin availability, pick waves, shipment readiness, and exceptions. Build the application main user workspace with modern JavaScript, accessible Lightning components, clear loading and error states, and responsive behavior.

**Guided lab:** Guided Lab: Build the primary Lightning Web Component workspace
**Estimated time:** 7 to 10 hours
**Deliverable:** A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and stakeholder-oriented demonstration.

### Week 13: Add advanced experience and documents

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. The primary experience is a warehouse control tower with receiving queues, bin availability, pick waves, shipment readiness, and exceptions. Extend the workspace with communicating components, Lightning Data Service or Apex data access, search, filtering, files, reusable utilities, caching, and performance improvements.

**Guided lab:** Guided Lab: Add advanced LWC, search, files, and performance
**Estimated time:** 7 to 10 hours
**Deliverable:** Advanced LWCs, document or file experience, component-communication evidence, performance notes, and Jest tests where practical.

### Week 14: Prepare the release

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Complete the feature-branch workflow, pull request, review corrections, static analysis, deployment validation, permission packaging, rollback plan, and post-deployment checks.

**Guided lab:** Guided Lab: Run the Git, quality, deployment, and release workflow
**Estimated time:** 6 to 8 hours
**Deliverable:** Git history, pull request evidence, analysis results, deployment package, release notes, rollback plan, and production-readiness checklist.

### Week 15: Add AI-assisted and MCP-enabled operations

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Use a controlled AI-assisted development workflow, configure approved MCP or CLI tools, define reusable agent instructions or skills, and validate least-privilege access.

**Guided lab:** Guided Lab: Use AI, MCP, CLI, and reusable agent skills safely
**Estimated time:** 6 to 9 hours
**Deliverable:** Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable instructions, execution evidence, and an AI-risk review.

### Week 16: Complete the Agentforce-enabled application

For the Warehouse Management & Logistics App, use the Warehouse, Zone, Bin, Product, Inventory Item, Stock Movement, Shipment, Carrier Event model and support receiving, putaway, cycle counting, replenishment, picking, packing, shipping, and exception handling. Complete a warehouse operations assistant that summarizes inventory risk, identifies blocked shipments, invokes approved replenishment or task actions, and escalates operational decisions. Integrate the full application, add the approved agent experience, test guardrails and escalation, complete monitoring and documentation, and present the production-ready solution.

**Guided lab:** Guided Lab: Complete, test, and demonstrate the Agentforce-enabled application
**Estimated time:** 10 to 14 hours
**Deliverable:** The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, architecture documentation, user guide, Git repository, and final classroom demonstration.

## Project 02: Patient Referral & Care Coordination App

**Industry:** Healthcare

A referral and care-coordination workspace for patients, providers, eligibility, authorizations, care tasks, and follow-up.

**Live integration:** CMS NPI Registry API  
**Base URL:** `https://npiregistry.cms.hhs.gov/api`  
**Training operation:** send a training provider NPI or search criteria to the live CMS registry, receive provider identity and practice-location data, and update the Provider validation fields

### Week 1: Define the product vision and backlog

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Translate the classroom project into personas, user journeys, user stories, acceptance criteria, success measures, scope boundaries, and a prioritized backlog.

**Guided lab:** Guided Lab: Establish the product and development workspace
**Estimated time:** 4 to 6 hours
**Deliverable:** A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance criteria, and initial Salesforce solution diagram.

### Week 2: Design the application data model

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Create the standard and custom object model, relationships, ownership strategy, external IDs, reporting considerations, and a documented schema.

**Guided lab:** Guided Lab: Build the application data model
**Estimated time:** 5 to 7 hours
**Deliverable:** A complete schema diagram, object-and-field inventory, relationship rationale, sample records, and data-volume assumptions.

### Week 3: Implement data quality and guided entry

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Add validation, formulas, duplicate prevention, record types, conditional visibility, required-data controls, and user-friendly error messages.

**Guided lab:** Guided Lab: Add data quality and guided user entry
**Estimated time:** 4 to 6 hours
**Deliverable:** Working data-quality controls with positive and negative test evidence, screenshots, and a data-quality decision log.

### Week 4: Configure persona-based security

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Design access for Referral Coordinator, Care Coordinator, Clinical Reviewer, Program Administrator. Create least-privilege access for the project personas using permission sets, permission set groups, sharing, field-level security, and record-access rules.

**Guided lab:** Guided Lab: Configure and test least-privilege access
**Estimated time:** 5 to 7 hours
**Deliverable:** A persona access matrix, security configuration, test users, permission test evidence, and documented exceptions.

### Week 5: Automate the core business process

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Build declarative automation for the end-to-end process using before-save, after-save, screen, scheduled, and reusable Flows with fault handling.

**Guided lab:** Guided Lab: Automate the core business process with Flow
**Estimated time:** 6 to 8 hours
**Deliverable:** Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an end-to-end process demonstration.

### Week 6: Build the Apex service layer

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Create maintainable Apex domain and service classes for business rules that should not live entirely in Flow. Validate inputs and return structured results.

**Guided lab:** Guided Lab: Build the Apex service layer
**Estimated time:** 6 to 8 hours
**Deliverable:** Apex classes, class diagram, example invocations, exception handling, design rationale, and unit-test scaffolding.

### Week 7: Create efficient data access

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Implement selective SOQL, relationship queries, aggregates, search, and data-access utilities for operational views, missing-data detection, and reporting.

**Guided lab:** Guided Lab: Create efficient SOQL, SOSL, and data-access utilities
**Estimated time:** 5 to 7 hours
**Deliverable:** Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and large-volume considerations.

### Week 8: Implement transaction orchestration

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Add bulk-safe trigger and handler logic for status changes, related-record coordination, duplicate prevention, and transaction-safe updates.

**Guided lab:** Guided Lab: Implement bulk-safe trigger orchestration
**Estimated time:** 6 to 8 hours
**Deliverable:** Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback reasoning, and transaction tests.

### Week 9: Harden Apex security

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Review the service and data-access layers for sharing, user mode, CRUD, field-level security, secure dynamic SOQL, validation, and sensitive-data exposure.

**Guided lab:** Guided Lab: Harden Apex security
**Estimated time:** 5 to 7 hours
**Deliverable:** A security review report, corrected code, permission-based tests, injection tests, and a documented threat model.

### Week 10: Create the automated test framework

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Build reusable test data, positive and negative tests, bulk tests, permission tests, asynchronous tests, and meaningful assertions across the application.

**Guided lab:** Guided Lab: Create the automated test framework
**Estimated time:** 6 to 9 hours
**Deliverable:** A test-data factory, behavior-focused test classes, coverage summary, test matrix, and documented residual risk.

### Week 11: Connect to a live external API

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Connect to the live CMS NPI Registry API at https://npiregistry.cms.hhs.gov/api using a Named Credential. The classroom operation is to send a training provider NPI or search criteria to the live CMS registry, receive provider identity and practice-location data, and update the Provider validation fields. Use training data only. Configure a Named Credential and External Credential, execute a genuine training callout, map the live response into Salesforce, and use HttpCalloutMock only inside automated tests.

**Guided lab:** Guided Lab: Connect Salesforce to a live external API
**Estimated time:** 7 to 10 hours
**Deliverable:** A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and recovery demonstration.

### Week 12: Deliver the primary LWC workspace

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. The primary experience is a care-coordination workbench with patient context, referral status, provider validation, missing information, and next actions. Build the application main user workspace with modern JavaScript, accessible Lightning components, clear loading and error states, and responsive behavior.

**Guided lab:** Guided Lab: Build the primary Lightning Web Component workspace
**Estimated time:** 7 to 10 hours
**Deliverable:** A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and stakeholder-oriented demonstration.

### Week 13: Add advanced experience and documents

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. The primary experience is a care-coordination workbench with patient context, referral status, provider validation, missing information, and next actions. Extend the workspace with communicating components, Lightning Data Service or Apex data access, search, filtering, files, reusable utilities, caching, and performance improvements.

**Guided lab:** Guided Lab: Add advanced LWC, search, files, and performance
**Estimated time:** 7 to 10 hours
**Deliverable:** Advanced LWCs, document or file experience, component-communication evidence, performance notes, and Jest tests where practical.

### Week 14: Prepare the release

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Complete the feature-branch workflow, pull request, review corrections, static analysis, deployment validation, permission packaging, rollback plan, and post-deployment checks.

**Guided lab:** Guided Lab: Run the Git, quality, deployment, and release workflow
**Estimated time:** 6 to 8 hours
**Deliverable:** Git history, pull request evidence, analysis results, deployment package, release notes, rollback plan, and production-readiness checklist.

### Week 15: Add AI-assisted and MCP-enabled operations

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Use a controlled AI-assisted development workflow, configure approved MCP or CLI tools, define reusable agent instructions or skills, and validate least-privilege access.

**Guided lab:** Guided Lab: Use AI, MCP, CLI, and reusable agent skills safely
**Estimated time:** 6 to 9 hours
**Deliverable:** Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable instructions, execution evidence, and an AI-risk review.

### Week 16: Complete the Agentforce-enabled application

For the Patient Referral & Care Coordination App, use the Patient, Provider, Referral, Eligibility Review, Authorization, Care Task, Appointment, Follow-Up model and support referral intake, provider validation, eligibility review, authorization, care assignment, appointment coordination, and follow-up. Complete a care-coordination assistant that summarizes referrals, identifies missing data, recommends approved next steps, and escalates clinical decisions. Integrate the full application, add the approved agent experience, test guardrails and escalation, complete monitoring and documentation, and present the production-ready solution.

**Guided lab:** Guided Lab: Complete, test, and demonstrate the Agentforce-enabled application
**Estimated time:** 10 to 14 hours
**Deliverable:** The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, architecture documentation, user guide, Git repository, and final classroom demonstration.

## Project 03: Donor & Volunteer Engagement App

**Industry:** Nonprofit

An engagement platform for donors, donations, campaigns, volunteers, shifts, acknowledgements, and outreach.

**Live integration:** US Census Geocoding Services  
**Base URL:** `https://geocoding.geo.census.gov/geocoder`  
**Training operation:** send a fictional outreach address to the live Census geocoder, receive matched address and coordinates, and store the standardized location for outreach planning

### Week 1: Define the product vision and backlog

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Translate the classroom project into personas, user journeys, user stories, acceptance criteria, success measures, scope boundaries, and a prioritized backlog.

**Guided lab:** Guided Lab: Establish the product and development workspace
**Estimated time:** 4 to 6 hours
**Deliverable:** A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance criteria, and initial Salesforce solution diagram.

### Week 2: Design the application data model

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Create the standard and custom object model, relationships, ownership strategy, external IDs, reporting considerations, and a documented schema.

**Guided lab:** Guided Lab: Build the application data model
**Estimated time:** 5 to 7 hours
**Deliverable:** A complete schema diagram, object-and-field inventory, relationship rationale, sample records, and data-volume assumptions.

### Week 3: Implement data quality and guided entry

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Add validation, formulas, duplicate prevention, record types, conditional visibility, required-data controls, and user-friendly error messages.

**Guided lab:** Guided Lab: Add data quality and guided user entry
**Estimated time:** 4 to 6 hours
**Deliverable:** Working data-quality controls with positive and negative test evidence, screenshots, and a data-quality decision log.

### Week 4: Configure persona-based security

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Design access for Fundraising Coordinator, Volunteer Manager, Program Manager, Nonprofit Administrator. Create least-privilege access for the project personas using permission sets, permission set groups, sharing, field-level security, and record-access rules.

**Guided lab:** Guided Lab: Configure and test least-privilege access
**Estimated time:** 5 to 7 hours
**Deliverable:** A persona access matrix, security configuration, test users, permission test evidence, and documented exceptions.

### Week 5: Automate the core business process

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Build declarative automation for the end-to-end process using before-save, after-save, screen, scheduled, and reusable Flows with fault handling.

**Guided lab:** Guided Lab: Automate the core business process with Flow
**Estimated time:** 6 to 8 hours
**Deliverable:** Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an end-to-end process demonstration.

### Week 6: Build the Apex service layer

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Create maintainable Apex domain and service classes for business rules that should not live entirely in Flow. Validate inputs and return structured results.

**Guided lab:** Guided Lab: Build the Apex service layer
**Estimated time:** 6 to 8 hours
**Deliverable:** Apex classes, class diagram, example invocations, exception handling, design rationale, and unit-test scaffolding.

### Week 7: Create efficient data access

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Implement selective SOQL, relationship queries, aggregates, search, and data-access utilities for operational views, missing-data detection, and reporting.

**Guided lab:** Guided Lab: Create efficient SOQL, SOSL, and data-access utilities
**Estimated time:** 5 to 7 hours
**Deliverable:** Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and large-volume considerations.

### Week 8: Implement transaction orchestration

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Add bulk-safe trigger and handler logic for status changes, related-record coordination, duplicate prevention, and transaction-safe updates.

**Guided lab:** Guided Lab: Implement bulk-safe trigger orchestration
**Estimated time:** 6 to 8 hours
**Deliverable:** Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback reasoning, and transaction tests.

### Week 9: Harden Apex security

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Review the service and data-access layers for sharing, user mode, CRUD, field-level security, secure dynamic SOQL, validation, and sensitive-data exposure.

**Guided lab:** Guided Lab: Harden Apex security
**Estimated time:** 5 to 7 hours
**Deliverable:** A security review report, corrected code, permission-based tests, injection tests, and a documented threat model.

### Week 10: Create the automated test framework

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Build reusable test data, positive and negative tests, bulk tests, permission tests, asynchronous tests, and meaningful assertions across the application.

**Guided lab:** Guided Lab: Create the automated test framework
**Estimated time:** 6 to 9 hours
**Deliverable:** A test-data factory, behavior-focused test classes, coverage summary, test matrix, and documented residual risk.

### Week 11: Connect to a live external API

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Connect to the live US Census Geocoding Services at https://geocoding.geo.census.gov/geocoder using a Named Credential. The classroom operation is to send a fictional outreach address to the live Census geocoder, receive matched address and coordinates, and store the standardized location for outreach planning. Use training data only. Configure a Named Credential and External Credential, execute a genuine training callout, map the live response into Salesforce, and use HttpCalloutMock only inside automated tests.

**Guided lab:** Guided Lab: Connect Salesforce to a live external API
**Estimated time:** 7 to 10 hours
**Deliverable:** A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and recovery demonstration.

### Week 12: Deliver the primary LWC workspace

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. The primary experience is a engagement dashboard with campaign results, donor history, volunteer availability, mapped outreach locations, and required follow-up. Build the application main user workspace with modern JavaScript, accessible Lightning components, clear loading and error states, and responsive behavior.

**Guided lab:** Guided Lab: Build the primary Lightning Web Component workspace
**Estimated time:** 7 to 10 hours
**Deliverable:** A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and stakeholder-oriented demonstration.

### Week 13: Add advanced experience and documents

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. The primary experience is a engagement dashboard with campaign results, donor history, volunteer availability, mapped outreach locations, and required follow-up. Extend the workspace with communicating components, Lightning Data Service or Apex data access, search, filtering, files, reusable utilities, caching, and performance improvements.

**Guided lab:** Guided Lab: Add advanced LWC, search, files, and performance
**Estimated time:** 7 to 10 hours
**Deliverable:** Advanced LWCs, document or file experience, component-communication evidence, performance notes, and Jest tests where practical.

### Week 14: Prepare the release

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Complete the feature-branch workflow, pull request, review corrections, static analysis, deployment validation, permission packaging, rollback plan, and post-deployment checks.

**Guided lab:** Guided Lab: Run the Git, quality, deployment, and release workflow
**Estimated time:** 6 to 8 hours
**Deliverable:** Git history, pull request evidence, analysis results, deployment package, release notes, rollback plan, and production-readiness checklist.

### Week 15: Add AI-assisted and MCP-enabled operations

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Use a controlled AI-assisted development workflow, configure approved MCP or CLI tools, define reusable agent instructions or skills, and validate least-privilege access.

**Guided lab:** Guided Lab: Use AI, MCP, CLI, and reusable agent skills safely
**Estimated time:** 6 to 9 hours
**Deliverable:** Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable instructions, execution evidence, and an AI-risk review.

### Week 16: Complete the Agentforce-enabled application

For the Donor & Volunteer Engagement App, use the Donor, Donation, Campaign, Volunteer, Volunteer Shift, Acknowledgement, Outreach Activity, Engagement Score model and support donor engagement, donation processing, volunteer registration, shift assignment, acknowledgement, and outreach follow-up. Complete a engagement assistant that summarizes donor and volunteer activity, identifies follow-up opportunities, drafts approved communications, and escalates sensitive outreach. Integrate the full application, add the approved agent experience, test guardrails and escalation, complete monitoring and documentation, and present the production-ready solution.

**Guided lab:** Guided Lab: Complete, test, and demonstrate the Agentforce-enabled application
**Estimated time:** 10 to 14 hours
**Deliverable:** The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, architecture documentation, user guide, Git repository, and final classroom demonstration.

## Project 04: Production & Quality Operations App

**Industry:** Manufacturing

A manufacturing workspace for production orders, work centers, material requirements, quality inspections, downtime, and finished-goods release.

**Live integration:** NHTSA vPIC API  
**Base URL:** `https://vpic.nhtsa.dot.gov/api`  
**Training operation:** send a manufacturer name or identifier to the live NHTSA vPIC API, receive manufacturer details, and enrich the Supplier or Manufacturer record used by the production plan

### Week 1: Define the product vision and backlog

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Translate the classroom project into personas, user journeys, user stories, acceptance criteria, success measures, scope boundaries, and a prioritized backlog.

**Guided lab:** Guided Lab: Establish the product and development workspace
**Estimated time:** 4 to 6 hours
**Deliverable:** A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance criteria, and initial Salesforce solution diagram.

### Week 2: Design the application data model

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Create the standard and custom object model, relationships, ownership strategy, external IDs, reporting considerations, and a documented schema.

**Guided lab:** Guided Lab: Build the application data model
**Estimated time:** 5 to 7 hours
**Deliverable:** A complete schema diagram, object-and-field inventory, relationship rationale, sample records, and data-volume assumptions.

### Week 3: Implement data quality and guided entry

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Add validation, formulas, duplicate prevention, record types, conditional visibility, required-data controls, and user-friendly error messages.

**Guided lab:** Guided Lab: Add data quality and guided user entry
**Estimated time:** 4 to 6 hours
**Deliverable:** Working data-quality controls with positive and negative test evidence, screenshots, and a data-quality decision log.

### Week 4: Configure persona-based security

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Design access for Production Planner, Line Supervisor, Quality Inspector, Plant Manager. Create least-privilege access for the project personas using permission sets, permission set groups, sharing, field-level security, and record-access rules.

**Guided lab:** Guided Lab: Configure and test least-privilege access
**Estimated time:** 5 to 7 hours
**Deliverable:** A persona access matrix, security configuration, test users, permission test evidence, and documented exceptions.

### Week 5: Automate the core business process

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Build declarative automation for the end-to-end process using before-save, after-save, screen, scheduled, and reusable Flows with fault handling.

**Guided lab:** Guided Lab: Automate the core business process with Flow
**Estimated time:** 6 to 8 hours
**Deliverable:** Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an end-to-end process demonstration.

### Week 6: Build the Apex service layer

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Create maintainable Apex domain and service classes for business rules that should not live entirely in Flow. Validate inputs and return structured results.

**Guided lab:** Guided Lab: Build the Apex service layer
**Estimated time:** 6 to 8 hours
**Deliverable:** Apex classes, class diagram, example invocations, exception handling, design rationale, and unit-test scaffolding.

### Week 7: Create efficient data access

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Implement selective SOQL, relationship queries, aggregates, search, and data-access utilities for operational views, missing-data detection, and reporting.

**Guided lab:** Guided Lab: Create efficient SOQL, SOSL, and data-access utilities
**Estimated time:** 5 to 7 hours
**Deliverable:** Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and large-volume considerations.

### Week 8: Implement transaction orchestration

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Add bulk-safe trigger and handler logic for status changes, related-record coordination, duplicate prevention, and transaction-safe updates.

**Guided lab:** Guided Lab: Implement bulk-safe trigger orchestration
**Estimated time:** 6 to 8 hours
**Deliverable:** Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback reasoning, and transaction tests.

### Week 9: Harden Apex security

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Review the service and data-access layers for sharing, user mode, CRUD, field-level security, secure dynamic SOQL, validation, and sensitive-data exposure.

**Guided lab:** Guided Lab: Harden Apex security
**Estimated time:** 5 to 7 hours
**Deliverable:** A security review report, corrected code, permission-based tests, injection tests, and a documented threat model.

### Week 10: Create the automated test framework

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Build reusable test data, positive and negative tests, bulk tests, permission tests, asynchronous tests, and meaningful assertions across the application.

**Guided lab:** Guided Lab: Create the automated test framework
**Estimated time:** 6 to 9 hours
**Deliverable:** A test-data factory, behavior-focused test classes, coverage summary, test matrix, and documented residual risk.

### Week 11: Connect to a live external API

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Connect to the live NHTSA vPIC API at https://vpic.nhtsa.dot.gov/api using a Named Credential. The classroom operation is to send a manufacturer name or identifier to the live NHTSA vPIC API, receive manufacturer details, and enrich the Supplier or Manufacturer record used by the production plan. Use training data only. Configure a Named Credential and External Credential, execute a genuine training callout, map the live response into Salesforce, and use HttpCalloutMock only inside automated tests.

**Guided lab:** Guided Lab: Connect Salesforce to a live external API
**Estimated time:** 7 to 10 hours
**Deliverable:** A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and recovery demonstration.

### Week 12: Deliver the primary LWC workspace

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. The primary experience is a production control board with material readiness, work-center schedule, quality holds, downtime events, and release actions. Build the application main user workspace with modern JavaScript, accessible Lightning components, clear loading and error states, and responsive behavior.

**Guided lab:** Guided Lab: Build the primary Lightning Web Component workspace
**Estimated time:** 7 to 10 hours
**Deliverable:** A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and stakeholder-oriented demonstration.

### Week 13: Add advanced experience and documents

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. The primary experience is a production control board with material readiness, work-center schedule, quality holds, downtime events, and release actions. Extend the workspace with communicating components, Lightning Data Service or Apex data access, search, filtering, files, reusable utilities, caching, and performance improvements.

**Guided lab:** Guided Lab: Add advanced LWC, search, files, and performance
**Estimated time:** 7 to 10 hours
**Deliverable:** Advanced LWCs, document or file experience, component-communication evidence, performance notes, and Jest tests where practical.

### Week 14: Prepare the release

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Complete the feature-branch workflow, pull request, review corrections, static analysis, deployment validation, permission packaging, rollback plan, and post-deployment checks.

**Guided lab:** Guided Lab: Run the Git, quality, deployment, and release workflow
**Estimated time:** 6 to 8 hours
**Deliverable:** Git history, pull request evidence, analysis results, deployment package, release notes, rollback plan, and production-readiness checklist.

### Week 15: Add AI-assisted and MCP-enabled operations

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Use a controlled AI-assisted development workflow, configure approved MCP or CLI tools, define reusable agent instructions or skills, and validate least-privilege access.

**Guided lab:** Guided Lab: Use AI, MCP, CLI, and reusable agent skills safely
**Estimated time:** 6 to 9 hours
**Deliverable:** Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable instructions, execution evidence, and an AI-risk review.

### Week 16: Complete the Agentforce-enabled application

For the Production & Quality Operations App, use the Plant, Work Center, Production Order, Material Requirement, Production Run, Quality Inspection, Downtime Event, Finished Good model and support production planning, material readiness, work-center scheduling, execution, quality inspection, downtime response, and finished-goods release. Complete a production operations assistant that summarizes schedule risk, material shortages, quality holds, and downtime, invokes approved task actions, and escalates release decisions. Integrate the full application, add the approved agent experience, test guardrails and escalation, complete monitoring and documentation, and present the production-ready solution.

**Guided lab:** Guided Lab: Complete, test, and demonstrate the Agentforce-enabled application
**Estimated time:** 10 to 14 hours
**Deliverable:** The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, architecture documentation, user guide, Git repository, and final classroom demonstration.

## Project 05: AI-Enabled Client Delivery App

**Industry:** Professional Services

A client-delivery workspace for projects, milestones, resource assignments, time, risks, deliverables, and AI-assisted coordination.

**Live integration:** GitHub REST API  
**Base URL:** `https://api.github.com`  
**Training operation:** call a live public training repository endpoint, receive issues or milestones, and create or update corresponding Project Risks and Milestones in Salesforce

### Week 1: Define the product vision and backlog

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Translate the classroom project into personas, user journeys, user stories, acceptance criteria, success measures, scope boundaries, and a prioritized backlog.

**Guided lab:** Guided Lab: Establish the product and development workspace
**Estimated time:** 4 to 6 hours
**Deliverable:** A classroom-approved product brief, persona set, process map, prioritized backlog, acceptance criteria, and initial Salesforce solution diagram.

### Week 2: Design the application data model

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Create the standard and custom object model, relationships, ownership strategy, external IDs, reporting considerations, and a documented schema.

**Guided lab:** Guided Lab: Build the application data model
**Estimated time:** 5 to 7 hours
**Deliverable:** A complete schema diagram, object-and-field inventory, relationship rationale, sample records, and data-volume assumptions.

### Week 3: Implement data quality and guided entry

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Add validation, formulas, duplicate prevention, record types, conditional visibility, required-data controls, and user-friendly error messages.

**Guided lab:** Guided Lab: Add data quality and guided user entry
**Estimated time:** 4 to 6 hours
**Deliverable:** Working data-quality controls with positive and negative test evidence, screenshots, and a data-quality decision log.

### Week 4: Configure persona-based security

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Design access for Consultant, Project Manager, Delivery Director, Services Administrator. Create least-privilege access for the project personas using permission sets, permission set groups, sharing, field-level security, and record-access rules.

**Guided lab:** Guided Lab: Configure and test least-privilege access
**Estimated time:** 5 to 7 hours
**Deliverable:** A persona access matrix, security configuration, test users, permission test evidence, and documented exceptions.

### Week 5: Automate the core business process

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Build declarative automation for the end-to-end process using before-save, after-save, screen, scheduled, and reusable Flows with fault handling.

**Guided lab:** Guided Lab: Automate the core business process with Flow
**Estimated time:** 6 to 8 hours
**Deliverable:** Working Flows, an automation diagram, fault-path evidence, recursion considerations, and an end-to-end process demonstration.

### Week 6: Build the Apex service layer

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Create maintainable Apex domain and service classes for business rules that should not live entirely in Flow. Validate inputs and return structured results.

**Guided lab:** Guided Lab: Build the Apex service layer
**Estimated time:** 6 to 8 hours
**Deliverable:** Apex classes, class diagram, example invocations, exception handling, design rationale, and unit-test scaffolding.

### Week 7: Create efficient data access

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Implement selective SOQL, relationship queries, aggregates, search, and data-access utilities for operational views, missing-data detection, and reporting.

**Guided lab:** Guided Lab: Create efficient SOQL, SOSL, and data-access utilities
**Estimated time:** 5 to 7 hours
**Deliverable:** Query examples, data-access classes, aggregate outputs, query-plan evidence where useful, and large-volume considerations.

### Week 8: Implement transaction orchestration

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Add bulk-safe trigger and handler logic for status changes, related-record coordination, duplicate prevention, and transaction-safe updates.

**Guided lab:** Guided Lab: Implement bulk-safe trigger orchestration
**Estimated time:** 6 to 8 hours
**Deliverable:** Trigger, handler, and service code with bulk evidence, recursion strategy, savepoint or rollback reasoning, and transaction tests.

### Week 9: Harden Apex security

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Review the service and data-access layers for sharing, user mode, CRUD, field-level security, secure dynamic SOQL, validation, and sensitive-data exposure.

**Guided lab:** Guided Lab: Harden Apex security
**Estimated time:** 5 to 7 hours
**Deliverable:** A security review report, corrected code, permission-based tests, injection tests, and a documented threat model.

### Week 10: Create the automated test framework

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Build reusable test data, positive and negative tests, bulk tests, permission tests, asynchronous tests, and meaningful assertions across the application.

**Guided lab:** Guided Lab: Create the automated test framework
**Estimated time:** 6 to 9 hours
**Deliverable:** A test-data factory, behavior-focused test classes, coverage summary, test matrix, and documented residual risk.

### Week 11: Connect to a live external API

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Connect to the live GitHub REST API at https://api.github.com using a Named Credential. The classroom operation is to call a live public training repository endpoint, receive issues or milestones, and create or update corresponding Project Risks and Milestones in Salesforce. Use training data only. Configure a Named Credential and External Credential, execute a genuine training callout, map the live response into Salesforce, and use HttpCalloutMock only inside automated tests.

**Guided lab:** Guided Lab: Connect Salesforce to a live external API
**Estimated time:** 7 to 10 hours
**Deliverable:** A redacted Named Credential setup, successful live HTTP response evidence, mapped Salesforce record, integration log, test mocks, retry evidence, sequence diagram, and recovery demonstration.

### Week 12: Deliver the primary LWC workspace

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. The primary experience is a delivery workbench with milestone health, resource allocation, risks, deliverables, and client-update actions. Build the application main user workspace with modern JavaScript, accessible Lightning components, clear loading and error states, and responsive behavior.

**Guided lab:** Guided Lab: Build the primary Lightning Web Component workspace
**Estimated time:** 7 to 10 hours
**Deliverable:** A functioning LWC workspace, component diagram, responsive screenshots, accessibility notes, and stakeholder-oriented demonstration.

### Week 13: Add advanced experience and documents

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. The primary experience is a delivery workbench with milestone health, resource allocation, risks, deliverables, and client-update actions. Extend the workspace with communicating components, Lightning Data Service or Apex data access, search, filtering, files, reusable utilities, caching, and performance improvements.

**Guided lab:** Guided Lab: Add advanced LWC, search, files, and performance
**Estimated time:** 7 to 10 hours
**Deliverable:** Advanced LWCs, document or file experience, component-communication evidence, performance notes, and Jest tests where practical.

### Week 14: Prepare the release

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Complete the feature-branch workflow, pull request, review corrections, static analysis, deployment validation, permission packaging, rollback plan, and post-deployment checks.

**Guided lab:** Guided Lab: Run the Git, quality, deployment, and release workflow
**Estimated time:** 6 to 8 hours
**Deliverable:** Git history, pull request evidence, analysis results, deployment package, release notes, rollback plan, and production-readiness checklist.

### Week 15: Add AI-assisted and MCP-enabled operations

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Use a controlled AI-assisted development workflow, configure approved MCP or CLI tools, define reusable agent instructions or skills, and validate least-privilege access.

**Guided lab:** Guided Lab: Use AI, MCP, CLI, and reusable agent skills safely
**Estimated time:** 6 to 9 hours
**Deliverable:** Reviewed AI-generated output, corrected code, MCP or CLI configuration, permissions, reusable instructions, execution evidence, and an AI-risk review.

### Week 16: Complete the Agentforce-enabled application

For the AI-Enabled Client Delivery App, use the Client, Project, Milestone, Resource Assignment, Time Entry, Risk, Deliverable, Client Update model and support project intake, milestone planning, resource assignment, time tracking, risk management, deliverable approval, and client communication. Complete a client-delivery assistant that summarizes project health, identifies risks and missing updates, invokes approved actions, and escalates commercial or delivery decisions. Integrate the full application, add the approved agent experience, test guardrails and escalation, complete monitoring and documentation, and present the production-ready solution.

**Guided lab:** Guided Lab: Complete, test, and demonstrate the Agentforce-enabled application
**Estimated time:** 10 to 14 hours
**Deliverable:** The complete deployed application, Agentforce configuration, guardrail tests, monitoring plan, architecture documentation, user guide, Git repository, and final classroom demonstration.

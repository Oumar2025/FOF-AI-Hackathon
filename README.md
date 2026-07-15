
---

# FOF-AI PROJECT HANDOVER DOCUMENT

## Part 1 – Project Overview & Architecture

---

# Project Name

**FOF-AI**
**AI Business Intelligence Assistant for Food Import & Export Companies**

Developed for:

**ETS FOFANA CONFISERIE**

---

# Purpose of This Document

This document is **NOT** the public README of the project.

It is an internal developer handover report written to explain the complete project to another ChatGPT/developer so development can continue without losing context.

The project has evolved through many development sessions, so this report explains:

* business background
* architecture
* AI philosophy
* database
* roadmap
* current progress
* future direction

The next ChatGPT should read this document first before writing any code.

---

# Project Background

This project is being developed specifically for my father's company.

Company:

**ETS FOFANA CONFISERIE**

The company imports food products from different countries and exports/distributes them across West Africa.

Current supplier countries include:

* Turkey
* Morocco
* Tunisia
* Brazil

Current destination countries include:

* Mali
* Burkina Faso
* Côte d'Ivoire
* Angola

Products include:

* Biscuits
* Chocolate
* Candy
* Dates

The company currently manages inventory manually.

The goal is to build an AI assistant capable of helping manage imports, inventory, forecasting and business decisions.

---

# Hackathon

This project is being developed for the

**Build with Gemma AI Hackathon**

Therefore,

Artificial Intelligence is the center of the project.

The application should NOT become just another inventory management system.

Instead, every feature should demonstrate practical AI usage that creates real business value.

---

# Main Vision

The long-term vision is to transform FOF-AI into a complete AI Business Consultant capable of helping small import/export companies make intelligent decisions.

Instead of only storing products, the system should eventually answer questions such as:

* Which products should I import next month?
* Which products sell the fastest?
* Which products should receive promotions?
* Which products are becoming dead stock?
* Which suppliers should I prioritize?
* Which products are likely to expire?
* Which products generate the highest profit?
* What business actions should I take this week?

The AI should behave like an experienced Supply Chain Consultant rather than a chatbot.

---

# Main Technologies

Programming Language

Python 3.12

Framework

Streamlit

Database

SQLite

Machine Learning

Facebook Prophet

Charts

Plotly Express

Artificial Intelligence

Google AI SDK

Gemini / Gemma Models

Email Notifications

SMTP

Environment Variables

python-dotenv

Future Deployment

Streamlit Cloud or Render

---

# Current Folder Structure

```
FOF-AI/

│

├── app.py

│

├── database/

│     └── database.py

│

├── models/

│     └── product.py

│

├── services/

│     ├── ai_service.py
│     ├── forecast_service.py
│     ├── gemma_service.py
│     ├── gemini_service.py
│     ├── notification_service.py
│     ├── product_service.py
│     └── promotion_service.py

│

├── pages/

│     ├── dashboard.py
│     ├── inventory.py
│     ├── forecast.py
│     └── ai_assistant.py

│

├── data/

│     └── inventory.db

│

├── .env

├── .env.example

├── README.md

└── requirements.txt
```

The project follows a simple layered architecture.

---

# Architecture

The application is divided into four layers.

## 1. UI Layer

Located inside

```
pages/
```

Responsible for:

* Dashboard
* Inventory
* Forecast
* AI Assistant

This layer contains no database logic.

It only communicates with Services.

---

## 2. Service Layer

Located inside

```
services/
```

This is the heart of the application.

It contains:

Business logic

AI

Forecasting

Email

Promotion Generation

Database interaction

Every intelligent feature should be placed here.

No AI logic should exist inside Streamlit pages.

---

## 3. Model Layer

Located inside

```
models/
```

Contains Python classes representing application objects.

Currently:

Product

Future models may include:

Supplier

Notification

Sales History

Promotion

Forecast

---

## 4. Database Layer

SQLite database

Currently stores:

Products

Future tables will include:

Sales History

Notifications

AI Logs

Forecast Cache

Promotion History

---

# Database Philosophy

The database should remain lightweight.

SQLite is sufficient for the hackathon.

Later versions may migrate to PostgreSQL.

Current database focuses on inventory.

Future database should become a complete business intelligence warehouse.

---

# Artificial Intelligence Philosophy

AI is NOT used only to answer questions.

Instead AI should actively help the company.

Examples:

Analyze inventory

Generate promotions

Recommend imports

Predict demand

Reduce expiry losses

Improve profitability

Generate business insights

Write executive reports

Detect risks

Generate marketing campaigns

Every AI feature must provide measurable business value.

---

# Forecasting Philosophy

Forecasting is based on Prophet.

Predictions are currently generated using available inventory information.

Future versions will use actual historical sales data.

Forecasting should become increasingly accurate as more inventory history is collected.

---

# Coding Philosophy

During development we followed these rules:

* Simple code over complex code.
* Clear separation between UI and business logic.
* One responsibility per service.
* Every feature should be modular.
* AI should be reusable.
* Database logic stays inside services.
* Streamlit pages should remain clean.
* Every major feature should have its own service.

---

# Current Development Status

The project has already evolved far beyond a CRUD inventory system.

Current focus has shifted toward AI-powered business intelligence.

The remaining work will mostly involve improving AI capabilities rather than adding traditional management features.

---

Excellent. This is the most important part because it explains **everything that has been built**. The next ChatGPT should read this before writing any code.

---

# FOF-AI PROJECT HANDOVER DOCUMENT

# Part 2 – Completed Features & AI Modules

---

# Overall Development Progress

The project originally started as a simple inventory management application.

However, during development the project direction changed completely.

Instead of becoming another CRUD application, FOF-AI evolved into an AI-powered Business Intelligence Platform specifically designed for food import/export companies.

The development philosophy became:

> Every new feature must solve a real business problem.

Traditional CRUD features are considered secondary compared to intelligent AI features.

---

# 1. Inventory Management

Current status:

Nearly Complete

Implemented Features

✔ Add Product

✔ View Inventory

✔ Search Products

✔ Filter by Category

✔ Filter by Supplier

✔ Filter by Status

✔ AI Product Analysis

✔ AI Import Recommendation

✔ Inventory Dashboard Integration

Update/Delete functionality has recently been implemented during development and should be verified again after future refactoring.

Products currently contain:

* Product Name
* Category
* Brand
* Supplier Country
* Destination Country
* Quantity
* Unit
* Cost Price
* Selling Price
* Manufacture Date
* Expiry Date
* Warehouse
* Status

---

# 2. Dashboard

Current Status

Working

Dashboard currently displays

Total Products

Low Stock

Expiring Products

Destination Countries

Category Charts

Supplier Charts

Destination Charts

Company Health Analysis

Executive AI Brief

Business Health

Inventory Warnings

Recommendations

The dashboard is intended to become the company's daily decision center.

---

# 3. AI Product Analysis

Current Status

Completed

For every product the AI currently analyzes

Stock Level

Profit Margin

Days Until Expiry

Inventory Status

Recommendation

Examples

Low Stock

Medium Stock

Healthy Stock

Critical Expiry

Warning

Safe

Recommendations currently include

Import More

Launch Promotion

Inventory Healthy

This analysis is rule-based but will gradually become Gemma-powered.

---

# 4. AI Company Advisor

Current Status

Completed

The AI scans every product and generates a company-wide health report.

Outputs include

Critical Alerts

Inventory Warnings

Business Recommendations

Overall Company Health

Health categories

Excellent

Good

Needs Attention

The dashboard displays this report visually.

---

# 5. Forecasting Module

Current Status

Completed

Technology

Facebook Prophet

Current Features

Demand Forecast

Monthly Forecast

Future Demand Prediction

Next Month Demand

Seasonal Multiplier

Current Seasonal Intelligence

Ramadan

Christmas

New Year

Normal Season

Forecasts are currently based on available inventory data.

Future versions will use actual sales history.

---

# 6. AI Import Advisor

Current Status

Completed

The system currently combines

Current Stock

Forecasted Demand

Seasonal Multiplier

Supplier Country

Then calculates

Predicted Demand

Recommended Import Quantity

Import Priority

Recommended Import Timing

Business Event

Priority Levels

High

Medium

Low

This feature is considered one of the strongest business features currently implemented.

---

# 7. Executive Report Generator

Current Status

Completed

The system automatically generates

Inventory Summary

Low Stock Summary

Expiry Summary

AI Business Insights

Business Recommendations

Executive Reports are currently text-based.

Future versions may export

PDF

Email

Presentation

---

# 8. AI Business Assistant

Current Status

Completed

This is the conversational AI page.

Instead of being a general chatbot, it behaves as

Supply Chain Consultant

Inventory Expert

Business Advisor

Import Consultant

Current Context Provided to AI

Inventory

Forecast

Predicted Demand

Supplier

Destination

Stock

Cost

Selling Price

Warehouse

Expiry

Season

Current Prompt Rules

Never invent products

Answer only from inventory

Provide business advice

Keep responses concise

Think like a Supply Chain Consultant

This page represents one of the core AI features.

---

# 9. Google AI Integration

Current Status

Working

SDK

google-genai

Models Tested

Gemini

Gemma

During development many authentication issues occurred.

Eventually these were solved by

Creating a new AI Studio API Key

Using a personal Google account

Updating SDK

Using the correct API key

Gemini currently works correctly.

Gemma access has been inconsistent due to API/account behavior and should always be tested independently before integrating new Gemma-powered features.

Important note:

Always test with a standalone script before assuming the application code is broken.

---

# 10. Email Notification System

Current Status

Completed

Technology

SMTP

Current Capabilities

Send Email

Business Alerts

Expiry Alerts

Manual Notification

Current Test

Email successfully sent from application.

Future versions

Low Stock Alerts

Forecast Alerts

Executive Report Emails

Daily Business Summary

---

# 11. AI Promotion Generator

Current Status

Completed

One of the newest AI features.

Technology

Gemma

Current Capabilities

Generate

Facebook Advertisement

WhatsApp Advertisement

Marketing Slogan

Call To Action

The output is structured into sections.

Instead of returning one long paragraph, the interface separates

Facebook

WhatsApp

Slogan

Call To Action

This feature provides direct business value because generated content can be copied directly into marketing campaigns.

---

# 12. Business Intelligence Philosophy

The project intentionally avoids creating AI features that simply "look intelligent."

Instead every feature should answer a practical business question.

Examples

Should I import more?

Should I launch a promotion?

Will this product expire?

Will demand increase?

Which supplier should I order from?

How can I increase profitability?

Every AI feature must support real business decision making.

---

# Major Problems Solved During Development

Many technical issues were solved during development.

Examples include

SQLite database path issues

Dashboard service errors

Missing ProductService methods

ForecastService errors

Pandas compatibility changes

Prophet frequency issues

Product filtering

Inventory CRUD improvements

GitHub API key exposure

GitHub Push Protection

Google AI authentication

Gemini SDK migration

Google API key management

SMTP configuration

Promotion generation

These issues have already been solved and should not be reintroduced.

---

# Current Project Maturity

FOF-AI is no longer an educational CRUD project.

It is now an AI Business Intelligence platform with

Inventory

Forecasting

AI Analysis

Business Chat

Promotion Generation

Email Notifications

Executive Reporting

Demand Forecasting

Import Planning

The remaining development should focus on making the AI smarter rather than adding ordinary management pages.

---

Excellent. This is probably the most important part because it tells the next ChatGPT **how to think** while working on the project.

---

# FOF-AI PROJECT HANDOVER DOCUMENT

# Part 3 – Development Rules, AI Philosophy & Future Roadmap

---

# IMPORTANT

This project has changed direction during development.

Originally it was simply an Inventory Management System.

It is **NO LONGER** an inventory management project.

It is now an

**AI Business Intelligence Platform**

Inventory management only exists because AI needs inventory data.

Therefore:

**Never develop features simply because inventory systems normally have them.**

Every new feature should answer the question:

> **How does this make the AI smarter and more useful for business decisions?**

---

# Primary Objective

The application should become a complete AI Business Consultant capable of helping the owner manage his import/export company.

The owner should eventually rely on FOF-AI every morning before making business decisions.

The AI should become another business partner.

---

# Business Objective

The system should help solve problems such as

Products expiring

Overstock

Understock

Wrong import quantities

Poor supplier decisions

Slow-moving inventory

Lost profits

Poor marketing

Seasonal demand

Import timing

Supplier planning

Profit optimization

Everything should revolve around improving business decisions.

---

# AI Philosophy

The AI is NOT a chatbot.

It is NOT ChatGPT inside Streamlit.

Instead, it should behave like an experienced

Supply Chain Consultant

Inventory Expert

Business Analyst

Import Planner

Marketing Consultant

Executive Advisor

Every response should sound like professional business consulting.

---

# Prompt Engineering Philosophy

Every AI prompt should include

Company context

Current inventory

Current supplier countries

Destination countries

Forecast

Season

Business objective

The AI should never answer general questions unrelated to the company.

Example

Good

"What should I import before Ramadan?"

Bad

"What is Python?"

The AI exists to support the company.

---

# Development Philosophy

During development we intentionally avoided

Huge complicated architecture

Unnecessary abstractions

Over-engineering

Everything should remain understandable.

Future ChatGPTs should continue this style.

---

# Coding Rules

Every feature should have its own service.

Examples

ForecastService

PromotionService

NotificationService

ProductService

AIService

GemmaService

Never place business logic inside Streamlit pages.

Pages should mainly contain

Buttons

Forms

Charts

Display

Services should perform all calculations.

---

# Database Philosophy

SQLite is intentionally used.

The goal is simplicity.

Future versions may migrate to PostgreSQL but this is NOT a priority.

Database should gradually evolve into a Business Intelligence database.

Future tables

Sales History

Notifications

Forecast Cache

Promotion History

AI Logs

Supplier Performance

Import History

---

# Dashboard Philosophy

Dashboard should NOT become crowded.

Every widget must provide value.

Avoid decorative charts.

Every chart should answer a business question.

Example

Good

Products by Supplier

Bad

Random colorful graphs

The dashboard should help the owner make decisions in under one minute.

---

# Current AI Features

Already Implemented

Inventory Analysis

Company Analysis

Forecast

Import Recommendation

Business Chat

Executive Report

Promotion Generator

Email Notifications

Current AI quality is already strong.

Future work should increase intelligence rather than adding many unrelated pages.

---

# Current Roadmap

Remaining work should focus almost entirely on AI.

Priority List

1.

Smart Notifications

Email

WhatsApp

Critical Alerts

Forecast Alerts

Daily Summary

Status

Started

---

2.

Promotion Generator

Facebook

WhatsApp

Marketing Slogan

Call To Action

Status

Working

Already generating high-quality marketing content using Gemma.

Future improvements

Instagram posts

Promotional posters

Flyers

Marketing strategy

---

3.

Sales Intelligence

Very Important

Current limitation

The system knows current inventory but does NOT yet know historical sales.

A Sales History table should be introduced.

Every inventory update should create a history record.

From that history AI should calculate

Fast-moving products

Slow-moving products

Dead stock

Seasonal products

Average sales

Inventory turnover

This is considered one of the most valuable future features.

---

4.

Business Intelligence Dashboard

Future AI widgets

Top Selling Products

Slow Moving Products

Most Profitable Products

Products Near Expiry

Import Recommendations

Supplier Performance

Predicted Monthly Revenue

The dashboard should eventually resemble Power BI or Tableau.

---

5.

Company Branding

The application should look like commercial software.

Future branding includes

Company Logo

Professional Sidebar

Business Theme

Executive Reports

Brand Colors

Professional Layout

This should be done after AI development.

---

# Features That Should NOT Be Prioritized

Avoid spending time on

Fancy animations

Complex login systems

Customer management

Employee management

Accounting

Invoices

POS

Payroll

These are outside the hackathon objective.

---

# Hackathon Strategy

The judges should immediately understand

"This is AI solving a real business problem."

Not

"This is another inventory application."

Therefore every new feature should demonstrate

Reasoning

Prediction

Recommendation

Decision support

Business intelligence

---

# User Preferences During Development

The project owner (me) repeatedly requested the following development style:

• Work step-by-step.

• Give only one step at a time.

• Always explain exactly where code should be pasted.

• Clearly specify

Inside function

Outside function

Before

After

Replace

Append

• Never tell me to rewrite an entire file if only a small section needs changing.

• Keep code modular.

• Avoid introducing unrelated improvements while implementing the current task.

This development style should continue throughout the project.

---

# Communication Style

During development, avoid repeatedly explaining the roadmap or summarizing previous work unless requested.

The user prefers to:

Choose a feature.

Implement it immediately.

Test it.

Continue to the next step.

Responses should therefore remain focused and practical.

---

# Long-Term Vision

The final vision is for FOF-AI to become an AI-powered business assistant that can genuinely improve the daily operations of ETS FOFANA CONFISERIE.

The owner should be able to ask natural-language business questions, receive intelligent recommendations, generate marketing content, receive proactive alerts, and make better purchasing and sales decisions—all from a single application.

---

# FOF-AI PROJECT HANDOVER DOCUMENT

# Part 4 – Current Project Status, Lessons Learned & Next Development Steps

---

# Current Project Status

At the time this document was written, the project is **fully functional**.

The application successfully runs and currently includes:

* Inventory Management
* Dashboard
* AI Product Analysis
* Company Health Analysis
* Demand Forecasting
* Import Recommendation
* Executive Reports
* AI Business Assistant
* Email Notifications
* AI Promotion Generator

The project is stable enough for demonstrations.

Future work should focus on improving AI intelligence instead of adding unrelated CRUD features.

---

# Current Development Stage

The project has reached approximately:

**85–90% completion** for the hackathon MVP.

Most remaining work is centered around making the AI more intelligent and more useful for real business decision-making.

---

# Current Project Workflow

Current application flow:

```
User

↓

Dashboard

↓

Inventory

↓

AI Analysis

↓

Forecast

↓

Import Recommendation

↓

Promotion Generator

↓

Business Chat

↓

Email Alerts
```

Future versions will insert **Sales Intelligence** between Inventory and Forecast.

---

# AI Modules Currently Available

The following AI capabilities are already implemented:

✔ Product Analysis

✔ Company Analysis

✔ Inventory Health

✔ Demand Forecast

✔ Import Recommendation

✔ Executive Reports

✔ Business Chat

✔ Promotion Generator

✔ Email Alerts

These modules should remain independent services.

---

# Features Under Development

The following feature has **already started** and should be completed next.

---

## Sales Intelligence

Current status:

Started

Reason:

Currently the application only knows the **current quantity** of each product.

It does NOT know

* how fast products sell
* how often inventory changes
* inventory turnover
* historical sales

Without history, forecasting and recommendations are limited.

---

## Planned Solution

Create a new table

```
sales_history
```

Store

* Product ID
* Previous Quantity
* New Quantity
* Quantity Sold
* Date

Every inventory update should automatically create one history record.

This history becomes the foundation of future AI.

---

## Future AI Questions

Once Sales History exists the AI should answer:

Which product sells fastest?

Which products are becoming dead stock?

Which products stay longest in storage?

Which products should receive promotions?

Which products should be imported more?

Which products should be discontinued?

These answers should come from data rather than hard-coded rules.

---

# Future AI Features

The following AI improvements are considered high priority.

---

## Smart Notifications

Current

Email Alerts

Future

WhatsApp

Telegram

Daily Summary

Morning Report

Critical Alerts

Forecast Alerts

Supplier Alerts

The AI should notify the owner automatically.

---

## Promotion Generator

Already Working

Current outputs

Facebook

WhatsApp

Marketing Slogan

Call To Action

Future versions

Instagram

Flyers

Promotional Posters

Email Campaigns

Holiday Campaigns

Ramadan Campaigns

Christmas Campaigns

AI Marketing Strategy

---

## Sales Intelligence

Highest Remaining Priority

Future calculations

Average Daily Sales

Inventory Turnover

Fast Moving Products

Slow Moving Products

Dead Inventory

Monthly Consumption

Supplier Performance

Predicted Revenue

Business Risk

---

## Executive Dashboard

Future widgets

Top Sellers

Slow Sellers

Most Profitable Products

Most Imported Products

Most Exported Products

Supplier Ranking

Country Performance

Inventory Turnover

Profit Forecast

---

# Company Branding

This task has intentionally been postponed.

Later improvements include

Company Logo

Professional Sidebar

Business Theme

Brand Colors

Executive Report Logo

Professional Landing Page

Footer

These are visual improvements and should only be completed after the AI functionality is finalized.

---

# Lessons Learned During Development

Throughout the project, several important technical lessons were learned.

---

## Google AI Integration

Google AI authentication caused several issues.

Problems included

401 UNAUTHENTICATED

403 PERMISSION DENIED

404 MODEL NOT FOUND

Wrong SDK

Old SDK

Wrong API Keys

Eventually solved by

* Using a personal Google account
* Creating a fresh AI Studio API key
* Using the latest `google-genai` SDK
* Testing models independently before integrating them

Future ChatGPTs should **always test AI services with a standalone script first** before assuming application code is broken.

---

## GitHub

A Google AI API key was accidentally committed.

GitHub Push Protection blocked the push.

Lesson

Never commit

```
.env
```

Always keep

```
.env
```

inside

```
.gitignore
```

Repository currently includes

```
.env.example
```

which should remain.

---

## Streamlit

One important lesson:

Do not perform expensive AI calls during page rendering.

Always trigger AI using buttons.

Examples

Generate Promotion

Send Alerts

Business Chat

This keeps the application responsive.

---

## Forecasting

Forecasts currently rely on Prophet.

Future improvements should come from better data instead of changing forecasting libraries.

Better historical data will naturally improve predictions.

---

# Coding Rules

Future ChatGPTs should continue using the existing architecture.

Rules

Never move business logic into Streamlit pages.

Create one service per feature.

Keep AI prompts inside services.

Keep pages clean.

Never duplicate business logic.

Reuse existing services whenever possible.

---

# Current File Responsibilities

```
app.py
```

Application entry point.

---

```
pages/
```

User interface only.

---

```
services/
```

Business logic.

---

```
database/
```

SQLite initialization.

---

```
models/
```

Application models.

---

Future features should follow this same architecture.

---

# Immediate Next Step

The **very next task** after this document is:

### Build Sales Intelligence

Specifically:

1. Create the `sales_history` table.
2. Update `ProductService.update_product()` so every stock change is recorded.
3. Build a new `SalesHistoryService`.
4. Calculate:

   * Average daily sales
   * Inventory turnover
   * Fast vs. slow-moving products
5. Expose these insights in the dashboard.
6. Allow Gemma to answer questions based on actual sales history.

This is the next major milestone.

---

# What Should NOT Change

Future ChatGPTs should **not** change the overall vision of the project.

The application is **not** intended to become:

* ERP software
* POS system
* Accounting software
* HR software
* Payroll software
* Customer management system

The goal is to remain focused on **AI Business Intelligence for Food Import & Export Companies**.

---

# Final Vision

When completed, FOF-AI should feel like an **AI Business Executive** rather than a traditional software application.

A business owner should be able to open the application each morning and immediately know:

* What needs attention today.
* Which products are at risk.
* Which imports should be planned.
* Which products deserve promotions.
* Which products generate the highest value.
* What decisions should be made this week.

The AI should proactively guide the business, not merely respond to questions.

---

# Final Note to the Next ChatGPT

If you are continuing this project:

1. Read all four parts of this handover document before making changes.
2. Preserve the modular architecture (UI → Services → Database).
3. Keep the focus on solving real business problems with AI.
4. Implement features incrementally, one tested step at a time.
5. When giving coding instructions, clearly state **where** code should be inserted (before, after, replace, inside a method, etc.).
6. Do not introduce unrelated enhancements while working on the current feature.
7. The immediate priority is **Sales Intelligence**, followed by richer AI insights built on real historical business data.

---


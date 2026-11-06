<div align="center">

# 🥗 PustiBondhu AI

### AI & ML Engine for Personalized Health and Nutrition Intelligence

*Smarter food decisions, personalized around your health and built for Bangladeshi food culture.*

![Status](https://img.shields.io/badge/status-under%20active%20development-yellow)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![RAG](https://img.shields.io/badge/AI-RAG%20%2B%20LLM-10B981)
![Platform](https://img.shields.io/badge/app-iOS%20%7C%20Android-lightgrey)

**[🌐 Project Overview](https://pustibondhu-portfolio.vercel.app)**

</div>

---

## 📖 Overview

**PustiBondhu AI** is a mobile health and nutrition assistant that gives food guidance based on a person's **medical background, medication, and local dietary habits**, instead of generic diet advice.

Most nutrition apps ignore two things: the health condition of the user, and the foods people actually eat in Bangladesh. PustiBondhu AI is designed around both.

This repository contains the **AI/ML engine** that powers the app. The mobile app and the backend are maintained in separate repositories.

> 📱 The product is a mobile app, so a live web demo isn't possible. The **[project overview site](https://pustibondhu-portfolio.vercel.app)** shows the idea, features, system architecture, and roadmap.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🩺 **Condition-Aware Food Guidance** | Evaluates conditions such as diabetes or hypertension against daily meals, and explains which foods to prefer, limit, or avoid, with suitable alternatives |
| 📄 **Medical Report & Medication Intelligence** | Extracts key metrics from uploaded lab reports and flags known food–medicine interactions using reliable references |
| 💬 **Bilingual AI Assistant** | Ask in **Bangla or English** and get culturally aware explanations, meal suggestions, and nutrition summaries |
| 🍛 **Food & Nutrition Explorer** | Calories, macros, vitamins, minerals, and serving sizes for local Bangladeshi dishes, plus affordable substitutes |
| 📷 **AI Food Image Recognition** | Identifies food from a photo, estimates portions and nutrition, and lets the user review the result before logging |
| ⌚ **Smartwatch Support** | Brings supported activity, heart-rate, and sleep data together with nutrition goals |

---

## 🏗️ System Architecture

PustiBondhu AI is organized in layers: a mobile client, a core backend, and an AI service that handles retrieval, vision, and report understanding.

```
┌──────────────────────────────────────────────────────────┐
│                  Flutter Mobile App                      │
│        UI · State · Secure local storage · Wearables     │
└────────────────────────────┬─────────────────────────────┘
                             │ REST
┌────────────────────────────▼─────────────────────────────┐
│                 Spring Boot Core Backend                 │
│     Auth · User profiles · Nutrition calculations ·      │
│            Meal logs · Secure document storage           │
└────────────────────────────┬─────────────────────────────┘
                             │ REST
┌────────────────────────────▼─────────────────────────────┐
│          FastAPI AI Service   ◄── THIS REPOSITORY        │
│                                                          │
│   ┌──────────────┐ ┌───────────────┐ ┌────────────────┐  │
│   │ LLM + RAG    │ │ Food-Vision   │ │ Report Parsing │  │
│   │ Pipeline     │ │ Pipeline      │ │ & Interaction  │  │
│   │              │ │               │ │ Checks         │  │
│   └──────┬───────┘ └───────┬───────┘ └───────┬────────┘  │
│          │                 │                 │           │
│   ┌──────▼─────────────────▼─────────────────▼────────┐  │
│   │  Vector Index · Food-Nutrition DB · Medical KB    │  │
│   └───────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### Guidance workflow

```
 Build Profile ─► Add Info ─► AI Context ─► Get Guidance ─► Track Progress
 conditions,      reports,    retrieval,    recommendations,  intake and
 goals, diet,     food logs,  nutrition     limits, reasons,  health
 medication       wearables   data, rules   alternatives      trends
```

---

## 🧠 AI Components

### 1. LLM & RAG Pipeline
Retrieval-Augmented Generation keeps answers grounded in medical and nutrition sources rather than relying only on the model's memory.
- Retrieves relevant knowledge for the user's condition and question
- Builds contextual prompts from the user profile and retrieved evidence
- Verifies outputs against rules before they reach the user
- Supports multi-turn conversation in Bangla and English

### 2. Food-Vision Pipeline
- Image preprocessing for meal photos
- Food recognition model for common Bangladeshi dishes
- Portion and nutritional composition estimation
- A review step so the user confirms before a meal is recorded

### 3. Report Intelligence
- OCR-based extraction of key values from lab reports
- Links findings to nutrition considerations
- Flags known food–medicine interactions from reliable references

### 4. Bangladeshi Food-Nutrition Data
- Collection and validation of local dishes
- Serving-size and nutrient data preparation
- Glycemic information for condition-aware recommendations
- Knowledge-base preparation for the RAG pipeline

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **AI service** | Python, FastAPI |
| **Language models** | LLM with Retrieval-Augmented Generation (RAG) |
| **Retrieval** | Vector index / database, embeddings |
| **Computer vision** | Food image recognition pipeline |
| **Document processing** | OCR for lab reports |
| **Rest of the system** | Flutter (mobile app), Spring Boot (backend), in separate repositories |

---

## 🗺️ Roadmap

- [x] System architecture
- [x] Repository structure and branching
- [ ] Bangladeshi nutrition database: local dishes, serving portions, glycemic data
- [ ] AI assistant and RAG pipeline: medical embeddings, multi-turn chat
- [ ] Food-image recognition model and evaluation
- [ ] Report parsing: OCR extraction and interaction flags
- [ ] Smartwatch data integration
- [ ] Validation and field testing

---

## 🔗 Related Repositories

| Repository | Description |
|---|---|
| **AI/ML Engine** *(this repo)* | RAG pipeline, food-vision, report intelligence, data preparation |
| **Backend** | Spring Boot services for auth, profiles, nutrition, and documents |
| **Mobile App** | Flutter app for iOS and Android |

---

## 🛡️ Responsible AI & Medical Notice

Health guidance needs extra care, so the system is designed to:

- Ground recommendations in **retrieved, reliable sources**
- Apply **rule-based checks** to AI output before showing it
- Keep the user in control, for example by letting them review recognized food before logging it
- Use **encrypted storage** for uploaded medical documents

> ⚠️ **Disclaimer:** PustiBondhu AI provides **informational nutrition guidance only**. It does not replace professional medical advice, diagnosis, or treatment. Food–medicine interaction warnings should rely on reliable sources. Always consult a qualified healthcare professional before changing medication or a prescribed diet.

---

<div align="center">

**[🌐 Visit the Project Overview](https://pustibondhu-portfolio.vercel.app)**

*PustiBondhu AI: nutrition intelligence that understands you.*

</div>

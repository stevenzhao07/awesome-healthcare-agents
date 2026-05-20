# Key Research Papers on Agents in Healthcare

Last updated: 2026-05-20

This page tracks papers on healthcare agents, multi-agent clinical workflows, agent benchmarks, medical RAG, multimodal tool use, EHR agents, and safety. Preference is given to papers with public code, public benchmarks, or clearly reusable datasets.

---

## Surveys, Taxonomies, and Governance

| Paper | Year | Venue/Source | Notes |
|---|---:|---|---|
| [A Survey of LLM-based Agents in Medicine](https://aclanthology.org/2025.findings-acl.539/) | 2025 | Findings of ACL | Survey of LLM-based medical agents, tasks, architectures, and evaluation gaps. |
| [Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents](https://arxiv.org/abs/2602.04813) | 2026 | arXiv | Reviews 49 studies and maps healthcare agents across capabilities, knowledge, interaction, safety, framework type, and tasks. |
| [Agentic AI Governance and Lifecycle Management in Healthcare](https://arxiv.org/abs/2601.15630) | 2026 | arXiv | Governance blueprint for identity, orchestration, PHI-bounded memory, runtime policy, and decommissioning. |
| [Agentic Large Language Models for Healthcare: Current Progress and Future Opportunities](https://doi.org/10.1002/med4.70000) | 2025 | Medicine Advances | Commentary on healthcare agent progress and future opportunities. |
| [Agents for Change: Artificial Intelligent Workflows for Quantitative Clinical Pharmacology and Translational Sciences](https://doi.org/10.1111/cts.70188) | 2025 | Clinical and Translational Science | Review of agentic workflows for pharmacology, translational science, simulation, and precision medicine. |
| [AI Agents in Clinical Medicine: A Systematic Review](https://www.medrxiv.org/content/10.1101/2025.08.22.25334232v1) | 2025 | medRxiv | Systematic review of AI agents in clinical medicine and near-term integration. |
| [An Empirical Study of Agent Skills for Healthcare: Practice, Gaps, and Governance](https://arxiv.org/abs/2605.02709) | 2026 | arXiv | Studies healthcare agent skills as reusable procedural packages and maps practical gaps. |
| [Large Language Model Agents for Biomedicine: A Comprehensive Review of Methods, Evaluations, Challenges, and Future Directions](https://www.mdpi.com/2078-2489/16/10/894) | 2025 | Information | Comprehensive biomedical LLM-agent review covering methods, benchmarks, and trustworthiness. |

---

## Clinical Reasoning and Multi-Agent Diagnosis

| Paper | Year | Code/Project | Notes |
|---|---:|---|---|
| [MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning](https://arxiv.org/abs/2311.10537) | 2024 | [GitHub](https://github.com/gersteinlab/MedAgents) | Multidisciplinary collaboration framework evaluated on MedQA, MedMCQA, PubMedQA, and MMLU medical subsets. |
| [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://arxiv.org/abs/2404.15155) | 2024 | [GitHub](https://github.com/mitmedialab/MDAgents) | Dynamically assigns solo, multidisciplinary, or integrated care team structures based on medical complexity. |
| [AI Hospital: Benchmarking Large Language Models in a Multi-agent Medical Interaction Simulator](https://aclanthology.org/2025.coling-main.680/) | 2025 | [GitHub](https://github.com/LibertFan/AI_Hospital) | Doctor, Patient, and Examiner agents with a Chinese medical-record benchmark. |
| [MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis](https://arxiv.org/abs/2502.19175) | 2025 | [GitHub](https://github.com/nec-research/meddxagent) | History-taking, retrieval, and diagnostic strategy modules for explainable differential diagnosis. |
| [MedAgent-Pro: Towards Multi-modal Evidence-based Medical Diagnosis via Reasoning Agentic Workflow](https://arxiv.org/abs/2503.18968) | 2025 | [GitHub](https://github.com/jinlab-imvr/MedAgent-Pro) | Evidence-based multimodal diagnosis with knowledge-based planning and specialized tool agents. |
| [MedAgentSim: Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions](https://arxiv.org/abs/2503.22678) | 2025 | [GitHub](https://github.com/MAXNORM8650/MedAgentSim) | Simulated clinical environment with doctor, patient, and measurement agents plus self-improvement. |
| [Healthcare agent: eliciting the power of large language models for medical consultation](https://www.nature.com/articles/s44387-025-00021-x) | 2025 | Paper | Patient-oriented consultation agent for medical advice scenarios. |
| [ConfAgents: A Conformal-Guided Multi-Agent Framework for Cost-Efficient Medical Diagnosis](https://arxiv.org/abs/2508.04915) | 2025 | Paper | Uses conformal guidance to route medical diagnosis among agents efficiently. |
| [MedLA: A Logic-Driven Multi-Agent Framework for Complex Medical Reasoning with Large Language Models](https://arxiv.org/abs/2509.23725) | 2025 | Paper | Logic-driven multi-agent framework for complex medical reasoning. |
| [MedCoAct: Confidence-Aware Multi-Agent Collaboration for Complete Clinical Decision](https://arxiv.org/abs/2510.10461) | 2025 | Paper | Doctor and pharmacist agents plus DrugCareQA for integrated diagnosis and treatment workflows. |
| [MedCollab: Causal-Driven Multi-Agent Collaboration for Full-Cycle Clinical Diagnosis via IBIS-Structured Argumentation](https://arxiv.org/abs/2603.01131) | 2026 | Paper | Uses causal reasoning and structured argumentation for full-cycle clinical diagnosis. |

---

## EHR, Clinical Workflow, and Administration Agents

| Paper | Year | Code/Project | Notes |
|---|---:|---|---|
| [MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents](https://arxiv.org/abs/2501.14654) | 2025 | [Project](https://stanfordmlgroup.github.io/projects/medagentbench/) | Virtual EHR benchmark for autonomous task execution, planning, and clinical data extraction. |
| [HealthAdminBench: A Benchmark for Evaluating LLMs on Solving Administrative Healthcare Tasks](https://som-shahlab.github.io/health-admin-bench-website/) | 2025 | [Project](https://som-shahlab.github.io/health-admin-bench-website/) | Web-environment benchmark for scheduling, prior authorization, referrals, and admin tasks. |
| [PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments](https://arxiv.org/abs/2605.02240) | 2026 | Paper | Long-horizon physician tasks grounded in real consultation cases and EHR APIs. |
| [AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks](https://arxiv.org/abs/2605.10286) | 2026 | Paper | Compares single-agent and multi-agent systems for multimodal clinical prediction using EHR, imaging, notes, and reports. |

---

## Benchmarks, Training Environments, and Evaluation Datasets

| Paper / Dataset | Year | Code/Data | Notes |
|---|---:|---|---|
| [AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments](https://arxiv.org/abs/2405.07960) | 2024 | [Project](https://agentclinic.github.io/) | Sequential decision-making benchmark with patient interaction, multimodal data, and tool use. |
| [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://arxiv.org/abs/2410.13610) | 2024 | [GitHub](https://github.com/shzyk/MENTI) | Introduces CalcQA for medical calculator tasks and nested medical-tool calling. |
| [ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents](https://arxiv.org/abs/2410.17657) | 2024 | Paper | Introduces ClinicalAgent Bench (CAB), 18 tasks across five realistic clinical dimensions. |
| [BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology](https://arxiv.org/abs/2503.00096) | 2025 | [Dataset](https://huggingface.co/datasets/futurehouse/BixBench) | Bioinformatics benchmark with 50+ scenarios and nearly 300 open-answer questions. |
| [MedAgentsBench: Benchmarking Thinking Models and Agent Frameworks for Complex Medical Reasoning](https://arxiv.org/abs/2503.07459) | 2025 | [GitHub](https://github.com/gersteinlab/medagents-benchmark) | Evaluates thinking models and agent frameworks on complex medical reasoning. |
| [MedAgentGym: Training LLM Agents for Code-Based Medical Reasoning at Scale](https://arxiv.org/abs/2506.04405) | 2025 | [GitHub](https://github.com/wshi83/MedAgentGym) | Training environment with 72,413 biomedical coding-task instances across 129 categories. |
| [HealthBench: Evaluating Large Language Models Towards Improved Human Health](https://arxiv.org/abs/2505.08775) | 2025 | [GitHub](https://github.com/openai/simple-evals) | 5,000 multi-turn health conversations with physician-validated rubrics. |
| [SymptomCheck Bench](https://github.com/medaks/symptomcheck-bench) | 2024 | [GitHub](https://github.com/medaks/symptomcheck-bench) | Open-source benchmark for evaluating diagnostic symptom-checking agents. |

---

## Medical RAG and Knowledge-Grounded Agents

| Paper | Year | Code/Project | Notes |
|---|---:|---|---|
| [Benchmarking Retrieval-Augmented Generation for Medicine](https://aclanthology.org/2024.findings-acl.372/) | 2024 | [Project](https://teddy-xionggz.github.io/benchmark-medical-rag/) | Systematic benchmark of RAG for medical question answering. |
| [Medical Graph RAG: Towards Safe Medical Large Language Model via Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2408.04187) | 2024 | [GitHub](https://github.com/MedicineToken/Medical-Graph-RAG) | Graph RAG framework connecting private data, credible medical sources, and controlled vocabularies. |
| [MMed-RAG: Versatile Multimodal Retrieval-Augmented Generation System for Medical Vision Language Models](https://arxiv.org/abs/2410.13085) | 2024 | [GitHub](https://github.com/richard-peng-xia/MMed-RAG) | Multimodal medical RAG across radiology, pathology, and ophthalmology. |
| [MedRAG: Enhancing Retrieval-Augmented Generation with Knowledge Graph-Elicited Reasoning for Healthcare Copilot](https://arxiv.org/abs/2502.04413) | 2025 | [GitHub](https://github.com/SNOWTEAM2023/MedRAG) | KG-elicited reasoning for diagnosis and treatment recommendation retrieval. |
| [Unlocking Electronic Health Records: A Hybrid Graph RAG Approach to Safe Clinical AI for Patient QA](https://arxiv.org/abs/2602.00009) | 2026 | Paper | MediGRAF hybrid graph-RAG framework for patient-facing EHR question answering. |

---

## Imaging, Multimodal, and Tool-Using Medical Agents

| Paper | Year | Code/Project | Notes |
|---|---:|---|---|
| [MMedAgent: Learning to Use Medical Tools with Multi-modal Agent](https://arxiv.org/abs/2407.02483) | 2024 | [GitHub](https://github.com/Wangyixinxin/MMedAgent) | Medical agent trained to select tools across medical modalities and tasks. |
| [MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673) | 2025 | [GitHub](https://github.com/bowang-lab/MedRAX) | Tool-using chest X-ray reasoning agent. |
| [A Proactive Agent Collaborative Framework for Zero-Shot Multimodal Medical Reasoning](https://doi.org/10.1002/aisy.202400840) | 2025 | Paper | MultiMedRes learner/expert framework for multimodal medical reasoning. |
| [MRGAgents: A Multi-Agent Framework for Improved Medical Report Generation with Med-LVLMs](https://arxiv.org/abs/2505.18530) | 2025 | Paper | Multi-agent framework for medical report generation with medical LVLMs. |
| [GMAT: Grounded Multi-agent Clinical Description Generation for Text Encoder in Vision-Language MIL for Whole Slide Image Classification](https://papers.miccai.org/miccai-2025/) | 2025 | MICCAI ELAMI | Multi-agent clinical description generation for pathology whole-slide image classification. |
| [NeuroReport-MS: Multi-scale Agentic AI for Automated Clinical Report Generation in Multiple Sclerosis](https://papers.miccai.org/miccai-2025/) | 2025 | MICCAI ELAMI | Multi-scale agentic AI for multiple-sclerosis clinical report generation. |
| [SIGMA: Auto-Regressive VLM for Automated Radiology Report Generation from Longitudinal 3D CT Volumes](https://papers.miccai.org/miccai-2025/) | 2025 | MICCAI ELAMI | Longitudinal 3D CT radiology report generation. |
| [MedSAM-Agent: Empowering Interactive Medical Image Segmentation with Multi-turn Agentic Reinforcement Learning](https://arxiv.org/abs/2602.03320) | 2026 | Paper | Agentic RL workflow for interactive medical image segmentation with SAM-style tools. |
| [Meissa: Multi-modal Medical Agentic Intelligence](https://arxiv.org/abs/2603.09018) | 2026 | [GitHub](https://github.com/Schuture/Meissa) | Offline lightweight multimodal medical agent model with structured trajectory learning. |
| [BAAI Cardiac Agent: An intelligent multimodal agent for automated reasoning and diagnosis of cardiovascular diseases from cardiac magnetic resonance imaging](https://arxiv.org/abs/2604.04078) | 2026 | [GitHub](https://github.com/plantain-herb/Cardiac-Agent) | Multimodal cardiovascular magnetic resonance reasoning and diagnosis agent. |

---

## Drug Discovery, Pharmacology, and Therapeutics

| Paper | Year | Code/Project | Notes |
|---|---:|---|---|
| [TxAgent: An AI Agent for Therapeutic Reasoning Across a Universe of Tools](https://arxiv.org/abs/2503.10970) | 2025 | [GitHub](https://github.com/mims-harvard/TxAgent) | Therapeutic reasoning agent using 211 biomedical tools. |
| [ChatMolData: A Multimodal Agent for Automatic Molecular Data Processing](https://doi.org/10.1002/aisy.202401089) | 2025 | Paper | Multimodal agent for molecular databases, images, structured files, documents, and prediction tools. |
| [DrugAgent: Automating AI-aided Drug Discovery Programming through LLM Multi-Agent Collaboration](https://arxiv.org/abs/2411.15692) | 2024 | Paper | Multi-agent programming workflow for drug discovery ML tasks. |

---

## Clinical Tool Use and Calculators

| Paper | Year | Code/Project | Notes |
|---|---:|---|---|
| [Large Language Model Agents Can Use Tools to Perform Clinical Calculation](https://github.com/stanfordaimlab/llm-as-clinical-calculator) | 2024 | [GitHub](https://github.com/stanfordaimlab/llm-as-clinical-calculator) | OpenMedCalc tool-use setup plus ABACUS clinical-calculation datasets. |
| [AgentMD: Empowering Language Agents for Risk Prediction with Large-Scale Clinical Tool Learning](https://arxiv.org/abs/2402.13225) | 2024 | [GitHub](https://github.com/ncbi-nlp/Clinical-Tool-Learning) | Curates RiskCalcs and applies clinical calculators to patient descriptions and notes. |
| [AgentMD: Empowering language agents for risk prediction with large-scale clinical tool learning](https://www.nature.com/articles/s41467-025-64430-x) | 2025 | Nature Communications | Peer-reviewed version of AgentMD clinical calculator learning. |

---

## Safety, Robustness, and Risk

| Paper | Year | Code/Project | Notes |
|---|---:|---|---|
| [MedSentry: Understanding and Mitigating Safety Risks in Medical LLM Multi-Agent Systems](https://arxiv.org/abs/2505.20824) | 2025 | Paper | 5,000 adversarial prompts across 25 threat categories for medical multi-agent safety evaluation. |
| [Mind the Evaluation Gap: Large Language Models for Structured Data Extraction from Radiology Reports](https://papers.miccai.org/miccai-2025/) | 2025 | MICCAI ELAMI | Structured radiology-report extraction and evaluation-gap analysis. |
| [SCOPE: Label Extraction of Stroke Diagnosis from Unstructured Medical Reports Using Retrieval-Augmented Generation](https://papers.miccai.org/miccai-2025/) | 2025 | MICCAI ELAMI | RAG-based extraction of stroke diagnosis labels from unstructured reports. |
| [Impact of Patient Communication Style on Agentic AI-Generated Clinical Advice in E-Medicine](https://www.medrxiv.org/content/10.64898/2025.12.02.25341475v1.full-text) | 2025 | medRxiv | Studies how patient communication style influences agentic clinical advice. |

---

## Foundational Datasets Often Used by Healthcare Agents

| Dataset | Domain | Link |
|---|---|---|
| AgentClinic data | Simulated clinical interactions | [Project](https://agentclinic.github.io/) |
| BixBench | Bioinformatics agent tasks | [Hugging Face](https://huggingface.co/datasets/futurehouse/BixBench) |
| CheXpert | Chest X-ray labels | [Stanford ML Group](https://stanfordmlgroup.github.io/competitions/chexpert/) |
| HealthBench | Health conversation evaluation | [GitHub](https://github.com/openai/simple-evals) |
| MedAgentBench | Virtual EHR agent tasks | [GitHub](https://github.com/stanfordmlgroup/MedAgentBench) |
| MedMCQA | Medical multiple-choice QA | [Project](https://medmcqa.github.io/) |
| MedQA | USMLE-style QA | [GitHub](https://github.com/jind11/MedQA) |
| MIMIC-CXR | Chest X-rays and reports | [PhysioNet](https://physionet.org/content/mimic-cxr/2.1.0/) |
| MIMIC-IV | EHR | [PhysioNet](https://physionet.org/content/mimiciv/3.1/) |
| MIMIC-IV-Note | Clinical notes | [PhysioNet](https://physionet.org/content/mimic-iv-note/2.2/) |
| PubMedQA | Biomedical QA | [Project](https://pubmedqa.github.io/) |
| RadGraph | Radiology entities and relations | [PhysioNet](https://physionet.org/content/radgraph/) |

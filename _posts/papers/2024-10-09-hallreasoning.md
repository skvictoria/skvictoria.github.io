---
layout: paper
categories: papers
permalink: papers/hallreasoning
id: hallreasoning
title: "LLM Hallucination Reasoning with Zero-shot Knowledge Test"
authors: 
  - Seongmin Lee
  - Hsiang Hsu
  - Chun-Fu (Richard) Chen
venue: 38th Conference on Neural Information Processing Systems (NeurIPS 2024) Socially Responsible Language Modelling Research Workshop
venue-shorthand: SoLaR
year: 2024
award: SoLaR Workshop Travel Fund Award
url: /papers/hallreasoning
pdf: https://arxiv.org/pdf/2411.09689
type: conference
selected: false
feature-title: hallreasoning
feature-description: 
featured: false
bibtex: |-

  @article{lee2024llm,
    title={{LLM} {H}allucination {R}easoning with {Z}ero-shot {K}nowledge {T}est},
    author={Lee, Seongmin and Hsu, Hsiang and Chen, Chun-Fu},
    journal={arXiv preprint arXiv:2411.09689},
    year={2024}
  }
---

LLM hallucination, where LLMs occasionally generate unfaithful text, poses significant challenges for their practical applications. Most existing detection methods rely on external knowledge, LLM fine-tuning, or hallucination-labeled datasets, and they do not distinguish between different types of hallucinations, which are crucial for improving detection performance. We introduce a new task, Hallucination Reasoning, which classifies LLM-generated text into one of three categories: aligned, misaligned, and fabricated. Our novel zero-shot method assesses whether LLM has enough knowledge about a given prompt and text. Our experiments conducted on new datasets demonstrate the effectiveness of our method in hallucination reasoning and underscore its importance for enhancing detection performance.
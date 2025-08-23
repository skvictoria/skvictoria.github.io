---
layout: paper
id: llm-hallucination-probing
categories: papers
permalink: papers/llm-hallucination-probing
title: "Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge"
authors: 
  - Seongmin Lee
  - Hsiang Hsu
  - Chun-Fu Chen
  - Duen Horng (Polo) Chau
venue: ArXiv
venue-shorthand: ArXiv
year: 2025
url: /papers/llm-hallucination-probing
pdf: https://arxiv.org/pdf/2411.09689
selected: false
figure: /images/papers/25-llm-hallucination-probing.png
image: /images/papers/25-llm-hallucination-probing.png
featured: false
feature-order: 1
feature-title: LLM Hallucination Probing
feature-description: Probing LLM Hallucination from Within
bibtex: |-

  @article{lee2025probing,
    title={Probing LLM Hallucination from Within: Perturbation-Driven Approach via Internal Knowledge},
    author={Seongmin Lee and Hsiang Hsu and Chun-Fu Chen and and Duen Horng Chau},
    journal={arXiv preprint arXiv:2411.09689},
    year={2025},
    url={https://arxiv.org/abs/2411.09689}, 
  }
---

LLM hallucination, where unfaithful text is generated, presents a critical challenge for LLMs' practical applications. Current detection methods often resort to external knowledge, LLM fine-tuning, or supervised training with large hallucination-labeled datasets. Moreover, these approaches do not distinguish between different types of hallucinations, which is crucial for enhancing detection performance. To address such limitations, we introduce hallucination probing, a new task that classifies LLM-generated text into three categories: aligned, misaligned, and fabricated. Driven by our novel discovery that perturbing key entities in prompts affects LLM's generation of these three types of text differently, we propose SHINE, a novel hallucination probing method that does not require external knowledge, supervised training, or LLM fine-tuning. SHINE is effective in hallucination probing across three modern LLMs, and achieves state-of-the-art performance in hallucination detection, outperforming seven competing methods across four datasets and four LLMs, underscoring the importance of probing for accurate detection.
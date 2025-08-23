---
layout: paper
id: transformer-explainer
categories: papers
permalink: papers/transformer-explainer
title: "Transformer Explainer: Interactive Learning of Text-Generative Models"
authors: 
  - Aeree Cho
  - Grace C Kim
  - Alexander Karpekov
  - Alec Helbling
  - Zijie J. Wang
  - Seongmin Lee
  - Benjamin Hoover
  - Duen Horng (Polo) Chau
venue: Poster, IEEE Visualization Conference
venue-shorthand: VIS
year: 2024
url: /papers/transformer-explainer
demo: https://poloclub.github.io/transformer-explainer/
pdf: https://arxiv.org/pdf/2408.04619
recording: https://youtu.be/ECR4oAwocjs
code: https://github.com/poloclub/transformer-explainer
code-star: 3.1k
award: Best Poster
selected: false
figure: /images/papers/24-transformer-explainer.png
image: /images/papers/24-transformer-explainer.png
featured: false
feature-order: 4
feature-title: Transformer Explainer
feature-description: Interactive Visualization Tool for Transformer-based models like GPT
bibtex: |-

  @article{cho2024transformer,
    title={{T}ransformer {E}xplainer: {I}nteractive {L}earning of {T}ext-{G}enerative {M}odels},
    author={Cho, Aeree and Kim, Grace C. and Karpekov, Alexander and Helbling, Alec and Wang, Zijie J. and Lee, Seongmin and Hoover, Benjamin and Chau, Duen Horng},
    journal={IEEE VIS},
    year={2024}
  }
---

While large language models (LLMs) have shown remarkable capability to generate convincing text across diverse domains, concerns around its potential risks have highlighted the importance of understanding the rationale behind text generation. We present LLM Attributor, a Python library that provides interactive visualizations for training data attribution of an LLM's text generation. Our library offers a new way to quickly attribute an LLM's text generation to training data points to inspect model behaviors, enhance its trustworthiness, and compare model-generated text with user-provided text. We describe the visual and interactive design of our tool and highlight usage scenarios for LLaMA2 models fine-tuned with two different datasets: online articles about recent disasters and finance-related question-answer pairs. Thanks to LLM Attributor's broad support for computational notebooks, users can easily integrate it into their workflow to interactively visualize attributions of their models. For easier access and extensibility, we open-source LLM Attributor at https://github.com/poloclub/ LLM-Attribution. The video demo is available at https://youtu.be/mIG2MDQKQxM.
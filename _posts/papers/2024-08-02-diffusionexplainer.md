---
layout: paper
id: diffusion-explainer
categories: papers
permalink: papers/diffusion-explainer
title: "Diffusion Explainer: Visual Explanation for Text-to-image Stable Diffusion"
authors: 
  - Seongmin Lee
  - Benjamin Hoover
  - Hendrik Strobelt
  - Zijie J. Wang
  - ShengYun Peng
  - Austin P. Wright
  - Kevin Li
  - Haekyu Park
  - Haoyang Yang
  - Duen Horng (Polo) Chau
venue-num:
  - 0
venue: 
  - Short Paper, IEEE Visualization Conference
venue-shorthand: 
  - VIS
year: 
  - 2024
url: /papers/diffusion-explainer
demo: https://poloclub.github.io/diffusion-explainer/
pdf: https://browse.arxiv.org/pdf/2305.03509.pdf
recording: https://www.youtube.com/watch?v=Zg4gxdIWDds
code: https://github.com/poloclub/diffusion-explainer
code-star: 221
poster: /papers/23-diffusion-explainer-poster.pdf
selected: false
type: poster
figure: /images/papers/23-diffusion-explainer-short.gif
featured: true
feature-order: 2
feature-title: Diffusion Explainer
image: /images/featured/23-diffusion-explainer-short.gif
feature-description: Interactive visualization tool that explains how Stable Diffusion transforms text prompts into images
bibtex: |-

  @article{lee2023diffusion,
    title={Diffusion Explainer: Visual Explanation for Text-to-image Stable Diffusion},
    author={Lee, Seongmin and Hoover, Benjamin and Strobelt, Hendrik and Wang, Zijie J and Peng, ShengYun and Wright, Austin and Li, Kevin and Park, Haekyu and Yang, Haoyang and Chau, Duen Horng},
    journal={arXiv preprint arXiv:2305.03509},
    year={2023}
  }
---

Diffusion-based generative models’ impressive ability to create convincing images has captured global attention. However, their complex internal structures and operations often make them difficult for non-experts to understand. We present Diffusion Explainer, the first interactive visualization tool that explains how Stable Diffusion transforms text prompts into images. Diffusion Explainer tightly integrates a visual overview of Stable Diffusion’s complex components with detailed explanations of their underlying operations, enabling users to fluidly transition between multiple levels of abstraction through animations and interactive elements. By comparing the evolutions of image representations guided by two related text prompts over refinement timesteps, users can discover the impact of prompts on image generation. Diffusion Explainer runs locally in users’ web browsers without the need for installation or specialized hardware, broadening the public’s education access to modern AI techniques. Our open-sourced tool is available at: https://poloclub.github.io/diffusion-explainer/. A video demo is available at https://youtu.be/Zg4gxdIWDds.
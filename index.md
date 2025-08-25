---
layout: home
title: Home
---

<div id="intro-wrapper" class="l-text">
	<div id="intro-title-wrapper">
		<div id="intro-title-text-wrapper">
			<div id="intro-title-socials">
				{% for link in site.data.social-links %}
					{% if link.on-homepage == true %}
						{% include social-link.html link=link %}
					{% endif %}
				{% endfor %}
				<div id="everything-else" class="social-link">
					<a href="{{ site.url }}/cv"><div><i class="fa fa-portrait icon icon-right-space"></i>CV</div></a>
				</div>
			</div>
			<h1 id="intro-title">Hi! I'm Seulgi Kim</h1>
		</div>
		<div id="intro-image-wrapper">
			<img id="intro-image" src="/images/seulgi.png">
		</div>
	</div>
	<!-- <div id="everything-else" class="l-middle">
		<a href="{{ site.url }}/cv"><div><i class="fa fa-portrait icon icon-right-space"></i>CV</div></a>
	</div> -->
	<div>
		My research lies with the intersection of <b>computer vision</b> and <b>multi-modal learning</b>, with a particular emphasis on modeling temporal and semantic relationships between actions in long-term video sequences.
	</div>
	<div style="height: 1rem"></div>
	<div>
		I am pursuing my Ph.D. at Georgia Tech, working with <a href="https://alregib.ece.gatech.edu/">Ghassan AlRegib</a>.
		I received my B.S. from Seoul National University, where I was supported by <a href="https://www.kosaf.go.kr/eng/jsp/aid/aid02_01_01.jsp">Hyundai Research Scholarship</a>.
	</div>
</div>

<hr class="l-middle home-hr">

<h2 class="feature-title">Featured <a href="/cv/#publications">Research Publications</a></h2>

<!-- vertical spacing -->
<div style="height:10px"></div>

<div class="cover-wrapper cover-wrapper-3-col l-page">
	{% assign sortedPublications = site.categories.papers | sort: 'feature-order' %}
	{% for feature in sortedPublications %}
		{% if feature.featured == true %}
			{% include feature.html feature=feature %}
		{% endif %}
	{% endfor %}
</div>





<!-- [gt]: http://www.gatech.edu "Georgia Tech"
[cse]: http://cse.gatech.edu "Georgia Tech Computational Science and Engineering"
[coc]: http://www.cc.gatech.edu "Georgia Tech College of Computing"

[cv]: {{ site.url }}/cv
[polo]: http://www.cc.gatech.edu/~dchau/ "Polo Chau"
[poloclub]: http://poloclub.gatech.edu "Polo Club of Data Science" -->
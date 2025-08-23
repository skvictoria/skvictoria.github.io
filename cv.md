---
layout: cv
title: CV
permalink: cv/
# jsarr:
# - js/scripts.js
---

<h1 id="cv-title"><a href="{{ site.url }}">Seongmin Lee</a></h1>

<p id="cv-subtitle"><i>CS PhD student at <span class="cv-gt">Georgia Tech</span></i></p>



<div>
My research bridges machine learning and human-computer interaction to advance <b>Responsible AI</b>.
I design and develop 
<b>novel visual explanations</b> for complex machine learning models, and
<b>scalable algorithms</b> that promote accountable use of AI.
</div>

<div class="cv-spacer"></div>

<div>
I have collaborated with researchers and developers at Adobe, Google, JP Morgan Chase & Co., Cisco Systems, IBM Research, ADP, and AVAST Software.
</div>

<div class="cv-spacer"></div>

<div class="cv-image-links-wrapper">
	<div class="cv-image-links">
		{% for link in site.data.social-links %}
			{% if link.cv-group == 1 %}
				{% include cv-social-link.html link=link %}
			{% endif %}
		{% endfor %}
	</div>
	<div class="cv-image-links">
		{% for link in site.data.social-links %}
			{% if link.cv-group == 2 %}
				{% include cv-social-link.html link=link %}
			{% endif %}
		{% endfor %}
	</div>
</div>

***

## Education

{::nomarkdown}
{% for degree in site.data.education %}
{% include cv/degree.html degree=degree %}
{% endfor %}
{:/}

## Research Experience

{% for experience in site.data.experiences %}
{% if experience.type == 'industry' %}
{% include cv/experience.html experience=experience %}
{% endif %}
{% endfor %}

<!-- ## Academic Research Experience -->

{% for experience in site.data.experiences %}
{% if experience.type == 'academic' %}
{% include cv/experience.html experience=experience %}
{% endif %}
{% endfor %}

## Honors and Awards

{% for award in site.data.awards %}
{% include cv/award.html award=award %}
{% endfor %}

## Publications

{% assign selectedBoolForBibtex = false %}

{% for pub in site.categories.papers %}
{% include cv/publication.html pub=pub selectedBoolForBibtex=selectedBoolForBibtex %}
{% endfor %}

## Patent

{% for patent in site.data.patents %}
{% include cv/patent.html patent=patent %}
{% endfor %}

## Book

{% for book in site.data.books %}
{% include cv/book.html book=book %}
{% endfor %}

## Invited Talks

{% assign talktitles = site.data.talks | group_by:"title" %}
{% for title in talktitles %}
{% include cv/talk.html talk=title%}
{% endfor %}

## Teaching

{% for teach in site.data.teaching %}
{% include cv/teaching.html teach=teach %}
{% endfor %}

## Mentoring

{::nomarkdown}
{% for mentee in site.data.mentoring %}
{% include cv/mentee.html mentee=mentee %}
{% endfor %}
{:/}

## Grants and Funding

{% for fund in site.data.funding %}
{% include cv/fund.html fund=fund %}
{% endfor %}

<!-- ## Technology Skills

{% for skill in site.data.skills %}
{% include cv/skill.html skill=skill %}
{% endfor %} -->

## Service

<div class="cv-service-title"><b>Reviewer</b></div>
{% for venue in site.data.reviewer %}
{% include cv/venue.html venue=venue %}
{% endfor %}

<div class="cv-service-title"><b>Institutional</b></div>
{% for institution in site.data.institutional %}
{% include cv/institutional.html institution=institution %}
{% endfor %}

<div class="cv-service-title"><b>Member</b></div>
{% for member in site.data.memberships %}
{% include cv/member.html member=member %}
{% endfor %}

## References

{% for reference in site.data.references %}
{% include cv/reference.html reference=reference %}
{% endfor %}



[cv]: {{ site.url }}/cv.pdf "My CV."

---
title: "Hướng Dẫn & Kiến Thức Học Thuật (Tutorials)"
permalink: /tutorials/
layout: single
author_profile: true
---

Chào mừng đến với danh mục Hướng dẫn & Phân tích chuyên sâu về lộ trình Kỹ thuật Cơ điện tử 4.0.

<div class="entries-list">
  {% for post in site.categories.Tutorials %}
      <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
        <h2 class="archive__item-title" itemprop="headline">
          <a href="{{ post.url | relative_url }}" rel="permalink">{{ post.title }}</a>
        </h2>
        <p class="page__meta">
          <i class="far fa-calendar-alt" aria-hidden="true"></i> {{ post.date | date: "%d/%m/%Y" }}
        </p>
        <p class="archive__item-excerpt" itemprop="description">{{ post.content | strip_html | truncate: 250 }}</p>
      </article>
  {% endfor %}
</div>

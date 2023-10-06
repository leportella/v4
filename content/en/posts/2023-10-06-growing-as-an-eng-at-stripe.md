---
layout: post
title: "Growing as an engineer at Stripe"
categories:
  - career
  - personal
tags:
  - events
  - technology
  - Stripe
  - San Francisco
  - Dublin
  - software engineering
  - scala
  - python
  - book
  - friendly guide to software development
featured-img: eng_at_stripe
slug: growing-at-stripe
date: 2023-10-05T18:25:52-05:00
translationKey: growing-at-stripe
---

Many many moons ago, I [wrote a blog post](https://leportella.com/new-eng-stripe/) about what was like in my first 6 months at Stripe. Since then, a lot has happened including a whole pandemic and me spending every free hour writing [my own book](https://leportella.com/book/). Because of that and many more things, I never got to write a second piece to what I was initially hoping to be a once-a-year kind of blog post. <!--more-->
 Recently, I was kindly invited to give a talk about my career at Stripe at our Bucharest office opening event and that triggered the writer in me again. This is an expanded version of that talk where I shared how I grew and continue to grow as an engineer at Stripe.

## Working in an awesome, awesome product

After my first few months at Stripe I had the wonderful opportunity to join a very nascent project. That project eventually became what is now [Stripe Tax](https://stripe.com/ie/tax). Tax is a complex topic and we all know the phrase "the only certainty in life is death and taxes". However, when a business starts selling world-wide the tax complexity increases exponentially and they suddenly find themselves subjected to tax rules they might not even be aware of. For instance, it doesn't matter if you only sell a single Euro in Switzerland. If you have a [global revenue bigger than a certain threshold](https://stripe.com/docs/tax/threshold-rules#europe,-the-middle-east-and-africa), as soon as you sell your product in Switzerland, you should pay taxes to their government.

As you can imagine, knowing these rules is already complicated. Being compliant with all those rules is something else.

When I joined the project, it was still just an idea of a product we wanted to build or, more accurately, a product our users were imploring us to build for them. I was lucky enough to have the opportunity to be there when we presented the initial project then on the discussions on how we would model and create a beautiful product on such a complex topic.

We were able to take our product from idea, to an early iteration of an MVP then to finally general availability. Our launch day was one of the best days in my career. This was my baby, something me and my team had worked so hard and for so long to put out there. This is me and the amazing Kelly Moriarty, our Product Manager, on Stripe Tax's launch day:

{{<figure src="/assets/img/posts/eng_at_stripe/1.jpg#center" lt="A photo of two women with champagne glasses and a computer">}}


If you want to know more about how we built Stripe Tax, I recommend [this blog post from Kelly](https://stripe.com/blog/building-stripe-tax).

Before you think I knew anything about taxes let me assure you: I knew absolutely nothing. At all! I had to learn *a lot*. But thankfully I had tax experts helping our eng team to learn a bunch of cool tax facts. For instance, one of my favorite tax facts is that in New York a bagel isn't subjected to sales tax. Unless you cut it, then it becomes a sandwich and now it must be taxed. Unless you buy twelve. Then it's not taxable again. Can you imagine figuring this out on your own!? But definitely my favorite tax fact is about gingerbread men. From Kelly's blog post:

> *In the United Kingdom, if a gingerbread man has just two chocolate eyes, it is legally a biscuit (tax exempt). However, if that gingerbread man is also wearing chocolate buttonspants or a shirt, it is now legally taxed at a standard rate of 20%.*

Stripe is obsessed with user experience, so we knew our Tax product had to be incredibly easy to adopt and use. With such a complex topic, we had countless discussions on how we could make taxes *as simple as possible.* Externally, we added a single parameter to our API:

{{<figure src="/assets/img/posts/eng_at_stripe/3.jpg#center" lt="">}}

It sounds simple, but as any developer knows, a really simple user experience hides a massive amount of complexity. The amount of discussions and iterations we had to have to make sure this was the best possible way to move forward were exhilarating. Kelly mentioned in the blog post that we had discussions on if we would ever need something like `is_a_gingerbread_man_wearing_pants` parameter to the API. It seems like a joke, but our discussions *went deep* and topics such as this came to life many times!

{{<figure src="/assets/img/posts/eng_at_stripe/2.jpg#center" lt="">}}

Working in tax I would think of myself as more of a product-engineer, meaning my main job was to solve our customers' problems. For instance, we were building this new API and our Beta customers said that a webhook would make their lives better. I discussed when and how we would trigger the webhook and if this was the right thing for any customer we wanted to use this API. Questions like "could we improve the experience in a way that they wouldn't even need this webhook?" were things we constantly asked ourselves. Once we added the webhook, I never had to think if the webhook was going to be delivered or how. I just knew it would. My job was to make sure we were helping our customers to have the best features as fast as possible.

As our Stripe Tax grew larger and more complex, we started to embrace new challenges.
On all of the products we added tax, we were considering a 1:1 relationship between a merchant and customer.

However, one of Stripe's biggest products is [Connect](https://stripe.com/ie/connect), which allows multi-merchant relationships to happen in a single payment transaction. Think of Doordash or Deliveroo, for instance. You, the customer, makes a single payment transaction for your bagel order, but the company is paying the driver and the restaurant, meaning that you have multiple merchants associated with this single transaction.

I led the first iteration on how we would make Stripe Tax work with Connect. This was a very challenging project where I had to deeply understand both products to figure out how we would merge those two together in a seemingless way. We just launched this last month, so I'm excited with our product being available in such complex scenarios that Connect allows our merchants to develop.

I was lucky enough to work on such an amazing product. I worked on many challenging projects with a group of people I deeply admire. But there were other ways I kept learning beyond those projects.

## Friction logs

As you get subject expertise, it's easy to follow into the trap of building a product that is not accessible *unless* they are experts themselves. To avoid that and make sure Stripe Tax would always have the best user experience, at least once a semester we hold *Friction log* sessions where all team members, whether newcomers or not, try to use our product from scratch, trying to think like a customer would. We take notes on which parts were difficult, which documentation could be improved, and which parts of the system didn’t make sense and could use some brushing up. In addition to generating a list of things we can improve, this exercise also helps us not to make a product for ourselves, who talk about taxes every day. It has been a great way to develop that *users-first* mindset and never lose track of who actually matters in all this.

## API reviews

We have a process for designing new APIs and adding improvements to existing APIs. I can propose a design and iterate with more experienced developers to learn best API designs and we have a group that makes sure our APIs are consistent across the board. This is particularly helpful as, on my day-to-day, I might not know about a new API being developed by a far away team that has a pattern it is useful for me to follow.



More recently, I started to study and ramp up as an API Reviewer myself, where I had the opportunity to learn these designs in more depth and learn from several APIs being developed throughout Stripe. I am happy to share that I just "graduated" as a reviewer and now I am part of the group that is helping Stripe have that high level quality of APIs we all know and love.

## Learning from others teams

What I like about Stripe is that we love documentation – a lot. So you have the opportunity to learn from other teams and projects that interest you, even if you never work on them. There's a lot we can learn from each other, so I like lurking into random documentation and learning from other people's experience.

## Education budget

As a nerdy person, one of the things I like the most to keep learning is the education budget we have. In our Stripe Tax team we often shared suggestions of books and we had a document with a very long list of books you should read. I used it to attend some conferences as well but books are my passion :)

{{<figure src="/assets/img/posts/eng_at_stripe/4.jpg#center" lt="">}}


*Sidenote: I REALLY use this! This is just a subset of the books I got with my budget over the years*. I would highly recommend Tanya Reilly ["The Staff Engineer's Path"](https://amzn.to/3F22Xdh).

## Communities

We have a very strong engineering community. We have a bunch of internal courses, tech talks and project presentations that you can follow to learn from other teams and people. I particularly like the work we've been doing in Dublin, to make sure engineers have a support network to lean on.

Beyond the eng-focused communities, I've also been part of the Unidos community for Hispanic and Latin folks. As a Brazilian immigrant, I had to face a lot of challenges when moving to a new country and working in a language that is not my native one. Even small things that I thought would be *normal* in a work environment were quite different (highly recommend "[The culture map](https://erinmeyer.com/books/the-culture-map/)" if you want to understand it better). Finding a community I could share all this was super valuable. It gave me a feeling of belonging as well as helping me connect with different parts of the company.

{{<figure src="/assets/img/posts/eng_at_stripe/5.jpg#center" lt="">}}


## Changing roles and spreading knowledge

Stripe encourages engineers to take what they've learned, deploy skills elsewhere, develop more skills and broadly spread knowledge within the company. We have an internal job board where you can check opportunities that are available all over the company and you are incentivized to change if you have been in your role for more than a period. That's one of the reasons why, after 4 years of working with Stripe Tax and more product-focused engineering, I decided to move to a different challenge.

I just recently moved to the team that is responsible for the infrastructure of our APIs, called API Platform. It's something completely new that I don't have experience with but I am glad I have the opportunity to work on something new and develop an area I haven't focused on until now.

## Learning from all kinds of people

Finally I just want to share that we have lots of incredible people all across the board. I've the opportunity to work with many many people from different teams, roles and orgs. I learned a lot from all of them!

{{<figure src="/assets/img/posts/eng_at_stripe/6.jpg#center" lt="">}}


My experience was so valuable that it helped me get some of the skills I needed to write a technical book about software development for folks that aren't developers but need to understand how software is made. I just launched it last year, so I am really happy that all my learnings are now helping other people outside the company as well.

{{<figure src="/assets/img/posts/eng_at_stripe/7.jpg#center" lt="">}}


Well, this is a *very* short summary of my now 4,5 years at Stripe. I guess thinking about it I could probably write another book just on the things I experienced here! Just happy to still be here, to still be growing and hopefully it won't take me 4 years to write a follow up one :)


---

*Special thanks to Kate Apostolou for making these beautiful slides and Paul Crayston, Steffi Hoydich and David Singleton for helping me write this <3*

---

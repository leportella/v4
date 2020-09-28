---
title: "Contact me!"
date: 2020-09-26T22:55:34+01:00
last_modified_at: 2020-09-26T22:55:34+01:00
draft: false
---

{{< raw >}}
<article class="card card-outline mb-4">
  <div class="card-body">
    <header>
      <h4 class="card-title">Send me a message!</h4>
      <p>I always like to receive messages, so feel free to write me!</p>
      <p>For companies that might find this page: this is my personal blog and I don't publish content that was not written by me 🤓</p>
    </header>
    <form
        action="https://formspree.io/mwkwplkv"
        method="POST"
    >
      <div class="form-group">
          <label>Your Name</label>
          <input type="text" name="name" id="name" class="form-control" name="_replyto">
      </div>
      <div class="form-group">
          <label>Your email</label>
          <input type="text" class="form-control" name="_replyto">
      </div>
      <div class="form-group">
          <label>Your message</label>
          <textarea name="message" class="form-control"></textarea>
      </div>
      <button type="submit" class="btn btn-dark">Send</button>
    </form>
  </div>
</article>
{{< /raw >}}
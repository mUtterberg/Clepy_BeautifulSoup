# Django

### The web framework for perfectionists with deadlines

---

## Brief description

<br>

"Django is a Python library for..."

<a href src="https://www.djangoproject.com/"></a>

@fa[fab fa-github](https://github.com/django/django)

---

## Django in the wild

![Logo](assets/image/BLS_OOH.png)

+++

## Other examples

- Vertical slash is a mid-slide arrow break |
- A dash is a bulleted list item
- These three list items with no vertical character
- No character prevents hide/reveal functionality
- Slide-specific Background Images |
- Email setting (private) prevented GitHub push from local |

---?code=sample/go/server.go&lang=golang&title=I Can Do Something Here

@[1,3-6](Present code found within any repo source file.)
@[8-18](Without ever leaving your slideshow.)
@[19-28](Using GitPitch code-presenting with (optional) annotations.)

---

@title[JavaScript Block]

<p><span class="slide-title">How Do I Make This Nav Down?</span></p>

```javascript
// Include http module.
var http = require("http");

// Create the server. Function passed as parameter
// is called on every request made.
http.createServer(function (request, response) {
  // Attach listener on end event.  This event is
  // called when client sent, awaiting response.
  request.on("end", function () {
    // Write headers to the response.
    // HTTP 200 status, Content-Type text/plain.
    response.writeHead(200, {
      'Content-Type': 'text/plain'
    });
    // Send data and end response.
    response.end('Hello HTTP!');
  });

// Listen on the 8080 port.
}).listen(8080);
```

@[1,2](You can present code inlined within your slide markdown too.)
@[9-17](Displayed using code-syntax highlighting just like your IDE.)
@[19-20](Just make comments on that snippet in parentheses!)

+++?gist=dwbelliston/c0cb4975483c39f5658e7e23ba040e5a&lang=python&title=This GIST could legitimately be usable

@[23](You can even present code found within any GitHub GIST.)
@[41-53](GIST source code is beautifully rendered on any slide.)
@[57-62](And code-presenting works seamlessly for GIST too, both online and offline.)

---

## Template Help

- [Code Presenting](https://github.com/gitpitch/gitpitch/wiki/Code-Presenting)
  + [Repo Source](https://github.com/gitpitch/gitpitch/wiki/Code-Delimiter-Slides), [Static Blocks](https://github.com/gitpitch/gitpitch/wiki/Code-Slides), [GIST](https://github.com/gitpitch/gitpitch/wiki/GIST-Slides)
- [Custom CSS Styling](https://github.com/gitpitch/gitpitch/wiki/Slideshow-Custom-CSS)
- [Slideshow Background Image](https://github.com/gitpitch/gitpitch/wiki/Background-Setting)
- [Slide-specific Background Images](https://github.com/gitpitch/gitpitch/wiki/Image-Slides#background)
- [Custom Logo](https://github.com/gitpitch/gitpitch/wiki/Logo-Setting), [TOC](https://github.com/gitpitch/gitpitch/wiki/Table-of-Contents), and [Footnotes](https://github.com/gitpitch/gitpitch/wiki/Footnote-Setting)

+++

## Go GitPitch Pro!

<br>
<div class="left">
    <i class="fa fa-user-secret fa-5x" aria-hidden="true"> </i><br>
    <a href="https://gitpitch.com/pro-features" class="pro-link">
    More details here.</a>
</div>
<div class="right">
   <iframe src="https://www.crummy.com/software/BeautifulSoup/zine/" style="height:10em;width:50em"></iframe>
</div>

+++

### Font Awesome integrates nicely

<br>

@fa[github gp-contact](gitpitch)
Removed some font awesome logos today...
This is how regular, unformatted text looks.

---?image=assets/image/gitpitch-audience.jpg

@title[Download this Template!]

### <span class="white">Get your presentation started!</span>
### [Download this template @fa[external-link gp-download]](https://gitpitch.com/template/download/aqua)

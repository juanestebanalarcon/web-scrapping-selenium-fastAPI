# Developer Trial Task

## Instructions:

- Copy ClassCentral Pages and Translate to Hindi
- Scrape pages one level deep using HTTrack, your custom script, or another app.
- Use Google Translate to Translate the text inside the HTML to Hindi. The hindi will be hardcoded into the page.
- Upload to a webserver.
- Make sure all the javascript/css/etc. is loading correctly.
- In your trial task form submission:
- Include a URL to the live website on your server so we can see that successfully copied it.
- Let me know how you scraped the pages. Did you use httrack, another piece of software, or a script you wrote your self?

# Used technologies:

```
fastapi = "*"
beautifulsoup4 = "*"
uvicorn = "*"
jinja2 = "*"
pydantic = "*"
googletrans = "*"
webdriver-manager = "*"
selenium = "*"
```

# Commandas

```
uvicorn <filename>:app --reload
```

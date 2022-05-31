// This script is based on one oroginally created by J Jandrell for a personal project
// GROOP my use this code however they may not claim ownership of it. This script was not made on company time
// J Jandrell owns the rights to this scrip and may use it eleswhere
//
// Owner Joshua Jandrell
// version 0.0
// staus: complete 05/30/22

// Make custom shadow templates for all <tempate elements> with class templateClsss
//  templateClass = '*' to make custom elements from ALL template tags => this is the default
function MakeShadowTemplates(templateClass = "*") {
  let templates = document.getElementsByTagName("template");
  Array.from(templates).forEach((template) => {
    if (templateClass == "*" || template.classList.contains(templateCalss))
      MakeShadowTemplate(template.id);
  });
}

// This funtion must be called AFTER template html has been loaded
// Creates a custom html elemnt that populates all html elements with the tage <templateName> with the custom content from the <template> element with the id='templateName'
// <slot> elments are supported for further customisation
function MakeShadowTemplate(templateName) {
  customElements.define(
    templateName,
    class extends HTMLElement {
      constructor() {
        super();
        let template = document.getElementById(templateName);
        let templateContent = template.content;
        const shadowRoot = this.attachShadow({ mode: "open" });
        shadowRoot.appendChild(templateContent.cloneNode(true));
      }
    }
  );
}

// Load an html templates stored in the html file with the given href.
// Then make this template into a custom element with the given name.
function LoadCustomTemplates(href) {
  fetch(href)
    .then((response) => {
      return response.text();
    })
    .then((text) => {
      let parser = new DOMParser();
      return parser.parseFromString(text, "text/html");
    })
    .then((doc) => {
      return doc.body;
    })
    .then((body) => {
      document.body.appendChild(body);

      let temps = body.querySelectorAll("template");
      Array.from(temps).forEach((template) => {
        MakeShadowTemplate(template.id);
      });
    });
}

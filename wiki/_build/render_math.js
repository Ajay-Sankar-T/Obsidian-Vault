// Render a batch of TeX snippets with KaTeX.  usage: node render_math.js in.json out.json
// in.json: [{"tex": "...", "display": true|false}, ...]   out.json: ["<span class=\"katex\">...", ...]
// Snippets KaTeX cannot parse are rendered as plain code and listed in math_errors.txt next to this file.
const fs = require("fs");
const path = require("path");
const katex = require("katex");
const [, , inFile, outFile] = process.argv;
const items = JSON.parse(fs.readFileSync(inFile, "utf8"));
const errors = [];
const macros = { "\\cdotp": "$\\cdot$" };   // U+00B7 inside \text maps to \cdotp, which KaTeX leaves undefined
const render = (tex, displayMode) => katex.renderToString(tex, { displayMode, throwOnError: true, strict: "ignore", trust: false, output: "html", macros: { ...macros } });
const out = items.map(({ tex, display }) => {
  try {
    try {
      return render(tex, !!display);
    } catch (e) {
      if (!display && /\\tag works only in display/.test(e.message)) return render(tex, true);   // numbered equation written inline
      throw e;
    }
  } catch (e) {
    errors.push(`${e.message.split("\n")[0]}  ::  ${tex.slice(0, 160).replace(/\n/g, " ")}`);
    return `<code class="math-error">${tex.replace(/&/g, "&amp;").replace(/</g, "&lt;")}</code>`;
  }
});
fs.writeFileSync(outFile, JSON.stringify(out));
if (errors.length) fs.appendFileSync(path.join(__dirname, "math_errors.txt"), errors.join("\n") + "\n");
console.log(`rendered ${out.length} snippets, ${errors.length} could not be parsed`);

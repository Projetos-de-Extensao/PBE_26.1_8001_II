/* Inicializa diagramas Mermaid após cada carregamento (Material for MkDocs). */
document$.subscribe(function () {
  if (typeof mermaid === "undefined") return;
  mermaid.initialize({ startOnLoad: false, securityLevel: "loose" });
  mermaid.run({ querySelector: ".mermaid" });
});

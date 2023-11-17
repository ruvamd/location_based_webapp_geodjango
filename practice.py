[out:json][timeout:25];
{{geocodeArea:Baltimore}}->.searchArea;

(
    node[shop](area.searchArea);
    way[shop](area.searchArea);
    relation[shop](area.searchArea);
);

out body;
>;
out skel qt;
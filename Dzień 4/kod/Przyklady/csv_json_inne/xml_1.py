import xml.etree.ElementTree as xml

txt = """<a>
    <b>A<h>qwe ... rty</h></b> ABCD... &amp;&apos; HIJ...
    <c x="q" w="p p">EE FĄ</c> <g y="zz" />
    <c x="pp">123 <d rr="oo">456</d> 78 90.</c>
</a>"""

rootNode = xml.fromstring(txt)

print("nazwa głównego elementu to:", rootNode.tag)
print("jego potomkowie to:")
for subNode in rootNode:
    print(" ", subNode.tag, ":", xml.tostring(subNode, encoding="unicode"))

# możemy pobrać listę potomków o określonej nazwie
# albo od razu po nich iterować pętlą for subNode in rootNode.iter("c"):
cSubNodes = list(rootNode.iter("c"))
if cSubNodes:
    for subNode in cSubNodes:
        print('element "c" ma atrybuty', subNode.attrib)
else:
    print('nie ma elementów "c"')


# możemy też używać iteratorów bezpośrednio, np:
print("pierwszy węzeł c ma atrybuty:")
try:
    ci = rootNode.iter("c")
    print(next(ci).attrib)
except StopIteration:
    print(" [brak takiego węzła]")

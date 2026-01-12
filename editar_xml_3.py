from lxml import etree

tree = etree.parse(r"C:\Users\922027\Documents\Babis\catalogos_git\catalogo_xml_2\teste_2.xml")
root = tree.getroot()

# lista com as 2 strings tableName
lista_xml = ["t120", "t130", "t140"]

for i in lista_xml:
    segunda_tabela = root.find(f'.//table[@tableName="{i}"]')

    nova_coluna = etree.Element("column")
    nova_coluna.set("bdcolname", "NOVA_COLUNA_3")
    nova_coluna.set("bdtype", "VARCHAR2(50)")
    nova_coluna.set("dbn0type", "ID")
    nova_coluna.set("id", "NOVA_COLUNA_TESTE")
    nova_coluna.set("udn", "novaColunaTeste")

    # adiciona a nova coluna dentro da tabela
    segunda_tabela.append(nova_coluna)

tree.write(
    r"C:\Users\922027\Documents\Babis\catalogos_git\catalogo_xml_2\teste_2.xml",
    encoding="utf-8",
    xml_declaration=True,
    pretty_print=True
)
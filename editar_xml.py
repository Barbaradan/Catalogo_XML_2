from lxml import etree

tree = etree.parse(r"C:\Users\922027\Documents\Babis\catalogos_git\catalogo_xml_2\teste_2.xml")
root = tree.getroot()

# encontra a tabela pelo atributo tableName
segunda_tabela = root.find('.//table[@tableName="t130"]')

# cria elementos da coluna nova
nova_coluna = etree.Element("column")
nova_coluna.set("bdcolname", "NOVA_COLUNA")
nova_coluna.set("bdtype", "VARCHAR2(50)")
nova_coluna.set("dbn0type", "ID")
nova_coluna.set("id", "NOVA_COLUNA")
nova_coluna.set("udn", "novaColuna")

# adiciona a nova coluna dentro da tabela
segunda_tabela.append(nova_coluna)

tree.write(
    r"C:\Users\922027\Documents\Babis\catalogos_git\catalogo_xml_2\teste_2.xml",
    encoding="utf-8",
    xml_declaration=True,
    pretty_print=True
)
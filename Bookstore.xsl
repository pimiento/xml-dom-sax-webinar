<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2> My Books collection</h2>
                <table border="1">
                    <tr bgcolor="red">
                        <th align="left">title</th>
                        <th align="left">author</th>
                    </tr>
                    <xsl:for-each select="/Bookstore/Book">
                        <tr>
                            <td><xsl:value-of select="Title"/></td>
                            <xsl:choose>
                                <xsl:when test="@Price > 90">
                                    <td bgcolor="yellow"><xsl:value-of select="Authors/Author"/></td>
                                </xsl:when>
                                <xsl:when test="@Price > 30">
                                    <td bgcolor="lightgreen"><xsl:value-of select="Authors/Author"/></td>
                                </xsl:when>
                                <xsl:otherwise>
                                    <td bgcolor="gray"><xsl:value-of select="Authors/Author"/></td>
                                </xsl:otherwise>
                            </xsl:choose>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>

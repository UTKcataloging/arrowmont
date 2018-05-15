<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.og/2001/XMLSchema" 
    exclude-result-prefixes="xs" version="2.0">

    <xsl:output encoding="UTF-8" method="text" indent="yes"/>
    <xsl:strip-space elements="*"/>
    <xsl:template match="fileDesc"/>
    <xsl:template match="encodingDesc"/>
    <xsl:template match="profileDesc"></xsl:template>
    <xsl:template match="div1">
        <xsl:apply-templates select="pb"></xsl:apply-templates>
        <xsl:apply-templates select="p"></xsl:apply-templates>
    </xsl:template>
    <xsl:template match="pb">
        
        Page <xsl:value-of select="attribute::seq"/>:  
        
        <xsl:value-of select="following-sibling::p/text()"/>
    </xsl:template>



</xsl:stylesheet>

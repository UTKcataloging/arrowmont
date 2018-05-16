<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:oai_dc='http://www.openarchives.org/OAI/2.0/oai_dc/' xmlns:dc="http://purl.org/dc/elements/1.1/" 
    xmlns:oai="http://www.openarchives.org/OAI/2.0/" xmlns:xlink="http://www.w3.org/1999/xlink"
    version="2.0" xmlns="http://www.loc.gov/mods/v3">
    
    <xsl:output encoding="UTF-8" method="xml" indent="yes"/>
    <xsl:strip-space elements="*"/>

    <!-- identity transform -->
    <xsl:template match="@* | node()">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="dc:subject">
        <subject><topic><xsl:value-of select="."/></topic></subject>
    </xsl:template>
    
    <xsl:template match="dc:title">
        <titleInfo><title><xsl:value-of select="."/></title></titleInfo>
    </xsl:template>
    
    <xsl:template match="dc:identifier">
        <identifier type="filename"><xsl:value-of select="."/></identifier>
    </xsl:template>
    
    <xsl:template match="oai_dc:dc">
        <mods xmlns="http://www.loc.gov/mods/v3" version="3.5"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
            <xsl:apply-templates select="@* | node()"/>
            <note displayLabel="Project Part">Arrowmont Simple Images from Scrapbooks</note>
            <accessCondition type="use and reproduction"
                xlink:href="http://rightsstatements.org/vocab/CNE/1.0/ ">Copyright Not
                Evaluated</accessCondition>
            <recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of
                Tennessee, Knoxville. Libraries</recordContentSource>
        </mods>
    </xsl:template>
</xsl:stylesheet>

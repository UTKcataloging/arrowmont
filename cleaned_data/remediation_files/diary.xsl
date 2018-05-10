<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.og/2001/XMLSchema" xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.loc.gov/mods/v3"
    xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-2.xsd"
    exclude-result-prefixes="xs" xpath-default-namespace="http://www.loc.gov/mods/v3" version="2.0">

    <xsl:output encoding="UTF-8" method="xml" indent="yes"/>
    <xsl:strip-space elements="*"/>

    <!-- identity transform -->
    <xsl:template match="@* | node()">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="*:metadata">
        <xsl:apply-templates select="mods"/>
    </xsl:template>

    <xsl:template match="mods">
        <mods xmlns="http://www.loc.gov/mods/v3" version="3.5"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
            <xsl:apply-templates select="@* | node()"/>
            <note displayLabel="Project Part">Ruth Sturley Diary</note>
        </mods>
    </xsl:template>

    <xsl:template match="accessCondition">
        <accessCondition type="use and reproduction"
            xlink:href="http://rightsstatements.org/vocab/CNE/1.0/ ">Copyright Not
            Evaluated</accessCondition>
    </xsl:template>


    <xsl:template match="name">
        <xsl:variable name="first" select="namePart[@type = 'given']"/>
        <xsl:variable name="last" select="namePart[@type = 'family']"/>
        <xsl:variable name="notype" select="namePart[not(@type)]"/>
        <name>
            <namePart>
                <xsl:value-of select="normalize-space(concat($first, $last, $notype))"/>
            </namePart>
            <role>
                <roleTerm authority="marcrelator"
                    valueURI="http://id.loc.gov/vocabulary/relators/aut">Author</roleTerm>
            </role>
        </name>
    </xsl:template>

    <xsl:template match="relatedItem/identifier"/>
    <xsl:template match="note[@displayLabel = 'Statement of Responsibility']"/>
    <xsl:template match="mods/identifier[@type = 'uri']"/>
    <xsl:template match="location/url"/>

    <!-- recordContentSource -->
    <xsl:template match="recordInfo/recordContentSource">
        <recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of
            Tennessee, Knoxville. Libraries</recordContentSource>
    </xsl:template>
    <!-- internetMediaType -->
    <xsl:template match="internetMediaType"/>
    <!-- Digital Collection to Project-->
    <xsl:template match="relatedItem/@displayLabel[. = 'Digital Collection']">
        <xsl:attribute name="displayLabel">
            <xsl:value-of select="'Project'"/>
        </xsl:attribute>
    </xsl:template>
    <xsl:template match="mods/@xsi:schemaLocation">
        <xsl:attribute name="xsi:schemaLocation">
            <xsl:value-of
                select="'http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd'"
            />
        </xsl:attribute>
    </xsl:template>
</xsl:stylesheet>

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

def generate_pdf(output_path):
    # Setup document: letter size with 0.65 in margins (same as classic resume)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch
    )

    styles = getSampleStyleSheet()

    # Define custom styles matching the Times New Roman serif look from the user's resume
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=22,
        leading=26,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#111111')
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#222222')
    )

    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#111111')
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#222222')
    )

    item_title_style = ParagraphStyle(
        'ItemTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#111111')
    )

    item_date_style = ParagraphStyle(
        'ItemDate',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13,
        alignment=TA_RIGHT,
        textColor=colors.HexColor('#555555')
    )

    item_subtitle_style = ParagraphStyle(
        'ItemSubtitle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#333333')
    )

    project_header_style = ParagraphStyle(
        'ProjectHeader',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#222222')
    )

    link_style = ParagraphStyle(
        'LinkStyle',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#1b4f91')
    )

    story = []

    def section_header(title):
        elements = [
            Spacer(1, 10),
            Paragraph(title, section_heading_style),
            Spacer(1, 2),
            HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#333333'), spaceBefore=1, spaceAfter=6)
        ]
        return elements

    content_width = 8.5 * inch - 1.3 * inch  # 7.2 inches

    # Header
    story.append(Paragraph("<b>VED DIXIT</b>", name_style))
    story.append(Spacer(1, 4))
    
    contact_text = (
        '<font color="#1b4f91"><a href="mailto:veddixit28@gmail.com">veddixit28@gmail.com</a></font> · '
        '7738353010 · Navi Mumbai · '
        '<font color="#1b4f91"><a href="https://www.linkedin.com/in/ved-dixit-b279983a1">LinkedIn</a></font> · '
        '<font color="#1b4f91"><a href="https://github.com/Vedd023">GitHub</a></font> · '
        '<font color="#1b4f91"><a href="https://vedd023.github.io/portfolio">Portfolio</a></font>'
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 6))

    # Professional Summary
    story.extend(section_header("PROFESSIONAL SUMMARY"))
    summary_text = (
        "AI &amp; Data Science engineering student with hands-on experience in web development and cloud technologies. "
        "Skilled in HTML, CSS, JavaScript, Python, and Firebase, with experience developing web-based projects such as "
        "College ERP and LinkGrid. Strong interest in building practical, user-focused solutions, with additional "
        "experience in social media management and volunteering."
    )
    story.append(Paragraph(summary_text, body_style))

    # Education
    story.extend(section_header("EDUCATION"))
    edu_table_data = [
        [
            Paragraph("<b>B.E. - Artificial Intelligence and Data Science</b>", item_title_style),
            Paragraph("Sept 2024 - Present", item_date_style)
        ]
    ]
    edu_table = Table(edu_table_data, colWidths=[content_width * 0.7, content_width * 0.3])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 2))
    story.append(Paragraph("Terna Engineering College, Nerul · GPA: 7.2", item_subtitle_style))

    # Work Experience
    story.extend(section_header("WORK EXPERIENCE"))
    work_table_data = [
        [
            Paragraph("<b>Web Operations Intern</b>", item_title_style),
            Paragraph("July 2026 - September", item_date_style)
        ]
    ]
    work_table = Table(work_table_data, colWidths=[content_width * 0.7, content_width * 0.3])
    work_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(work_table)
    story.append(Spacer(1, 2))
    story.append(Paragraph("Concept Simplified — Remote", item_subtitle_style))

    # Skills
    story.extend(section_header("SKILLS"))
    story.append(Paragraph("<b>Web Development Skills:</b> HTML, CSS, Javascript", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Programming Languages:</b> Python", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Database:</b> Cloud Firestore", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Editing:</b> Da Vinci, Capcut", body_style))

    # Projects (Page 1)
    story.extend(section_header("PROJECTS"))
    
    # EduNexus ERP
    story.append(Paragraph(
        "<b>EduNexus ERP</b> | <font color='#444444'>HTML + CSS + Vanilla JavaScript, Cloud Firestore, Firebase Authentication</font>",
        project_header_style
    ))
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "College ERP is a web-based college management system that helps manage students, faculty, attendance, exams, "
        "grades, timetable, assignments, and fees. It provides separate dashboards for Admin, Faculty, and Students and "
        "uses HTML, CSS, JavaScript, and Firebase.",
        body_style
    ))
    story.append(Spacer(1, 2))
    story.append(Paragraph('<font color="#1b4f91"><a href="https://github.com/Vedd023/College-ERP">GitHub</a></font>', link_style))

    # LinkGrid
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>LinkGrid</b> | <font color='#444444'>HTML + CSS + Javascript</font>",
        project_header_style
    ))
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "LinkGrid is a web-based tool that shortens long URLs and converts links into QR codes. It makes links easier "
        "to share and access while providing a simple and user-friendly interface.",
        body_style
    ))

    # Polaris
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Polaris</b> | <font color='#444444'>Next.js 15, TypeScript, Tailwind CSS, Supabase, PostgreSQL, Supabase Auth, PostgreSQL Row-Level Security (RLS).</font>",
        project_header_style
    ))
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "An integrated polar expedition management platform that streamlines expedition planning, asset and inventory "
        "management, logistics, risk monitoring, and AI-assisted operational decision-making.",
        body_style
    ))
    story.append(Spacer(1, 2))
    story.append(Paragraph('<font color="#1b4f91"><a href="https://github.com/Vedd023/Polaris">Live Demo</a></font>', link_style))

    # Page Break for Page 2 (as in original PDF)
    story.append(PageBreak())

    # Projects Continued (Page 2)
    story.extend(section_header("PROJECTS"))
    
    # Belt Guard AI
    story.append(Paragraph(
        "<b>Belt Guard AI</b> | <font color='#444444'>React 19, TypeScript 6, Vite 8, Tailwind CSS 4, Recharts, React Router DOM, Lucide React, date-fns.</font>",
        project_header_style
    ))
    story.append(Spacer(1, 3))
    story.append(Paragraph(
        "An AI-powered industrial monitoring dashboard that uses simulated multi-sensor telemetry, sensor-fusion risk "
        "scoring, and anomaly detection to monitor conveyor belt health, identify potential faults, and support "
        "predictive maintenance.",
        body_style
    ))
    story.append(Spacer(1, 2))
    story.append(Paragraph('<font color="#1b4f91"><a href="https://github.com/Vedd023/Belt-Guard-AI">Live Demo</a></font>', link_style))

    # Volunteer Experience
    story.extend(section_header("VOLUNTEER EXPERIENCE"))
    
    vol1_table_data = [
        [
            Paragraph("<b>Social Media Head</b>", item_title_style),
            Paragraph("Jan 2026 - March 2026", item_date_style)
        ]
    ]
    vol1_table = Table(vol1_table_data, colWidths=[content_width * 0.7, content_width * 0.3])
    vol1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(vol1_table)
    story.append(Spacer(1, 2))
    story.append(Paragraph("Avalon Terna Techfest 2026", item_subtitle_style))

    story.append(Spacer(1, 8))
    vol2_table_data = [
        [
            Paragraph("<b>Volunteer</b>", item_title_style),
            Paragraph("Sept 2025 - Present", item_date_style)
        ]
    ]
    vol2_table = Table(vol2_table_data, colWidths=[content_width * 0.7, content_width * 0.3])
    vol2_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(vol2_table)
    story.append(Spacer(1, 2))
    story.append(Paragraph("NSS", item_subtitle_style))

    doc.build(story)
    print(f"Successfully generated {output_path}")

if __name__ == '__main__':
    generate_pdf("Ved_Dixit_Resume.pdf")

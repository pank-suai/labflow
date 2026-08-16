#import "context.typ": *
#import "titlepage.typ": titlepage

#let init(body) = {
  titlepage(
    title: document_title,
    subject: document_subject,
    kind: document_kind,
    author: document_author,
    group: document_group,
    university: document_university,
    faculty: document_faculty,
    department: document_department,
    teacher: document_teacher,
    city: document_city,
    date: document_date,
  )

  set text(
    font: "Times New Roman",
    size: 14pt,
    lang: "ru",
    region: "ru",
    hyphenate: true,
  )
  set heading(numbering: "1.1")
  set par(justify: true, leading: 1.2em, first-line-indent: (amount: 1.25cm, all: true))

  show table: set text(hyphenate: true)
  show table: set par(justify: false, leading: 0.3em, first-line-indent: 0em)
  show figure.where(kind: image): set figure(supplement: "Рисунок")
  show figure.where(kind: table): set figure(supplement: "Таблица")
  show figure.where(kind: table): set figure.caption(position: top)
  show raw: set text(10pt, font: "JetBrains Mono")

  set list(marker: [---], body-indent: 0.7em, indent: 1.25cm)
  set enum(numbering: "1.", body-indent: 0.7em, indent: 1.25cm)
  set page(numbering: "1", margin: (top: 20mm, bottom: 20mm, left: 30mm, right: 15mm))
  set math.equation(numbering: "(1)")

  body
}

#let ch(content) = {
  align(heading(upper(content), numbering: none), center)
}
